# newton

Solved in 0.01 seconds. 11 programs considered, over 3 rounds.

## Winner

-- score: -57.96 (accuracy -59.96, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

## Runner-ups

-- score: -56.96 (accuracy -60.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -56.41 (accuracy -58.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -54.07 (accuracy -56.47, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -53.12 (accuracy -55.92, token simplicity 1.80, parameter simplicity 1.00) --
diff.x -= params.a
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.002, b = 0.003
  Demo 1: a = -0.074, b = 0.001
  Demo 2: a = 1.131, b = 0.050

# The Search

## Round 0 | 0.00s | best score: -57.96

+5 new programs (5 actually scored)
* add_terms: +5
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -57.96 (accuracy -59.96, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -56.96 (accuracy -60.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -41.21 (accuracy -42.51, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

-- score: -37.92 (accuracy -39.02, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = -0.162
  Demo 1: a = -0.126
  Demo 2: a = 0.077

-- score: -20.96 (accuracy -21.86, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = -4.470
  Demo 1: a = -1.897
  Demo 2: a = 2.008

## Round 1 | 0.00s | best score: -57.96

+5 new programs (5 actually scored)
* add_terms: +2
* delete_lines: +2
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 5 parents for the next round

-- score: -57.96 (accuracy -59.96, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -56.96 (accuracy -60.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -56.41 (accuracy -58.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -54.07 (accuracy -56.47, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -53.12 (accuracy -55.92, token simplicity 1.80, parameter simplicity 1.00) --
diff.x -= params.a
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.002, b = 0.003
  Demo 1: a = -0.074, b = 0.001
  Demo 2: a = 1.131, b = 0.050

## Round 2 | 0.00s | best score: -57.96

+5 new programs (5 actually scored)
* add_terms: +1
* delete_lines: +3
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 5 parents for the next round

-- score: -57.96 (accuracy -59.96, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -56.96 (accuracy -60.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -56.41 (accuracy -58.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -54.07 (accuracy -56.47, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -53.12 (accuracy -55.92, token simplicity 1.80, parameter simplicity 1.00) --
diff.x -= params.a
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.002, b = 0.003
  Demo 1: a = -0.074, b = 0.001
  Demo 2: a = 1.131, b = 0.050

