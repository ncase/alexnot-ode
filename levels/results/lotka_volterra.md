# lotka_volterra

Solved in 0.39 seconds. 525 programs considered, over 7 rounds.

## Winner

-- score: -56.19 (accuracy -60.99, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

## Runner-ups

-- score: -55.31 (accuracy -61.01, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -55.30 (accuracy -61.00, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -55.14 (accuracy -61.04, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -55.11 (accuracy -61.01, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

# The Search

## Round 0 | 0.00s | best score: -24.18

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -24.18 (accuracy -31.18, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040

-- score: -23.23 (accuracy -30.23, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 0.953, b = 0.058, c = -0.002, d = 0.081, e = 1.878, f = 0.009
  Demo 1: a = -0.322, b = 0.016, c = 0.000, d = 0.018, e = 0.837, f = 0.004
  Demo 2: a = -0.419, b = 0.029, c = -0.001, d = 0.099, e = 0.479, f = -0.014

-- score: -17.87 (accuracy -20.97, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y += params.c * data.y
  Demo 0: a = 16.105, b = 0.796, c = 0.023
  Demo 1: a = 9.060, b = 0.242, c = -0.033
  Demo 2: a = 4.846, b = 0.653, c = 0.050

-- score: -16.34 (accuracy -19.44, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
  Demo 0: a = 20.685, b = 0.061, c = 2.007
  Demo 1: a = 21.536, b = 0.034, c = 1.959
  Demo 2: a = 15.889, b = 0.094, c = 2.405

-- score: -10.32 (accuracy -11.62, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.x
  Demo 0: a = 0.009
  Demo 1: a = 0.001
  Demo 2: a = 0.019

-- score: -7.79 (accuracy -9.09, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.y
  Demo 0: a = 0.022
  Demo 1: a = 0.005
  Demo 2: a = 0.060

-- score: -6.35 (accuracy -7.45, token simplicity 0.60, parameter simplicity 0.50) --
diff.y += params.a * data.x
  Demo 0: a = 0.241
  Demo 1: a = 0.061
  Demo 2: a = 0.397

-- score: -5.71 (accuracy -7.01, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.y * data.y
  Demo 0: a = 0.039
  Demo 1: a = 0.038
  Demo 2: a = 0.075

-- score: -2.00 (accuracy -3.30, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.x * data.y
  Demo 0: a = 0.022
  Demo 1: a = 0.015
  Demo 2: a = 0.050

-- score: -1.94 (accuracy -3.04, token simplicity 0.60, parameter simplicity 0.50) --
diff.x -= params.a * data.y
  Demo 0: a = 0.543
  Demo 1: a = 0.638
  Demo 2: a = 0.584

## Round 1 | 0.05s | best score: -47.40

+137 new programs (137 actually scored)
* add_terms: +120
* delete_lines: +15
* delete_near_zeros: +2
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -47.40 (accuracy -61.40, token simplicity 8.00, parameter simplicity 6.00) --
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

-- score: -42.05 (accuracy -52.15, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -39.57 (accuracy -49.67, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -34.50 (accuracy -42.80, token simplicity 4.80, parameter simplicity 3.50) --
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

-- score: -34.21 (accuracy -40.41, token simplicity 3.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
diff.y += params.f * data.y
  Demo 0: a = 20.685, b = 0.061, c = 2.007, d = 16.105, e = 0.796, f = 0.023
  Demo 1: a = 21.536, b = 0.034, c = 1.959, d = 9.060, e = 0.242, f = -0.033
  Demo 2: a = 15.889, b = 0.094, c = 2.405, d = 4.846, e = 0.653, f = 0.050

-- score: -31.97 (accuracy -40.27, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 0.022
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = 0.005
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = 0.060

-- score: -30.53 (accuracy -38.63, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 0.241
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = 0.061
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = 0.397

-- score: -28.93 (accuracy -37.23, token simplicity 4.80, parameter simplicity 3.50) --
diff.x -= params.a * data.y * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 0.039, b = 0.953, c = 0.058, d = -0.002, e = 0.081, f = 1.878, g = 0.009
  Demo 1: a = 0.038, b = -0.322, c = 0.016, d = 0.000, e = 0.018, f = 0.837, g = 0.004
  Demo 2: a = 0.075, b = -0.419, c = 0.029, d = -0.001, e = 0.099, f = 0.479, g = -0.014

-- score: -28.54 (accuracy -30.94, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
  Demo 0: a = 1.117, b = 0.100
  Demo 1: a = 0.608, b = 0.050
  Demo 2: a = 2.127, b = 0.312

-- score: -27.66 (accuracy -30.06, token simplicity 1.40, parameter simplicity 1.00) --
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
  Demo 0: a = 0.076, b = 1.551
  Demo 1: a = 0.020, b = 0.798
  Demo 2: a = 0.100, b = 0.683

## Round 2 | 0.10s | best score: -51.83

+134 new programs (134 actually scored)
* add_terms: +61
* delete_lines: +60
* delete_near_zeros: +8
* relate_parameters: +4
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -51.83 (accuracy -61.23, token simplicity 5.40, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 0.076, h = 1.551
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = 0.020, h = 0.798
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = 0.100, h = 0.683

-- score: -51.76 (accuracy -61.16, token simplicity 5.40, parameter simplicity 4.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y += params.e * data.x * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
diff.y += params.h * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.953, d = 0.058, e = -0.002, f = 0.081, g = 1.878, h = 0.009
  Demo 1: a = 0.608, b = 0.050, c = -0.322, d = 0.016, e = 0.000, f = 0.018, g = 0.837, h = 0.004
  Demo 2: a = 2.127, b = 0.312, c = -0.419, d = 0.029, e = -0.001, f = 0.099, g = 0.479, h = -0.014

-- score: -51.17 (accuracy -61.27, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -49.93 (accuracy -61.33, token simplicity 6.40, parameter simplicity 5.00) --
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

-- score: -49.91 (accuracy -61.31, token simplicity 6.40, parameter simplicity 5.00) --
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

-- score: -48.70 (accuracy -61.40, token simplicity 7.20, parameter simplicity 5.50) --
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

-- score: -48.68 (accuracy -61.38, token simplicity 7.20, parameter simplicity 5.50) --
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

-- score: -48.67 (accuracy -61.37, token simplicity 7.20, parameter simplicity 5.50) --
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

-- score: -48.66 (accuracy -61.36, token simplicity 7.20, parameter simplicity 5.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 4.696, b = 1.330, c = 0.120, d = 0.392, e = 0.003, f = 0.953, g = 0.058, h = -0.002, i = 0.081, j = 1.878, k = 0.009
  Demo 1: a = 2.344, b = 0.621, c = 0.049, d = 0.353, e = -0.013, f = -0.322, g = 0.016, h = 0.000, i = 0.018, j = 0.837, k = 0.004
  Demo 2: a = 0.173, b = 2.099, c = 0.306, d = 0.108, e = -0.011, f = -0.419, g = 0.029, h = -0.001, i = 0.099, j = 0.479, k = -0.014

-- score: -48.50 (accuracy -61.40, token simplicity 7.40, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = -0.084, b = 1.002, c = 0.007, d = 0.120, e = -0.010, f = 0.017, g = 1.777, h = -0.001, i = 0.081, j = 1.949, k = 0.011
  Demo 1: a = 4.304, b = 0.374, c = 0.003, d = 0.050, e = -0.175, f = 0.005, g = 0.112, h = 0.000, i = 0.018, j = 0.871, k = 0.005
  Demo 2: a = -2.008, b = 2.340, c = -0.011, d = 0.304, e = 0.590, f = -0.040, g = -0.198, h = -0.000, i = 0.100, j = 0.532, k = -0.011

## Round 3 | 0.11s | best score: -54.27

+103 new programs (103 actually scored)
* add_terms: +12
* delete_lines: +81
* delete_near_zeros: +7
* relate_parameters: +3
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -54.27 (accuracy -61.07, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.117, b = 0.100, c = 1.022, d = -0.051, e = 0.080, f = 1.629
  Demo 1: a = 0.608, b = 0.050, c = -1.042, d = 0.030, e = 0.018, f = 0.728
  Demo 2: a = 2.127, b = 0.312, c = 0.218, d = 0.002, e = 0.099, f = 0.706

-- score: -53.10 (accuracy -61.20, token simplicity 4.60, parameter simplicity 3.50) --
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

-- score: -53.09 (accuracy -61.19, token simplicity 4.60, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 4.696, b = 1.330, c = 0.120, d = 0.392, e = 0.003, f = 0.076, g = 1.551
  Demo 1: a = 2.344, b = 0.621, c = 0.049, d = 0.353, e = -0.013, f = 0.020, g = 0.798
  Demo 2: a = 0.173, b = 2.099, c = 0.306, d = 0.108, e = -0.011, f = 0.100, g = 0.683

-- score: -53.06 (accuracy -61.16, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 2.379, d = -0.044, e = 0.081, f = 2.002, g = 0.013
  Demo 1: a = 0.608, b = 0.050, c = -0.706, d = 0.030, e = 0.018, f = 0.806, g = 0.003
  Demo 2: a = 2.127, b = 0.312, c = -0.192, d = -0.001, e = 0.099, f = 0.538, g = -0.010

-- score: -53.04 (accuracy -61.14, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y += params.e * data.x * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 1.117, b = 0.100, c = -1.390, d = 0.208, e = -0.005, f = 0.081, g = 1.632
  Demo 1: a = 0.608, b = 0.050, c = -1.421, d = 0.052, e = -0.000, f = 0.018, g = 0.729
  Demo 2: a = 2.127, b = 0.312, c = 0.335, d = -0.040, e = 0.002, f = 0.099, g = 0.708

-- score: -52.92 (accuracy -61.22, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = -0.182, b = 1.008, c = 0.007, d = 0.120, e = 0.017, f = 0.076, g = 1.551
  Demo 1: a = 2.505, b = 0.431, c = 0.002, d = 0.050, e = -0.000, f = 0.020, g = 0.798
  Demo 2: a = 0.019, b = 2.154, c = -0.003, d = 0.303, e = -0.006, f = 0.100, g = 0.683

-- score: -52.86 (accuracy -61.16, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 1.777, d = -0.001, e = 0.081, f = 1.949, g = 0.011
  Demo 1: a = 0.608, b = 0.050, c = 0.112, d = 0.000, e = 0.018, f = 0.871, g = 0.005
  Demo 2: a = 2.127, b = 0.312, c = -0.198, d = -0.000, e = 0.100, f = 0.532, g = -0.011

-- score: -52.72 (accuracy -61.22, token simplicity 5.00, parameter simplicity 3.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 0.997, b = 0.007, c = 0.120, d = -0.018, e = 0.018, f = 0.076, g = 1.551
  Demo 1: a = 0.521, b = 0.001, c = 0.050, d = 0.188, e = -0.006, f = 0.020, g = 0.798
  Demo 2: a = 2.143, b = -0.003, c = 0.302, d = 0.072, e = -0.012, f = 0.100, g = 0.683

-- score: -52.66 (accuracy -61.16, token simplicity 5.00, parameter simplicity 3.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.121, d = -0.003, e = 0.080, f = 1.790, g = 0.006
  Demo 1: a = 0.608, b = 0.050, c = 0.005, d = 0.000, e = 0.018, f = 0.864, g = 0.004
  Demo 2: a = 2.127, b = 0.312, c = -0.012, d = 0.000, e = 0.100, f = 0.587, g = -0.008

-- score: -52.44 (accuracy -61.24, token simplicity 4.80, parameter simplicity 4.00) --
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

## Round 4 | 0.06s | best score: -55.31

+93 new programs (93 actually scored)
* add_terms: +35
* delete_lines: +52
* delete_near_zeros: +6
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -55.31 (accuracy -61.01, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -55.30 (accuracy -61.00, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -55.14 (accuracy -61.04, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -55.11 (accuracy -61.01, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -54.36 (accuracy -61.16, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.076, f = 1.551
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.020, f = 0.798
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.100, f = 0.683

-- score: -54.27 (accuracy -61.07, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.117, b = 0.100, c = 1.022, d = -0.051, e = 0.080, f = 1.629
  Demo 1: a = 0.608, b = 0.050, c = -1.042, d = 0.030, e = 0.018, f = 0.728
  Demo 2: a = 2.127, b = 0.312, c = 0.218, d = 0.002, e = 0.099, f = 0.706

-- score: -54.15 (accuracy -61.15, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -2.677, b = 1.296, c = 0.116, d = 0.014, e = 0.076, f = 1.551
  Demo 1: a = -0.295, b = 0.602, c = 0.048, d = -0.004, e = 0.020, f = 0.798
  Demo 2: a = 0.138, b = 2.095, c = 0.305, d = -0.005, e = 0.100, f = 0.683

-- score: -54.09 (accuracy -61.09, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 1.523, d = 0.077, e = 1.944, f = 0.014
  Demo 1: a = 0.608, b = 0.050, c = 0.420, d = 0.020, e = 0.881, f = 0.003
  Demo 2: a = 2.127, b = 0.312, c = -0.197, d = 0.099, e = 0.538, f = -0.010

-- score: -54.08 (accuracy -61.08, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.873, d = -0.002, e = 0.082, f = 1.675
  Demo 1: a = 0.608, b = 0.050, c = -0.358, d = 0.000, e = 0.018, f = 0.747
  Demo 2: a = 2.127, b = 0.312, c = 0.165, d = 0.001, e = 0.098, f = 0.696

-- score: -54.05 (accuracy -61.05, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.018, b = 1.099, c = 0.001, d = 0.100, e = 0.076, f = 1.551
  Demo 1: a = 2.495, b = 0.430, c = 0.002, d = 0.051, e = 0.020, f = 0.798
  Demo 2: a = -0.316, b = 2.184, c = -0.002, d = 0.311, e = 0.100, f = 0.683

## Round 5 | 0.04s | best score: -56.19

+73 new programs (73 actually scored)
* add_terms: +36
* delete_lines: +36
* delete_near_zeros: +1
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -56.19 (accuracy -60.99, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -55.31 (accuracy -61.01, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -55.30 (accuracy -61.00, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -55.14 (accuracy -61.04, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -55.11 (accuracy -61.01, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -54.97 (accuracy -61.07, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

-- score: -54.94 (accuracy -61.04, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.001, d = 0.079, e = 1.580
  Demo 1: a = 0.608, b = 0.050, c = 0.000, d = 0.019, e = 0.781
  Demo 2: a = 2.127, b = 0.312, c = 0.001, d = 0.096, e = 0.675

-- score: -54.93 (accuracy -61.03, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.100, b = 0.001, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.552, b = 0.001, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

-- score: -54.93 (accuracy -61.03, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.077, d = 1.636, e = 0.004
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.806, e = 0.000
  Demo 2: a = 2.127, b = 0.312, c = 0.099, d = 0.598, e = -0.007

-- score: -54.42 (accuracy -61.02, token simplicity 3.60, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.234, e = 0.099, f = 0.707

## Round 6 | 0.02s | best score: -56.19 (stable)

+30 new programs (30 actually scored)
* add_terms: +10
* delete_lines: +20
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -56.19 (accuracy -60.99, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -55.31 (accuracy -61.01, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -55.30 (accuracy -61.00, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -55.14 (accuracy -61.04, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -55.11 (accuracy -61.01, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -54.97 (accuracy -61.07, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

-- score: -54.94 (accuracy -61.04, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.001, d = 0.079, e = 1.580
  Demo 1: a = 0.608, b = 0.050, c = 0.000, d = 0.019, e = 0.781
  Demo 2: a = 2.127, b = 0.312, c = 0.001, d = 0.096, e = 0.675

-- score: -54.93 (accuracy -61.03, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.100, b = 0.001, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.552, b = 0.001, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

-- score: -54.93 (accuracy -61.03, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.077, d = 1.636, e = 0.004
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.806, e = 0.000
  Demo 2: a = 2.127, b = 0.312, c = 0.099, d = 0.598, e = -0.007

-- score: -54.42 (accuracy -61.02, token simplicity 3.60, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.234, e = 0.099, f = 0.707

