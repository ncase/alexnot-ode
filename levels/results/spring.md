# spring

Solved in 0.26 seconds. 418 programs considered, over 6 rounds.

## Winner

-- score: -79.46 (accuracy -82.06, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

## Runner-ups

-- score: -78.91 (accuracy -82.21, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -78.61 (accuracy -82.11, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -78.57 (accuracy -82.07, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -78.57 (accuracy -82.07, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

# The Search

## Round 0 | 0.00s | best score: -40.73

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -40.73 (accuracy -41.83, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.y
  Demo 0: a = 1.041
  Demo 1: a = 0.967
  Demo 2: a = 1.034

-- score: -38.82 (accuracy -41.92, token simplicity 1.60, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033
  Demo 1: a = 0.010, b = 0.041, c = 0.968
  Demo 2: a = 0.022, b = 0.014, c = 1.034

-- score: -37.29 (accuracy -40.39, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -35.15 (accuracy -42.15, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = -0.042, b = -0.022, c = 0.180, d = 0.121, e = 1.040, f = 0.002
  Demo 1: a = 0.005, b = 0.040, c = 0.025, d = -0.030, e = 0.977, f = -0.040
  Demo 2: a = -0.099, b = 0.014, c = 0.068, d = 0.011, e = 1.042, f = 0.005

-- score: -34.75 (accuracy -35.85, token simplicity 0.60, parameter simplicity 0.50) --
diff.y -= params.a * data.x
  Demo 0: a = 3.745
  Demo 1: a = 1.523
  Demo 2: a = 8.077

-- score: -33.61 (accuracy -40.61, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 0.007, b = 3.835, c = 0.136, d = 0.151, e = 0.361, f = -0.041
  Demo 1: a = 0.002, b = 1.537, c = 0.058, d = 0.021, e = 0.310, f = -0.057
  Demo 2: a = -0.493, b = 8.356, c = 0.345, d = 0.150, e = 0.538, f = 0.028

-- score: -1.44 (accuracy -2.74, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.y * data.y
  Demo 0: a = -0.372
  Demo 1: a = 0.039
  Demo 2: a = -0.119

-- score: -0.38 (accuracy -1.68, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.y
  Demo 0: a = 2.000
  Demo 1: a = -0.106
  Demo 2: a = 1.188

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

-- score: 0.19 (accuracy -1.11, token simplicity 0.80, parameter simplicity 0.50) --
diff.y -= params.a * data.x * data.x
  Demo 0: a = 0.833
  Demo 1: a = 0.565
  Demo 2: a = 0.033

## Round 1 | 0.05s | best score: -78.02

+128 new programs (128 actually scored)
* add_terms: +107
* delete_lines: +17
* delete_near_zeros: +1
* relate_parameters: +0
* snap_to_one: +3
* tie_parameters: +0

### 10 parents for the next round

-- score: -78.02 (accuracy -82.22, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -76.11 (accuracy -82.31, token simplicity 3.20, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d
diff.y -= params.e * data.x
diff.y -= params.f * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 0.000, e = 3.859, f = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 0.011, e = 1.530, f = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 0.123, e = 8.429, f = 0.584

-- score: -75.48 (accuracy -77.68, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
  Demo 0: a = 1.041, b = 3.745
  Demo 1: a = 0.967, b = 1.523
  Demo 2: a = 1.034, b = 8.077

-- score: -74.34 (accuracy -82.44, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 1.041, b = 0.007, c = 3.835, d = 0.136, e = 0.151, f = 0.361, g = -0.041
  Demo 1: a = 0.967, b = 0.002, c = 1.537, d = 0.058, e = 0.021, f = 0.310, g = -0.057
  Demo 2: a = 1.034, b = -0.493, c = 8.356, d = 0.345, e = 0.150, f = 0.538, g = 0.028

-- score: -73.57 (accuracy -77.77, token simplicity 2.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d * data.x
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 3.745
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 1.523
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 8.077

-- score: -72.44 (accuracy -82.54, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y -= params.g
diff.y -= params.h * data.x
diff.y -= params.i * data.y
  Demo 0: a = -0.042, b = -0.022, c = 0.180, d = 0.121, e = 1.040, f = 0.002, g = 0.000, h = 3.859, i = 0.348
  Demo 1: a = 0.005, b = 0.040, c = 0.025, d = -0.030, e = 0.977, f = -0.040, g = 0.011, h = 1.530, i = 0.312
  Demo 2: a = -0.099, b = 0.014, c = 0.068, d = 0.011, e = 1.042, f = 0.005, g = 0.123, h = 8.429, i = 0.584

-- score: -72.43 (accuracy -82.53, token simplicity 5.60, parameter simplicity 4.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
diff.y += params.i * data.y * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 0.007, e = 3.835, f = 0.136, g = 0.151, h = 0.361, i = -0.041
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 0.002, e = 1.537, f = 0.058, g = 0.021, h = 0.310, i = -0.057
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = -0.493, e = 8.356, f = 0.345, g = 0.150, h = 0.538, i = 0.028

-- score: -69.90 (accuracy -78.00, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y -= params.g * data.x
  Demo 0: a = -0.042, b = -0.022, c = 0.180, d = 0.121, e = 1.040, f = 0.002, g = 3.745
  Demo 1: a = 0.005, b = 0.040, c = 0.025, d = -0.030, e = 0.977, f = -0.040, g = 1.523
  Demo 2: a = -0.099, b = 0.014, c = 0.068, d = 0.011, e = 1.042, f = 0.005, g = 8.077

-- score: -68.76 (accuracy -82.76, token simplicity 8.00, parameter simplicity 6.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.h * data.x
diff.y += params.i * data.x * data.x
diff.y += params.j * data.x * data.y
diff.y -= params.k * data.y
diff.y += params.l * data.y * data.y
  Demo 0: a = -0.042, b = -0.022, c = 0.180, d = 0.121, e = 1.040, f = 0.002, g = 0.007, h = 3.835, i = 0.136, j = 0.151, k = 0.361, l = -0.041
  Demo 1: a = 0.005, b = 0.040, c = 0.025, d = -0.030, e = 0.977, f = -0.040, g = 0.002, h = 1.537, i = 0.058, j = 0.021, k = 0.310, l = -0.057
  Demo 2: a = -0.099, b = 0.014, c = 0.068, d = 0.011, e = 1.042, f = 0.005, g = -0.493, h = 8.356, i = 0.345, j = 0.150, k = 0.538, l = 0.028

-- score: -41.27 (accuracy -41.67, token simplicity 0.40, parameter simplicity 0.00) --
diff.x += data.y

## Round 2 | 0.08s | best score: -78.91

+138 new programs (138 actually scored)
* add_terms: +74
* delete_lines: +51
* delete_near_zeros: +3
* relate_parameters: +1
* snap_to_one: +9
* tie_parameters: +0

### 10 parents for the next round

-- score: -78.91 (accuracy -82.21, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -78.57 (accuracy -82.07, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -78.02 (accuracy -82.22, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -77.15 (accuracy -82.25, token simplicity 2.60, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.018, b = 1.036, c = 0.000, d = 3.859, e = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 0.011, d = 1.530, e = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 0.123, d = 8.429, e = 0.584

-- score: -77.00 (accuracy -82.30, token simplicity 2.80, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 3.859, e = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 1.533, e = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 8.415, e = 0.577

-- score: -76.98 (accuracy -82.28, token simplicity 2.80, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = -0.035, b = 1.038, c = 0.000, d = 3.859, e = 0.348
  Demo 1: a = 0.039, b = 0.968, c = 0.011, d = 1.530, e = 0.312
  Demo 2: a = 0.016, b = 1.035, c = 0.123, d = 8.429, e = 0.584

-- score: -76.85 (accuracy -82.35, token simplicity 3.00, parameter simplicity 2.50) --
diff.x += params.a * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.y
  Demo 0: a = 1.041, b = 0.029, c = 3.861, d = 0.371, e = -0.055
  Demo 1: a = 0.967, b = 0.026, c = 1.521, d = 0.307, e = -0.059
  Demo 2: a = 1.034, b = -0.164, c = 8.432, d = 0.577, e = 0.006

-- score: -76.80 (accuracy -82.30, token simplicity 3.00, parameter simplicity 2.50) --
diff.x += params.a * data.x * data.y
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.092, b = 1.037, c = 0.000, d = 3.859, e = 0.348
  Demo 1: a = -0.039, b = 0.974, c = 0.011, d = 1.530, e = 0.312
  Demo 2: a = -0.001, b = 1.034, c = 0.123, d = 8.429, e = 0.584

-- score: -76.78 (accuracy -82.28, token simplicity 3.00, parameter simplicity 2.50) --
diff.x += params.a * data.y
diff.x -= params.b * data.y * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 1.030, b = 0.020, c = 0.000, d = 3.859, e = 0.348
  Demo 1: a = 0.969, b = 0.025, c = 0.011, d = 1.530, e = 0.312
  Demo 2: a = 1.033, b = 0.001, c = 0.123, d = 8.429, e = 0.584

-- score: -76.78 (accuracy -82.28, token simplicity 3.00, parameter simplicity 2.50) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y -= params.e * data.y
  Demo 0: a = 1.041, b = 0.013, c = 3.866, d = 0.078, e = 0.346
  Demo 1: a = 0.967, b = 0.038, c = 1.548, d = 0.068, e = 0.310
  Demo 2: a = 1.034, b = 0.253, c = 8.444, d = 0.169, e = 0.577

## Round 3 | 0.05s | best score: -79.46

+96 new programs (96 actually scored)
* add_terms: +70
* delete_lines: +22
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +4
* tie_parameters: +0

### 10 parents for the next round

-- score: -79.46 (accuracy -82.06, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -78.91 (accuracy -82.21, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -78.57 (accuracy -82.07, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -78.04 (accuracy -82.24, token simplicity 2.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.018, b = 1.036, c = 3.859, d = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 1.533, d = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 8.415, d = 0.577

-- score: -78.02 (accuracy -82.22, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -77.87 (accuracy -82.27, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = -0.035, b = 1.038, c = 3.859, d = 0.348
  Demo 1: a = 0.039, b = 0.968, c = 1.533, d = 0.312
  Demo 2: a = 0.016, b = 1.035, c = 8.415, d = 0.577

-- score: -77.72 (accuracy -82.12, token simplicity 2.40, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.023, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.006, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 0.034, b = 0.123, c = 8.429, d = 0.584

-- score: -77.71 (accuracy -82.31, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
diff.y -= params.d * data.y * data.y
  Demo 0: a = 1.041, b = 3.860, c = 0.367, d = 0.035
  Demo 1: a = 0.967, b = 1.520, c = 0.308, d = 0.042
  Demo 2: a = 1.034, b = 8.417, c = 0.588, d = 0.007

-- score: -77.69 (accuracy -82.29, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.x * data.y
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.092, b = 1.037, c = 3.859, d = 0.348
  Demo 1: a = -0.039, b = 0.974, c = 1.533, d = 0.312
  Demo 2: a = -0.001, b = 1.034, c = 8.415, d = 0.577

-- score: -77.67 (accuracy -82.27, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.x -= params.b * data.y * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.030, b = 0.020, c = 3.859, d = 0.348
  Demo 1: a = 0.969, b = 0.025, c = 1.533, d = 0.312
  Demo 2: a = 1.033, b = 0.001, c = 8.415, d = 0.577

## Round 4 | 0.04s | best score: -79.46 (stable)

+79 new programs (79 actually scored)
* add_terms: +62
* delete_lines: +15
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +2
* tie_parameters: +0

### 10 parents for the next round

-- score: -79.46 (accuracy -82.06, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -78.91 (accuracy -82.21, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -78.61 (accuracy -82.11, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -78.57 (accuracy -82.07, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -78.43 (accuracy -82.13, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

-- score: -78.28 (accuracy -82.18, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -78.27 (accuracy -82.17, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.101, b = 3.859, c = 0.348
  Demo 1: a = -0.053, b = 1.533, c = 0.312
  Demo 2: a = 0.003, b = 8.415, c = 0.577

-- score: -78.26 (accuracy -82.16, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
diff.y -= params.c * data.y * data.y
  Demo 0: a = 3.860, b = 0.367, c = 0.035
  Demo 1: a = 1.520, b = 0.308, c = 0.042
  Demo 2: a = 8.417, b = 0.588, c = 0.007

-- score: -78.19 (accuracy -82.09, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.824, b = 0.136, c = 0.350
  Demo 1: a = 1.533, b = 0.009, c = 0.314
  Demo 2: a = 8.348, b = 0.091, c = 0.580

-- score: -78.17 (accuracy -82.07, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.x * data.x
diff.y -= params.c * data.y
  Demo 0: a = 3.863, b = 0.047, c = 0.345
  Demo 1: a = 1.543, b = 0.026, c = 0.312
  Demo 2: a = 8.416, b = 0.009, c = 0.576

## Round 5 | 0.03s | best score: -79.46 (stable)

+76 new programs (76 actually scored)
* add_terms: +60
* delete_lines: +16
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -79.46 (accuracy -82.06, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -78.91 (accuracy -82.21, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -78.61 (accuracy -82.11, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -78.57 (accuracy -82.07, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -78.43 (accuracy -82.13, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

-- score: -78.28 (accuracy -82.18, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -78.27 (accuracy -82.17, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.101, b = 3.859, c = 0.348
  Demo 1: a = -0.053, b = 1.533, c = 0.312
  Demo 2: a = 0.003, b = 8.415, c = 0.577

-- score: -78.26 (accuracy -82.16, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
diff.y -= params.c * data.y * data.y
  Demo 0: a = 3.860, b = 0.367, c = 0.035
  Demo 1: a = 1.520, b = 0.308, c = 0.042
  Demo 2: a = 8.417, b = 0.588, c = 0.007

-- score: -78.19 (accuracy -82.09, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.824, b = 0.136, c = 0.350
  Demo 1: a = 1.533, b = 0.009, c = 0.314
  Demo 2: a = 8.348, b = 0.091, c = 0.580

-- score: -78.17 (accuracy -82.07, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.x * data.x
diff.y -= params.c * data.y
  Demo 0: a = 3.863, b = 0.047, c = 0.345
  Demo 1: a = 1.543, b = 0.026, c = 0.312
  Demo 2: a = 8.416, b = 0.009, c = 0.576

