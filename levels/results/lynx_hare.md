# lynx_hare

Solved in 5.11 seconds. 3946 programs considered, over 9 rounds.

## Winner

-- score: -121.46 (accuracy -130.36, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= (params.d / params.c) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.b / params.c) * data.y
  Demo 0: a = 11.600, b = 0.319, c = 0.212, d = 0.010, e = 0.042

## Runner-ups

-- score: -121.46 (accuracy -130.36, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.b) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.d / params.b) * data.y
  Demo 0: a = 3.704, b = 0.212, c = 0.010, d = 0.319, e = 0.042

-- score: -121.34 (accuracy -130.24, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += (params.a / params.c)
diff.y -= params.c * data.x
diff.y += (params.a * params.d) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.786, b = 0.048, c = 0.321, d = 0.011, e = 1.519

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

-- score: -121.30 (accuracy -130.20, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 4.044, b = 0.193, c = 0.010, d = 0.331, e = 1.525

# The Search

## Round 0 | 0.00s | best score: -59.44

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

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

-- score: -9.37 (accuracy -10.67, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.x
  Demo 0: a = 0.003

-- score: -6.24 (accuracy -7.34, token simplicity 0.60, parameter simplicity 0.50) --
diff.x -= params.a * data.y
  Demo 0: a = 0.328

-- score: -5.82 (accuracy -7.12, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.x * data.y
  Demo 0: a = 0.008

-- score: -3.57 (accuracy -4.67, token simplicity 0.60, parameter simplicity 0.50) --
diff.y += params.a * data.x
  Demo 0: a = 0.140

-- score: -3.36 (accuracy -4.66, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.y
  Demo 0: a = 0.005

## Round 1 | 0.05s | best score: -116.86

+179 new programs (179 actually scored)
* add_terms: +120
* delete_lines: +16
* delete_near_zeros: +2
* relate_parameters: +38
* snap_to_one: +1
* tie_parameters: +2

### 10 parents for the next round

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

-- score: -65.68 (accuracy -73.78, token simplicity 4.60, parameter simplicity 3.50) --
diff.x -= params.a * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 0.328, b = 16.151, c = 0.479, d = 0.002, e = 0.041, f = 1.754, g = 0.005

-- score: -65.26 (accuracy -73.56, token simplicity 4.80, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 0.008, b = 16.151, c = 0.479, d = 0.002, e = 0.041, f = 1.754, g = 0.005

-- score: -61.62 (accuracy -66.02, token simplicity 2.40, parameter simplicity 2.00) --
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 11.505, b = 0.313, c = 0.042, d = 1.505

-- score: -60.99 (accuracy -69.09, token simplicity 4.60, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 0.140

-- score: -60.78 (accuracy -69.08, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 0.005

## Round 2 | 0.52s | best score: -119.04

+658 new programs (658 actually scored)
* add_terms: +48
* delete_lines: +67
* delete_near_zeros: +10
* relate_parameters: +517
* snap_to_one: +1
* tie_parameters: +15

### 10 parents for the next round

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

-- score: -117.61 (accuracy -130.51, token simplicity 7.40, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x -= params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 8.161, b = 0.013, c = 0.047, d = 0.172, e = 0.013, f = 16.151, g = 0.479, h = 0.002, i = 0.041, j = 1.754, k = 0.005

-- score: -117.36 (accuracy -130.86, token simplicity 8.00, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 2.830, b = 0.221, c = 0.010, d = 0.047, e = 0.009, f = 16.151, g = 0.479, h = 0.002, i = 0.041, j = 1.754, k = 0.005

-- score: -117.36 (accuracy -130.86, token simplicity 8.00, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.h * data.x
diff.y += params.i * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 2.929, b = 0.218, c = 0.010, d = 0.047, e = 0.041, f = 0.010, g = 16.151, h = 0.479, i = 0.002, j = 1.754, k = 0.005

-- score: -117.35 (accuracy -130.85, token simplicity 8.00, parameter simplicity 5.50) --
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
diff.y -= params.a * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 1.756, b = 0.257, c = 0.009, d = 0.047, e = 0.102, f = 0.008, g = 16.178, h = 0.480, i = 0.002, j = 0.041, k = 0.005

-- score: -117.35 (accuracy -130.85, token simplicity 8.00, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.c * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.x
diff.y += params.i * data.x * data.y
diff.y -= params.j * data.y
diff.y += params.k * data.y * data.y
  Demo 0: a = 3.135, b = 0.217, c = 0.010, d = 0.047, e = 0.018, f = 16.151, g = 0.479, h = 0.002, i = 0.041, j = 1.754, k = 0.005

## Round 3 | 1.39s | best score: -120.12

+1242 new programs (1242 actually scored)
* add_terms: +1
* delete_lines: +97
* delete_near_zeros: +9
* relate_parameters: +1116
* snap_to_one: +0
* tie_parameters: +19

### 10 parents for the next round

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
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 2.830, b = 0.221, c = 0.010, d = 0.047, e = 0.009, f = 11.505, g = 0.313, h = 0.042, i = 1.505

-- score: -119.53 (accuracy -130.43, token simplicity 6.40, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.h * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 2.911, b = 0.218, c = 0.010, d = 0.047, e = 0.042, f = 0.010, g = 11.505, h = 0.313, i = 1.505

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

-- score: -119.49 (accuracy -130.39, token simplicity 6.40, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g
diff.y -= params.b * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 0.644, b = 0.308, c = 0.009, d = 0.047, e = 0.142, f = 0.008, g = 11.332, h = 0.042, i = 1.498

-- score: -119.34 (accuracy -130.44, token simplicity 6.60, parameter simplicity 4.50) --
diff.x += (params.a * params.b)
diff.x += params.a * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.b
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
  Demo 0: a = 0.227, b = 11.504, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 0.313, h = 0.042, i = 1.505

-- score: -119.34 (accuracy -130.44, token simplicity 6.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += (params.e * params.f) * data.y
diff.x += params.g * data.y * data.y
diff.y += params.h
diff.y -= params.i * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 2.565, b = 0.229, c = 0.010, d = 0.047, e = 0.042, f = 1.505, g = 0.009, h = 11.504, i = 0.313

## Round 4 | 0.71s | best score: -120.71

+795 new programs (795 actually scored)
* add_terms: +4
* delete_lines: +82
* delete_near_zeros: +7
* relate_parameters: +681
* snap_to_one: +1
* tie_parameters: +20

### 10 parents for the next round

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

-- score: -120.47 (accuracy -130.27, token simplicity 5.80, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.b * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 2.032, b = 0.300, c = 0.009, d = 0.046, e = 0.010, f = 11.068, g = 0.041, h = 1.487

-- score: -120.42 (accuracy -130.42, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= (params.a / params.f) * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.602, b = 0.198, c = 0.010, d = 0.047, e = 0.010, f = 11.502, g = 0.042, h = 1.505

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
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.b) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.355, b = 0.214, c = 0.010, d = 0.010, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -120.42 (accuracy -130.42, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.868, b = 0.181, c = 0.010, d = 0.010, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -120.42 (accuracy -130.42, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += (params.b * params.d) * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.305, b = 0.217, c = 0.010, d = 0.047, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -120.42 (accuracy -130.42, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.991, b = 0.174, c = 0.010, d = 0.047, e = 0.010, f = 11.484, g = 0.313, h = 1.504

-- score: -120.41 (accuracy -130.41, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += (params.b / params.a) * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 4.053, b = 0.170, c = 0.011, d = 0.047, e = 0.010, f = 11.517, g = 0.314, h = 1.506

## Round 5 | 1.00s | best score: -121.00

+487 new programs (487 actually scored)
* add_terms: +25
* delete_lines: +78
* delete_near_zeros: +17
* relate_parameters: +357
* snap_to_one: +1
* tie_parameters: +9

### 10 parents for the next round

-- score: -121.00 (accuracy -129.90, token simplicity 5.40, parameter simplicity 3.50) --
diff.x += (params.a / params.b)
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.a * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 0.314, b = 0.047, c = 0.013, d = 0.011, e = 11.520, f = 0.042, g = 1.506

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
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= (params.f / params.b) * data.y
  Demo 0: a = 3.480, b = 0.207, c = 0.010, d = 0.046, e = 11.447, f = 0.311, g = 0.042

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

-- score: -120.91 (accuracy -130.41, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.b) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.398, b = 0.214, c = 0.010, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -120.91 (accuracy -130.41, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.961, b = 0.176, c = 0.011, d = 0.047, e = 11.458, f = 0.312, g = 1.503

-- score: -120.90 (accuracy -130.20, token simplicity 5.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.b * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.a * data.y
  Demo 0: a = 1.511, b = 0.317, c = 0.009, d = 0.047, e = 0.010, f = 11.627, g = 0.042

-- score: -120.90 (accuracy -130.40, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 4.038, b = 0.042, c = 0.011, d = 0.047, e = 11.538, f = 0.314, g = 1.507

-- score: -120.88 (accuracy -130.38, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += (params.c / params.b) * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.201, b = 0.229, c = 0.010, d = 0.046, e = 11.565, f = 0.315, g = 1.508

## Round 6 | 0.51s | best score: -121.28

+303 new programs (303 actually scored)
* add_terms: +36
* delete_lines: +69
* delete_near_zeros: +10
* relate_parameters: +177
* snap_to_one: +1
* tie_parameters: +10

### 10 parents for the next round

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

-- score: -121.22 (accuracy -130.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += (params.a / params.e)
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= (params.e / params.b) * data.y
  Demo 0: a = 3.513, b = 0.206, c = 0.010, d = 0.046, e = 0.309, f = 0.042

-- score: -121.21 (accuracy -130.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= (params.d / params.c) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.288, b = 0.307, c = 0.213, d = 0.010, e = 0.042, f = 1.496

-- score: -121.20 (accuracy -130.40, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.817, b = 0.180, c = 0.010, d = 0.323, e = 0.042, f = 1.519

-- score: -121.20 (accuracy -130.40, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.b) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= (params.e / params.b) * data.y
  Demo 0: a = 3.423, b = 0.214, c = 0.010, d = 11.840, e = 0.324, f = 0.042

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

-- score: -121.17 (accuracy -130.37, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.a / params.e) * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.967, b = 0.042, c = 0.011, d = 0.047, e = 12.053, f = 1.529

-- score: -121.17 (accuracy -130.37, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.978, b = 0.188, c = 0.010, d = 11.109, e = 0.301, f = 1.486

-- score: -121.15 (accuracy -130.35, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += (params.a / params.e)
diff.y -= params.e * data.x
diff.y += (params.c / params.b) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.346, b = 0.230, c = 0.010, d = 0.046, e = 0.302, f = 1.489

-- score: -121.10 (accuracy -130.30, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.c * data.x
diff.y += (params.a * params.d) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.787, b = 0.048, c = 0.297, d = 0.011, e = 10.985, f = 1.485

## Round 7 | 0.73s | best score: -121.46

+217 new programs (217 actually scored)
* add_terms: +42
* delete_lines: +75
* delete_near_zeros: +18
* relate_parameters: +72
* snap_to_one: +5
* tie_parameters: +5

### 10 parents for the next round

-- score: -121.46 (accuracy -130.36, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= (params.d / params.c) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.b / params.c) * data.y
  Demo 0: a = 11.600, b = 0.319, c = 0.212, d = 0.010, e = 0.042

-- score: -121.34 (accuracy -130.24, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += (params.a / params.c)
diff.y -= params.c * data.x
diff.y += (params.a * params.d) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.786, b = 0.048, c = 0.321, d = 0.011, e = 1.519

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
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= (params.c / params.a) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.c * data.x
diff.y += (params.b / params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 6.446, b = 0.013, c = 0.306, d = 0.011, e = 11.275, f = 1.494

-- score: -121.27 (accuracy -130.37, token simplicity 6.60, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += (params.b / params.a) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b / params.a) * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.976, b = 0.042, c = 0.047, d = 12.069, e = 1.529

-- score: -121.26 (accuracy -130.36, token simplicity 6.60, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b * params.c) * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.d / params.b) * data.y
  Demo 0: a = 3.704, b = 0.212, c = 0.046, d = 0.319, e = 0.042

-- score: -121.24 (accuracy -130.14, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= (params.e / params.b) * data.y
  Demo 0: a = 3.989, b = 0.186, c = 0.010, d = 10.321, e = 0.274

-- score: -121.23 (accuracy -130.13, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += (params.a * params.b)
diff.x += params.a * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.b
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.d / params.a) * data.y
  Demo 0: a = 0.217, b = 12.287, c = 0.010, d = 0.334, e = 0.043

-- score: -121.22 (accuracy -130.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += (params.a / params.e)
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= (params.e / params.b) * data.y
  Demo 0: a = 3.513, b = 0.206, c = 0.010, d = 0.046, e = 0.309, f = 0.042

-- score: -121.21 (accuracy -130.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= (params.d / params.c) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.288, b = 0.307, c = 0.213, d = 0.010, e = 0.042, f = 1.496

## Round 8 | 0.18s | best score: -121.46 (stable)

+105 new programs (105 actually scored)
* add_terms: +28
* delete_lines: +56
* delete_near_zeros: +10
* relate_parameters: +9
* snap_to_one: +0
* tie_parameters: +2

### 10 parents for the next round

-- score: -121.46 (accuracy -130.36, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= (params.d / params.c) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.b / params.c) * data.y
  Demo 0: a = 11.600, b = 0.319, c = 0.212, d = 0.010, e = 0.042

-- score: -121.34 (accuracy -130.24, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += (params.a / params.c)
diff.y -= params.c * data.x
diff.y += (params.a * params.d) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.786, b = 0.048, c = 0.321, d = 0.011, e = 1.519

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
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= (params.c / params.a) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.c * data.x
diff.y += (params.b / params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 6.446, b = 0.013, c = 0.306, d = 0.011, e = 11.275, f = 1.494

-- score: -121.27 (accuracy -130.37, token simplicity 6.60, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += (params.b / params.a) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b / params.a) * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.976, b = 0.042, c = 0.047, d = 12.069, e = 1.529

-- score: -121.26 (accuracy -130.36, token simplicity 6.60, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b * params.c) * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.d / params.b) * data.y
  Demo 0: a = 3.704, b = 0.212, c = 0.046, d = 0.319, e = 0.042

-- score: -121.24 (accuracy -130.14, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= (params.e / params.b) * data.y
  Demo 0: a = 3.989, b = 0.186, c = 0.010, d = 10.321, e = 0.274

-- score: -121.23 (accuracy -130.13, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += (params.a * params.b)
diff.x += params.a * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.c / params.a) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.b
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.d / params.a) * data.y
  Demo 0: a = 0.217, b = 12.287, c = 0.010, d = 0.334, e = 0.043

-- score: -121.22 (accuracy -130.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += (params.a / params.e)
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= (params.e / params.b) * data.y
  Demo 0: a = 3.513, b = 0.206, c = 0.010, d = 0.046, e = 0.309, f = 0.042

-- score: -121.21 (accuracy -130.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= (params.d / params.c) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.288, b = 0.307, c = 0.213, d = 0.010, e = 0.042, f = 1.496

