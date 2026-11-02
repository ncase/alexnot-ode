# lynx_hare

Solved in 6.39 seconds. 2827 programs considered, over 8 rounds.

## Winner

-- score: -199.44 (accuracy -208.34, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= (params.b * params.d) * data.y
  Demo 0: a = 4.282, b = 0.135, c = 0.011, d = 11.035, e = 0.308

## Runner-ups

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.978, b = 0.047, c = 0.010, d = 11.109, e = 0.301, f = 1.486

-- score: -199.28 (accuracy -208.48, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b * params.d) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.d * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.787, b = 0.160, c = 0.011, d = 0.297, e = 10.985, f = 1.485

-- score: -199.25 (accuracy -208.65, token simplicity 6.40, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += (params.c * params.d) * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += (params.c * params.d) * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.288, b = 0.307, c = 0.213, d = 0.046, e = 0.042, f = 1.496

-- score: -199.25 (accuracy -208.45, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.b * params.f) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.992, b = 0.195, c = 0.010, d = 0.047, e = 10.666, f = 1.470

# The Search

## Round 0 | 0.00s | best score: -196.12

+17 new programs (17 actually scored)
* linear_fit: +2
* quadratic_fit: +3
* add_single_terms: +12
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

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

-- score: -192.96 (accuracy -201.76, token simplicity 4.80, parameter simplicity 4.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 12.122, b = 0.968, c = 0.043, d = 0.481, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -87.94 (accuracy -94.14, token simplicity 3.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
diff.y -= params.f * data.y
  Demo 0: a = 16.896, b = 0.082, c = 0.958, d = 16.983, e = 0.556, f = 0.093

-- score: -87.63 (accuracy -91.63, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.y
diff.y -= params.c
diff.y += params.d * data.x
  Demo 0: a = 19.471, b = 0.946, c = 18.665, d = 0.549

-- score: -37.47 (accuracy -42.57, token simplicity 2.60, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.y -= params.c
diff.y += params.d * data.x
diff.y -= params.e * data.y
  Demo 0: a = 0.432, b = 0.005, c = 16.983, d = 0.556, e = 0.093

-- score: -22.22 (accuracy -23.52, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.y * data.y
  Demo 0: a = 0.010

-- score: -15.77 (accuracy -17.07, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.x
  Demo 0: a = 0.003

-- score: -10.64 (accuracy -11.74, token simplicity 0.60, parameter simplicity 0.50) --
diff.x -= params.a * data.y
  Demo 0: a = 0.328

-- score: -10.09 (accuracy -11.39, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.x * data.y
  Demo 0: a = 0.008

-- score: -6.38 (accuracy -7.48, token simplicity 0.60, parameter simplicity 0.50) --
diff.y += params.a * data.x
  Demo 0: a = 0.140

## Round 1 | 0.14s | best score: -197.30

+388 new programs (388 actually scored)
* linear_fit: +10
* quadratic_fit: +20
* add_single_terms: +77
* delete_interactions: +57
* delete_lines: +33
* delete_near_zeros: +4
* relate_parameters: +176
* snap_to_one: +0
* tie_parameters: +11

### 10 parents for the next round

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

-- score: -197.27 (accuracy -207.37, token simplicity 5.60, parameter simplicity 4.50) --
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

-- score: -197.21 (accuracy -208.81, token simplicity 6.60, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
diff.y += params.j * data.y * data.y
  Demo 0: a = 3.596, b = 0.198, c = 0.010, d = 0.047, e = 0.010, f = 12.208, g = 0.312, h = 0.042, i = 1.588, j = 0.001

-- score: -196.92 (accuracy -208.72, token simplicity 6.80, parameter simplicity 5.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
diff.y += params.j * data.y * data.y
  Demo 0: a = 0.319, b = 0.009, c = 0.047, d = 0.189, e = 0.007, f = 12.208, g = 0.312, h = 0.042, i = 1.588, j = 0.001

-- score: -196.67 (accuracy -208.27, token simplicity 6.60, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x -= params.d * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
diff.y += params.j * data.y * data.y
  Demo 0: a = 8.161, b = 0.013, c = 0.047, d = 0.172, e = 0.013, f = 12.208, g = 0.312, h = 0.042, i = 1.588, j = 0.001

-- score: -196.62 (accuracy -208.82, token simplicity 7.20, parameter simplicity 5.00) --
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
diff.y += params.j * data.y * data.y
  Demo 0: a = 2.830, b = 0.221, c = 0.010, d = 0.047, e = 0.009, f = 12.208, g = 0.312, h = 0.042, i = 1.588, j = 0.001

-- score: -196.62 (accuracy -208.82, token simplicity 7.20, parameter simplicity 5.00) --
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
diff.y += params.j * data.y * data.y
  Demo 0: a = 2.912, b = 0.218, c = 0.010, d = 0.047, e = 0.042, f = 0.010, g = 12.209, h = 0.312, i = 1.588, j = 0.001

-- score: -196.61 (accuracy -208.81, token simplicity 7.20, parameter simplicity 5.00) --
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
diff.y += params.j * data.y * data.y
  Demo 0: a = 3.135, b = 0.217, c = 0.010, d = 0.047, e = 0.018, f = 12.208, g = 0.312, h = 0.042, i = 1.588, j = 0.001

-- score: -196.55 (accuracy -208.75, token simplicity 7.20, parameter simplicity 5.00) --
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
diff.y += params.j * data.y * data.y
  Demo 0: a = 0.668, b = 0.307, c = 0.009, d = 0.047, e = 0.141, f = 0.008, g = 12.042, h = 0.042, i = 1.582, j = 0.002

-- score: -196.42 (accuracy -208.82, token simplicity 7.40, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.c - params.d) * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
diff.y += params.j * data.y * data.y
  Demo 0: a = 2.669, b = 0.226, c = 0.057, d = 0.047, e = 0.009, f = 12.208, g = 0.312, h = 0.042, i = 1.588, j = 0.001

## Round 2 | 0.46s | best score: -198.38

+791 new programs (791 actually scored)
* linear_fit: +1
* quadratic_fit: +6
* add_single_terms: +6
* delete_interactions: +178
* delete_lines: +90
* delete_near_zeros: +8
* relate_parameters: +483
* snap_to_one: +0
* tie_parameters: +19

### 10 parents for the next round

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

-- score: -197.80 (accuracy -208.70, token simplicity 6.40, parameter simplicity 4.50) --
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

-- score: -197.79 (accuracy -208.69, token simplicity 6.40, parameter simplicity 4.50) --
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

-- score: -197.72 (accuracy -208.62, token simplicity 6.40, parameter simplicity 4.50) --
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

-- score: -197.71 (accuracy -208.81, token simplicity 6.60, parameter simplicity 4.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
diff.y += params.i * data.y * data.y
  Demo 0: a = 3.627, b = 0.196, c = 0.010, d = 0.047, e = 12.208, f = 0.312, g = 0.042, h = 1.588, i = 0.001

-- score: -197.69 (accuracy -207.29, token simplicity 5.60, parameter simplicity 4.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.b * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 5.751, b = 0.521, c = 0.006, d = 0.044, e = 11.505, f = 0.313, g = 0.042, h = 1.505

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

## Round 3 | 0.40s | best score: -198.88

+622 new programs (622 actually scored)
* linear_fit: +1
* quadratic_fit: +2
* add_single_terms: +12
* delete_interactions: +159
* delete_lines: +78
* delete_near_zeros: +3
* relate_parameters: +350
* snap_to_one: +0
* tie_parameters: +17

### 10 parents for the next round

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
diff.y -= (params.b * params.g) * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.445, b = 0.208, c = 0.010, d = 0.047, e = 0.010, f = 11.486, g = 1.505, h = 0.042

-- score: -198.67 (accuracy -208.67, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.355, b = 0.214, c = 0.047, d = 0.010, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -198.67 (accuracy -208.67, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.868, b = 0.047, c = 0.010, d = 0.010, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -198.67 (accuracy -208.67, token simplicity 6.00, parameter simplicity 4.00) --
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

-- score: -198.66 (accuracy -208.66, token simplicity 6.00, parameter simplicity 4.00) --
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

-- score: -198.66 (accuracy -208.66, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 4.053, b = 0.042, c = 0.011, d = 0.047, e = 0.010, f = 11.517, g = 0.314, h = 1.506

-- score: -198.66 (accuracy -208.66, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += (params.a * params.e) * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 4.050, b = 0.171, c = 0.011, d = 0.047, e = 0.010, f = 11.475, g = 0.312, h = 1.504

-- score: -198.65 (accuracy -208.65, token simplicity 6.00, parameter simplicity 4.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.f
diff.y -= params.g * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 3.074, b = 0.233, c = 0.042, d = 0.047, e = 0.010, f = 11.531, g = 0.314, h = 1.507

## Round 4 | 1.67s | best score: -199.18

+407 new programs (407 actually scored)
* linear_fit: +0
* quadratic_fit: +13
* add_single_terms: +10
* delete_interactions: +150
* delete_lines: +79
* delete_near_zeros: +6
* relate_parameters: +140
* snap_to_one: +0
* tie_parameters: +9

### 10 parents for the next round

-- score: -199.18 (accuracy -208.68, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.e * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 11.519, b = 0.314, c = 0.197, d = 0.010, e = 0.047, f = 0.042, g = 1.506

-- score: -199.17 (accuracy -208.67, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.b * params.f) * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.480, b = 0.207, c = 0.010, d = 0.046, e = 11.447, f = 1.503, g = 0.042

-- score: -199.16 (accuracy -208.66, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.851, b = 0.047, c = 0.010, d = 11.505, e = 0.313, f = 0.042, g = 1.505

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

-- score: -199.13 (accuracy -208.63, token simplicity 6.00, parameter simplicity 3.50) --
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

-- score: -199.08 (accuracy -208.58, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b * params.d) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.d * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 4.159, b = 0.156, c = 0.011, d = 0.307, e = 11.288, f = 0.042, g = 1.496

-- score: -199.04 (accuracy -208.54, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 4.382, b = 0.152, c = 0.011, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -198.96 (accuracy -208.66, token simplicity 6.20, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b * params.c) * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 3.398, b = 0.214, c = 0.046, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -198.96 (accuracy -208.46, token simplicity 6.00, parameter simplicity 3.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += (params.b * params.f) * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 4.430, b = 0.136, c = 0.011, d = 0.048, e = 11.290, f = 0.307, g = 1.497

-- score: -198.96 (accuracy -208.66, token simplicity 6.20, parameter simplicity 3.50) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += (params.c * params.d) * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 11.251, b = 0.306, c = 0.213, d = 0.047, e = 0.010, f = 0.042, g = 1.495

## Round 5 | 1.40s | best score: -199.39

+307 new programs (307 actually scored)
* linear_fit: +3
* quadratic_fit: +10
* add_single_terms: +11
* delete_interactions: +140
* delete_lines: +68
* delete_near_zeros: +5
* relate_parameters: +63
* snap_to_one: +0
* tie_parameters: +7

### 10 parents for the next round

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.978, b = 0.047, c = 0.010, d = 11.109, e = 0.301, f = 1.486

-- score: -199.28 (accuracy -208.48, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b * params.d) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.d * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.787, b = 0.160, c = 0.011, d = 0.297, e = 10.985, f = 1.485

-- score: -199.25 (accuracy -208.65, token simplicity 6.40, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += (params.c * params.d) * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += (params.c * params.d) * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.288, b = 0.307, c = 0.213, d = 0.046, e = 0.042, f = 1.496

-- score: -199.25 (accuracy -208.45, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.b * params.f) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.992, b = 0.195, c = 0.010, d = 0.047, e = 10.666, f = 1.470

-- score: -199.24 (accuracy -208.44, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 4.291, b = 0.137, c = 0.011, d = 11.170, e = 0.303, f = 1.492

-- score: -199.24 (accuracy -208.44, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += (params.b - params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 10.661, b = 0.288, c = 0.046, d = 0.009, e = 0.041, f = 1.470

-- score: -199.24 (accuracy -208.64, token simplicity 6.40, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b * params.c) * data.y * data.y
diff.y += params.d
diff.y -= (params.b * params.e) * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.423, b = 0.214, c = 0.046, d = 11.840, e = 1.518, f = 0.042

-- score: -199.22 (accuracy -208.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b * params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= (params.a * params.b) * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 4.275, b = 0.011, c = 11.910, d = 0.324, e = 0.042, f = 1.522

-- score: -199.21 (accuracy -208.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= (params.b * params.d) * data.y
  Demo 0: a = 4.276, b = 0.134, c = 0.011, d = 11.111, e = 0.303, f = 0.041

-- score: -199.21 (accuracy -208.41, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 12.130, b = 0.330, c = 0.146, d = 0.011, e = 0.043, f = 1.531

## Round 6 | 2.12s | best score: -199.44

+293 new programs (293 actually scored)
* linear_fit: +10
* quadratic_fit: +10
* add_single_terms: +20
* delete_interactions: +146
* delete_lines: +75
* delete_near_zeros: +11
* relate_parameters: +17
* snap_to_one: +0
* tie_parameters: +4

### 10 parents for the next round

-- score: -199.44 (accuracy -208.34, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= (params.b * params.d) * data.y
  Demo 0: a = 4.282, b = 0.135, c = 0.011, d = 11.035, e = 0.308

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.978, b = 0.047, c = 0.010, d = 11.109, e = 0.301, f = 1.486

-- score: -199.28 (accuracy -208.48, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b * params.d) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.d * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.787, b = 0.160, c = 0.011, d = 0.297, e = 10.985, f = 1.485

-- score: -199.25 (accuracy -208.65, token simplicity 6.40, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += (params.c * params.d) * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += (params.c * params.d) * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.288, b = 0.307, c = 0.213, d = 0.046, e = 0.042, f = 1.496

-- score: -199.25 (accuracy -208.45, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.b * params.f) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.992, b = 0.195, c = 0.010, d = 0.047, e = 10.666, f = 1.470

-- score: -199.24 (accuracy -208.44, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 4.291, b = 0.137, c = 0.011, d = 11.170, e = 0.303, f = 1.492

-- score: -199.24 (accuracy -208.44, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += (params.b - params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 10.661, b = 0.288, c = 0.046, d = 0.009, e = 0.041, f = 1.470

-- score: -199.24 (accuracy -208.64, token simplicity 6.40, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b * params.c) * data.y * data.y
diff.y += params.d
diff.y -= (params.b * params.e) * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.423, b = 0.214, c = 0.046, d = 11.840, e = 1.518, f = 0.042

-- score: -199.23 (accuracy -208.13, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.b * params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= (params.a * params.b) * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.a * params.d) * data.y
  Demo 0: a = 4.342, b = 0.011, c = 13.028, d = 0.360, e = 0.044

-- score: -199.22 (accuracy -208.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b * params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= (params.a * params.b) * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 4.275, b = 0.011, c = 11.910, d = 0.324, e = 0.042, f = 1.522

## Round 7 | 0.21s | best score: -199.44 (stable)

+55 new programs (55 actually scored)
* linear_fit: +2
* quadratic_fit: +2
* add_single_terms: +4
* delete_interactions: +29
* delete_lines: +15
* delete_near_zeros: +2
* relate_parameters: +1
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -199.44 (accuracy -208.34, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= (params.b * params.d) * data.y
  Demo 0: a = 4.282, b = 0.135, c = 0.011, d = 11.035, e = 0.308

-- score: -199.39 (accuracy -208.59, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.a * params.b) * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.978, b = 0.047, c = 0.010, d = 11.109, e = 0.301, f = 1.486

-- score: -199.28 (accuracy -208.48, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.b * params.d) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= params.d * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.787, b = 0.160, c = 0.011, d = 0.297, e = 10.985, f = 1.485

-- score: -199.25 (accuracy -208.65, token simplicity 6.40, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += params.c * data.x
diff.x += (params.c * params.d) * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += (params.c * params.d) * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.288, b = 0.307, c = 0.213, d = 0.046, e = 0.042, f = 1.496

-- score: -199.25 (accuracy -208.45, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.e
diff.y -= (params.b * params.f) * data.x
diff.y += (params.a * params.c) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 3.992, b = 0.195, c = 0.010, d = 0.047, e = 10.666, f = 1.470

-- score: -199.24 (accuracy -208.44, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= (params.a * params.c) * data.x * data.y
diff.x += params.c * data.y * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 4.291, b = 0.137, c = 0.011, d = 11.170, e = 0.303, f = 1.492

-- score: -199.24 (accuracy -208.44, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += (params.a * params.b)
diff.x += (params.b - params.c) * data.x
diff.x += params.d * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y * data.y
diff.y += params.a
diff.y -= params.b * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 10.661, b = 0.288, c = 0.046, d = 0.009, e = 0.041, f = 1.470

-- score: -199.24 (accuracy -208.64, token simplicity 6.40, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += (params.b * params.c) * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.b * params.c) * data.y * data.y
diff.y += params.d
diff.y -= (params.b * params.e) * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 3.423, b = 0.214, c = 0.046, d = 11.840, e = 1.518, f = 0.042

-- score: -199.23 (accuracy -208.13, token simplicity 6.40, parameter simplicity 2.50) --
diff.x += params.a
diff.x += (params.b * params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= (params.a * params.b) * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.a * params.d) * data.y
  Demo 0: a = 4.342, b = 0.011, c = 13.028, d = 0.360, e = 0.044

-- score: -199.22 (accuracy -208.42, token simplicity 6.20, parameter simplicity 3.00) --
diff.x += params.a
diff.x += (params.b * params.c) * data.x
diff.x += params.b * data.x * data.x
diff.x -= (params.a * params.b) * data.x * data.y
diff.x += params.b * data.y * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 4.275, b = 0.011, c = 11.910, d = 0.324, e = 0.042, f = 1.522

