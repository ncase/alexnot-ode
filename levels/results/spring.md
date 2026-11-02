# spring

Solved in 0.14 seconds. 245 programs considered, over 6 rounds.

## Winner

-- score: -319.06 (accuracy -321.66, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

## Runner-ups

-- score: -318.96 (accuracy -322.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -318.38 (accuracy -321.88, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -318.25 (accuracy -322.15, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -318.25 (accuracy -321.95, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

# The Search

## Round 0 | 0.00s | best score: -162.86

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -162.86 (accuracy -163.96, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.y
  Demo 0: a = 1.041
  Demo 1: a = 0.967
  Demo 2: a = 1.034

-- score: -161.23 (accuracy -164.33, token simplicity 1.60, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033
  Demo 1: a = 0.010, b = 0.041, c = 0.968
  Demo 2: a = 0.022, b = 0.014, c = 1.034

-- score: -158.23 (accuracy -165.23, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = -0.042, b = -0.022, c = 0.180, d = 0.121, e = 1.040, f = 0.002
  Demo 1: a = 0.005, b = 0.040, c = 0.025, d = -0.030, e = 0.977, f = -0.040
  Demo 2: a = -0.099, b = 0.014, c = 0.068, d = 0.011, e = 1.042, f = 0.005

-- score: -155.24 (accuracy -158.34, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -152.19 (accuracy -159.19, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 0.007, b = 3.835, c = 0.136, d = 0.151, e = 0.361, f = -0.041
  Demo 1: a = 0.002, b = 1.537, c = 0.058, d = 0.021, e = 0.310, f = -0.057
  Demo 2: a = -0.493, b = 8.356, c = 0.345, d = 0.150, e = 0.538, f = 0.028

## Round 1 | 0.03s | best score: -318.10

+78 new programs (78 actually scored)
* add_terms: +53
* delete_lines: +17
* relate_parameters: +0
* snap_to_one: +3
* tie_parameters: +5

### 5 parents for the next round

-- score: -318.10 (accuracy -322.30, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -316.47 (accuracy -322.67, token simplicity 3.20, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d
diff.y -= params.e * data.x
diff.y -= params.f * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 0.000, e = 3.859, f = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 0.011, e = 1.530, f = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 0.123, e = 8.429, f = 0.584

-- score: -315.06 (accuracy -323.16, token simplicity 4.60, parameter simplicity 3.50) --
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

-- score: -313.47 (accuracy -323.57, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -313.42 (accuracy -323.52, token simplicity 5.60, parameter simplicity 4.50) --
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

## Round 2 | 0.05s | best score: -318.96

+77 new programs (77 actually scored)
* add_terms: +30
* delete_lines: +31
* relate_parameters: +0
* snap_to_one: +5
* tie_parameters: +11

### 5 parents for the next round

-- score: -318.96 (accuracy -322.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -318.20 (accuracy -321.70, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -318.10 (accuracy -322.30, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

-- score: -317.33 (accuracy -322.43, token simplicity 2.60, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.018, b = 1.036, c = 0.000, d = 3.859, e = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 0.011, d = 1.530, e = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 0.123, d = 8.429, e = 0.584

-- score: -317.33 (accuracy -322.63, token simplicity 2.80, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.018, b = -0.035, c = 1.033, d = 3.859, e = 0.348
  Demo 1: a = 0.010, b = 0.041, c = 0.968, d = 1.533, e = 0.312
  Demo 2: a = 0.022, b = 0.014, c = 1.034, d = 8.415, e = 0.577

## Round 3 | 0.02s | best score: -319.06

+47 new programs (47 actually scored)
* add_terms: +35
* delete_lines: +10
* relate_parameters: +0
* snap_to_one: +2
* tie_parameters: +0

### 5 parents for the next round

-- score: -319.06 (accuracy -321.66, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -318.96 (accuracy -322.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -318.20 (accuracy -321.70, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.859, c = 0.348
  Demo 1: a = 0.011, b = 1.530, c = 0.312
  Demo 2: a = 0.123, b = 8.429, c = 0.584

-- score: -318.19 (accuracy -322.39, token simplicity 2.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.018, b = 1.036, c = 3.859, d = 0.348
  Demo 1: a = 0.005, b = 0.967, c = 1.533, d = 0.312
  Demo 2: a = 0.023, b = 1.033, c = 8.415, d = 0.577

-- score: -318.10 (accuracy -322.30, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.041, b = 0.000, c = 3.859, d = 0.348
  Demo 1: a = 0.967, b = 0.011, c = 1.530, d = 0.312
  Demo 2: a = 1.034, b = 0.123, c = 8.429, d = 0.584

## Round 4 | 0.01s | best score: -319.06

+24 new programs (24 actually scored)
* add_terms: +18
* delete_lines: +5
* relate_parameters: +0
* snap_to_one: +1
* tie_parameters: +0

### 5 parents for the next round

-- score: -319.06 (accuracy -321.66, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -318.96 (accuracy -322.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -318.38 (accuracy -321.88, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -318.25 (accuracy -322.15, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -318.25 (accuracy -321.95, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

## Round 5 | 0.02s | best score: -319.06

+35 new programs (35 actually scored)
* add_terms: +27
* delete_lines: +8
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -319.06 (accuracy -321.66, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.859, b = 0.348
  Demo 1: a = 1.533, b = 0.312
  Demo 2: a = 8.415, b = 0.577

-- score: -318.96 (accuracy -322.26, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.041, b = 3.859, c = 0.348
  Demo 1: a = 0.967, b = 1.533, c = 0.312
  Demo 2: a = 1.034, b = 8.415, c = 0.577

-- score: -318.38 (accuracy -321.88, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.023, b = 3.859, c = 0.348
  Demo 1: a = 0.006, b = 1.533, c = 0.312
  Demo 2: a = 0.034, b = 8.415, c = 0.577

-- score: -318.25 (accuracy -322.15, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.030, b = 3.859, c = 0.348
  Demo 1: a = 0.027, b = 1.533, c = 0.312
  Demo 2: a = 0.005, b = 8.415, c = 0.577

-- score: -318.25 (accuracy -321.95, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.047, b = 3.859, c = 0.348
  Demo 1: a = 0.040, b = 1.533, c = 0.312
  Demo 2: a = -0.005, b = 8.415, c = 0.577

