# newton

Solved in 0.01 seconds. 8 programs considered, over 2 rounds.

## Winner

-- score: -13.30 (accuracy -15.30, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

## Runner-ups

-- score: -12.75 (accuracy -14.95, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -12.07 (accuracy -15.37, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -12.01 (accuracy -14.41, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -9.55 (accuracy -10.85, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

# The Search

## Round 0 | 0.00s | best score: -13.30

+5 new programs (5 actually scored)
* add_terms: +5
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -13.30 (accuracy -15.30, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -12.07 (accuracy -15.37, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -9.55 (accuracy -10.85, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

-- score: -8.85 (accuracy -9.95, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = -0.162
  Demo 1: a = -0.126
  Demo 2: a = 0.077

-- score: -4.68 (accuracy -5.58, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = -4.470
  Demo 1: a = -1.897
  Demo 2: a = 2.008

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -13.30 (stable)

+4 new programs (4 actually scored)
* add_terms: +2
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 8 parents for the next round

-- score: -13.30 (accuracy -15.30, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -12.75 (accuracy -14.95, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -12.07 (accuracy -15.37, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -12.01 (accuracy -14.41, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -9.55 (accuracy -10.85, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

-- score: -8.85 (accuracy -9.95, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = -0.162
  Demo 1: a = -0.126
  Demo 2: a = 0.077

-- score: -4.68 (accuracy -5.58, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = -4.470
  Demo 1: a = -1.897
  Demo 2: a = 2.008

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

