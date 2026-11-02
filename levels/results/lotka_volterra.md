# lotka_volterra

Solved in 0.27 seconds. 382 programs considered, over 10 rounds.

## Winner

-- score: -234.28 (accuracy -239.08, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

## Runner-ups

-- score: -233.45 (accuracy -239.15, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -233.45 (accuracy -239.15, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -233.41 (accuracy -239.11, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -233.36 (accuracy -239.26, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

# The Search

## Round 0 | 0.00s | best score: -115.22

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -115.22 (accuracy -122.22, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040

-- score: -111.49 (accuracy -118.49, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 0.953, b = 0.058, c = -0.002, d = 0.081, e = 1.878, f = 0.009
  Demo 1: a = -0.322, b = 0.016, c = 0.000, d = 0.018, e = 0.837, f = 0.004
  Demo 2: a = -0.419, b = 0.029, c = -0.001, d = 0.099, e = 0.479, f = -0.014

-- score: -79.11 (accuracy -82.21, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y += params.c * data.y
  Demo 0: a = 16.105, b = 0.796, c = 0.023
  Demo 1: a = 9.060, b = 0.242, c = -0.033
  Demo 2: a = 4.846, b = 0.653, c = 0.050

-- score: -73.11 (accuracy -76.21, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
  Demo 0: a = 20.685, b = 0.061, c = 2.007
  Demo 1: a = 21.536, b = 0.034, c = 1.959
  Demo 2: a = 15.889, b = 0.094, c = 2.405

-- score: -44.25 (accuracy -45.55, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.x
  Demo 0: a = 0.009
  Demo 1: a = 0.001
  Demo 2: a = 0.019

## Round 1 | 0.03s | best score: -226.70

+72 new programs (72 actually scored)
* add_terms: +54
* delete_lines: +18
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -226.70 (accuracy -240.70, token simplicity 8.00, parameter simplicity 6.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y += params.h * data.x
diff.y += params.i * data.x * data.x
diff.y += params.j * data.x * data.y
diff.y -= params.k * data.y
diff.y += params.l * data.y * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 0.953, h = 0.058, i = -0.002, j = 0.081, k = 1.878, l = 0.009
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = -0.322, h = 0.016, i = 0.000, j = 0.018, k = 0.837, l = 0.004
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = -0.419, h = 0.029, i = -0.001, j = 0.099, k = 0.479, l = -0.014

-- score: -194.33 (accuracy -204.43, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y -= params.g
diff.y += params.h * data.x
diff.y += params.i * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 16.105, h = 0.796, i = 0.023
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = 9.060, h = 0.242, i = -0.033
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = 4.846, h = 0.653, i = 0.050

-- score: -184.60 (accuracy -194.70, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y += params.f * data.x * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
diff.y += params.i * data.y * data.y
  Demo 0: a = 20.685, b = 0.061, c = 2.007, d = 0.953, e = 0.058, f = -0.002, g = 0.081, h = 1.878, i = 0.009
  Demo 1: a = 21.536, b = 0.034, c = 1.959, d = -0.322, e = 0.016, f = 0.000, g = 0.018, h = 0.837, i = 0.004
  Demo 2: a = 15.889, b = 0.094, c = 2.405, d = -0.419, e = 0.029, f = -0.001, g = 0.099, h = 0.479, i = -0.014

-- score: -159.47 (accuracy -167.77, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x * data.x
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 0.009
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = 0.001
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = 0.019

-- score: -152.22 (accuracy -158.42, token simplicity 3.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
diff.y += params.f * data.y
  Demo 0: a = 20.685, b = 0.061, c = 2.007, d = 16.105, e = 0.796, f = 0.023
  Demo 1: a = 21.536, b = 0.034, c = 1.959, d = 9.060, e = 0.242, f = -0.033
  Demo 2: a = 15.889, b = 0.094, c = 2.405, d = 4.846, e = 0.653, f = 0.050

## Round 2 | 0.05s | best score: -229.02

+64 new programs (64 actually scored)
* add_terms: +22
* delete_lines: +42
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -229.02 (accuracy -240.42, token simplicity 6.40, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
diff.y += params.j * data.y * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.953, f = 0.058, g = -0.002, h = 0.081, i = 1.878, j = 0.009
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = -0.322, f = 0.016, g = 0.000, h = 0.018, i = 0.837, j = 0.004
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = -0.419, f = 0.029, g = -0.001, h = 0.099, i = 0.479, j = -0.014

-- score: -228.94 (accuracy -240.34, token simplicity 6.40, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y += params.h * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 1.022, h = -0.051, i = 0.080, j = 1.629
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = -1.042, h = 0.030, i = 0.018, j = 0.728
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = 0.218, h = 0.002, i = 0.099, j = 0.706

-- score: -227.99 (accuracy -240.69, token simplicity 7.20, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y += params.h * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 2.379, h = -0.044, i = 0.081, j = 2.002, k = 0.013
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = -0.706, h = 0.030, i = 0.018, j = 0.806, k = 0.003
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = -0.192, h = -0.001, i = 0.099, j = 0.538, k = -0.010

-- score: -227.93 (accuracy -240.63, token simplicity 7.20, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y += params.h * data.x
diff.y += params.i * data.x * data.x
diff.y += params.j * data.x * data.y
diff.y -= params.k * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = -1.390, h = 0.208, i = -0.005, j = 0.081, k = 1.632
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = -1.421, h = 0.052, i = -0.000, j = 0.018, k = 0.729
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = 0.335, h = -0.040, i = 0.002, j = 0.099, k = 0.708

-- score: -227.88 (accuracy -240.58, token simplicity 7.20, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = -4.626, b = 1.293, c = 0.001, d = 0.120, e = 0.467, f = 0.953, g = 0.058, h = -0.002, i = 0.081, j = 1.878, k = 0.009
  Demo 1: a = 2.792, b = 0.424, c = 0.002, d = 0.050, e = -0.027, f = -0.322, g = 0.016, h = 0.000, i = 0.018, j = 0.837, k = 0.004
  Demo 2: a = 0.167, b = 2.140, c = -0.002, d = 0.306, e = -0.072, f = -0.419, g = 0.029, h = -0.001, i = 0.099, j = 0.479, k = -0.014

## Round 3 | 0.04s | best score: -230.30

+47 new programs (47 actually scored)
* add_terms: +0
* delete_lines: +47
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -230.30 (accuracy -240.40, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
diff.y += params.i * data.y * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 2.379, f = -0.044, g = 0.081, h = 2.002, i = 0.013
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = -0.706, f = 0.030, g = 0.018, h = 0.806, i = 0.003
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = -0.192, f = -0.001, g = 0.099, h = 0.538, i = -0.010

-- score: -230.24 (accuracy -240.34, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = -1.390, f = 0.208, g = -0.005, h = 0.081, i = 1.632
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = -1.421, f = 0.052, g = -0.000, h = 0.018, i = 0.729
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.335, f = -0.040, g = 0.002, h = 0.099, i = 0.708

-- score: -230.12 (accuracy -240.22, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = -4.626, b = 1.293, c = 0.001, d = 0.120, e = 0.467, f = 1.022, g = -0.051, h = 0.080, i = 1.629
  Demo 1: a = 2.792, b = 0.424, c = 0.002, d = 0.050, e = -0.027, f = -1.042, g = 0.030, h = 0.018, i = 0.728
  Demo 2: a = 0.167, b = 2.140, c = -0.002, d = 0.306, e = -0.072, f = 0.218, g = 0.002, h = 0.099, i = 0.706

-- score: -230.11 (accuracy -240.41, token simplicity 5.80, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
diff.y += params.i * data.y * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 1.777, f = -0.001, g = 0.081, h = 1.949, i = 0.011
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.112, f = 0.000, g = 0.018, h = 0.871, i = 0.005
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = -0.198, f = -0.000, g = 0.100, h = 0.532, i = -0.011

-- score: -230.06 (accuracy -240.16, token simplicity 5.60, parameter simplicity 4.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 4.696, b = 1.330, c = 0.120, d = 0.392, e = 0.003, f = 1.022, g = -0.051, h = 0.080, i = 1.629
  Demo 1: a = 2.344, b = 0.621, c = 0.049, d = 0.353, e = -0.013, f = -1.042, g = 0.030, h = 0.018, i = 0.728
  Demo 2: a = 0.173, b = 2.099, c = 0.306, d = 0.108, e = -0.011, f = 0.218, g = 0.002, h = 0.099, i = 0.706

## Round 4 | 0.03s | best score: -231.25

+43 new programs (43 actually scored)
* add_terms: +2
* delete_lines: +41
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -231.25 (accuracy -240.05, token simplicity 4.80, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 1.022, f = -0.051, g = 0.080, h = 1.629
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = -1.042, f = 0.030, g = 0.018, h = 0.728
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.218, f = 0.002, g = 0.099, h = 0.706

-- score: -231.15 (accuracy -240.15, token simplicity 5.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
diff.y += params.h * data.y * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 1.523, f = 0.077, g = 1.944, h = 0.014
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.420, f = 0.020, g = 0.881, h = 0.003
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = -0.197, f = 0.099, g = 0.538, h = -0.010

-- score: -231.09 (accuracy -240.09, token simplicity 5.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.873, f = -0.002, g = 0.082, h = 1.675
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = -0.358, f = 0.000, g = 0.018, h = 0.747
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.165, f = 0.001, g = 0.098, h = 0.696

-- score: -231.00 (accuracy -240.00, token simplicity 5.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = -2.677, b = 1.296, c = 0.116, d = 0.014, e = 1.022, f = -0.051, g = 0.080, h = 1.629
  Demo 1: a = -0.295, b = 0.602, c = 0.048, d = -0.004, e = -1.042, f = 0.030, g = 0.018, h = 0.728
  Demo 2: a = 0.138, b = 2.095, c = 0.305, d = -0.005, e = 0.218, f = 0.002, g = 0.099, h = 0.706

-- score: -230.95 (accuracy -239.95, token simplicity 5.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.y += params.f
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = -4.626, b = 1.293, c = 0.001, d = 0.120, e = 0.467, f = -0.016, g = 0.076, h = 1.550
  Demo 1: a = 2.792, b = 0.424, c = 0.002, d = 0.050, e = -0.027, f = 0.084, g = 0.020, h = 0.803
  Demo 2: a = 0.167, b = 2.140, c = -0.002, d = 0.306, e = -0.072, f = 0.234, g = 0.099, h = 0.707

## Round 5 | 0.03s | best score: -232.08

+43 new programs (43 actually scored)
* add_terms: +7
* delete_lines: +36
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -232.08 (accuracy -239.78, token simplicity 4.20, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = -0.016, f = 0.076, g = 1.550
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.084, f = 0.020, g = 0.803
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.234, f = 0.099, g = 0.707

-- score: -231.94 (accuracy -239.84, token simplicity 4.40, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = -0.008, f = 0.077, g = 1.553
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.007, f = 0.019, g = 0.797
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.019, f = 0.097, g = 0.681

-- score: -231.84 (accuracy -239.94, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = -0.001, f = 0.079, g = 1.580
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.000, f = 0.019, g = 0.781
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.001, f = 0.096, g = 0.675

-- score: -231.83 (accuracy -239.73, token simplicity 4.40, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = -2.677, b = 1.296, c = 0.116, d = 0.014, e = -0.016, f = 0.076, g = 1.550
  Demo 1: a = -0.295, b = 0.602, c = 0.048, d = -0.004, e = 0.084, f = 0.020, g = 0.803
  Demo 2: a = 0.138, b = 2.095, c = 0.305, d = -0.005, e = 0.234, f = 0.099, g = 0.707

-- score: -231.82 (accuracy -239.92, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = -4.626, b = 1.293, c = 0.001, d = 0.120, e = 0.467, f = 0.076, g = 1.551
  Demo 1: a = 2.792, b = 0.424, c = 0.002, d = 0.050, e = -0.027, f = 0.020, g = 0.798
  Demo 2: a = 0.167, b = 2.140, c = -0.002, d = 0.306, e = -0.072, f = 0.100, g = 0.683

## Round 6 | 0.02s | best score: -232.95

+41 new programs (41 actually scored)
* add_terms: +10
* delete_lines: +31
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -232.95 (accuracy -239.75, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.076, f = 1.551
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.020, f = 0.798
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.100, f = 0.683

-- score: -232.70 (accuracy -239.70, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -2.677, b = 1.296, c = 0.116, d = 0.014, e = 0.076, f = 1.551
  Demo 1: a = -0.295, b = 0.602, c = 0.048, d = -0.004, e = 0.020, f = 0.798
  Demo 2: a = 0.138, b = 2.095, c = 0.305, d = -0.005, e = 0.100, f = 0.683

-- score: -232.58 (accuracy -239.18, token simplicity 3.60, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.234, e = 0.099, f = 0.707

-- score: -232.49 (accuracy -239.29, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.234, e = 0.099, f = 0.707

-- score: -232.46 (accuracy -239.66, token simplicity 4.20, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.943, b = 0.006, c = 0.114, d = 0.305, e = 0.076, f = 1.551
  Demo 1: a = 0.534, b = 0.001, c = 0.052, d = 0.062, e = 0.020, f = 0.798
  Demo 2: a = 2.161, b = -0.002, c = 0.307, d = -0.056, e = 0.100, f = 0.683

## Round 7 | 0.02s | best score: -233.45

+39 new programs (39 actually scored)
* add_terms: +13
* delete_lines: +26
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -233.45 (accuracy -239.15, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -233.41 (accuracy -239.11, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -233.36 (accuracy -239.26, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -233.31 (accuracy -239.41, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

-- score: -233.14 (accuracy -239.24, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.100, b = 0.001, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.552, b = 0.001, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

## Round 8 | 0.02s | best score: -234.28

+43 new programs (43 actually scored)
* add_terms: +22
* delete_lines: +21
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -234.28 (accuracy -239.08, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -233.45 (accuracy -239.15, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -233.41 (accuracy -239.11, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -233.36 (accuracy -239.26, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -233.31 (accuracy -239.41, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

## Round 9 | 0.01s | best score: -234.28

+7 new programs (7 actually scored)
* add_terms: +3
* delete_lines: +4
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -234.28 (accuracy -239.08, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -233.45 (accuracy -239.15, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -233.41 (accuracy -239.11, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -233.36 (accuracy -239.26, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -233.31 (accuracy -239.41, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

