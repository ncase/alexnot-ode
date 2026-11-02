# drag

Solved in 0.02 seconds. 59 programs considered, over 5 rounds.

## Winner

-- score: -24.95 (accuracy -27.15, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

## Runner-ups

-- score: -24.15 (accuracy -27.15, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -24.05 (accuracy -27.15, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.846, b = -0.527, c = 0.004
  Demo 1: a = 0.998, b = 9.167, c = 0.052
  Demo 2: a = 3.389, b = 0.155, c = 0.019

-- score: -24.01 (accuracy -26.01, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -24.01 (accuracy -27.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

# The Search

## Round 0 | 0.00s | best score: -24.01

+5 new programs (5 actually scored)
* linear_fit: +1
* quadratic_fit: +2
* add_single_terms: +2
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -24.01 (accuracy -26.01, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -24.01 (accuracy -27.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -10.97 (accuracy -12.27, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

-- score: -8.07 (accuracy -8.97, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 3.394
  Demo 1: a = -12.393
  Demo 2: a = 1.149

-- score: -7.37 (accuracy -8.47, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.053
  Demo 1: a = -0.902
  Demo 2: a = 0.063

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -24.95

+14 new programs (14 actually scored)
* linear_fit: +0
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +8
* delete_lines: +3
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -24.95 (accuracy -27.15, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -24.05 (accuracy -27.15, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.846, b = -0.527, c = 0.004
  Demo 1: a = 0.998, b = 9.167, c = 0.052
  Demo 2: a = 3.389, b = 0.155, c = 0.019

-- score: -24.01 (accuracy -26.01, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -24.01 (accuracy -27.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -22.91 (accuracy -26.01, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 11.781, b = 0.150, c = 0.070
  Demo 1: a = 41.074, b = 0.606, c = 2.135
  Demo 2: a = 4.397, b = 0.103, c = 0.200

-- score: -21.24 (accuracy -23.64, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.600, b = 0.012
  Demo 1: a = 0.888, b = 0.068
  Demo 2: a = 0.899, b = 0.067

-- score: -19.05 (accuracy -21.65, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -2.598, b = 0.019
  Demo 1: a = -1.468, b = 0.070
  Demo 2: a = 0.375, b = 0.077

-- score: -10.97 (accuracy -12.27, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

-- score: -8.07 (accuracy -8.97, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 3.394
  Demo 1: a = -12.393
  Demo 2: a = 1.149

-- score: -7.37 (accuracy -8.47, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.053
  Demo 1: a = -0.902
  Demo 2: a = 0.063

## Round 2 | 0.00s | best score: -24.95 (stable)

+17 new programs (17 actually scored)
* linear_fit: +1
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +11
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -24.95 (accuracy -27.15, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -24.05 (accuracy -27.15, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.846, b = -0.527, c = 0.004
  Demo 1: a = 0.998, b = 9.167, c = 0.052
  Demo 2: a = 3.389, b = 0.155, c = 0.019

-- score: -24.01 (accuracy -26.01, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -24.01 (accuracy -27.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -23.61 (accuracy -26.01, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 1.220
  Demo 1: a = 41.074, b = 3.742
  Demo 2: a = 4.397, b = 1.303

-- score: -23.11 (accuracy -26.01, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x
  Demo 0: a = 11.856, b = 0.075, c = 0.220
  Demo 1: a = 41.377, b = 0.303, c = 2.742
  Demo 2: a = 4.448, b = 0.051, c = 0.303

-- score: -23.11 (accuracy -27.31, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.333, b = -0.041, c = -0.082, d = 0.002
  Demo 1: a = -7.443, b = 0.726, c = 1.451, d = 0.078
  Demo 2: a = 3.271, b = 0.037, c = 0.074, d = 0.023

-- score: -22.91 (accuracy -26.01, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 11.781, b = 0.150, c = 0.070
  Demo 1: a = 41.074, b = 0.606, c = 2.135
  Demo 2: a = 4.397, b = 0.103, c = 0.200

-- score: -22.91 (accuracy -27.31, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.292, b = -0.080, c = 0.001, d = 0.002
  Demo 1: a = -6.718, b = 1.490, c = 0.039, d = 0.078
  Demo 2: a = 3.309, b = 0.086, c = 0.011, d = 0.023

-- score: -21.24 (accuracy -23.64, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.600, b = 0.012
  Demo 1: a = 0.888, b = 0.068
  Demo 2: a = 0.899, b = 0.067

## Round 3 | 0.01s | best score: -24.95 (stable)

+21 new programs (21 actually scored)
* linear_fit: +0
* quadratic_fit: +2
* add_single_terms: +0
* delete_interactions: +14
* delete_lines: +5
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -24.95 (accuracy -27.15, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -24.05 (accuracy -27.15, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.846, b = -0.527, c = 0.004
  Demo 1: a = 0.998, b = 9.167, c = 0.052
  Demo 2: a = 3.389, b = 0.155, c = 0.019

-- score: -24.01 (accuracy -26.01, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -24.01 (accuracy -27.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -23.61 (accuracy -26.01, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 1.220
  Demo 1: a = 41.074, b = 3.742
  Demo 2: a = 4.397, b = 1.303

-- score: -23.61 (accuracy -27.31, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = 0.918, c = 0.002
  Demo 1: a = -6.718, b = 2.451, c = 0.078
  Demo 2: a = 3.309, b = 1.074, c = 0.023

-- score: -23.15 (accuracy -27.15, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.036, b = -0.338, c = -0.379, d = 0.004
  Demo 1: a = -2.300, b = 5.869, c = 6.595, d = 0.052
  Demo 2: a = 3.325, b = 0.091, c = 0.128, d = 0.019

-- score: -23.11 (accuracy -26.01, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x
  Demo 0: a = 11.856, b = 0.075, c = 0.220
  Demo 1: a = 41.377, b = 0.303, c = 2.742
  Demo 2: a = 4.448, b = 0.051, c = 0.303

-- score: -23.11 (accuracy -27.31, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.333, b = -0.041, c = -0.082, d = 0.002
  Demo 1: a = -7.443, b = 0.726, c = 1.451, d = 0.078
  Demo 2: a = 3.271, b = 0.037, c = 0.074, d = 0.023

-- score: -22.91 (accuracy -26.01, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 11.781, b = 0.150, c = 0.070
  Demo 1: a = 41.074, b = 0.606, c = 2.135
  Demo 2: a = 4.397, b = 0.103, c = 0.200

## Round 4 | 0.00s | best score: -24.95 (stable)

+13 new programs (13 actually scored)
* linear_fit: +1
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +6
* delete_lines: +3
* delete_near_zeros: +0
* relate_parameters: +2
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -24.95 (accuracy -27.15, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -24.15 (accuracy -27.15, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.319, b = 0.004
  Demo 1: a = 10.165, b = 0.052
  Demo 2: a = 3.545, b = 0.019

-- score: -24.05 (accuracy -27.15, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.846, b = -0.527, c = 0.004
  Demo 1: a = 0.998, b = 9.167, c = 0.052
  Demo 2: a = 3.389, b = 0.155, c = 0.019

-- score: -24.01 (accuracy -26.01, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 0.220
  Demo 1: a = 41.074, b = 2.742
  Demo 2: a = 4.397, b = 0.303

-- score: -24.01 (accuracy -27.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = -0.082, c = 0.002
  Demo 1: a = -6.718, b = 1.451, c = 0.078
  Demo 2: a = 3.309, b = 0.074, c = 0.023

-- score: -23.65 (accuracy -27.15, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.027, b = -0.354, c = 0.004
  Demo 1: a = -2.154, b = 6.160, c = 0.052
  Demo 2: a = 3.333, b = 0.106, c = 0.019

-- score: -23.61 (accuracy -26.01, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 11.781, b = 1.220
  Demo 1: a = 41.074, b = 3.742
  Demo 2: a = 4.397, b = 1.303

-- score: -23.61 (accuracy -27.31, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.292, b = 0.918, c = 0.002
  Demo 1: a = -6.718, b = 2.451, c = 0.078
  Demo 2: a = 3.309, b = 1.074, c = 0.023

-- score: -23.45 (accuracy -27.15, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += (params.b + params.c)
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.027, b = -0.356, c = 0.004
  Demo 1: a = -2.165, b = 6.139, c = 0.052
  Demo 2: a = 3.329, b = 0.099, c = 0.019

-- score: -23.15 (accuracy -27.15, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.036, b = -0.338, c = -0.379, d = 0.004
  Demo 1: a = -2.300, b = 5.869, c = 6.595, d = 0.052
  Demo 2: a = 3.325, b = 0.091, c = 0.128, d = 0.019

