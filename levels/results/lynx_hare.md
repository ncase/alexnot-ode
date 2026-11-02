# lynx_hare

Solved in 1.41 seconds. 1201 programs considered, over 9 rounds.

## Winner

-- score: -186.63 (accuracy -195.53, token simplicity 6.40, parameter simplicity 2.50) --
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

## Runner-ups

-- score: -186.63 (accuracy -195.53, token simplicity 6.40, parameter simplicity 2.50) --
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

-- score: -186.43 (accuracy -195.63, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.43 (accuracy -195.63, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.e * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += (params.a / params.b)
diff.y -= params.b * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 3.513, b = 0.309, c = 1.500, d = 0.010, e = 0.046, f = 0.042

-- score: -186.41 (accuracy -195.61, token simplicity 6.20, parameter simplicity 3.00) --
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

# The Search

## Round 0 | 0.00s | best score: -92.66

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -92.66 (accuracy -99.66, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 16.151, b = 0.479, c = 0.002, d = 0.041, e = 1.754, f = 0.005

-- score: -89.63 (accuracy -96.63, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009

-- score: -45.26 (accuracy -48.36, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
  Demo 0: a = 16.896, b = 0.082, c = 0.958

-- score: -36.79 (accuracy -39.89, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 16.983, b = 0.556, c = 0.093

-- score: -20.75 (accuracy -22.05, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.y * data.y
  Demo 0: a = 0.010

## Round 1 | 0.03s | best score: -182.29

+92 new programs (92 actually scored)
* add_terms: +55
* delete_lines: +18
* relate_parameters: +17
* snap_to_one: +1
* tie_parameters: +1

### 5 parents for the next round

-- score: -182.29 (accuracy -196.29, token simplicity 8.00, parameter simplicity 6.00) --
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

-- score: -137.92 (accuracy -148.02, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -126.42 (accuracy -136.52, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -113.41 (accuracy -121.71, token simplicity 4.80, parameter simplicity 3.50) --
diff.x -= params.a * data.y * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 0.010, b = 16.151, c = 0.479, d = 0.002, e = 0.041, f = 1.754, g = 0.005

-- score: -104.33 (accuracy -112.63, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x * data.x
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 0.003

## Round 2 | 0.20s | best score: -184.25

+256 new programs (256 actually scored)
* add_terms: +21
* delete_lines: +42
* relate_parameters: +187
* snap_to_one: +1
* tie_parameters: +5

### 5 parents for the next round

-- score: -184.25 (accuracy -195.65, token simplicity 6.40, parameter simplicity 5.00) --
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

-- score: -183.37 (accuracy -196.27, token simplicity 7.40, parameter simplicity 5.50) --
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

-- score: -183.09 (accuracy -196.19, token simplicity 7.60, parameter simplicity 5.50) --
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

-- score: -183.07 (accuracy -195.77, token simplicity 7.20, parameter simplicity 5.50) --
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

-- score: -183.01 (accuracy -195.71, token simplicity 7.20, parameter simplicity 5.50) --
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

## Round 3 | 0.29s | best score: -185.34

+321 new programs (321 actually scored)
* add_terms: +0
* delete_lines: +47
* relate_parameters: +265
* snap_to_one: +0
* tie_parameters: +9

### 5 parents for the next round

-- score: -185.34 (accuracy -195.64, token simplicity 5.80, parameter simplicity 4.50) --
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

-- score: -185.05 (accuracy -195.55, token simplicity 6.00, parameter simplicity 4.50) --
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

-- score: -184.84 (accuracy -195.14, token simplicity 5.80, parameter simplicity 4.50) --
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

-- score: -184.74 (accuracy -195.64, token simplicity 6.40, parameter simplicity 4.50) --
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

-- score: -184.55 (accuracy -195.65, token simplicity 6.60, parameter simplicity 4.50) --
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

## Round 4 | 0.17s | best score: -185.84

+210 new programs (210 actually scored)
* add_terms: +2
* delete_lines: +42
* relate_parameters: +158
* snap_to_one: +0
* tie_parameters: +8

### 5 parents for the next round

-- score: -185.84 (accuracy -195.64, token simplicity 5.80, parameter simplicity 4.00) --
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

-- score: -185.66 (accuracy -194.86, token simplicity 5.20, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 6.635, b = 0.013, c = 0.047, d = 0.011, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -185.64 (accuracy -195.64, token simplicity 6.00, parameter simplicity 4.00) --
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

-- score: -185.63 (accuracy -195.63, token simplicity 6.00, parameter simplicity 4.00) --
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

-- score: -185.63 (accuracy -195.63, token simplicity 6.00, parameter simplicity 4.00) --
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

## Round 5 | 0.14s | best score: -186.14

+133 new programs (133 actually scored)
* add_terms: +13
* delete_lines: +39
* relate_parameters: +76
* snap_to_one: +0
* tie_parameters: +5

### 5 parents for the next round

-- score: -186.14 (accuracy -195.64, token simplicity 6.00, parameter simplicity 3.50) --
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

-- score: -186.13 (accuracy -195.63, token simplicity 6.00, parameter simplicity 3.50) --
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

-- score: -186.12 (accuracy -195.62, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += (params.a / params.b)
diff.x += params.a * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 0.181, b = 0.047, c = 0.010, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -186.12 (accuracy -195.62, token simplicity 6.00, parameter simplicity 3.50) --
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

-- score: -186.11 (accuracy -195.61, token simplicity 6.00, parameter simplicity 3.50) --
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

## Round 6 | 0.30s | best score: -186.43

+99 new programs (99 actually scored)
* add_terms: +17
* delete_lines: +40
* relate_parameters: +39
* snap_to_one: +0
* tie_parameters: +3

### 5 parents for the next round

-- score: -186.43 (accuracy -195.63, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.41 (accuracy -195.61, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.41 (accuracy -195.61, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.40 (accuracy -195.60, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.35 (accuracy -195.55, token simplicity 6.20, parameter simplicity 3.00) --
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

## Round 7 | 0.24s | best score: -186.63

+71 new programs (71 actually scored)
* add_terms: +20
* delete_lines: +38
* relate_parameters: +12
* snap_to_one: +0
* tie_parameters: +1

### 5 parents for the next round

-- score: -186.63 (accuracy -195.53, token simplicity 6.40, parameter simplicity 2.50) --
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

-- score: -186.43 (accuracy -195.63, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.41 (accuracy -195.61, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.41 (accuracy -195.61, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.40 (accuracy -195.30, token simplicity 6.40, parameter simplicity 2.50) --
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

## Round 8 | 0.04s | best score: -186.63

+25 new programs (25 actually scored)
* add_terms: +8
* delete_lines: +15
* relate_parameters: +2
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -186.63 (accuracy -195.53, token simplicity 6.40, parameter simplicity 2.50) --
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

-- score: -186.43 (accuracy -195.63, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.41 (accuracy -195.61, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.41 (accuracy -195.61, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -186.40 (accuracy -195.30, token simplicity 6.40, parameter simplicity 2.50) --
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

