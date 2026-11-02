# drag

Solved in 0.00 seconds. 10 programs considered, over 2 rounds.

## Winner

-- score: -14.77 (accuracy -16.97, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

## Runner-ups

-- score: -14.77 (accuracy -16.97, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -14.26 (accuracy -16.26, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -13.77 (accuracy -17.07, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -12.38 (accuracy -14.78, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.600, b = 0.012
  Demo 1: a = 0.888, b = 0.068
  Demo 2: a = 0.899, b = 0.067

# The Search

## Round 0 | 0.00s | best score: -14.26

+5 new programs (5 actually scored)
* add_terms: +5
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -14.26 (accuracy -16.26, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -13.77 (accuracy -17.07, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -6.37 (accuracy -7.67, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

-- score: -4.71 (accuracy -5.61, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 3.394
  Demo 1: a = -12.393
  Demo 2: a = 1.149

-- score: -4.19 (accuracy -5.29, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.053
  Demo 1: a = -0.902
  Demo 2: a = 0.063

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -14.77

+6 new programs (6 actually scored)
* add_terms: +3
* delete_lines: +3
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 8 parents for the next round

-- score: -14.77 (accuracy -16.97, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -14.26 (accuracy -16.26, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -13.77 (accuracy -17.07, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -12.38 (accuracy -14.78, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.600, b = 0.012
  Demo 1: a = 0.888, b = 0.068
  Demo 2: a = 0.899, b = 0.067

-- score: -6.37 (accuracy -7.67, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

-- score: -4.71 (accuracy -5.61, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 3.394
  Demo 1: a = -12.393
  Demo 2: a = 1.149

-- score: -4.19 (accuracy -5.29, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.053
  Demo 1: a = -0.902
  Demo 2: a = 0.063

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

