# lynx_hare

Solved in 1.24 seconds. 1189 programs considered, over 9 rounds.

## Winner

-- score: -121.30 (accuracy -130.20, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 4.044, b = 0.193, c = 0.010, d = 12.212, e = 1.525

## Runner-ups

-- score: -121.30 (accuracy -130.20, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 4.044, b = 0.048, c = 0.010, d = 12.212, e = 1.525

-- score: -121.28 (accuracy -129.88, token simplicity 5.60, parameter simplicity 3.00) --
diff.x += (params.a / params.b)
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.a * data.x
diff.y += (params.c / params.a) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.306, b = 0.048, c = 0.013, d = 0.011, e = 11.275, f = 1.494

-- score: -121.28 (accuracy -129.88, token simplicity 5.60, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= (params.c / params.a) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.c * data.x
diff.y += (params.b / params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 6.446, b = 0.013, c = 0.306, d = 0.011, e = 11.275, f = 1.494

-- score: -121.28 (accuracy -129.88, token simplicity 5.60, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 6.446, b = 0.306, c = 0.042, d = 0.011, e = 11.275, f = 1.494

# The Search

## Round 0 | 0.00s | best score: -59.44

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -59.44 (accuracy -66.44, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 16.151, b = 0.479, c = 0.002, d = 0.041, e = 1.754, f = 0.005

-- score: -57.42 (accuracy -64.42, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009

-- score: -29.14 (accuracy -32.24, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
  Demo 0: a = 16.896, b = 0.082, c = 0.958

-- score: -23.50 (accuracy -26.60, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 16.983, b = 0.556, c = 0.093

-- score: -13.40 (accuracy -14.70, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.y * data.y
  Demo 0: a = 0.010

## Round 1 | 0.03s | best score: -116.86

+92 new programs (92 actually scored)
* add_terms: +55
* delete_lines: +18
* relate_parameters: +17
* snap_to_one: +1
* tie_parameters: +1

### 5 parents for the next round

-- score: -116.86 (accuracy -130.86, token simplicity 8.00, parameter simplicity 6.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.h * data.x
diff.y += params.i * data.x * data.x
diff.y += params.j * data.x * data.y
diff.y -= params.k * data.y
diff.y += params.l * data.y * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 16.151, h = 0.479, i = 0.002, j = 0.041, k = 1.754, l = 0.005

-- score: -88.58 (accuracy -98.68, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
diff.y += params.i * data.y * data.y
  Demo 0: a = 16.896, b = 0.082, c = 0.958, d = 16.151, e = 0.479, f = 0.002, g = 0.041, h = 1.754, i = 0.005

-- score: -80.92 (accuracy -91.02, token simplicity 5.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y -= params.g
diff.y += params.h * data.x
diff.y -= params.i * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 16.983, h = 0.556, i = 0.093

-- score: -72.84 (accuracy -81.14, token simplicity 4.80, parameter simplicity 3.50) --
diff.x -= params.a * data.y * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 0.010, b = 16.151, c = 0.479, d = 0.002, e = 0.041, f = 1.754, g = 0.005

-- score: -66.79 (accuracy -75.09, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x * data.x
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 0.003

## Round 2 | 0.20s | best score: -119.04

+256 new programs (256 actually scored)
* add_terms: +21
* delete_lines: +42
* relate_parameters: +187
* snap_to_one: +1
* tie_parameters: +5

### 5 parents for the next round

-- score: -119.04 (accuracy -130.44, token simplicity 6.40, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.h * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 11.505, h = 0.313, i = 0.042, j = 1.505

-- score: -117.95 (accuracy -130.85, token simplicity 7.40, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 3.596, b = 0.198, c = 0.010, d = 0.047, e = 0.010, f = 16.151, g = 0.479, h = 0.002, i = 0.041, j = 1.754, k = 0.005

-- score: -117.82 (accuracy -130.52, token simplicity 7.20, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.h * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 12.208, h = 0.312, i = 0.042, j = 1.588, k = 0.001

-- score: -117.77 (accuracy -130.47, token simplicity 7.20, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.h * data.x
diff.y += params.i * data.x * data.x
diff.y += params.j * data.x * data.y
diff.y -= params.k * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 12.016, h = 0.350, i = 0.000, j = 0.042, k = 1.501

-- score: -117.69 (accuracy -130.79, token simplicity 7.60, parameter simplicity 5.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 0.319, b = 0.009, c = 0.047, d = 0.189, e = 0.007, f = 16.151, g = 0.479, h = 0.002, i = 0.041, j = 1.754, k = 0.005

## Round 3 | 0.29s | best score: -120.12

+321 new programs (321 actually scored)
* add_terms: +0
* delete_lines: +47
* relate_parameters: +265
* snap_to_one: +0
* tie_parameters: +9

### 5 parents for the next round

-- score: -120.12 (accuracy -130.42, token simplicity 5.80, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 3.596, b = 0.198, c = 0.010, d = 0.047, e = 0.010, f = 11.505, g = 0.313, h = 0.042, i = 1.505

-- score: -119.87 (accuracy -130.37, token simplicity 6.00, parameter simplicity 4.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 0.319, b = 0.009, c = 0.047, d = 0.189, e = 0.007, f = 11.505, g = 0.313, h = 0.042, i = 1.505

-- score: -119.79 (accuracy -130.09, token simplicity 5.80, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x -= params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 8.161, b = 0.013, c = 0.047, d = 0.172, e = 0.013, f = 11.505, g = 0.313, h = 0.042, i = 1.505

-- score: -119.53 (accuracy -130.43, token simplicity 6.40, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.c * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 3.135, b = 0.217, c = 0.010, d = 0.047, e = 0.018, f = 11.505, g = 0.313, h = 0.042, i = 1.505

-- score: -119.51 (accuracy -129.61, token simplicity 5.60, parameter simplicity 4.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 5.212, b = 0.472, c = 0.007, d = 0.045, e = 0.540, f = 11.505, g = 0.313, h = 0.042, i = 1.505

## Round 4 | 0.16s | best score: -120.71

+216 new programs (216 actually scored)
* add_terms: +2
* delete_lines: +41
* relate_parameters: +165
* snap_to_one: +0
* tie_parameters: +8

### 5 parents for the next round

-- score: -120.71 (accuracy -129.91, token simplicity 5.20, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 6.635, b = 0.013, c = 0.047, d = 0.011, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -120.62 (accuracy -130.42, token simplicity 5.80, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.627, b = 0.196, c = 0.010, d = 0.047, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -120.42 (accuracy -130.42, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.e * data.x * data.y
diff.x += params.f * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 11.502, b = 0.313, c = 0.198, d = 0.010, e = 0.047, f = 0.010, g = 0.042, h = 1.505

-- score: -120.42 (accuracy -130.42, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= (params.g / params.b) * data.y
  Demo 0: a = 3.445, b = 0.208, c = 0.010, d = 0.047, e = 0.010, f = 11.486, g = 0.313, h = 0.042

-- score: -120.42 (accuracy -130.42, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.355, b = 0.010, c = 0.047, d = 0.010, e = 11.505, f = 0.313, g = 0.042, h = 1.505

## Round 5 | 0.14s | best score: -121.00

+133 new programs (133 actually scored)
* add_terms: +13
* delete_lines: +39
* relate_parameters: +76
* snap_to_one: +0
* tie_parameters: +5

### 5 parents for the next round

-- score: -121.00 (accuracy -129.90, token simplicity 5.40, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= (params.c / params.a) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.c * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 6.631, b = 0.013, c = 0.314, d = 0.011, e = 11.520, f = 0.042, g = 1.506

-- score: -121.00 (accuracy -129.90, token simplicity 5.40, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += (params.b / params.f) * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 6.619, b = 0.013, c = 0.047, d = 0.011, e = 11.237, f = 0.305, g = 1.494

-- score: -120.92 (accuracy -130.42, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.a / params.e) * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.613, b = 0.197, c = 0.010, d = 0.047, e = 11.519, f = 0.042, g = 1.506

-- score: -120.92 (accuracy -130.42, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.e * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.f
diff.y -= params.b * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.480, b = 0.311, c = 1.503, d = 0.010, e = 0.046, f = 11.447, g = 0.042

-- score: -120.92 (accuracy -130.42, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.851, b = 0.181, c = 0.010, d = 11.505, e = 0.313, f = 0.042, g = 1.505

## Round 6 | 0.14s | best score: -121.28

+100 new programs (100 actually scored)
* add_terms: +22
* delete_lines: +38
* relate_parameters: +37
* snap_to_one: +0
* tie_parameters: +3

### 5 parents for the next round

-- score: -121.28 (accuracy -129.88, token simplicity 5.60, parameter simplicity 3.00) --
diff.x += (params.a / params.b)
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.a * data.x
diff.y += (params.c / params.a) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.306, b = 0.048, c = 0.013, d = 0.011, e = 11.275, f = 1.494

-- score: -121.22 (accuracy -130.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += (params.a / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.e * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.b
diff.y -= params.a * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.309, b = 11.367, c = 1.500, d = 0.010, e = 0.046, f = 0.042

-- score: -121.21 (accuracy -130.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.b) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.213, c = 0.010, d = 11.288, e = 0.042, f = 1.496

-- score: -121.20 (accuracy -130.40, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.817, b = 0.180, c = 0.010, d = 11.831, e = 0.042, f = 1.519

-- score: -121.17 (accuracy -130.37, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.a / params.e) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.976, b = 0.171, c = 0.011, d = 0.048, e = 12.074, f = 1.528

## Round 7 | 0.26s | best score: -121.30

+71 new programs (71 actually scored)
* add_terms: +22
* delete_lines: +38
* relate_parameters: +9
* snap_to_one: +0
* tie_parameters: +2

### 5 parents for the next round

-- score: -121.30 (accuracy -130.20, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 4.044, b = 0.193, c = 0.010, d = 12.212, e = 1.525

-- score: -121.28 (accuracy -129.88, token simplicity 5.60, parameter simplicity 3.00) --
diff.x += (params.a / params.b)
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.a * data.x
diff.y += (params.c / params.a) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.306, b = 0.048, c = 0.013, d = 0.011, e = 11.275, f = 1.494

-- score: -121.22 (accuracy -130.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += (params.a / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.e * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.b
diff.y -= params.a * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.309, b = 11.367, c = 1.500, d = 0.010, e = 0.046, f = 0.042

-- score: -121.21 (accuracy -130.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.b) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.213, c = 0.010, d = 11.288, e = 0.042, f = 1.496

-- score: -121.20 (accuracy -130.40, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.817, b = 0.180, c = 0.010, d = 11.831, e = 0.042, f = 1.519

## Round 8 | 0.02s | best score: -121.30

+11 new programs (11 actually scored)
* add_terms: +4
* delete_lines: +7
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -121.30 (accuracy -130.20, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 4.044, b = 0.193, c = 0.010, d = 12.212, e = 1.525

-- score: -121.28 (accuracy -129.88, token simplicity 5.60, parameter simplicity 3.00) --
diff.x += (params.a / params.b)
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.a * data.x
diff.y += (params.c / params.a) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.306, b = 0.048, c = 0.013, d = 0.011, e = 11.275, f = 1.494

-- score: -121.22 (accuracy -130.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += (params.a / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.e * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.b
diff.y -= params.a * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.309, b = 11.367, c = 1.500, d = 0.010, e = 0.046, f = 0.042

-- score: -121.21 (accuracy -130.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.b) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.213, c = 0.010, d = 11.288, e = 0.042, f = 1.496

-- score: -121.20 (accuracy -130.40, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.817, b = 0.180, c = 0.010, d = 11.831, e = 0.042, f = 1.519

