# drag

Solved in 0.02 seconds. 62 programs considered, over 5 rounds.

## Winner

-- score: -60.58 (accuracy -62.78, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

## Runner-ups

-- score: -60.58 (accuracy -62.78, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

-- score: -59.78 (accuracy -62.78, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

-- score: -59.68 (accuracy -62.78, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.828, b = -0.258, c = 0.004
  Demo 1: a = 5.787, b = 4.139, c = 0.051
  Demo 2: a = 3.534, b = 0.095, c = 0.019

-- score: -59.68 (accuracy -62.78, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.909, b = 1.340, c = 0.004
  Demo 1: a = 26.730, b = 16.805, c = 0.051
  Demo 2: a = 4.234, b = 0.605, c = 0.019

# The Search

## Round 0 | 0.00s | best score: -59.62

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

-- score: -59.62 (accuracy -62.92, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.046, b = -0.041, c = 0.003
  Demo 1: a = 2.303, b = 0.655, c = 0.062
  Demo 2: a = 3.485, b = 0.046, c = 0.022

-- score: -57.10 (accuracy -59.10, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 12.021, b = 0.228
  Demo 1: a = 40.816, b = 2.719
  Demo 2: a = 4.524, b = 0.316

-- score: -21.61 (accuracy -22.91, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

-- score: -14.92 (accuracy -15.82, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 3.338
  Demo 1: a = -12.157
  Demo 2: a = 1.139

-- score: -12.64 (accuracy -13.74, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.051
  Demo 1: a = -0.891
  Demo 2: a = 0.061

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -60.58

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

-- score: -60.58 (accuracy -62.78, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

-- score: -59.68 (accuracy -62.78, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.828, b = -0.258, c = 0.004
  Demo 1: a = 5.787, b = 4.139, c = 0.051
  Demo 2: a = 3.534, b = 0.095, c = 0.019

-- score: -59.62 (accuracy -62.92, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.046, b = -0.041, c = 0.003
  Demo 1: a = 2.303, b = 0.655, c = 0.062
  Demo 2: a = 3.485, b = 0.046, c = 0.022

-- score: -57.10 (accuracy -59.10, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 12.021, b = 0.228
  Demo 1: a = 40.816, b = 2.719
  Demo 2: a = 4.524, b = 0.316

-- score: -56.00 (accuracy -59.10, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 12.021, b = 0.133, c = 0.095
  Demo 1: a = 40.816, b = 1.001, c = 1.718
  Demo 2: a = 4.524, b = 0.124, c = 0.192

-- score: -48.17 (accuracy -50.57, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.634, b = 0.013
  Demo 1: a = 0.847, b = 0.066
  Demo 2: a = 0.908, b = 0.068

-- score: -43.91 (accuracy -46.51, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -2.105, b = 0.020
  Demo 1: a = -1.720, b = 0.069
  Demo 2: a = 0.458, b = 0.078

-- score: -21.61 (accuracy -22.91, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.001
  Demo 1: a = -0.039
  Demo 2: a = 0.004

-- score: -14.92 (accuracy -15.82, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 3.338
  Demo 1: a = -12.157
  Demo 2: a = 1.139

-- score: -14.02 (accuracy -15.82, token simplicity 0.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b
  Demo 0: a = 7.794, b = 4.455
  Demo 1: a = 15.689, b = 27.846
  Demo 2: a = 2.989, b = 1.850

## Round 2 | 0.01s | best score: -60.58 (stable)

+21 new programs (21 actually scored)
* linear_fit: +2
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +11
* delete_lines: +5
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -60.58 (accuracy -62.78, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

-- score: -59.68 (accuracy -62.78, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.828, b = -0.258, c = 0.004
  Demo 1: a = 5.787, b = 4.139, c = 0.051
  Demo 2: a = 3.534, b = 0.095, c = 0.019

-- score: -59.62 (accuracy -62.92, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.046, b = -0.041, c = 0.003
  Demo 1: a = 2.303, b = 0.655, c = 0.062
  Demo 2: a = 3.485, b = 0.046, c = 0.022

-- score: -58.72 (accuracy -62.92, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.066, b = -0.020, c = -0.041, d = 0.003
  Demo 1: a = 1.976, b = 0.327, c = 0.655, d = 0.062
  Demo 2: a = 3.462, b = 0.023, c = 0.046, d = 0.022

-- score: -58.52 (accuracy -62.92, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.046, b = -0.039, c = 0.002, d = 0.003
  Demo 1: a = 2.303, b = 0.686, c = 0.031, d = 0.062
  Demo 2: a = 3.485, b = 0.057, c = 0.011, d = 0.022

-- score: -57.10 (accuracy -59.10, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 12.021, b = 0.228
  Demo 1: a = 40.816, b = 2.719
  Demo 2: a = 4.524, b = 0.316

-- score: -56.70 (accuracy -59.10, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 12.021, b = 1.228
  Demo 1: a = 40.816, b = 3.719
  Demo 2: a = 4.524, b = 1.316

-- score: -56.20 (accuracy -59.10, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 11.054, b = 0.967, c = 0.228
  Demo 1: a = 21.233, b = 19.584, c = 2.719
  Demo 2: a = 3.981, b = 0.542, c = 0.316

-- score: -56.00 (accuracy -59.10, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 12.021, b = 0.133, c = 0.095
  Demo 1: a = 40.816, b = 1.001, c = 1.718
  Demo 2: a = 4.524, b = 0.124, c = 0.192

-- score: -48.17 (accuracy -50.57, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.634, b = 0.013
  Demo 1: a = 0.847, b = 0.066
  Demo 2: a = 0.908, b = 0.068

## Round 3 | 0.01s | best score: -60.58 (stable)

+19 new programs (19 actually scored)
* linear_fit: +0
* quadratic_fit: +2
* add_single_terms: +0
* delete_interactions: +13
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -60.58 (accuracy -62.78, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

-- score: -59.68 (accuracy -62.78, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.828, b = -0.258, c = 0.004
  Demo 1: a = 5.787, b = 4.139, c = 0.051
  Demo 2: a = 3.534, b = 0.095, c = 0.019

-- score: -59.62 (accuracy -62.92, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.046, b = -0.041, c = 0.003
  Demo 1: a = 2.303, b = 0.655, c = 0.062
  Demo 2: a = 3.485, b = 0.046, c = 0.022

-- score: -59.22 (accuracy -62.92, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.046, b = 0.959, c = 0.003
  Demo 1: a = 2.303, b = 1.655, c = 0.062
  Demo 2: a = 3.485, b = 1.046, c = 0.022

-- score: -58.78 (accuracy -62.78, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c
diff.x -= params.d * data.x * data.x
  Demo 0: a = 9.921, b = -0.165, c = -0.186, d = 0.004
  Demo 1: a = 4.299, b = 2.650, c = 2.977, d = 0.051
  Demo 2: a = 3.495, b = 0.056, c = 0.079, d = 0.019

-- score: -58.72 (accuracy -62.92, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.066, b = -0.020, c = -0.041, d = 0.003
  Demo 1: a = 1.976, b = 0.327, c = 0.655, d = 0.062
  Demo 2: a = 3.462, b = 0.023, c = 0.046, d = 0.022

-- score: -58.52 (accuracy -62.92, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.046, b = -0.039, c = 0.002, d = 0.003
  Demo 1: a = 2.303, b = 0.686, c = 0.031, d = 0.062
  Demo 2: a = 3.485, b = 0.057, c = 0.011, d = 0.022

-- score: -57.10 (accuracy -59.10, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 12.021, b = 0.228
  Demo 1: a = 40.816, b = 2.719
  Demo 2: a = 4.524, b = 0.316

-- score: -56.70 (accuracy -59.10, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 12.021, b = 1.228
  Demo 1: a = 40.816, b = 3.719
  Demo 2: a = 4.524, b = 1.316

-- score: -56.20 (accuracy -59.10, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 11.054, b = 0.967, c = 0.228
  Demo 1: a = 21.233, b = 19.584, c = 2.719
  Demo 2: a = 3.981, b = 0.542, c = 0.316

## Round 4 | 0.00s | best score: -60.58 (stable)

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

-- score: -60.58 (accuracy -62.78, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

-- score: -59.78 (accuracy -62.78, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 9.570, b = 0.004
  Demo 1: a = 9.926, b = 0.051
  Demo 2: a = 3.629, b = 0.019

-- score: -59.68 (accuracy -62.78, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.828, b = -0.258, c = 0.004
  Demo 1: a = 5.787, b = 4.139, c = 0.051
  Demo 2: a = 3.534, b = 0.095, c = 0.019

-- score: -59.62 (accuracy -62.92, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.046, b = -0.041, c = 0.003
  Demo 1: a = 2.303, b = 0.655, c = 0.062
  Demo 2: a = 3.485, b = 0.046, c = 0.022

-- score: -59.28 (accuracy -62.78, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.917, b = -0.174, c = 0.004
  Demo 1: a = 4.364, b = 2.781, c = 0.051
  Demo 2: a = 3.500, b = 0.065, c = 0.019

-- score: -59.22 (accuracy -62.92, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 10.046, b = 0.959, c = 0.003
  Demo 1: a = 2.303, b = 1.655, c = 0.062
  Demo 2: a = 3.485, b = 1.046, c = 0.022

-- score: -59.08 (accuracy -62.78, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += (params.b + params.c)
diff.x -= params.c * data.x * data.x
  Demo 0: a = 9.916, b = -0.175, c = 0.004
  Demo 1: a = 4.354, b = 2.761, c = 0.051
  Demo 2: a = 3.496, b = 0.057, c = 0.019

-- score: -58.78 (accuracy -62.78, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c
diff.x -= params.d * data.x * data.x
  Demo 0: a = 9.921, b = -0.165, c = -0.186, d = 0.004
  Demo 1: a = 4.299, b = 2.650, c = 2.977, d = 0.051
  Demo 2: a = 3.495, b = 0.056, c = 0.079, d = 0.019

-- score: -58.72 (accuracy -62.92, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.066, b = -0.020, c = -0.041, d = 0.003
  Demo 1: a = 1.976, b = 0.327, c = 0.655, d = 0.062
  Demo 2: a = 3.462, b = 0.023, c = 0.046, d = 0.022

-- score: -58.52 (accuracy -62.92, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 10.046, b = -0.039, c = 0.002, d = 0.003
  Demo 1: a = 2.303, b = 0.686, c = 0.031, d = 0.062
  Demo 2: a = 3.485, b = 0.057, c = 0.011, d = 0.022

