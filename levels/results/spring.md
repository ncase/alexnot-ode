# spring

Solved in 0.30 seconds. 515 programs considered, over 5 rounds.

## Winner

-- score: -128.69 (accuracy -131.29, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

## Runner-ups

-- score: -128.29 (accuracy -131.29, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= data.y
  Demo 0: a = 3.859, b = 0.652
  Demo 1: a = 1.533, b = 0.688
  Demo 2: a = 8.415, b = 0.423

-- score: -128.29 (accuracy -131.29, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += data.y
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 1.348
  Demo 1: a = 1.533, b = 1.312
  Demo 2: a = 8.415, b = 1.577

-- score: -128.29 (accuracy -131.29, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += data.x
diff.y -= params.b * data.y
  Demo 0: a = 4.859, b = 0.348
  Demo 1: a = 2.533, b = 0.312
  Demo 2: a = 9.415, b = 0.577

-- score: -128.24 (accuracy -131.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

# The Search

## Round 0 | 0.01s | best score: -128.24

+24 new programs (24 actually scored)
* linear_fit: +5
* quadratic_fit: +7
* add_single_terms: +12
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -128.24 (accuracy -131.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -127.39 (accuracy -131.59, token simplicity 2.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.018, b = 1.036, c = 3.859, d = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 1.533, d = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 8.415, d = 0.577

-- score: -126.99 (accuracy -131.59, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 3.824, c = 0.136, d = 0.350
  Demo 1: a = 0.967, b = 1.533, c = 0.009, d = 0.314
  Demo 2: a = 1.034, b = 8.348, c = 0.091, d = 0.580

-- score: -126.39 (accuracy -131.69, token simplicity 2.80, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 3.859, e = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 1.533, e = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 8.415, e = 0.577

-- score: -126.34 (accuracy -131.64, token simplicity 2.80, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = -0.035, b = 1.038, c = 0.000, d = 3.859, e = 0.348
  Demo 1: a = 0.039, b = 0.968, c = 0.011, d = 1.530, e = 0.312
  Demo 2: a = 0.016, b = 1.035, c = 0.123, d = 8.429, e = 0.584

-- score: -125.50 (accuracy -131.70, token simplicity 3.20, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d
diff.y -= params.e * data.x
diff.y -= params.f * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 0.000, e = 3.859, f = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 0.011, e = 1.530, f = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 0.123, e = 8.429, f = 0.584

-- score: -124.93 (accuracy -131.73, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.041, b = 0.016, c = 3.828, d = 0.154, e = 0.178, f = 0.343
  Demo 1: a = 0.967, b = 0.038, c = 1.548, d = 0.069, e = 0.011, f = 0.312
  Demo 2: a = 1.034, b = 0.271, c = 8.358, d = 0.270, e = 0.120, f = 0.573

-- score: -121.79 (accuracy -132.09, token simplicity 5.80, parameter simplicity 4.50) --
diff.x -= params.a
diff.x += params.b * data.x * data.x
diff.x += params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
diff.y += params.i * data.y * data.y
  Demo 0: a = 0.036, b = 0.109, c = 1.041, d = 0.007, e = 3.835, f = 0.136, g = 0.151, h = 0.361, i = -0.041
  Demo 1: a = 0.026, b = 0.049, c = 0.969, d = 0.002, e = 1.537, f = 0.058, g = 0.021, h = 0.310, i = -0.057
  Demo 2: a = 0.062, b = 0.051, c = 1.036, d = -0.493, e = 8.356, f = 0.345, g = 0.150, h = 0.538, i = 0.028

-- score: -119.58 (accuracy -132.28, token simplicity 7.20, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = -0.034, b = -0.048, c = 0.126, d = 1.034, e = -0.009, f = 0.007, g = 3.835, h = 0.136, i = 0.151, j = 0.361, k = -0.041
  Demo 1: a = 0.007, b = 0.041, c = 0.026, d = 0.972, e = -0.042, f = 0.002, g = 1.537, h = 0.058, i = 0.021, j = 0.310, k = -0.057
  Demo 2: a = -0.089, b = 0.006, c = 0.057, d = 1.041, e = 0.004, f = -0.493, g = 8.356, h = 0.345, i = 0.150, j = 0.538, k = 0.028

-- score: -119.55 (accuracy -132.25, token simplicity 7.20, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y -= params.g
diff.y -= params.h * data.x
diff.y += params.i * data.x * data.x
diff.y += params.j * data.x * data.y
diff.y -= params.k * data.y
  Demo 0: a = -0.042, b = -0.022, c = 0.180, d = 0.121, e = 1.040, f = 0.002, g = 0.016, h = 3.828, i = 0.154, j = 0.178, k = 0.343
  Demo 1: a = 0.005, b = 0.040, c = 0.025, d = -0.030, e = 0.977, f = -0.040, g = 0.038, h = 1.548, i = 0.069, j = 0.011, k = 0.312
  Demo 2: a = -0.099, b = 0.014, c = 0.068, d = 0.011, e = 1.042, f = 0.005, g = 0.271, h = 8.358, i = 0.270, j = 0.120, k = 0.573

## Round 1 | 0.16s | best score: -128.69

+251 new programs (251 actually scored)
* linear_fit: +13
* quadratic_fit: +17
* add_single_terms: +46
* delete_interactions: +110
* delete_lines: +53
* delete_near_zeros: +5
* relate_parameters: +7
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -128.69 (accuracy -131.29, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -128.24 (accuracy -131.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -127.88 (accuracy -131.38, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -127.45 (accuracy -131.35, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.824, b = 0.136, c = 0.350
  Demo 1: a = 1.533, b = 0.009, c = 0.314
  Demo 2: a = 8.348, b = 0.091, c = 0.580

-- score: -127.39 (accuracy -131.59, token simplicity 2.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.018, b = 1.036, c = 3.859, d = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 1.533, d = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 8.415, d = 0.577

-- score: -127.35 (accuracy -131.55, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -127.23 (accuracy -131.63, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = -0.035, b = 1.038, c = 3.859, d = 0.348
  Demo 1: a = 0.039, b = 0.968, c = 1.533, d = 0.312
  Demo 2: a = 0.016, b = 1.035, c = 8.415, d = 0.577

-- score: -127.14 (accuracy -131.54, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 3.909, c = 0.050, d = 0.348
  Demo 1: a = 0.967, b = 1.537, c = 0.004, d = 0.312
  Demo 2: a = 1.034, b = 8.427, c = 0.012, d = 0.577

-- score: -127.10 (accuracy -131.70, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
diff.y -= params.d * data.y * data.y
  Demo 0: a = 1.041, b = 3.860, c = 0.367, d = 0.035
  Demo 1: a = 0.967, b = 1.520, c = 0.308, d = 0.042
  Demo 2: a = 1.034, b = 8.417, c = 0.588, d = 0.007

-- score: -127.06 (accuracy -131.66, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.x * data.y
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.092, b = 1.037, c = 3.859, d = 0.348
  Demo 1: a = -0.039, b = 0.974, c = 1.533, d = 0.312
  Demo 2: a = -0.001, b = 1.034, c = 8.415, d = 0.577

## Round 2 | 0.06s | best score: -128.69 (stable)

+154 new programs (154 actually scored)
* linear_fit: +19
* quadratic_fit: +22
* add_single_terms: +49
* delete_interactions: +45
* delete_lines: +19
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -128.69 (accuracy -131.29, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -128.24 (accuracy -131.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -127.88 (accuracy -131.38, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -127.84 (accuracy -131.54, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 4.859, c = 0.348
  Demo 1: a = 0.967, b = 2.533, c = 0.312
  Demo 2: a = 1.034, b = 9.415, c = 0.577

-- score: -127.81 (accuracy -131.31, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -127.71 (accuracy -131.41, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

-- score: -127.59 (accuracy -131.29, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.859, b = 0.069, c = 0.417
  Demo 1: a = 1.533, b = 0.005, c = 0.318
  Demo 2: a = 8.415, b = 0.048, c = 0.624

-- score: -127.59 (accuracy -131.49, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -127.57 (accuracy -131.47, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.101, b = 3.859, c = 0.348
  Demo 1: a = -0.053, b = 1.533, c = 0.312
  Demo 2: a = 0.003, b = 8.415, c = 0.577

-- score: -127.56 (accuracy -131.46, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
diff.y -= params.c * data.y * data.y
  Demo 0: a = 3.860, b = 0.367, c = 0.035
  Demo 1: a = 1.520, b = 0.308, c = 0.042
  Demo 2: a = 8.417, b = 0.588, c = 0.007

## Round 3 | 0.06s | best score: -128.69 (stable)

+139 new programs (139 actually scored)
* linear_fit: +20
* quadratic_fit: +23
* add_single_terms: +43
* delete_interactions: +38
* delete_lines: +15
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -128.69 (accuracy -131.29, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -128.29 (accuracy -131.29, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= data.y
  Demo 0: a = 3.859, b = 0.652
  Demo 1: a = 1.533, b = 0.688
  Demo 2: a = 8.415, b = 0.423

-- score: -128.24 (accuracy -131.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -127.88 (accuracy -131.38, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -127.84 (accuracy -131.54, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 4.859, c = 0.348
  Demo 1: a = 0.967, b = 2.533, c = 0.312
  Demo 2: a = 1.034, b = 9.415, c = 0.577

-- score: -127.81 (accuracy -131.31, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -127.71 (accuracy -131.41, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

-- score: -127.59 (accuracy -131.29, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.859, b = 0.069, c = 0.417
  Demo 1: a = 1.533, b = 0.005, c = 0.318
  Demo 2: a = 8.415, b = 0.048, c = 0.624

-- score: -127.59 (accuracy -131.49, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -127.57 (accuracy -131.47, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.101, b = 3.859, c = 0.348
  Demo 1: a = -0.053, b = 1.533, c = 0.312
  Demo 2: a = 0.003, b = 8.415, c = 0.577

## Round 4 | 0.01s | best score: -128.69 (stable)

+22 new programs (22 actually scored)
* linear_fit: +4
* quadratic_fit: +5
* add_single_terms: +8
* delete_interactions: +3
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -128.69 (accuracy -131.29, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -128.29 (accuracy -131.29, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= data.y
  Demo 0: a = 3.859, b = 0.652
  Demo 1: a = 1.533, b = 0.688
  Demo 2: a = 8.415, b = 0.423

-- score: -128.24 (accuracy -131.54, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -127.88 (accuracy -131.38, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -127.84 (accuracy -131.54, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 4.859, c = 0.348
  Demo 1: a = 0.967, b = 2.533, c = 0.312
  Demo 2: a = 1.034, b = 9.415, c = 0.577

-- score: -127.81 (accuracy -131.31, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -127.71 (accuracy -131.41, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

-- score: -127.59 (accuracy -131.29, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.859, b = 0.069, c = 0.417
  Demo 1: a = 1.533, b = 0.005, c = 0.318
  Demo 2: a = 8.415, b = 0.048, c = 0.624

-- score: -127.59 (accuracy -131.49, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -127.57 (accuracy -131.47, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.101, b = 3.859, c = 0.348
  Demo 1: a = -0.053, b = 1.533, c = 0.312
  Demo 2: a = 0.003, b = 8.415, c = 0.577

