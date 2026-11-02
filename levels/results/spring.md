# spring

Solved in 0.11 seconds. 215 programs considered, over 6 rounds.

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

# The Search

## Round 0 | 0.00s | best score: -40.73

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

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

## Round 1 | 0.03s | best score: -78.02

+74 new programs (74 actually scored)
* add_terms: +60
* delete_lines: +11
* relate_parameters: +0
* snap_to_one: +3
* tie_parameters: +0

### 5 parents for the next round

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

## Round 2 | 0.03s | best score: -78.91

+67 new programs (67 actually scored)
* add_terms: +46
* delete_lines: +16
* relate_parameters: +0
* snap_to_one: +5
* tie_parameters: +0

### 5 parents for the next round

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

## Round 3 | 0.02s | best score: -79.46

+49 new programs (49 actually scored)
* add_terms: +37
* delete_lines: +10
* relate_parameters: +0
* snap_to_one: +2
* tie_parameters: +0

### 5 parents for the next round

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

## Round 4 | 0.01s | best score: -79.46

+22 new programs (22 actually scored)
* add_terms: +18
* delete_lines: +3
* relate_parameters: +0
* snap_to_one: +1
* tie_parameters: +0

### 5 parents for the next round

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

## Round 5 | 0.01s | best score: -79.46

+22 new programs (22 actually scored)
* add_terms: +17
* delete_lines: +5
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

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

