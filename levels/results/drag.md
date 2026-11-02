# drag

Solved in 0.00 seconds. 10 programs considered, over 2 rounds.

## Winner

-- score: -64.31 (accuracy -66.51, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

## Runner-ups

-- score: -64.31 (accuracy -66.51, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -63.60 (accuracy -66.90, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -61.73 (accuracy -63.73, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -55.52 (accuracy -57.92, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.600, b = 0.012
  Demo 1: a = 0.888, b = 0.068
  Demo 2: a = 0.899, b = 0.067

# The Search

## Round 0 | 0.00s | best score: -63.60

+5 new programs (5 actually scored)
* add_terms: +5
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -63.60 (accuracy -66.90, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -61.73 (accuracy -63.73, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -28.76 (accuracy -30.06, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

-- score: -21.08 (accuracy -21.98, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 3.394
  Demo 1: a = -12.393
  Demo 2: a = 1.149

-- score: -19.65 (accuracy -20.75, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.053
  Demo 1: a = -0.902
  Demo 2: a = 0.063

## Round 1 | 0.00s | best score: -64.31

+6 new programs (6 actually scored)
* add_terms: +3
* delete_lines: +3
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -64.31 (accuracy -66.51, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -63.60 (accuracy -66.90, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -61.73 (accuracy -63.73, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -55.52 (accuracy -57.92, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.600, b = 0.012
  Demo 1: a = 0.888, b = 0.068
  Demo 2: a = 0.899, b = 0.067

-- score: -28.76 (accuracy -30.06, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

