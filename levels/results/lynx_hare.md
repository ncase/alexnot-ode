# lynx_hare

Solved in 1.45 seconds. 1171 programs considered, over 9 rounds.

## Winner

-- score: -199.47 (accuracy -208.67, token simplicity 6.20, parameter simplicity 3.00) --
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

## Runner-ups

-- score: -199.47 (accuracy -208.67, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.010, c = 0.046, d = 0.307, e = 0.042, f = 1.496

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += params.d
diff.y -= (params.a / params.d) * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.010, c = 0.046, d = 11.288, e = 0.042, f = 1.496

# The Search

## Round 0 | 0.00s | best score: -99.30

+16 new programs (16 actually scored)
* add_terms: +16
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -99.30 (accuracy -106.30, token simplicity 4.00, parameter simplicity 3.00) --
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
diff.y += params.f * data.y * data.y
  Demo 0: a = 16.151, b = 0.479, c = 0.002, d = 0.041, e = 1.754, f = 0.005

-- score: -96.07 (accuracy -103.07, token simplicity 4.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009

-- score: -48.48 (accuracy -51.58, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
  Demo 0: a = 16.896, b = 0.082, c = 0.958

-- score: -39.45 (accuracy -42.55, token simplicity 1.60, parameter simplicity 1.50) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y -= params.c * data.y
  Demo 0: a = 16.983, b = 0.556, c = 0.093

-- score: -22.22 (accuracy -23.52, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.y * data.y
  Demo 0: a = 0.010

## Round 1 | 0.03s | best score: -195.37

+92 new programs (92 actually scored)
* add_terms: +55
* delete_lines: +18
* relate_parameters: +17
* snap_to_one: +1
* tie_parameters: +1

### 5 parents for the next round

-- score: -195.37 (accuracy -209.37, token simplicity 8.00, parameter simplicity 6.00) --
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

-- score: -147.79 (accuracy -157.89, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -135.53 (accuracy -145.63, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -121.53 (accuracy -129.83, token simplicity 4.80, parameter simplicity 3.50) --
diff.x -= params.a * data.y * data.y
diff.y += params.b
diff.y -= params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
diff.y += params.g * data.y * data.y
  Demo 0: a = 0.010, b = 16.151, c = 0.479, d = 0.002, e = 0.041, f = 1.754, g = 0.005

-- score: -111.84 (accuracy -120.14, token simplicity 4.80, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.y += params.g * data.x * data.x
  Demo 0: a = 2.610, b = 0.227, c = 0.010, d = 0.047, e = 0.060, f = 0.009, g = 0.003

## Round 2 | 0.21s | best score: -197.30

+256 new programs (256 actually scored)
* add_terms: +21
* delete_lines: +42
* relate_parameters: +187
* snap_to_one: +1
* tie_parameters: +5

### 5 parents for the next round

-- score: -197.30 (accuracy -208.70, token simplicity 6.40, parameter simplicity 5.00) --
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

-- score: -196.46 (accuracy -209.36, token simplicity 7.40, parameter simplicity 5.50) --
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

-- score: -196.17 (accuracy -209.27, token simplicity 7.60, parameter simplicity 5.50) --
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

-- score: -196.12 (accuracy -208.82, token simplicity 7.20, parameter simplicity 5.50) --
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

-- score: -196.05 (accuracy -208.75, token simplicity 7.20, parameter simplicity 5.50) --
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

## Round 3 | 0.31s | best score: -198.38

+321 new programs (321 actually scored)
* add_terms: +0
* delete_lines: +47
* relate_parameters: +265
* snap_to_one: +0
* tie_parameters: +9

### 5 parents for the next round

-- score: -198.38 (accuracy -208.68, token simplicity 5.80, parameter simplicity 4.50) --
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

-- score: -198.09 (accuracy -208.59, token simplicity 6.00, parameter simplicity 4.50) --
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

-- score: -197.85 (accuracy -208.15, token simplicity 5.80, parameter simplicity 4.50) --
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

-- score: -197.78 (accuracy -208.68, token simplicity 6.40, parameter simplicity 4.50) --
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

-- score: -197.60 (accuracy -208.70, token simplicity 6.60, parameter simplicity 4.50) --
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

## Round 4 | 0.18s | best score: -198.88

+210 new programs (210 actually scored)
* add_terms: +2
* delete_lines: +42
* relate_parameters: +158
* snap_to_one: +0
* tie_parameters: +8

### 5 parents for the next round

-- score: -198.88 (accuracy -208.68, token simplicity 5.80, parameter simplicity 4.00) --
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

-- score: -198.68 (accuracy -208.68, token simplicity 6.00, parameter simplicity 4.00) --
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

-- score: -198.68 (accuracy -208.68, token simplicity 6.00, parameter simplicity 4.00) --
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

-- score: -198.67 (accuracy -208.67, token simplicity 6.00, parameter simplicity 4.00) --
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

-- score: -198.67 (accuracy -208.67, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += (params.a / params.b)
diff.x += params.a * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 0.181, b = 0.047, c = 0.010, d = 0.010, e = 11.505, f = 0.313, g = 0.042, h = 1.505

## Round 5 | 0.15s | best score: -199.18

+120 new programs (120 actually scored)
* add_terms: +14
* delete_lines: +39
* relate_parameters: +62
* snap_to_one: +0
* tie_parameters: +5

### 5 parents for the next round

-- score: -199.18 (accuracy -208.68, token simplicity 6.00, parameter simplicity 3.50) --
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

-- score: -199.17 (accuracy -208.67, token simplicity 6.00, parameter simplicity 3.50) --
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

-- score: -199.16 (accuracy -208.66, token simplicity 6.00, parameter simplicity 3.50) --
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

-- score: -199.16 (accuracy -208.66, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.398, b = 0.010, c = 0.046, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -199.15 (accuracy -208.65, token simplicity 6.00, parameter simplicity 3.50) --
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

## Round 6 | 0.30s | best score: -199.47

+96 new programs (96 actually scored)
* add_terms: +17
* delete_lines: +39
* relate_parameters: +37
* snap_to_one: +0
* tie_parameters: +3

### 5 parents for the next round

-- score: -199.47 (accuracy -208.67, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.010, c = 0.046, d = 0.307, e = 0.042, f = 1.496

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
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

## Round 7 | 0.26s | best score: -199.47

+72 new programs (72 actually scored)
* add_terms: +20
* delete_lines: +37
* relate_parameters: +13
* snap_to_one: +0
* tie_parameters: +2

### 5 parents for the next round

-- score: -199.47 (accuracy -208.67, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.010, c = 0.046, d = 0.307, e = 0.042, f = 1.496

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.42 (accuracy -208.32, token simplicity 6.40, parameter simplicity 2.50) --
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

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
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

## Round 8 | 0.02s | best score: -199.47

+10 new programs (10 actually scored)
* add_terms: +4
* delete_lines: +6
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -199.47 (accuracy -208.67, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b / params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += (params.a / params.d)
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.466, b = 0.010, c = 0.046, d = 0.307, e = 0.042, f = 1.496

-- score: -199.45 (accuracy -208.65, token simplicity 6.20, parameter simplicity 3.00) --
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

-- score: -199.42 (accuracy -208.32, token simplicity 6.40, parameter simplicity 2.50) --
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

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
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

