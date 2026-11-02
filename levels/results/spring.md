# spring

Solved in 0.12 seconds. 219 programs considered, over 6 rounds.

## Winner

-- score: -120.49 (accuracy -123.09, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

## Runner-ups

-- score: -120.01 (accuracy -123.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -120.01 (accuracy -123.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -119.67 (accuracy -123.17, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -119.67 (accuracy -123.17, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

# The Search

## Round 0 | 0.00s | best score: -61.64

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -61.64 (accuracy -62.74, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.y
  Demo 0: a = 1.041
  Demo 1: a = 0.967
  Demo 2: a = 1.034

-- score: -59.78 (accuracy -62.88, token simplicity 1.60, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033
  Demo 1: a = 0.010, b = 0.041, c = 0.968
  Demo 2: a = 0.022, b = 0.014, c = 1.034

-- score: -57.49 (accuracy -60.59, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -56.23 (accuracy -63.23, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = -0.042, b = -0.022, c = 0.180, d = 0.121, e = 1.040, f = 0.002
  Demo 1: a = 0.005, b = 0.040, c = 0.025, d = -0.030, e = 0.977, f = -0.040
  Demo 2: a = -0.099, b = 0.014, c = 0.068, d = 0.011, e = 1.042, f = 0.005

-- score: -53.92 (accuracy -60.92, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 0.007, b = 3.835, c = 0.136, d = 0.151, e = 0.361, f = -0.041
  Demo 1: a = 0.002, b = 1.537, c = 0.058, d = 0.021, e = 0.310, f = -0.057
  Demo 2: a = -0.493, b = 8.356, c = 0.345, d = 0.150, e = 0.538, f = 0.028

## Round 1 | 0.03s | best score: -119.13

+73 new programs (73 actually scored)
* add_terms: +53
* delete_lines: +17
* relate_parameters: +0
* snap_to_one: +3
* tie_parameters: +0

### 5 parents for the next round

-- score: -119.13 (accuracy -123.33, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -117.27 (accuracy -123.47, token simplicity 3.20, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d
diff.y -= params.e * data.x
diff.y -= params.f * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 0.000, e = 3.859, f = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 0.011, e = 1.530, f = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 0.123, e = 8.429, f = 0.584

-- score: -115.56 (accuracy -123.66, token simplicity 4.60, parameter simplicity 3.50) --
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

-- score: -114.32 (accuracy -116.52, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
  Demo 0: a = 1.041, b = 3.745
  Demo 1: a = 0.967, b = 1.523
  Demo 2: a = 1.034, b = 8.077

-- score: -113.72 (accuracy -123.82, token simplicity 5.60, parameter simplicity 4.50) --
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

## Round 2 | 0.04s | best score: -120.01

+67 new programs (67 actually scored)
* add_terms: +39
* delete_lines: +23
* relate_parameters: +0
* snap_to_one: +5
* tie_parameters: +0

### 5 parents for the next round

-- score: -120.01 (accuracy -123.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -119.60 (accuracy -123.10, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -119.13 (accuracy -123.33, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -118.28 (accuracy -123.38, token simplicity 2.60, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.018, b = 1.036, c = 0.000, d = 3.859, e = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 0.011, d = 1.530, e = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 0.123, d = 8.429, e = 0.584

-- score: -118.16 (accuracy -123.46, token simplicity 2.80, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 3.859, e = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 1.533, e = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 8.415, e = 0.577

## Round 3 | 0.02s | best score: -120.49

+47 new programs (47 actually scored)
* add_terms: +35
* delete_lines: +10
* relate_parameters: +0
* snap_to_one: +2
* tie_parameters: +0

### 5 parents for the next round

-- score: -120.49 (accuracy -123.09, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -120.01 (accuracy -123.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -119.60 (accuracy -123.10, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -119.17 (accuracy -123.37, token simplicity 2.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.018, b = 1.036, c = 3.859, d = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 1.533, d = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 8.415, d = 0.577

-- score: -119.13 (accuracy -123.33, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

## Round 4 | 0.01s | best score: -120.49

+22 new programs (22 actually scored)
* add_terms: +18
* delete_lines: +3
* relate_parameters: +0
* snap_to_one: +1
* tie_parameters: +0

### 5 parents for the next round

-- score: -120.49 (accuracy -123.09, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -120.01 (accuracy -123.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -119.67 (accuracy -123.17, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -119.60 (accuracy -123.10, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -119.49 (accuracy -123.19, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

## Round 5 | 0.01s | best score: -120.49

+22 new programs (22 actually scored)
* add_terms: +17
* delete_lines: +5
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -120.49 (accuracy -123.09, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -120.01 (accuracy -123.31, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -119.67 (accuracy -123.17, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -119.60 (accuracy -123.10, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -119.49 (accuracy -123.19, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

