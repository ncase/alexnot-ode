"""Lorenz at 5, 10 & 20% noise on all 20 seeds, without stopping at 1%. Counts exact solves, and winners with the right terms but looser numbers. Writes nothing to the repo."""
from collections import Counter
import multiprocessing

from programs import TIMESERIES_PATH, ScoredProgram, load_level, split_line
from rank_intended import INTENDED_PROGRAMS, score_directly, short_text
from search import search_population

INTENDED: set[str] = INTENDED_PROGRAMS['lorenz']
TRUE_TERMS: set[tuple[str, str, str]] = {split_line(line) for line in next(iter(INTENDED)).splitlines()}


def run_job(job: tuple[str, int]) -> tuple[bool, int, int, float, str]:
    noise, seed = job
    level = load_level(TIMESERIES_PATH / 'fan' / f'lorenz_noise{noise}_seed{seed:02d}.json')
    winner: ScoredProgram = min(search_population(level), key=lambda program: program.score)
    terms: set[tuple[str, str, str]] = {split_line(line) for line in winner.source.splitlines()}
    return winner.source in INTENDED, len(terms & TRUE_TERMS), len(terms - TRUE_TERMS), score_directly(next(iter(INTENDED)), level) - winner.score, short_text(winner.source)


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        for noise in ['05', '10', '20']:
            results = pool.map(run_job, [(noise, seed) for seed in range(20)])
            exact: int = sum(result[0] for result in results)
            right_terms: int = sum(result[1] == 7 and result[2] == 0 for result in results)
            search_misses: int = sum(result[3] < -1e-5 for result in results)
            print(f'noise {noise}%: exact {exact}/20, right 7 terms & nothing extra {right_terms}/20, search problems {search_misses}, median true terms {sorted(result[1] for result in results)[10]}/7', flush=True)
            for winner, count in Counter(result[4] for result in results).most_common(4):
                print(f'    {count:2d}x {winner}', flush=True)
    print('ALL DONE', flush=True)
