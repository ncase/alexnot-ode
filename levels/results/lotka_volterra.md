# lotka_volterra

Solved in 0.40 seconds. 623 programs considered, over 6 rounds.

## Winner

-- score: -92.79 (accuracy -97.59, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

## Runner-ups

-- score: -92.39 (accuracy -97.59, token simplicity 3.20, parameter simplicity 2.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = -0.392, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 1.127, b = 0.312, c = 0.100, d = 0.683

-- score: -92.39 (accuracy -97.59, token simplicity 3.20, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = -0.392, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 1.127, b = 0.312, c = 0.100, d = 0.683

-- score: -91.91 (accuracy -97.61, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -91.90 (accuracy -97.60, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

# The Search

## Round 0 | 0.01s | best score: -90.17

+23 new programs (23 actually scored)
* linear_fit: +3
* quadratic_fit: +8
* add_single_terms: +12
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -90.17 (accuracy -97.87, token simplicity 4.20, parameter simplicity 3.50) --
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

-- score: -87.93 (accuracy -98.03, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -86.77 (accuracy -98.17, token simplicity 6.40, parameter simplicity 5.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
diff.y += params.j * data.y * data.y
  Demo 0: a = 4.696, b = 1.330, c = 0.120, d = 0.392, e = 0.003, f = 2.379, g = -0.044, h = 0.081, i = 2.002, j = 0.013
  Demo 1: a = 2.344, b = 0.621, c = 0.049, d = 0.353, e = -0.013, f = -0.706, g = 0.030, h = 0.018, i = 0.806, j = 0.003
  Demo 2: a = 0.173, b = 2.099, c = 0.306, d = 0.108, e = -0.011, f = -0.192, g = -0.001, h = 0.099, i = 0.538, j = -0.010

-- score: -85.54 (accuracy -98.24, token simplicity 7.20, parameter simplicity 5.50) --
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

-- score: -84.25 (accuracy -98.25, token simplicity 8.00, parameter simplicity 6.00) --
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

-- score: -62.01 (accuracy -66.61, token simplicity 2.60, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.386, d = 0.418
  Demo 1: a = 0.608, b = 0.050, c = 0.118, d = 0.274
  Demo 2: a = 2.127, b = 0.312, c = 0.515, d = 0.345

-- score: -60.44 (accuracy -64.44, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.y
diff.y -= params.c
diff.y += params.d * data.x
  Demo 0: a = 21.989, b = 2.000, c = 15.909, d = 0.797
  Demo 1: a = 22.764, b = 1.952, c = 9.378, d = 0.241
  Demo 2: a = 16.731, b = 2.406, c = 4.540, d = 0.653

-- score: -59.49 (accuracy -64.59, token simplicity 2.60, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
  Demo 0: a = 20.685, b = 0.061, c = 2.007, d = 15.909, e = 0.797
  Demo 1: a = 21.536, b = 0.034, c = 1.959, d = 9.378, e = 0.241
  Demo 2: a = 15.889, b = 0.094, c = 2.405, d = 4.540, e = 0.653

-- score: -58.46 (accuracy -64.66, token simplicity 3.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
diff.y += params.f * data.y
  Demo 0: a = 20.685, b = 0.061, c = 2.007, d = 16.105, e = 0.796, f = 0.023
  Demo 1: a = 21.536, b = 0.034, c = 1.959, d = 9.060, e = 0.242, f = -0.033
  Demo 2: a = 15.889, b = 0.094, c = 2.405, d = 4.846, e = 0.653, f = 0.050

-- score: -44.09 (accuracy -50.49, token simplicity 3.40, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.847, f = 0.115
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = -0.276, f = 0.012
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 1.004, f = 0.037

## Round 1 | 0.18s | best score: -91.72

+257 new programs (257 actually scored)
* linear_fit: +5
* quadratic_fit: +14
* add_single_terms: +35
* delete_interactions: +123
* delete_lines: +68
* delete_near_zeros: +8
* relate_parameters: +3
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -91.72 (accuracy -97.62, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -91.06 (accuracy -97.86, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.076, f = 1.551
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.020, f = 0.798
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.100, f = 0.683

-- score: -91.03 (accuracy -97.63, token simplicity 3.60, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.234, e = 0.099, f = 0.707

-- score: -90.87 (accuracy -97.67, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.234, e = 0.099, f = 0.707

-- score: -90.17 (accuracy -97.87, token simplicity 4.20, parameter simplicity 3.50) --
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

-- score: -90.13 (accuracy -97.63, token simplicity 4.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.y
diff.y += params.e
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = -2.837, b = 2.595, c = 1.126, d = 0.100, e = -0.016, f = 0.076, g = 1.550
  Demo 1: a = -0.844, b = -0.204, c = 0.630, d = 0.050, e = 0.084, f = 0.020, g = 0.803
  Demo 2: a = 0.069, b = -0.279, c = 2.141, d = 0.312, e = 0.234, f = 0.099, g = 0.707

-- score: -89.18 (accuracy -97.98, token simplicity 4.80, parameter simplicity 4.00) --
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

-- score: -89.02 (accuracy -98.02, token simplicity 5.00, parameter simplicity 4.00) --
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

-- score: -89.00 (accuracy -98.00, token simplicity 5.00, parameter simplicity 4.00) --
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

-- score: -88.96 (accuracy -97.96, token simplicity 5.00, parameter simplicity 4.00) --
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

## Round 2 | 0.11s | best score: -92.79

+196 new programs (196 actually scored)
* linear_fit: +5
* quadratic_fit: +10
* add_single_terms: +29
* delete_interactions: +103
* delete_lines: +42
* delete_near_zeros: +7
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -92.79 (accuracy -97.59, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -91.91 (accuracy -97.61, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -91.90 (accuracy -97.60, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -91.76 (accuracy -97.66, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -91.72 (accuracy -97.62, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -91.06 (accuracy -97.86, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.076, f = 1.551
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.020, f = 0.798
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.100, f = 0.683

-- score: -91.03 (accuracy -97.63, token simplicity 3.60, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.234, e = 0.099, f = 0.707

-- score: -91.01 (accuracy -97.61, token simplicity 3.60, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -2.837, b = 2.595, c = 1.126, d = 0.100, e = 0.076, f = 1.551
  Demo 1: a = -0.844, b = -0.204, c = 0.630, d = 0.050, e = 0.020, f = 0.798
  Demo 2: a = 0.069, b = -0.279, c = 2.141, d = 0.312, e = 0.100, f = 0.683

-- score: -90.91 (accuracy -97.71, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.117, b = 0.100, c = 1.022, d = -0.051, e = 0.080, f = 1.629
  Demo 1: a = 0.608, b = 0.050, c = -1.042, d = 0.030, e = 0.018, f = 0.728
  Demo 2: a = 2.127, b = 0.312, c = 0.218, d = 0.002, e = 0.099, f = 0.706

-- score: -90.87 (accuracy -97.67, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = -0.016, e = 0.076, f = 1.550
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.084, e = 0.020, f = 0.803
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.234, e = 0.099, f = 0.707

## Round 3 | 0.05s | best score: -92.79 (stable)

+100 new programs (100 actually scored)
* linear_fit: +0
* quadratic_fit: +4
* add_single_terms: +23
* delete_interactions: +53
* delete_lines: +19
* delete_near_zeros: +1
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -92.79 (accuracy -97.59, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -91.91 (accuracy -97.61, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -91.90 (accuracy -97.60, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -91.76 (accuracy -97.66, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -91.72 (accuracy -97.62, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -91.62 (accuracy -97.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

-- score: -91.56 (accuracy -97.66, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.001, d = 0.079, e = 1.580
  Demo 1: a = 0.608, b = 0.050, c = 0.000, d = 0.019, e = 0.781
  Demo 2: a = 2.127, b = 0.312, c = 0.001, d = 0.096, e = 0.675

-- score: -91.55 (accuracy -97.65, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.100, b = 0.001, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.552, b = 0.001, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

-- score: -91.54 (accuracy -97.64, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.077, d = 1.636, e = 0.004
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.806, e = 0.000
  Demo 2: a = 2.127, b = 0.312, c = 0.099, d = 0.598, e = -0.007

-- score: -91.06 (accuracy -97.86, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = -4.966, b = 1.329, c = 0.120, d = 0.466, e = 0.076, f = 1.551
  Demo 1: a = -0.673, b = 0.621, c = 0.049, d = -0.033, e = 0.020, f = 0.798
  Demo 2: a = 0.273, b = 2.102, c = 0.306, d = -0.075, e = 0.100, f = 0.683

## Round 4 | 0.03s | best score: -92.79 (stable)

+69 new programs (69 actually scored)
* linear_fit: +1
* quadratic_fit: +3
* add_single_terms: +7
* delete_interactions: +42
* delete_lines: +16
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -92.79 (accuracy -97.59, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -91.91 (accuracy -97.61, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -91.90 (accuracy -97.60, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -91.76 (accuracy -97.66, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -91.72 (accuracy -97.62, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -91.69 (accuracy -97.59, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.109, b = 0.009, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.580, b = 0.028, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

-- score: -91.62 (accuracy -97.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

-- score: -91.56 (accuracy -97.66, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.001, d = 0.079, e = 1.580
  Demo 1: a = 0.608, b = 0.050, c = 0.000, d = 0.019, e = 0.781
  Demo 2: a = 2.127, b = 0.312, c = 0.001, d = 0.096, e = 0.675

-- score: -91.55 (accuracy -97.65, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.100, b = 0.001, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.552, b = 0.001, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

-- score: -91.54 (accuracy -97.64, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.077, d = 1.636, e = 0.004
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.806, e = 0.000
  Demo 2: a = 2.127, b = 0.312, c = 0.099, d = 0.598, e = -0.007

## Round 5 | 0.02s | best score: -92.79 (stable)

+28 new programs (28 actually scored)
* linear_fit: +4
* quadratic_fit: +6
* add_single_terms: +5
* delete_interactions: +10
* delete_lines: +3
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -92.79 (accuracy -97.59, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = 0.608, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 2.127, b = 0.312, c = 0.100, d = 0.683

-- score: -92.39 (accuracy -97.59, token simplicity 3.20, parameter simplicity 2.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.117, b = 0.100, c = 0.076, d = 1.551
  Demo 1: a = -0.392, b = 0.050, c = 0.020, d = 0.798
  Demo 2: a = 1.127, b = 0.312, c = 0.100, d = 0.683

-- score: -91.91 (accuracy -97.61, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.243, b = 1.126, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 1.048, b = 0.630, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 0.209, b = 2.141, c = 0.312, d = 0.100, e = 0.683

-- score: -91.90 (accuracy -97.60, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.016, d = 0.076, e = 1.550
  Demo 1: a = 0.608, b = 0.050, c = 0.084, d = 0.020, e = 0.803
  Demo 2: a = 2.127, b = 0.312, c = 0.234, d = 0.099, e = 0.707

-- score: -91.76 (accuracy -97.66, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.122, b = 0.104, c = 0.099, d = 0.076, e = 1.551
  Demo 1: a = 0.606, b = 0.048, c = -0.078, d = 0.020, e = 0.798
  Demo 2: a = 2.123, b = 0.308, c = -0.044, d = 0.100, e = 0.683

-- score: -91.72 (accuracy -97.62, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.008, d = 0.077, e = 1.553
  Demo 1: a = 0.608, b = 0.050, c = 0.007, d = 0.019, e = 0.797
  Demo 2: a = 2.127, b = 0.312, c = 0.019, d = 0.097, e = 0.681

-- score: -91.69 (accuracy -97.59, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.109, b = 0.009, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.580, b = 0.028, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

-- score: -91.62 (accuracy -97.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.153, b = 0.107, c = 0.006, d = 0.076, e = 1.551
  Demo 1: a = 0.594, b = 0.047, c = -0.004, d = 0.020, e = 0.798
  Demo 2: a = 2.108, b = 0.306, c = -0.004, d = 0.100, e = 0.683

-- score: -91.56 (accuracy -97.66, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.100, c = -0.001, d = 0.079, e = 1.580
  Demo 1: a = 0.608, b = 0.050, c = 0.000, d = 0.019, e = 0.781
  Demo 2: a = 2.127, b = 0.312, c = 0.001, d = 0.096, e = 0.675

-- score: -91.55 (accuracy -97.65, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.100, b = 0.001, c = 0.100, d = 0.076, e = 1.551
  Demo 1: a = 0.552, b = 0.001, c = 0.050, d = 0.020, e = 0.798
  Demo 2: a = 2.127, b = 0.000, c = 0.312, d = 0.100, e = 0.683

