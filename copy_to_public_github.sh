#!/bin/bash
# Copies the public parts of this repo into "../AlexNot-ODE For Public GitHub", for the public GitHub release.
# Each copied item is replaced fresh every run, but anything else in the destination (like its .git) is left alone.
# Run from anywhere: bash copy_to_public_github.sh
set -euo pipefail

# This script's folder = the repo root
SOURCE="$(cd "$(dirname "$0")" && pwd)"
DESTINATION="$(cd "$SOURCE/.." && pwd)/AlexNot-ODE For Public GitHub"
mkdir -p "$DESTINATION"

# What goes public (_old.md stays out: LLM speculation, with local paths in it)
FOLDERS=("solver" "levels" "data" "21-sample")
FILES=("README.md" "FINAL_WRITEUP.md" "LICENSE" "requirements.txt")

# Never copied: OS / Python clutter, and the regenerable noisy level copies (levels/generators/generate_fan.py remakes them)
EXCLUDES=(--exclude ".DS_Store" --exclude "__pycache__/" --exclude "*.pyc"
          --exclude "/timeseries/fan/" --exclude "/timeseries/fan_samples20/")

# Start each copied item fresh, so files deleted here don't linger there
for item in "${FOLDERS[@]}" "${FILES[@]}"; do
    rm -rf "${DESTINATION:?}/$item"
done
for folder in "${FOLDERS[@]}"; do
    rsync -a "${EXCLUDES[@]}" "$SOURCE/$folder/" "$DESTINATION/$folder/"
done
for file in "${FILES[@]}"; do
    cp "$SOURCE/$file" "$DESTINATION/$file"
done

# The public repo's own .gitignore
cat > "$DESTINATION/.gitignore" <<'GITIGNORE'
.DS_Store
__pycache__/
*.pyc
.venv/
venv/

# Regenerable noisy level copies: run levels/generators/generate_fan.py
levels/timeseries/fan/
levels/timeseries/fan_samples20/
GITIGNORE

echo "Copied into: $DESTINATION ($(du -sh "$DESTINATION" | cut -f1))"

# Safety checks on the copy: things that should never go public. Warnings only, nothing gets changed
echo
echo "Checking the copy for local paths, secrets and leftovers..."
warnings=0
check() {
    # $1 = what we're looking for, $2 = grep -E pattern
    local hits
    hits="$(grep -rIlE "$2" "$DESTINATION" --exclude-dir ".git" || true)"
    if [ -n "$hits" ]; then
        echo "⚠️  $1:"
        echo "$hits" | sed "s|$DESTINATION/|    |"
        warnings=$((warnings + 1))
    fi
}
check "Local absolute paths" "/Users/|twocats"
check "Possible secrets" "(API_KEY|SECRET|Bearer |hf_[A-Za-z0-9]{20}|sk-[A-Za-z0-9]{20}|rpa_[A-Za-z0-9]{20})"
check "Code-agent mentions" "CLAUDE|SUBAGENT_|_old\.md"
check "Paths into sibling repos" "AlexNot Fallback|\.\./AlexNot"
for leftover in ".env" "CLAUDE.md" ".claude"; do
    if find "$DESTINATION" -name "$leftover" -not -path "*/.git/*" | grep -q .; then
        echo "⚠️  Found a $leftover in the copy"
        warnings=$((warnings + 1))
    fi
done
echo "Done, with $warnings warning(s)."
