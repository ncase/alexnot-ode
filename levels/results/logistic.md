# logistic

Solved in 0.02 seconds. 63 programs considered, over 5 rounds.

## Winner

-- score: -9.44 (accuracy -11.84, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

## Runner-ups

-- score: -9.04 (accuracy -11.84, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.234, b = 0.074
  Demo 1: a = -0.487, b = 0.017
  Demo 2: a = 0.176, b = 0.291

-- score: -9.04 (accuracy -11.84, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.234, b = 0.074
  Demo 1: a = -0.487, b = 0.017
  Demo 2: a = 0.176, b = 0.291

-- score: -9.04 (accuracy -11.84, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.766, b = 0.074
  Demo 1: a = 1.513, b = 0.017
  Demo 2: a = 2.176, b = 0.291

-- score: -8.55 (accuracy -11.85, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

# The Search

## Round 0 | 0.00s | best score: -8.55

+5 new programs (5 actually scored)
* linear_fit: +2
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -8.55 (accuracy -11.85, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -5.89 (accuracy -7.89, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.495, b = 0.097
  Demo 1: a = 3.193, b = 0.083
  Demo 2: a = 0.873, b = 0.141

-- score: -5.56 (accuracy -6.46, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.825
  Demo 1: a = 1.456
  Demo 2: a = 0.484

-- score: -1.94 (accuracy -3.04, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.075
  Demo 1: a = 0.042
  Demo 2: a = 0.113

-- score: -0.32 (accuracy -1.62, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.006
  Demo 1: a = 0.001
  Demo 2: a = 0.023

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -9.44

+15 new programs (15 actually scored)
* linear_fit: +0
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +8
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -9.44 (accuracy -11.84, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

-- score: -8.55 (accuracy -11.85, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -8.53 (accuracy -11.13, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.458, b = 0.094
  Demo 1: a = -2.945, b = 0.031
  Demo 2: a = 0.129, b = 0.253

-- score: -6.62 (accuracy -8.82, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.459, b = 0.011
  Demo 1: a = 3.022, b = 0.003
  Demo 2: a = 0.867, b = 0.040

-- score: -5.89 (accuracy -7.89, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.495, b = 0.097
  Demo 1: a = 3.193, b = 0.083
  Demo 2: a = 0.873, b = 0.141

-- score: -5.72 (accuracy -8.82, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.322, b = 1.137, c = 0.011
  Demo 1: a = 1.162, b = 1.860, c = 0.003
  Demo 2: a = -0.158, b = 1.025, c = 0.040

-- score: -5.56 (accuracy -6.46, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.825
  Demo 1: a = 1.456
  Demo 2: a = 0.484

-- score: -4.79 (accuracy -7.89, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 1.495, b = 0.379, c = 0.476
  Demo 1: a = 3.193, b = 0.235, c = 0.317
  Demo 2: a = 0.873, b = 0.665, c = 0.806

-- score: -4.66 (accuracy -6.46, token simplicity 0.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b
  Demo 0: a = 1.209, b = 0.384
  Demo 1: a = 2.366, b = 0.910
  Demo 2: a = 0.749, b = 0.265

-- score: -1.94 (accuracy -3.04, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.075
  Demo 1: a = 0.042
  Demo 2: a = 0.113

## Round 2 | 0.01s | best score: -9.44 (stable)

+20 new programs (20 actually scored)
* linear_fit: +3
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +9
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -9.44 (accuracy -11.84, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

-- score: -8.55 (accuracy -11.85, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -8.53 (accuracy -11.13, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.458, b = 0.094
  Demo 1: a = -2.945, b = 0.031
  Demo 2: a = 0.129, b = 0.253

-- score: -7.65 (accuracy -11.85, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.779, b = 0.814, c = 0.779, d = 0.075
  Demo 1: a = 1.556, b = 1.720, c = 0.534, d = 0.018
  Demo 2: a = 0.505, b = 0.509, c = 1.179, d = 0.291

-- score: -7.45 (accuracy -11.85, token simplicity 2.40, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.035, b = 0.817, c = 0.038, d = 0.075
  Demo 1: a = 0.164, b = 0.543, c = 0.009, d = 0.018
  Demo 2: a = 0.004, b = 1.325, c = 0.146, d = 0.291

-- score: -7.11 (accuracy -8.81, token simplicity 1.20, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.099
  Demo 1: a = 0.035
  Demo 2: a = 0.244

-- score: -6.62 (accuracy -8.82, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.459, b = 0.011
  Demo 1: a = 3.022, b = 0.003
  Demo 2: a = 0.867, b = 0.040

-- score: -5.89 (accuracy -7.89, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.495, b = 0.097
  Demo 1: a = 3.193, b = 0.083
  Demo 2: a = 0.873, b = 0.141

-- score: -5.72 (accuracy -8.82, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.322, b = 1.137, c = 0.011
  Demo 1: a = 1.162, b = 1.860, c = 0.003
  Demo 2: a = -0.158, b = 1.025, c = 0.040

-- score: -5.56 (accuracy -6.46, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.825
  Demo 1: a = 1.456
  Demo 2: a = 0.484

## Round 3 | 0.01s | best score: -9.44 (stable)

+15 new programs (15 actually scored)
* linear_fit: +0
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +12
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -9.44 (accuracy -11.84, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

-- score: -8.55 (accuracy -11.85, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -8.53 (accuracy -11.13, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.458, b = 0.094
  Demo 1: a = -2.945, b = 0.031
  Demo 2: a = 0.129, b = 0.253

-- score: -8.34 (accuracy -11.84, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.810, b = 0.045, c = 0.074
  Demo 1: a = 0.532, b = 0.019, c = 0.017
  Demo 2: a = 1.323, b = 0.148, c = 0.291

-- score: -8.15 (accuracy -11.85, token simplicity 2.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.x
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = -0.221, c = 0.075
  Demo 1: a = 0.164, b = -0.466, c = 0.018
  Demo 2: a = 0.004, b = 0.179, c = 0.291

-- score: -8.14 (accuracy -11.84, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.779, b = 0.766, c = 0.074
  Demo 1: a = 1.556, b = 0.513, c = 0.017
  Demo 2: a = 0.505, b = 1.176, c = 0.291

-- score: -7.65 (accuracy -11.85, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.779, b = 0.814, c = 0.779, d = 0.075
  Demo 1: a = 1.556, b = 1.720, c = 0.534, d = 0.018
  Demo 2: a = 0.505, b = 0.509, c = 1.179, d = 0.291

-- score: -7.63 (accuracy -11.13, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x += data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.567, b = 1.025, c = 0.094
  Demo 1: a = 0.165, b = 3.110, c = 0.031
  Demo 2: a = 0.571, b = 0.443, c = 0.253

-- score: -7.45 (accuracy -11.85, token simplicity 2.40, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.035, b = 0.817, c = 0.038, d = 0.075
  Demo 1: a = 0.164, b = 0.543, c = 0.009, d = 0.018
  Demo 2: a = 0.004, b = 1.325, c = 0.146, d = 0.291

-- score: -7.11 (accuracy -8.81, token simplicity 1.20, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.099
  Demo 1: a = 0.035
  Demo 2: a = 0.244

## Round 4 | 0.01s | best score: -9.44 (stable)

+23 new programs (23 actually scored)
* linear_fit: +1
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +15
* delete_lines: +6
* delete_near_zeros: +1
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -9.44 (accuracy -11.84, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.766, b = 0.074
  Demo 1: a = 0.513, b = 0.017
  Demo 2: a = 1.176, b = 0.291

-- score: -9.04 (accuracy -11.84, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.234, b = 0.074
  Demo 1: a = -0.487, b = 0.017
  Demo 2: a = 0.176, b = 0.291

-- score: -8.55 (accuracy -11.85, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = 0.779, c = 0.075
  Demo 1: a = 0.164, b = 0.534, c = 0.018
  Demo 2: a = 0.004, b = 1.179, c = 0.291

-- score: -8.53 (accuracy -11.13, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.458, b = 0.094
  Demo 1: a = -2.945, b = 0.031
  Demo 2: a = 0.129, b = 0.253

-- score: -8.34 (accuracy -11.84, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.810, b = 0.045, c = 0.074
  Demo 1: a = 0.532, b = 0.019, c = 0.017
  Demo 2: a = 1.323, b = 0.148, c = 0.291

-- score: -8.15 (accuracy -11.85, token simplicity 2.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.x
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.035, b = -0.221, c = 0.075
  Demo 1: a = 0.164, b = -0.466, c = 0.018
  Demo 2: a = 0.004, b = 0.179, c = 0.291

-- score: -8.14 (accuracy -11.84, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.779, b = 0.766, c = 0.074
  Demo 1: a = 1.556, b = 0.513, c = 0.017
  Demo 2: a = 0.505, b = 1.176, c = 0.291

-- score: -7.65 (accuracy -11.85, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.779, b = 0.814, c = 0.779, d = 0.075
  Demo 1: a = 1.556, b = 1.720, c = 0.534, d = 0.018
  Demo 2: a = 0.505, b = 0.509, c = 1.179, d = 0.291

-- score: -7.63 (accuracy -11.13, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x += data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.567, b = 1.025, c = 0.094
  Demo 1: a = 0.165, b = 3.110, c = 0.031
  Demo 2: a = 0.571, b = 0.443, c = 0.253

-- score: -7.45 (accuracy -11.85, token simplicity 2.40, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.035, b = 0.817, c = 0.038, d = 0.075
  Demo 1: a = 0.164, b = 0.543, c = 0.009, d = 0.018
  Demo 2: a = 0.004, b = 1.325, c = 0.146, d = 0.291

