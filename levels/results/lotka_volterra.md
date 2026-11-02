# lotka_volterra

Solved in 0.34 seconds. 534 programs considered, over 5 rounds.

## Winner

-- score: -183.84 (accuracy -188.64, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.695

## Runner-ups

-- score: -183.44 (accuracy -188.64, token simplicity 3.20, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
diff.y += params.d * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = -0.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.198
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.305

-- score: -183.44 (accuracy -188.64, token simplicity 3.20, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 2.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 1.802
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 1.695

-- score: -182.98 (accuracy -188.68, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.100, e = 0.695

-- score: -182.95 (accuracy -188.65, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.024, d = 0.076, e = 1.533
  Demo 1: a = 0.606, b = 0.050, c = 0.043, d = 0.020, e = 0.805
  Demo 2: a = 2.082, b = 0.309, c = 0.098, d = 0.100, e = 0.705

# The Search

## Round 0 | 0.01s | best score: -182.09

+24 new programs (24 actually scored)
* linear_fit: +3
* quadratic_fit: +9
* add_single_terms: +12
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -182.09 (accuracy -188.69, token simplicity 3.60, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = -0.024, e = 0.076, f = 1.533
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = 0.043, e = 0.020, f = 0.805
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.098, e = 0.100, f = 0.705

-- score: -181.28 (accuracy -188.98, token simplicity 4.20, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 2.782, b = 1.234, c = 0.112, d = 0.259, e = -0.024, f = 0.076, g = 1.533
  Demo 1: a = 0.677, b = 0.620, c = 0.050, d = 0.012, e = 0.043, f = 0.020, g = 0.805
  Demo 2: a = 0.088, b = 2.087, c = 0.308, d = -0.007, e = 0.098, f = 0.100, g = 0.705

-- score: -180.28 (accuracy -189.08, token simplicity 4.80, parameter simplicity 4.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 2.782, b = 1.234, c = 0.112, d = 0.259, e = 0.647, f = -0.032, g = 0.079, h = 1.584
  Demo 1: a = 0.677, b = 0.620, c = 0.050, d = 0.012, e = -0.417, f = 0.012, g = 0.019, h = 0.774
  Demo 2: a = 0.088, b = 2.087, c = 0.308, d = -0.007, e = 0.164, f = -0.008, g = 0.101, h = 0.713

-- score: -179.05 (accuracy -189.15, token simplicity 5.60, parameter simplicity 4.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 2.585, b = 1.234, c = 0.112, d = 0.206, e = 0.002, f = 0.647, g = -0.032, h = 0.079, i = 1.584
  Demo 1: a = 1.702, b = 0.619, c = 0.050, d = 0.253, e = -0.008, f = -0.417, g = 0.012, h = 0.019, i = 0.774
  Demo 2: a = 0.333, b = 2.086, c = 0.308, d = 0.090, e = -0.006, f = 0.164, g = -0.008, h = 0.101, i = 0.713

-- score: -177.89 (accuracy -189.29, token simplicity 6.40, parameter simplicity 5.00) --
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
  Demo 0: a = 2.585, b = 1.234, c = 0.112, d = 0.206, e = 0.002, f = 1.325, g = -0.030, h = 0.079, i = 1.766, j = 0.007
  Demo 1: a = 1.702, b = 0.619, c = 0.050, d = 0.253, e = -0.008, f = -0.263, g = 0.012, h = 0.019, i = 0.810, j = 0.001
  Demo 2: a = 0.333, b = 2.086, c = 0.308, d = 0.090, e = -0.006, f = -0.098, g = -0.009, h = 0.101, i = 0.609, j = -0.006

-- score: -176.62 (accuracy -189.32, token simplicity 7.20, parameter simplicity 5.50) --
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
  Demo 0: a = 2.585, b = 1.234, c = 0.112, d = 0.206, e = 0.002, f = -0.327, g = 0.085, h = -0.002, i = 0.079, j = 1.616, k = 0.001
  Demo 1: a = 1.702, b = 0.619, c = 0.050, d = 0.253, e = -0.008, f = 0.270, g = -0.007, h = 0.000, i = 0.019, j = 0.855, k = 0.003
  Demo 2: a = 0.333, b = 2.086, c = 0.308, d = 0.090, e = -0.006, f = -0.499, g = 0.043, h = -0.002, i = 0.101, j = 0.504, k = -0.013

-- score: -175.41 (accuracy -189.41, token simplicity 8.00, parameter simplicity 6.00) --
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
  Demo 0: a = 2.476, b = 0.884, c = 0.007, d = 0.112, e = -0.255, f = 0.019, g = -0.327, h = 0.085, i = -0.002, j = 0.079, k = 1.616, l = 0.001
  Demo 1: a = 0.930, b = 0.524, c = 0.001, d = 0.051, e = 0.034, f = -0.001, g = 0.270, h = -0.007, i = 0.000, j = 0.019, k = 0.855, l = 0.003
  Demo 2: a = -0.894, b = 2.158, c = -0.003, d = 0.308, e = 0.236, f = -0.015, g = -0.499, h = 0.043, i = -0.002, j = 0.101, k = 0.504, l = -0.013

-- score: -95.81 (accuracy -99.81, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.y
diff.y -= params.c
diff.y += params.d * data.x
  Demo 0: a = 22.547, b = 2.061, c = 15.840, d = 0.796
  Demo 1: a = 22.850, b = 1.952, c = 9.260, d = 0.238
  Demo 2: a = 16.555, b = 2.378, c = 4.640, d = 0.649

-- score: -94.94 (accuracy -100.04, token simplicity 2.60, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
  Demo 0: a = 21.304, b = 0.058, c = 2.067, d = 15.840, e = 0.796
  Demo 1: a = 21.929, b = 0.025, c = 1.956, d = 9.260, e = 0.238
  Demo 2: a = 15.744, b = 0.087, c = 2.374, d = 4.640, e = 0.649

-- score: -94.03 (accuracy -100.23, token simplicity 3.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
diff.y += params.f * data.y
  Demo 0: a = 21.304, b = 0.058, c = 2.067, d = 16.290, e = 0.794, f = 0.052
  Demo 1: a = 21.929, b = 0.025, c = 1.956, d = 9.003, e = 0.238, f = -0.027
  Demo 2: a = 15.744, b = 0.087, c = 2.374, d = 5.041, e = 0.649, f = 0.065

## Round 1 | 0.17s | best score: -183.84

+246 new programs (246 actually scored)
* linear_fit: +0
* quadratic_fit: +7
* add_single_terms: +31
* delete_interactions: +130
* delete_lines: +65
* delete_near_zeros: +12
* relate_parameters: +1
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -183.84 (accuracy -188.64, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.695

-- score: -182.98 (accuracy -188.68, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.100, e = 0.695

-- score: -182.95 (accuracy -188.65, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.024, d = 0.076, e = 1.533
  Demo 1: a = 0.606, b = 0.050, c = 0.043, d = 0.020, e = 0.805
  Demo 2: a = 2.082, b = 0.309, c = 0.098, d = 0.100, e = 0.705

-- score: -182.17 (accuracy -188.97, token simplicity 3.80, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 2.782, b = 1.234, c = 0.112, d = 0.259, e = 0.076, f = 1.534
  Demo 1: a = 0.677, b = 0.620, c = 0.050, d = 0.012, e = 0.020, f = 0.802
  Demo 2: a = 0.088, b = 2.087, c = 0.308, d = -0.007, e = 0.100, f = 0.695

-- score: -182.09 (accuracy -188.69, token simplicity 3.60, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = -0.024, e = 0.076, f = 1.533
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = 0.043, e = 0.020, f = 0.805
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.098, e = 0.100, f = 0.705

-- score: -181.92 (accuracy -188.72, token simplicity 3.80, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 1.120, b = 0.103, c = 0.053, d = -0.024, e = 0.076, f = 1.533
  Demo 1: a = 0.605, b = 0.049, c = -0.033, d = 0.043, e = 0.020, f = 0.805
  Demo 2: a = 2.080, b = 0.307, c = -0.017, d = 0.098, e = 0.100, f = 0.705

-- score: -181.28 (accuracy -188.98, token simplicity 4.20, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 2.782, b = 1.234, c = 0.112, d = 0.259, e = -0.024, f = 0.076, g = 1.533
  Demo 1: a = 0.677, b = 0.620, c = 0.050, d = 0.012, e = 0.043, f = 0.020, g = 0.805
  Demo 2: a = 0.088, b = 2.087, c = 0.308, d = -0.007, e = 0.098, f = 0.100, g = 0.705

-- score: -181.19 (accuracy -188.69, token simplicity 4.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.y
diff.y += params.e
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 1.603, b = 1.438, c = 1.124, d = 0.101, e = -0.024, f = 0.076, g = 1.533
  Demo 1: a = 0.616, b = 0.073, c = 0.617, d = 0.050, e = 0.043, f = 0.020, g = 0.805
  Demo 2: a = 0.108, b = -0.027, c = 2.091, d = 0.309, e = 0.098, f = 0.100, g = 0.705

-- score: -181.10 (accuracy -189.00, token simplicity 4.40, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 2.782, b = 1.234, c = 0.112, d = 0.259, e = -0.006, f = 0.076, g = 1.536
  Demo 1: a = 0.677, b = 0.620, c = 0.050, d = 0.012, e = 0.003, f = 0.020, g = 0.802
  Demo 2: a = 0.088, b = 2.087, c = 0.308, d = -0.007, e = 0.004, f = 0.100, g = 0.695

-- score: -181.09 (accuracy -188.79, token simplicity 4.20, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = 0.647, e = -0.032, f = 0.079, g = 1.584
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = -0.417, e = 0.012, f = 0.019, g = 0.774
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.164, e = -0.008, f = 0.101, g = 0.713

## Round 2 | 0.08s | best score: -183.84 (stable)

+158 new programs (158 actually scored)
* linear_fit: +5
* quadratic_fit: +5
* add_single_terms: +34
* delete_interactions: +84
* delete_lines: +28
* delete_near_zeros: +2
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -183.84 (accuracy -188.64, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.695

-- score: -182.98 (accuracy -188.68, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.100, e = 0.695

-- score: -182.95 (accuracy -188.65, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.024, d = 0.076, e = 1.533
  Demo 1: a = 0.606, b = 0.050, c = 0.043, d = 0.020, e = 0.805
  Demo 2: a = 2.082, b = 0.309, c = 0.098, d = 0.100, e = 0.705

-- score: -182.81 (accuracy -188.71, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.120, b = 0.103, c = 0.053, d = 0.076, e = 1.534
  Demo 1: a = 0.605, b = 0.049, c = -0.033, d = 0.020, e = 0.802
  Demo 2: a = 2.080, b = 0.307, c = -0.017, d = 0.100, e = 0.695

-- score: -182.77 (accuracy -188.67, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.006, d = 0.076, e = 1.536
  Demo 1: a = 0.606, b = 0.050, c = 0.003, d = 0.020, e = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.004, d = 0.100, e = 0.695

-- score: -182.68 (accuracy -188.78, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.137, b = 0.105, c = 0.004, d = 0.076, e = 1.534
  Demo 1: a = 0.599, b = 0.049, c = -0.002, d = 0.020, e = 0.802
  Demo 2: a = 2.075, b = 0.307, c = -0.002, d = 0.100, e = 0.695

-- score: -182.62 (accuracy -188.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.103, b = 0.000, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.577, b = 0.000, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 2.062, b = 0.001, c = 0.309, d = 0.100, e = 0.695

-- score: -182.62 (accuracy -188.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.000, d = 0.078, e = 1.552
  Demo 1: a = 0.606, b = 0.050, c = 0.000, d = 0.020, e = 0.795
  Demo 2: a = 2.082, b = 0.309, c = 0.000, d = 0.100, e = 0.693

-- score: -182.60 (accuracy -188.70, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.577, e = 0.002
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.805, e = 0.000
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.652, e = -0.004

-- score: -182.17 (accuracy -188.97, token simplicity 3.80, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 2.782, b = 1.234, c = 0.112, d = 0.259, e = 0.076, f = 1.534
  Demo 1: a = 0.677, b = 0.620, c = 0.050, d = 0.012, e = 0.020, f = 0.802
  Demo 2: a = 0.088, b = 2.087, c = 0.308, d = -0.007, e = 0.100, f = 0.695

## Round 3 | 0.06s | best score: -183.84 (stable)

+121 new programs (121 actually scored)
* linear_fit: +12
* quadratic_fit: +5
* add_single_terms: +14
* delete_interactions: +67
* delete_lines: +23
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -183.84 (accuracy -188.64, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.695

-- score: -182.98 (accuracy -188.68, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.100, e = 0.695

-- score: -182.95 (accuracy -188.65, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.024, d = 0.076, e = 1.533
  Demo 1: a = 0.606, b = 0.050, c = 0.043, d = 0.020, e = 0.805
  Demo 2: a = 2.082, b = 0.309, c = 0.098, d = 0.100, e = 0.705

-- score: -182.81 (accuracy -188.71, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.120, b = 0.103, c = 0.053, d = 0.076, e = 1.534
  Demo 1: a = 0.605, b = 0.049, c = -0.033, d = 0.020, e = 0.802
  Demo 2: a = 2.080, b = 0.307, c = -0.017, d = 0.100, e = 0.695

-- score: -182.77 (accuracy -188.67, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.006, d = 0.076, e = 1.536
  Demo 1: a = 0.606, b = 0.050, c = 0.003, d = 0.020, e = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.004, d = 0.100, e = 0.695

-- score: -182.74 (accuracy -188.64, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.557, e = 0.022
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.804, e = 0.001
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.672, e = -0.023

-- score: -182.68 (accuracy -188.78, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.137, b = 0.105, c = 0.004, d = 0.076, e = 1.534
  Demo 1: a = 0.599, b = 0.049, c = -0.002, d = 0.020, e = 0.802
  Demo 2: a = 2.075, b = 0.307, c = -0.002, d = 0.100, e = 0.695

-- score: -182.62 (accuracy -188.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.103, b = 0.000, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.577, b = 0.000, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 2.062, b = 0.001, c = 0.309, d = 0.100, e = 0.695

-- score: -182.62 (accuracy -188.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.000, d = 0.078, e = 1.552
  Demo 1: a = 0.606, b = 0.050, c = 0.000, d = 0.020, e = 0.795
  Demo 2: a = 2.082, b = 0.309, c = 0.000, d = 0.100, e = 0.693

-- score: -182.60 (accuracy -188.70, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.577, e = 0.002
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.805, e = 0.000
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.652, e = -0.004

## Round 4 | 0.02s | best score: -183.84 (stable)

+30 new programs (30 actually scored)
* linear_fit: +5
* quadratic_fit: +4
* add_single_terms: +6
* delete_interactions: +11
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -183.84 (accuracy -188.64, token simplicity 2.80, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.695

-- score: -183.44 (accuracy -188.64, token simplicity 3.20, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
diff.y += params.d * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = -0.534
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.198
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.305

-- score: -182.98 (accuracy -188.68, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.165, b = 1.124, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.544, b = 0.617, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 0.136, b = 2.091, c = 0.309, d = 0.100, e = 0.695

-- score: -182.95 (accuracy -188.65, token simplicity 3.20, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.024, d = 0.076, e = 1.533
  Demo 1: a = 0.606, b = 0.050, c = 0.043, d = 0.020, e = 0.805
  Demo 2: a = 2.082, b = 0.309, c = 0.098, d = 0.100, e = 0.705

-- score: -182.81 (accuracy -188.71, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.120, b = 0.103, c = 0.053, d = 0.076, e = 1.534
  Demo 1: a = 0.605, b = 0.049, c = -0.033, d = 0.020, e = 0.802
  Demo 2: a = 2.080, b = 0.307, c = -0.017, d = 0.100, e = 0.695

-- score: -182.77 (accuracy -188.67, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.006, d = 0.076, e = 1.536
  Demo 1: a = 0.606, b = 0.050, c = 0.003, d = 0.020, e = 0.802
  Demo 2: a = 2.082, b = 0.309, c = 0.004, d = 0.100, e = 0.695

-- score: -182.74 (accuracy -188.64, token simplicity 3.40, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = 0.076, d = 1.557, e = 0.022
  Demo 1: a = 0.606, b = 0.050, c = 0.020, d = 0.804, e = 0.001
  Demo 2: a = 2.082, b = 0.309, c = 0.100, d = 0.672, e = -0.023

-- score: -182.68 (accuracy -188.78, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.137, b = 0.105, c = 0.004, d = 0.076, e = 1.534
  Demo 1: a = 0.599, b = 0.049, c = -0.002, d = 0.020, e = 0.802
  Demo 2: a = 2.075, b = 0.307, c = -0.002, d = 0.100, e = 0.695

-- score: -182.62 (accuracy -188.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.103, b = 0.000, c = 0.101, d = 0.076, e = 1.534
  Demo 1: a = 0.577, b = 0.000, c = 0.050, d = 0.020, e = 0.802
  Demo 2: a = 2.062, b = 0.001, c = 0.309, d = 0.100, e = 0.695

-- score: -182.62 (accuracy -188.72, token simplicity 3.60, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 1.117, b = 0.101, c = -0.000, d = 0.078, e = 1.552
  Demo 1: a = 0.606, b = 0.050, c = 0.000, d = 0.020, e = 0.795
  Demo 2: a = 2.082, b = 0.309, c = 0.000, d = 0.100, e = 0.693

