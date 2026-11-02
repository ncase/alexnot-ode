# spring

Solved in 0.29 seconds. 514 programs considered, over 5 rounds.

## Winner

-- score: -226.33 (accuracy -228.93, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.947, b = 0.378
  Demo 1: a = 1.524, b = 0.284
  Demo 2: a = 8.745, b = 0.594

## Runner-ups

-- score: -225.93 (accuracy -228.93, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= data.y
  Demo 0: a = 3.947, b = 0.622
  Demo 1: a = 1.524, b = 0.716
  Demo 2: a = 8.745, b = 0.406

-- score: -225.93 (accuracy -228.93, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += data.y
diff.y -= params.b * data.y
  Demo 0: a = 3.947, b = 1.378
  Demo 1: a = 1.524, b = 1.284
  Demo 2: a = 8.745, b = 1.594

-- score: -225.93 (accuracy -229.23, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.378
  Demo 1: a = 0.989, b = 1.524, c = 0.284
  Demo 2: a = 1.021, b = 8.745, c = 0.594

-- score: -225.53 (accuracy -229.23, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.y
diff.y -= data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.622
  Demo 1: a = 0.989, b = 1.524, c = 0.716
  Demo 2: a = 1.021, b = 8.745, c = 0.406

# The Search

## Round 0 | 0.01s | best score: -225.93

+23 new programs (23 actually scored)
* linear_fit: +5
* quadratic_fit: +6
* add_single_terms: +12
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -225.93 (accuracy -229.23, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.378
  Demo 1: a = 0.989, b = 1.524, c = 0.284
  Demo 2: a = 1.021, b = 8.745, c = 0.594

-- score: -224.69 (accuracy -229.29, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.025, b = 3.928, c = 0.071, d = 0.380
  Demo 1: a = 0.989, b = 1.524, c = 0.007, d = 0.285
  Demo 2: a = 1.021, b = 8.715, c = 0.039, d = 0.595

-- score: -224.20 (accuracy -229.30, token simplicity 2.60, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.009, b = 1.023, c = 0.000, d = 3.947, e = 0.378
  Demo 1: a = 0.003, b = 0.989, c = 0.005, d = 1.523, e = 0.283
  Demo 2: a = 0.011, b = 1.021, c = 0.067, d = 8.751, e = 0.598

-- score: -224.08 (accuracy -229.38, token simplicity 2.80, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.009, b = -0.020, c = 1.021, d = 3.947, e = 0.378
  Demo 1: a = 0.005, b = 0.020, c = 0.989, d = 1.524, e = 0.284
  Demo 2: a = 0.010, b = 0.007, c = 1.021, d = 8.745, e = 0.594

-- score: -224.04 (accuracy -229.34, token simplicity 2.80, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.y
diff.y -= params.c
diff.y -= params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = -0.019, b = 1.023, c = 0.000, d = 3.947, e = 0.378
  Demo 1: a = 0.019, b = 0.989, c = 0.005, d = 1.523, e = 0.283
  Demo 2: a = 0.008, b = 1.022, c = 0.067, d = 8.751, e = 0.598

-- score: -223.45 (accuracy -229.35, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.025, b = 3.929, c = 0.069, d = 0.096, e = 0.376
  Demo 1: a = 0.989, b = 1.530, c = 0.013, d = 0.007, e = 0.285
  Demo 2: a = 1.021, b = 8.711, c = 0.025, d = 0.045, e = 0.593

-- score: -223.20 (accuracy -229.40, token simplicity 3.20, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.y -= params.d
diff.y -= params.e * data.x
diff.y -= params.f * data.y
  Demo 0: a = 0.009, b = -0.020, c = 1.021, d = 0.000, e = 3.947, f = 0.378
  Demo 1: a = 0.005, b = 0.020, c = 0.989, d = 0.005, e = 1.523, f = 0.283
  Demo 2: a = 0.010, b = 0.007, c = 1.021, d = 0.067, e = 8.751, f = 0.598

-- score: -221.47 (accuracy -229.57, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 1.025, b = 0.002, c = 3.934, d = 0.082, e = 0.083, f = 0.384, g = -0.019
  Demo 1: a = 0.989, b = -0.000, c = 1.527, d = 0.028, e = 0.012, f = 0.283, g = -0.025
  Demo 2: a = 1.021, b = -0.204, c = 8.721, d = 0.134, e = 0.060, f = 0.580, g = 0.010

-- score: -220.52 (accuracy -229.72, token simplicity 5.20, parameter simplicity 4.00) --
diff.x += params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.x
diff.y -= params.g * data.y
diff.y += params.h * data.y * data.y
  Demo 0: a = -0.020, b = 1.018, c = -0.010, d = 0.008, e = 3.952, f = 0.045, g = 0.388, h = -0.027
  Demo 1: a = 0.024, b = 0.991, c = -0.016, d = -0.001, e = 1.527, f = 0.028, g = 0.281, h = -0.025
  Demo 2: a = 0.008, b = 1.022, c = 0.000, d = -0.148, e = 8.761, f = 0.073, g = 0.589, h = 0.004

-- score: -216.84 (accuracy -229.94, token simplicity 7.60, parameter simplicity 5.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x += params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = -0.013, b = 0.047, c = 0.047, d = 1.020, e = -0.010, f = 0.002, g = 3.934, h = 0.082, i = 0.083, j = 0.384, k = -0.019
  Demo 1: a = 0.019, b = 0.012, c = -0.017, d = 0.994, e = -0.018, f = -0.000, g = 1.527, h = 0.028, i = 0.012, j = 0.283, k = -0.025
  Demo 2: a = 0.012, b = 0.010, c = 0.006, d = 1.023, e = 0.000, f = -0.204, g = 8.721, h = 0.134, i = 0.060, j = 0.580, k = 0.010

## Round 1 | 0.13s | best score: -226.33

+234 new programs (234 actually scored)
* linear_fit: +16
* quadratic_fit: +20
* add_single_terms: +47
* delete_interactions: +105
* delete_lines: +43
* delete_near_zeros: +3
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -226.33 (accuracy -228.93, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.947, b = 0.378
  Demo 1: a = 1.524, b = 0.284
  Demo 2: a = 8.745, b = 0.594

-- score: -225.93 (accuracy -229.23, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.378
  Demo 1: a = 0.989, b = 1.524, c = 0.284
  Demo 2: a = 1.021, b = 8.745, c = 0.594

-- score: -225.09 (accuracy -228.99, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.928, b = 0.071, c = 0.380
  Demo 1: a = 1.524, b = 0.007, c = 0.285
  Demo 2: a = 8.715, b = 0.039, c = 0.595

-- score: -225.08 (accuracy -229.28, token simplicity 2.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.009, b = 1.023, c = 3.947, d = 0.378
  Demo 1: a = 0.003, b = 0.989, c = 1.524, d = 0.284
  Demo 2: a = 0.011, b = 1.021, c = 8.745, d = 0.594

-- score: -225.05 (accuracy -229.25, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.025, b = 0.000, c = 3.947, d = 0.378
  Demo 1: a = 0.989, b = 0.005, c = 1.523, d = 0.283
  Demo 2: a = 1.021, b = 0.067, c = 8.751, d = 0.598

-- score: -224.93 (accuracy -229.33, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = -0.019, b = 1.023, c = 3.947, d = 0.378
  Demo 1: a = 0.019, b = 0.989, c = 1.524, d = 0.284
  Demo 2: a = 0.008, b = 1.022, c = 8.745, d = 0.594

-- score: -224.83 (accuracy -229.23, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.036, d = 0.415
  Demo 1: a = 0.989, b = 1.524, c = 0.004, d = 0.288
  Demo 2: a = 1.021, b = 8.745, c = 0.020, d = 0.614

-- score: -224.78 (accuracy -229.38, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
diff.y -= params.d * data.y * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.387, d = 0.017
  Demo 1: a = 0.989, b = 1.518, c = 0.281, d = 0.019
  Demo 2: a = 1.021, b = 8.745, c = 0.601, d = 0.005

-- score: -224.76 (accuracy -229.36, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.x * data.y
diff.x += params.b * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 0.045, b = 1.023, c = 3.947, d = 0.378
  Demo 1: a = -0.021, b = 0.993, c = 1.524, d = 0.284
  Demo 2: a = 0.002, b = 1.021, c = 8.745, d = 0.594

-- score: -224.73 (accuracy -229.33, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.y
diff.x += params.b * data.y * data.y
diff.y -= params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.020, b = -0.010, c = 3.947, d = 0.378
  Demo 1: a = 0.990, b = -0.012, c = 1.524, d = 0.284
  Demo 2: a = 1.021, b = 0.000, c = 8.745, d = 0.594

## Round 2 | 0.07s | best score: -226.33 (stable)

+161 new programs (161 actually scored)
* linear_fit: +23
* quadratic_fit: +21
* add_single_terms: +44
* delete_interactions: +50
* delete_lines: +23
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -226.33 (accuracy -228.93, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.947, b = 0.378
  Demo 1: a = 1.524, b = 0.284
  Demo 2: a = 8.745, b = 0.594

-- score: -225.93 (accuracy -229.23, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.378
  Demo 1: a = 0.989, b = 1.524, c = 0.284
  Demo 2: a = 1.021, b = 8.745, c = 0.594

-- score: -225.53 (accuracy -229.23, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.y
diff.y -= data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.622
  Demo 1: a = 0.989, b = 1.524, c = 0.716
  Demo 2: a = 1.021, b = 8.745, c = 0.406

-- score: -225.53 (accuracy -229.03, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.012, b = 3.947, c = 0.378
  Demo 1: a = 0.003, b = 1.524, c = 0.284
  Demo 2: a = 0.018, b = 8.745, c = 0.594

-- score: -225.45 (accuracy -228.95, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.947, c = 0.378
  Demo 1: a = 0.005, b = 1.523, c = 0.283
  Demo 2: a = 0.067, b = 8.751, c = 0.598

-- score: -225.36 (accuracy -229.06, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.028, b = 3.947, c = 0.378
  Demo 1: a = 0.019, b = 1.524, c = 0.284
  Demo 2: a = -0.005, b = 8.745, c = 0.594

-- score: -225.25 (accuracy -229.15, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.017, b = 3.947, c = 0.378
  Demo 1: a = 0.013, b = 1.524, c = 0.284
  Demo 2: a = 0.002, b = 8.745, c = 0.594

-- score: -225.23 (accuracy -228.93, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.947, b = 0.036, c = 0.415
  Demo 1: a = 1.524, b = 0.004, c = 0.288
  Demo 2: a = 8.745, b = 0.020, c = 0.614

-- score: -225.21 (accuracy -229.11, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.052, b = 3.947, c = 0.378
  Demo 1: a = -0.025, b = 1.524, c = 0.284
  Demo 2: a = 0.005, b = 8.745, c = 0.594

-- score: -225.18 (accuracy -229.08, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
diff.y -= params.c * data.y * data.y
  Demo 0: a = 3.947, b = 0.387, c = 0.017
  Demo 1: a = 1.518, b = 0.281, c = 0.019
  Demo 2: a = 8.745, b = 0.601, c = 0.005

## Round 3 | 0.07s | best score: -226.33 (stable)

+152 new programs (152 actually scored)
* linear_fit: +22
* quadratic_fit: +30
* add_single_terms: +45
* delete_interactions: +40
* delete_lines: +15
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -226.33 (accuracy -228.93, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.947, b = 0.378
  Demo 1: a = 1.524, b = 0.284
  Demo 2: a = 8.745, b = 0.594

-- score: -225.93 (accuracy -228.93, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= data.y
  Demo 0: a = 3.947, b = 0.622
  Demo 1: a = 1.524, b = 0.716
  Demo 2: a = 8.745, b = 0.406

-- score: -225.93 (accuracy -229.23, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.378
  Demo 1: a = 0.989, b = 1.524, c = 0.284
  Demo 2: a = 1.021, b = 8.745, c = 0.594

-- score: -225.53 (accuracy -229.23, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.y
diff.y -= data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.622
  Demo 1: a = 0.989, b = 1.524, c = 0.716
  Demo 2: a = 1.021, b = 8.745, c = 0.406

-- score: -225.53 (accuracy -229.03, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.012, b = 3.947, c = 0.378
  Demo 1: a = 0.003, b = 1.524, c = 0.284
  Demo 2: a = 0.018, b = 8.745, c = 0.594

-- score: -225.45 (accuracy -228.95, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.947, c = 0.378
  Demo 1: a = 0.005, b = 1.523, c = 0.283
  Demo 2: a = 0.067, b = 8.751, c = 0.598

-- score: -225.36 (accuracy -229.06, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.028, b = 3.947, c = 0.378
  Demo 1: a = 0.019, b = 1.524, c = 0.284
  Demo 2: a = -0.005, b = 8.745, c = 0.594

-- score: -225.25 (accuracy -229.15, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.017, b = 3.947, c = 0.378
  Demo 1: a = 0.013, b = 1.524, c = 0.284
  Demo 2: a = 0.002, b = 8.745, c = 0.594

-- score: -225.23 (accuracy -228.93, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.947, b = 0.036, c = 0.415
  Demo 1: a = 1.524, b = 0.004, c = 0.288
  Demo 2: a = 8.745, b = 0.020, c = 0.614

-- score: -225.21 (accuracy -229.11, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.052, b = 3.947, c = 0.378
  Demo 1: a = -0.025, b = 1.524, c = 0.284
  Demo 2: a = 0.005, b = 8.745, c = 0.594

## Round 4 | 0.01s | best score: -226.33 (stable)

+20 new programs (20 actually scored)
* linear_fit: +4
* quadratic_fit: +5
* add_single_terms: +7
* delete_interactions: +3
* delete_lines: +1
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -226.33 (accuracy -228.93, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y -= params.b * data.y
  Demo 0: a = 3.947, b = 0.378
  Demo 1: a = 1.524, b = 0.284
  Demo 2: a = 8.745, b = 0.594

-- score: -225.93 (accuracy -228.93, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= data.y
  Demo 0: a = 3.947, b = 0.622
  Demo 1: a = 1.524, b = 0.716
  Demo 2: a = 8.745, b = 0.406

-- score: -225.93 (accuracy -229.23, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.378
  Demo 1: a = 0.989, b = 1.524, c = 0.284
  Demo 2: a = 1.021, b = 8.745, c = 0.594

-- score: -225.53 (accuracy -229.23, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.y
diff.y -= params.b * data.x
diff.y += params.c * data.y
diff.y -= data.y
  Demo 0: a = 1.025, b = 3.947, c = 0.622
  Demo 1: a = 0.989, b = 1.524, c = 0.716
  Demo 2: a = 1.021, b = 8.745, c = 0.406

-- score: -225.53 (accuracy -229.03, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.012, b = 3.947, c = 0.378
  Demo 1: a = 0.003, b = 1.524, c = 0.284
  Demo 2: a = 0.018, b = 8.745, c = 0.594

-- score: -225.45 (accuracy -228.95, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.000, b = 3.947, c = 0.378
  Demo 1: a = 0.005, b = 1.523, c = 0.283
  Demo 2: a = 0.067, b = 8.751, c = 0.598

-- score: -225.36 (accuracy -229.06, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = -0.028, b = 3.947, c = 0.378
  Demo 1: a = 0.019, b = 1.524, c = 0.284
  Demo 2: a = -0.005, b = 8.745, c = 0.594

-- score: -225.25 (accuracy -229.15, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += data.y
diff.x -= params.a * data.y * data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.017, b = 3.947, c = 0.378
  Demo 1: a = 0.013, b = 1.524, c = 0.284
  Demo 2: a = 0.002, b = 8.745, c = 0.594

-- score: -225.23 (accuracy -228.93, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += data.y
diff.y -= params.a * data.x
diff.y += params.b * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.947, b = 0.036, c = 0.415
  Demo 1: a = 1.524, b = 0.004, c = 0.288
  Demo 2: a = 8.745, b = 0.020, c = 0.614

-- score: -225.21 (accuracy -229.11, token simplicity 2.40, parameter simplicity 1.50) --
diff.x += params.a * data.x * data.y
diff.x += data.y
diff.y -= params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 0.052, b = 3.947, c = 0.378
  Demo 1: a = -0.025, b = 1.524, c = 0.284
  Demo 2: a = 0.005, b = 8.745, c = 0.594

