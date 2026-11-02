# logistic

Solved in 0.00 seconds. 9 programs considered, over 2 rounds.

## Winner

-- score: -26.62 (accuracy -29.02, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

## Runner-ups

-- score: -26.62 (accuracy -29.02, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

-- score: -25.72 (accuracy -29.02, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -19.41 (accuracy -21.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.459, b = 0.011
  Demo 1: a = 3.022, b = 0.003
  Demo 2: a = 0.867, b = 0.040

-- score: -17.33 (accuracy -19.33, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.495, b = 0.097
  Demo 1: a = 3.193, b = 0.083
  Demo 2: a = 0.873, b = 0.141

# The Search

## Round 0 | 0.00s | best score: -25.72

+5 new programs (5 actually scored)
* add_terms: +5
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -25.72 (accuracy -29.02, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -17.33 (accuracy -19.33, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.495, b = 0.097
  Demo 1: a = 3.193, b = 0.083
  Demo 2: a = 0.873, b = 0.141

-- score: -14.94 (accuracy -15.84, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.825
  Demo 1: a = 1.456
  Demo 2: a = 0.484

-- score: -6.35 (accuracy -7.45, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.075
  Demo 1: a = 0.042
  Demo 2: a = 0.113

-- score: -2.66 (accuracy -3.96, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.006
  Demo 1: a = 0.001
  Demo 2: a = 0.023

## Round 1 | 0.00s | best score: -26.62

+7 new programs (7 actually scored)
* add_terms: +3
* delete_lines: +4
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -26.62 (accuracy -29.02, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

-- score: -25.72 (accuracy -29.02, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -19.41 (accuracy -21.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.459, b = 0.011
  Demo 1: a = 3.022, b = 0.003
  Demo 2: a = 0.867, b = 0.040

-- score: -17.33 (accuracy -19.33, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.495, b = 0.097
  Demo 1: a = 3.193, b = 0.083
  Demo 2: a = 0.873, b = 0.141

-- score: -14.94 (accuracy -15.84, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.825
  Demo 1: a = 1.456
  Demo 2: a = 0.484

