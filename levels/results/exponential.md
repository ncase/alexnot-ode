# exponential

Solved in 0.01 seconds. 35 programs considered, over 4 rounds.

## Winner

-- score: -19.36 (accuracy -20.46, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

## Runner-ups

-- score: -18.96 (accuracy -20.46, token simplicity 1.00, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x
  Demo 0: a = 0.694
  Demo 1: a = 1.511
  Demo 2: a = 0.842

-- score: -18.96 (accuracy -20.46, token simplicity 1.00, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x
  Demo 0: a = 0.694
  Demo 1: a = 1.511
  Demo 2: a = 0.842

-- score: -18.96 (accuracy -20.46, token simplicity 1.00, parameter simplicity 0.50) --
diff.x -= params.a * data.x
diff.x += data.x
  Demo 0: a = 0.694
  Demo 1: a = 1.511
  Demo 2: a = 0.842

-- score: -18.48 (accuracy -20.48, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

# The Search

## Round 0 | 0.00s | best score: -19.36

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

-- score: -19.36 (accuracy -20.46, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

-- score: -18.48 (accuracy -20.48, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

-- score: -17.35 (accuracy -20.65, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.144, b = 0.365, c = -0.003
  Demo 1: a = -0.159, b = -0.315, c = -0.025
  Demo 2: a = 0.424, b = 0.040, c = 0.005

-- score: -16.94 (accuracy -18.24, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.019
  Demo 1: a = -0.071
  Demo 2: a = 0.008

-- score: -8.96 (accuracy -9.86, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 1.972
  Demo 1: a = -1.039
  Demo 2: a = 1.725

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -19.36 (stable)

+10 new programs (10 actually scored)
* linear_fit: +1
* quadratic_fit: +0
* add_single_terms: +1
* delete_interactions: +8
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -19.36 (accuracy -20.46, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

-- score: -18.48 (accuracy -20.48, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

-- score: -18.18 (accuracy -20.58, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.329, b = -0.002
  Demo 1: a = -0.408, b = -0.016
  Demo 2: a = 0.110, b = 0.003

-- score: -17.74 (accuracy -19.94, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.905, b = 0.015
  Demo 1: a = -0.417, b = -0.062
  Demo 2: a = 0.632, b = 0.006

-- score: -17.38 (accuracy -20.48, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 0.012, b = 0.337, c = -0.032
  Demo 1: a = -0.027, b = -0.398, c = -0.108
  Demo 2: a = -0.218, b = 0.103, c = 0.068

-- score: -17.35 (accuracy -20.65, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.144, b = 0.365, c = -0.003
  Demo 1: a = -0.159, b = -0.315, c = -0.025
  Demo 2: a = 0.424, b = 0.040, c = 0.005

-- score: -16.94 (accuracy -18.24, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.019
  Demo 1: a = -0.071
  Demo 2: a = 0.008

-- score: -16.84 (accuracy -19.94, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x * data.x
  Demo 0: a = 0.198, b = 0.707, c = 0.015
  Demo 1: a = -0.131, b = -0.286, c = -0.062
  Demo 2: a = 0.508, b = 0.124, c = 0.006

-- score: -10.45 (accuracy -13.05, token simplicity 1.60, parameter simplicity 1.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.967, b = 0.035
  Demo 1: a = 1.236, b = 0.180
  Demo 2: a = 4.574, b = 0.028

-- score: -8.96 (accuracy -9.86, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 1.972
  Demo 1: a = -1.039
  Demo 2: a = 1.725

## Round 2 | 0.00s | best score: -19.36 (stable)

+14 new programs (14 actually scored)
* linear_fit: +1
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +10
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -19.36 (accuracy -20.46, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

-- score: -18.48 (accuracy -20.48, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

-- score: -18.26 (accuracy -20.46, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x
  Demo 0: a = 0.318, b = -0.012
  Demo 1: a = -0.451, b = -0.060
  Demo 2: a = 0.132, b = 0.025

-- score: -18.18 (accuracy -20.58, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.329, b = -0.002
  Demo 1: a = -0.408, b = -0.016
  Demo 2: a = 0.110, b = 0.003

-- score: -18.08 (accuracy -20.48, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 0.012, b = 0.695
  Demo 1: a = -0.027, b = 1.506
  Demo 2: a = -0.218, b = 0.828

-- score: -17.74 (accuracy -19.94, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.905, b = 0.015
  Demo 1: a = -0.417, b = -0.062
  Demo 2: a = 0.632, b = 0.006

-- score: -17.58 (accuracy -20.48, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
  Demo 0: a = -0.156, b = 0.168, c = 0.305
  Demo 1: a = 0.171, b = -0.199, c = -0.506
  Demo 2: a = -0.269, b = 0.052, c = 0.172

-- score: -17.38 (accuracy -20.48, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 0.012, b = 0.337, c = -0.032
  Demo 1: a = -0.027, b = -0.398, c = -0.108
  Demo 2: a = -0.218, b = 0.103, c = 0.068

-- score: -17.35 (accuracy -20.65, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.144, b = 0.365, c = -0.003
  Demo 1: a = -0.159, b = -0.315, c = -0.025
  Demo 2: a = 0.424, b = 0.040, c = 0.005

-- score: -16.94 (accuracy -18.24, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.019
  Demo 1: a = -0.071
  Demo 2: a = 0.008

## Round 3 | 0.00s | best score: -19.36 (stable)

+10 new programs (10 actually scored)
* linear_fit: +0
* quadratic_fit: +1
* add_single_terms: +1
* delete_interactions: +6
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -19.36 (accuracy -20.46, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

-- score: -18.96 (accuracy -20.46, token simplicity 1.00, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x
  Demo 0: a = 0.694
  Demo 1: a = 1.511
  Demo 2: a = 0.842

-- score: -18.48 (accuracy -20.48, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

-- score: -18.26 (accuracy -20.46, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x
  Demo 0: a = 0.318, b = -0.012
  Demo 1: a = -0.451, b = -0.060
  Demo 2: a = 0.132, b = 0.025

-- score: -18.18 (accuracy -20.58, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.329, b = -0.002
  Demo 1: a = -0.408, b = -0.016
  Demo 2: a = 0.110, b = 0.003

-- score: -18.08 (accuracy -20.48, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 0.012, b = 0.695
  Demo 1: a = -0.027, b = 1.506
  Demo 2: a = -0.218, b = 0.828

-- score: -17.74 (accuracy -19.94, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.905, b = 0.015
  Demo 1: a = -0.417, b = -0.062
  Demo 2: a = 0.632, b = 0.006

-- score: -17.58 (accuracy -20.48, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
  Demo 0: a = -0.156, b = 0.168, c = 0.305
  Demo 1: a = 0.171, b = -0.199, c = -0.506
  Demo 2: a = -0.269, b = 0.052, c = 0.172

-- score: -17.38 (accuracy -20.48, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 0.012, b = 0.337, c = -0.032
  Demo 1: a = -0.027, b = -0.398, c = -0.108
  Demo 2: a = -0.218, b = 0.103, c = 0.068

-- score: -17.35 (accuracy -20.65, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.144, b = 0.365, c = -0.003
  Demo 1: a = -0.159, b = -0.315, c = -0.025
  Demo 2: a = 0.424, b = 0.040, c = 0.005

