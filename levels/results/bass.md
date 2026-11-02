# bass

Solved in 0.04 seconds. 70 programs considered, over 5 rounds.

## Winner

-- score: -11.41 (accuracy -14.41, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.025, b = 0.372
  Demo 1: a = 0.005, b = 0.356
  Demo 2: a = 0.264, b = 0.184

## Runner-ups

-- score: -11.41 (accuracy -14.41, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += (params.b - params.a) * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.025, b = 0.397
  Demo 1: a = 0.005, b = 0.361
  Demo 2: a = 0.264, b = 0.448

-- score: -11.24 (accuracy -14.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -11.04 (accuracy -14.54, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.c + params.b) * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.015
  Demo 1: a = 0.005, b = 0.369, c = 0.010
  Demo 2: a = 0.269, b = 0.154, c = 0.263

-- score: -11.04 (accuracy -14.54, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.c) * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.321
  Demo 1: a = 0.005, b = 0.369, c = 0.375
  Demo 2: a = 0.269, b = 0.154, c = 0.148

# The Search

## Round 0 | 0.00s | best score: -11.24

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

-- score: -11.24 (accuracy -14.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -10.63 (accuracy -13.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

-- score: -10.41 (accuracy -12.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.087, b = 0.061
  Demo 1: a = 0.046, b = 0.023
  Demo 2: a = 0.305, b = 0.296

-- score: -9.86 (accuracy -11.86, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 0.088, b = 0.053
  Demo 1: a = 0.039, b = 0.004
  Demo 2: a = 0.378, b = 0.357

-- score: -6.25 (accuracy -7.15, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.053
  Demo 1: a = 0.037
  Demo 2: a = 0.086

-- score: -2.03 (accuracy -3.13, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.050
  Demo 1: a = 0.045
  Demo 2: a = 0.061

-- score: -0.36 (accuracy -1.66, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.041
  Demo 1: a = 0.036
  Demo 2: a = 0.047

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -11.41

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

-- score: -11.41 (accuracy -14.41, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.025, b = 0.372
  Demo 1: a = 0.005, b = 0.356
  Demo 2: a = 0.264, b = 0.184

-- score: -11.24 (accuracy -14.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -11.02 (accuracy -12.92, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.462
  Demo 1: a = 0.376
  Demo 2: a = 1.044

-- score: -10.63 (accuracy -13.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

-- score: -10.41 (accuracy -12.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.087, b = 0.061
  Demo 1: a = 0.046, b = 0.023
  Demo 2: a = 0.305, b = 0.296

-- score: -9.86 (accuracy -11.86, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 0.088, b = 0.053
  Demo 1: a = 0.039, b = 0.004
  Demo 2: a = 0.378, b = 0.357

-- score: -9.51 (accuracy -12.61, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = -0.110, b = 0.197, c = 0.061
  Demo 1: a = -0.159, b = 0.205, c = 0.023
  Demo 2: a = 0.210, b = 0.095, c = 0.296

-- score: -8.76 (accuracy -11.86, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 0.088, b = 0.315, c = 0.369
  Demo 1: a = 0.039, b = 0.372, c = 0.376
  Demo 2: a = 0.378, b = 0.107, c = 0.464

-- score: -6.25 (accuracy -7.15, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.053
  Demo 1: a = 0.037
  Demo 2: a = 0.086

-- score: -5.35 (accuracy -7.15, token simplicity 0.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b
  Demo 0: a = 0.097, b = 0.044
  Demo 1: a = 0.040, b = 0.003
  Demo 2: a = 0.411, b = 0.325

## Round 2 | 0.01s | best score: -11.41 (stable)

+22 new programs (22 actually scored)
* linear_fit: +3
* quadratic_fit: +3
* add_single_terms: +0
* delete_interactions: +9
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +3
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -11.41 (accuracy -14.41, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.025, b = 0.372
  Demo 1: a = 0.005, b = 0.356
  Demo 2: a = 0.264, b = 0.184

-- score: -11.24 (accuracy -14.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -11.02 (accuracy -12.92, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.462
  Demo 1: a = 0.376
  Demo 2: a = 1.044

-- score: -10.63 (accuracy -13.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

-- score: -10.43 (accuracy -13.03, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= (params.b + params.a) * data.x * data.x
  Demo 0: a = 0.442, b = -0.012
  Demo 1: a = 0.388, b = 0.006
  Demo 2: a = 1.061, b = 0.007

-- score: -10.41 (accuracy -12.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.087, b = 0.061
  Demo 1: a = 0.046, b = 0.023
  Demo 2: a = 0.305, b = 0.296

-- score: -10.34 (accuracy -13.14, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.017, b = 0.373
  Demo 1: a = 0.000, b = 0.376
  Demo 2: a = 0.010, b = 0.985

-- score: -10.34 (accuracy -14.54, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = -0.139, b = 0.167, c = 0.335, d = 0.349
  Demo 1: a = -0.180, b = 0.185, c = 0.369, d = 0.379
  Demo 2: a = 0.192, b = 0.077, c = 0.154, d = 0.417

-- score: -10.31 (accuracy -12.01, token simplicity 1.20, parameter simplicity 0.50) --
diff.x += params.a
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.093
  Demo 1: a = 0.050
  Demo 2: a = 0.309

-- score: -10.21 (accuracy -12.61, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.087, b = -0.026
  Demo 1: a = 0.046, b = -0.023
  Demo 2: a = 0.305, b = -0.009

## Round 3 | 0.01s | best score: -11.41 (stable)

+17 new programs (17 actually scored)
* linear_fit: +3
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +11
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +1
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -11.41 (accuracy -14.41, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.025, b = 0.372
  Demo 1: a = 0.005, b = 0.356
  Demo 2: a = 0.264, b = 0.184

-- score: -11.24 (accuracy -14.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -11.04 (accuracy -14.54, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.c + params.b) * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.015
  Demo 1: a = 0.005, b = 0.369, c = 0.010
  Demo 2: a = 0.269, b = 0.154, c = 0.263

-- score: -11.02 (accuracy -12.92, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.462
  Demo 1: a = 0.376
  Demo 2: a = 1.044

-- score: -10.64 (accuracy -14.54, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += (params.b * params.c)
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = -0.089, b = 0.335, c = 0.349
  Demo 1: a = -0.135, b = 0.369, c = 0.379
  Demo 2: a = 0.205, b = 0.154, c = 0.417

-- score: -10.63 (accuracy -13.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

-- score: -10.43 (accuracy -13.03, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= (params.b + params.a) * data.x * data.x
  Demo 0: a = 0.442, b = -0.012
  Demo 1: a = 0.388, b = 0.006
  Demo 2: a = 1.061, b = 0.007

-- score: -10.41 (accuracy -12.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.087, b = 0.061
  Demo 1: a = 0.046, b = 0.023
  Demo 2: a = 0.305, b = 0.296

-- score: -10.34 (accuracy -13.14, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.017, b = 0.373
  Demo 1: a = 0.000, b = 0.376
  Demo 2: a = 0.010, b = 0.985

-- score: -10.34 (accuracy -14.54, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = -0.139, b = 0.167, c = 0.335, d = 0.349
  Demo 1: a = -0.180, b = 0.185, c = 0.369, d = 0.379
  Demo 2: a = 0.192, b = 0.077, c = 0.154, d = 0.417

## Round 4 | 0.03s | best score: -11.41 (stable)

+11 new programs (11 actually scored)
* linear_fit: +0
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +7
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -11.41 (accuracy -14.41, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.025, b = 0.372
  Demo 1: a = 0.005, b = 0.356
  Demo 2: a = 0.264, b = 0.184

-- score: -11.24 (accuracy -14.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -11.04 (accuracy -14.54, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.c + params.b) * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.015
  Demo 1: a = 0.005, b = 0.369, c = 0.010
  Demo 2: a = 0.269, b = 0.154, c = 0.263

-- score: -11.03 (accuracy -14.03, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += (params.a * params.b)
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.212, b = 0.246
  Demo 1: a = 0.169, b = 0.191
  Demo 2: a = 0.370, b = 0.586

-- score: -11.02 (accuracy -12.92, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.462
  Demo 1: a = 0.376
  Demo 2: a = 1.044

-- score: -10.64 (accuracy -14.54, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += (params.b * params.c)
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = -0.089, b = 0.335, c = 0.349
  Demo 1: a = -0.135, b = 0.369, c = 0.379
  Demo 2: a = 0.205, b = 0.154, c = 0.417

-- score: -10.63 (accuracy -13.03, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

-- score: -10.43 (accuracy -13.03, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= (params.b + params.a) * data.x * data.x
  Demo 0: a = 0.442, b = -0.012
  Demo 1: a = 0.388, b = 0.006
  Demo 2: a = 1.061, b = 0.007

-- score: -10.41 (accuracy -12.61, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.087, b = 0.061
  Demo 1: a = 0.046, b = 0.023
  Demo 2: a = 0.305, b = 0.296

-- score: -10.34 (accuracy -13.14, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.017, b = 0.373
  Demo 1: a = 0.000, b = 0.376
  Demo 2: a = 0.010, b = 0.985

