# bass

Solved in 0.05 seconds. 81 programs considered, over 5 rounds.

## Winner

-- score: -36.75 (accuracy -39.75, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.026, b = 0.368
  Demo 1: a = 0.004, b = 0.371
  Demo 2: a = 0.281, b = 0.140

## Runner-ups

-- score: -36.75 (accuracy -39.75, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += (params.b - params.a) * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.026, b = 0.394
  Demo 1: a = 0.004, b = 0.374
  Demo 2: a = 0.281, b = 0.421

-- score: -36.57 (accuracy -39.87, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.369
  Demo 1: a = 0.003, b = 0.380, c = 0.387
  Demo 2: a = 0.283, b = 0.128, c = 0.408

-- score: -36.37 (accuracy -39.87, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.c) * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.340
  Demo 1: a = 0.003, b = 0.380, c = 0.384
  Demo 2: a = 0.283, b = 0.128, c = 0.125

-- score: -36.37 (accuracy -39.87, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.c + params.b) * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.022
  Demo 1: a = 0.003, b = 0.380, c = 0.007
  Demo 2: a = 0.283, b = 0.128, c = 0.280

# The Search

## Round 0 | 0.00s | best score: -36.57

+7 new programs (7 actually scored)
* linear_fit: +2
* quadratic_fit: +4
* add_single_terms: +1
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 8 parents for the next round

-- score: -36.57 (accuracy -39.87, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.369
  Demo 1: a = 0.003, b = 0.380, c = 0.387
  Demo 2: a = 0.283, b = 0.128, c = 0.408

-- score: -31.63 (accuracy -34.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.456, b = 0.452
  Demo 1: a = 0.393, b = 0.397
  Demo 2: a = 1.075, b = 1.087

-- score: -30.57 (accuracy -32.77, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.088, b = 0.066
  Demo 1: a = 0.046, b = 0.020
  Demo 2: a = 0.313, b = 0.307

-- score: -28.11 (accuracy -30.11, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 0.090, b = 0.058
  Demo 1: a = 0.039, b = 0.002
  Demo 2: a = 0.388, b = 0.371

-- score: -15.46 (accuracy -16.36, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.052
  Demo 1: a = 0.038
  Demo 2: a = 0.085

-- score: -5.72 (accuracy -6.82, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.049
  Demo 1: a = 0.047
  Demo 2: a = 0.059

-- score: -2.21 (accuracy -3.51, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.040
  Demo 1: a = 0.039
  Demo 2: a = 0.045

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -36.75

+18 new programs (18 actually scored)
* linear_fit: +0
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +12
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +2
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -36.75 (accuracy -39.75, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.026, b = 0.368
  Demo 1: a = 0.004, b = 0.371
  Demo 2: a = 0.281, b = 0.140

-- score: -36.57 (accuracy -39.87, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.369
  Demo 1: a = 0.003, b = 0.380, c = 0.387
  Demo 2: a = 0.283, b = 0.128, c = 0.408

-- score: -31.96 (accuracy -33.86, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.463
  Demo 1: a = 0.385
  Demo 2: a = 1.044

-- score: -31.63 (accuracy -34.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.456, b = 0.452
  Demo 1: a = 0.393, b = 0.397
  Demo 2: a = 1.075, b = 1.087

-- score: -30.57 (accuracy -32.77, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.088, b = 0.066
  Demo 1: a = 0.046, b = 0.020
  Demo 2: a = 0.313, b = 0.307

-- score: -29.67 (accuracy -32.77, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = -0.115, b = 0.203, c = 0.066
  Demo 1: a = -0.165, b = 0.212, c = 0.020
  Demo 2: a = 0.234, b = 0.079, c = 0.307

-- score: -28.11 (accuracy -30.11, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 0.090, b = 0.058
  Demo 1: a = 0.039, b = 0.002
  Demo 2: a = 0.388, b = 0.371

-- score: -27.01 (accuracy -30.11, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 0.090, b = 0.329, c = 0.387
  Demo 1: a = 0.039, b = 0.383, c = 0.384
  Demo 2: a = 0.388, b = 0.083, c = 0.453

-- score: -16.11 (accuracy -18.71, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.084, b = 0.938
  Demo 1: a = -0.067, b = 0.986
  Demo 2: a = 0.079, b = 1.097

-- score: -15.95 (accuracy -18.55, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x * data.x
  Demo 0: a = -0.077, b = 1.040
  Demo 1: a = -0.054, b = 0.985
  Demo 2: a = 0.129, b = 0.851

## Round 2 | 0.01s | best score: -36.75 (stable)

+21 new programs (21 actually scored)
* linear_fit: +2
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +11
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +3
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -36.75 (accuracy -39.75, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.026, b = 0.368
  Demo 1: a = 0.004, b = 0.371
  Demo 2: a = 0.281, b = 0.140

-- score: -36.57 (accuracy -39.87, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.369
  Demo 1: a = 0.003, b = 0.380, c = 0.387
  Demo 2: a = 0.283, b = 0.128, c = 0.408

-- score: -35.67 (accuracy -39.87, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = -0.145, b = 0.173, c = 0.347, d = 0.369
  Demo 1: a = -0.187, b = 0.190, c = 0.380, d = 0.387
  Demo 2: a = 0.219, b = 0.064, c = 0.128, d = 0.408

-- score: -35.47 (accuracy -39.87, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.028, b = 0.531, c = 0.184, d = 0.369
  Demo 1: a = 0.003, b = 0.574, c = 0.193, d = 0.387
  Demo 2: a = 0.283, b = 0.332, c = 0.204, d = 0.408

-- score: -31.96 (accuracy -33.86, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.463
  Demo 1: a = 0.385
  Demo 2: a = 1.044

-- score: -31.63 (accuracy -34.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.456, b = 0.452
  Demo 1: a = 0.393, b = 0.397
  Demo 2: a = 1.075, b = 1.087

-- score: -31.43 (accuracy -34.03, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= (params.b + params.a) * data.x * data.x
  Demo 0: a = 0.456, b = -0.004
  Demo 1: a = 0.393, b = 0.004
  Demo 2: a = 1.075, b = 0.012

-- score: -31.38 (accuracy -34.18, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.011, b = 0.403
  Demo 1: a = -0.000, b = 0.385
  Demo 2: a = 0.007, b = 1.004

-- score: -30.57 (accuracy -32.77, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.088, b = 0.066
  Demo 1: a = 0.046, b = 0.020
  Demo 2: a = 0.313, b = 0.307

-- score: -30.37 (accuracy -32.77, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.088, b = -0.022
  Demo 1: a = 0.046, b = -0.026
  Demo 2: a = 0.313, b = -0.005

## Round 3 | 0.01s | best score: -36.75 (stable)

+24 new programs (24 actually scored)
* linear_fit: +2
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +16
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +1
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -36.75 (accuracy -39.75, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.026, b = 0.368
  Demo 1: a = 0.004, b = 0.371
  Demo 2: a = 0.281, b = 0.140

-- score: -36.57 (accuracy -39.87, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.369
  Demo 1: a = 0.003, b = 0.380, c = 0.387
  Demo 2: a = 0.283, b = 0.128, c = 0.408

-- score: -36.37 (accuracy -39.87, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.c) * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.340
  Demo 1: a = 0.003, b = 0.380, c = 0.384
  Demo 2: a = 0.283, b = 0.128, c = 0.125

-- score: -36.17 (accuracy -39.87, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 1.347, c = 0.369
  Demo 1: a = 0.003, b = 1.380, c = 0.387
  Demo 2: a = 0.283, b = 1.128, c = 0.408

-- score: -35.97 (accuracy -39.87, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += (params.b * params.c)
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = -0.099, b = 0.347, c = 0.369
  Demo 1: a = -0.144, b = 0.380, c = 0.387
  Demo 2: a = 0.231, b = 0.128, c = 0.408

-- score: -35.67 (accuracy -39.87, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = -0.145, b = 0.173, c = 0.347, d = 0.369
  Demo 1: a = -0.187, b = 0.190, c = 0.380, d = 0.387
  Demo 2: a = 0.219, b = 0.064, c = 0.128, d = 0.408

-- score: -35.47 (accuracy -39.87, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.028, b = 0.531, c = 0.184, d = 0.369
  Demo 1: a = 0.003, b = 0.574, c = 0.193, d = 0.387
  Demo 2: a = 0.283, b = 0.332, c = 0.204, d = 0.408

-- score: -31.96 (accuracy -33.86, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.463
  Demo 1: a = 0.385
  Demo 2: a = 1.044

-- score: -31.63 (accuracy -34.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.456, b = 0.452
  Demo 1: a = 0.393, b = 0.397
  Demo 2: a = 1.075, b = 1.087

-- score: -31.43 (accuracy -34.03, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= (params.b + params.a) * data.x * data.x
  Demo 0: a = 0.456, b = -0.004
  Demo 1: a = 0.393, b = 0.004
  Demo 2: a = 1.075, b = 0.012

## Round 4 | 0.03s | best score: -36.75 (stable)

+16 new programs (16 actually scored)
* linear_fit: +0
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +10
* delete_lines: +6
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -36.75 (accuracy -39.75, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.026, b = 0.368
  Demo 1: a = 0.004, b = 0.371
  Demo 2: a = 0.281, b = 0.140

-- score: -36.57 (accuracy -39.87, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.369
  Demo 1: a = 0.003, b = 0.380, c = 0.387
  Demo 2: a = 0.283, b = 0.128, c = 0.408

-- score: -36.37 (accuracy -39.87, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.c) * data.x * data.x
  Demo 0: a = 0.028, b = 0.347, c = 0.340
  Demo 1: a = 0.003, b = 0.380, c = 0.384
  Demo 2: a = 0.283, b = 0.128, c = 0.125

-- score: -36.17 (accuracy -39.87, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 1.347, c = 0.369
  Demo 1: a = 0.003, b = 1.380, c = 0.387
  Demo 2: a = 0.283, b = 1.128, c = 0.408

-- score: -35.97 (accuracy -39.87, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += (params.b * params.c)
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = -0.099, b = 0.347, c = 0.369
  Demo 1: a = -0.144, b = 0.380, c = 0.387
  Demo 2: a = 0.231, b = 0.128, c = 0.408

-- score: -35.67 (accuracy -39.87, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = -0.145, b = 0.173, c = 0.347, d = 0.369
  Demo 1: a = -0.187, b = 0.190, c = 0.380, d = 0.387
  Demo 2: a = 0.219, b = 0.064, c = 0.128, d = 0.408

-- score: -35.47 (accuracy -39.87, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.028, b = 0.531, c = 0.184, d = 0.369
  Demo 1: a = 0.003, b = 0.574, c = 0.193, d = 0.387
  Demo 2: a = 0.283, b = 0.332, c = 0.204, d = 0.408

-- score: -34.67 (accuracy -37.67, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += (params.a * params.b)
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.213, b = 0.254
  Demo 1: a = 0.170, b = 0.188
  Demo 2: a = 0.373, b = 0.600

-- score: -31.96 (accuracy -33.86, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.463
  Demo 1: a = 0.385
  Demo 2: a = 1.044

-- score: -31.63 (accuracy -34.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.456, b = 0.452
  Demo 1: a = 0.393, b = 0.397
  Demo 2: a = 1.075, b = 1.087

