# newton

Solved in 0.01 seconds. 45 programs considered, over 4 rounds.

## Winner

-- score: -22.47 (accuracy -24.47, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

## Runner-ups

-- score: -22.07 (accuracy -24.47, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += data.x
  Demo 0: a = 6.720, b = 1.314
  Demo 1: a = 0.695, b = 1.151
  Demo 2: a = 10.390, b = 1.464

-- score: -22.07 (accuracy -24.47, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= data.x
diff.x += params.b * data.x
  Demo 0: a = 6.720, b = 0.686
  Demo 1: a = 0.695, b = 0.849
  Demo 2: a = 10.390, b = 0.536

-- score: -21.72 (accuracy -23.92, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -21.57 (accuracy -24.47, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 7.980, b = -1.260, c = 0.314
  Demo 1: a = 0.418, b = 0.277, c = 0.151
  Demo 2: a = 10.505, b = -0.115, c = 0.464

# The Search

## Round 0 | 0.00s | best score: -22.47

+5 new programs (5 actually scored)
* linear_fit: +1
* quadratic_fit: +1
* add_single_terms: +3
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -22.47 (accuracy -24.47, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -21.29 (accuracy -24.59, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -16.05 (accuracy -17.35, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

-- score: -14.83 (accuracy -15.93, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = -0.162
  Demo 1: a = -0.126
  Demo 2: a = 0.077

-- score: -8.02 (accuracy -8.92, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = -4.470
  Demo 1: a = -1.897
  Demo 2: a = 2.008

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -22.47 (stable)

+12 new programs (12 actually scored)
* linear_fit: +1
* quadratic_fit: +0
* add_single_terms: +1
* delete_interactions: +8
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -22.47 (accuracy -24.47, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -21.72 (accuracy -23.92, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -21.37 (accuracy -24.47, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 6.720, b = 0.369, c = 0.055
  Demo 1: a = 0.695, b = 0.111, c = -0.040
  Demo 2: a = 10.390, b = 0.448, c = -0.016

-- score: -21.29 (accuracy -24.59, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -20.82 (accuracy -23.92, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 4.828, b = 4.413, c = 0.003
  Demo 1: a = -0.211, b = 0.352, c = 0.003
  Demo 2: a = 8.957, b = 1.664, c = 0.015

-- score: -20.65 (accuracy -23.05, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -16.05 (accuracy -17.35, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

-- score: -14.83 (accuracy -15.93, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = -0.162
  Demo 1: a = -0.126
  Demo 2: a = 0.077

-- score: -12.67 (accuracy -15.27, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 20.312, b = 0.007
  Demo 1: a = 8.065, b = 0.015
  Demo 2: a = 13.977, b = 0.018

-- score: -8.02 (accuracy -8.92, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = -4.470
  Demo 1: a = -1.897
  Demo 2: a = 2.008

## Round 2 | 0.01s | best score: -22.47 (stable)

+18 new programs (18 actually scored)
* linear_fit: +2
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +11
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -22.47 (accuracy -24.47, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -22.07 (accuracy -24.47, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += data.x
  Demo 0: a = 6.720, b = 1.314
  Demo 1: a = 0.695, b = 1.151
  Demo 2: a = 10.390, b = 1.464

-- score: -21.72 (accuracy -23.92, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -21.57 (accuracy -24.47, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 7.980, b = -1.260, c = 0.314
  Demo 1: a = 0.418, b = 0.277, c = 0.151
  Demo 2: a = 10.505, b = -0.115, c = 0.464

-- score: -21.37 (accuracy -24.47, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 6.720, b = 0.369, c = 0.055
  Demo 1: a = 0.695, b = 0.111, c = -0.040
  Demo 2: a = 10.390, b = 0.448, c = -0.016

-- score: -21.29 (accuracy -24.59, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -20.82 (accuracy -23.92, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 4.828, b = 4.413, c = 0.003
  Demo 1: a = -0.211, b = 0.352, c = 0.003
  Demo 2: a = 8.957, b = 1.664, c = 0.015

-- score: -20.65 (accuracy -23.05, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -20.39 (accuracy -24.59, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = 9.030, b = 0.211, c = 0.422, d = 0.001
  Demo 1: a = 0.105, b = 0.037, c = 0.073, d = -0.001
  Demo 2: a = 10.404, b = 0.217, c = 0.433, d = -0.001

-- score: -20.19 (accuracy -24.59, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = 8.818, b = 0.423, c = 0.001, d = 0.001
  Demo 1: a = 0.068, b = 0.072, c = -0.001, d = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001, d = -0.001

## Round 3 | 0.01s | best score: -22.47 (stable)

+19 new programs (19 actually scored)
* linear_fit: +0
* quadratic_fit: +2
* add_single_terms: +0
* delete_interactions: +12
* delete_lines: +5
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -22.47 (accuracy -24.47, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.720, b = 0.314
  Demo 1: a = 0.695, b = 0.151
  Demo 2: a = 10.390, b = 0.464

-- score: -22.07 (accuracy -24.47, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += data.x
  Demo 0: a = 6.720, b = 1.314
  Demo 1: a = 0.695, b = 1.151
  Demo 2: a = 10.390, b = 1.464

-- score: -21.72 (accuracy -23.92, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.415, b = 0.003
  Demo 1: a = -0.563, b = 0.003
  Demo 2: a = 7.293, b = 0.015

-- score: -21.57 (accuracy -24.47, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 7.980, b = -1.260, c = 0.314
  Demo 1: a = 0.418, b = 0.277, c = 0.151
  Demo 2: a = 10.505, b = -0.115, c = 0.464

-- score: -21.37 (accuracy -24.47, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 6.720, b = 0.369, c = 0.055
  Demo 1: a = 0.695, b = 0.111, c = -0.040
  Demo 2: a = 10.390, b = 0.448, c = -0.016

-- score: -21.29 (accuracy -24.59, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.422, c = 0.001
  Demo 1: a = 0.068, b = 0.073, c = -0.001
  Demo 2: a = 10.188, b = 0.433, c = -0.001

-- score: -20.89 (accuracy -24.59, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= data.x
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 8.818, b = 0.578, c = 0.001
  Demo 1: a = 0.068, b = 0.927, c = -0.001
  Demo 2: a = 10.188, b = 0.567, c = -0.001

-- score: -20.82 (accuracy -23.92, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 4.828, b = 4.413, c = 0.003
  Demo 1: a = -0.211, b = 0.352, c = 0.003
  Demo 2: a = 8.957, b = 1.664, c = 0.015

-- score: -20.65 (accuracy -23.05, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.003, b = 0.003
  Demo 1: a = -0.067, b = 0.002
  Demo 2: a = 0.991, b = 0.046

-- score: -20.47 (accuracy -24.47, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
diff.x += params.d * data.x
  Demo 0: a = 7.980, b = -1.260, c = 0.369, d = 0.055
  Demo 1: a = 0.418, b = 0.277, c = 0.111, d = -0.040
  Demo 2: a = 10.505, b = -0.115, c = 0.448, d = -0.016

