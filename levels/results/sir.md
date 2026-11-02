# sir

Solved in 1.75 seconds. 2041 programs considered, over 8 rounds.

## Winner

-- score: -38.37 (accuracy -42.17, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

## Runner-ups

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -37.63 (accuracy -41.63, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a - params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.526, b = 0.104
  Demo 1: a = 0.309, b = 0.052
  Demo 2: a = 0.859, b = 0.259

-- score: -37.63 (accuracy -41.63, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a + params.b) * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.421, b = 0.104
  Demo 1: a = 0.257, b = 0.052
  Demo 2: a = 0.600, b = 0.259

# The Search

## Round 0 | 0.01s | best score: -12.30

+36 new programs (36 actually scored)
* add_terms: +36
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -12.30 (accuracy -24.30, token simplicity 7.00, parameter simplicity 5.00) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.x * data.z
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.y * data.z
diff.y += params.i * data.z
diff.y += params.j * data.z * data.z
  Demo 0: a = 0.431, b = 0.939, c = -0.509, d = -0.518, e = 0.941, f = 0.870, g = -0.507, h = -0.848, i = 0.737, j = -0.305
  Demo 1: a = 0.014, b = 0.344, c = -0.336, d = 0.328, e = 0.143, f = -0.426, g = 0.372, h = 0.462, i = -0.053, j = 0.068
  Demo 2: a = 0.021, b = -0.088, c = 0.106, d = 1.194, e = 0.029, f = -0.372, g = 0.214, h = 0.297, i = -0.087, j = 0.121

-- score: -10.08 (accuracy -11.38, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.x * data.y
  Demo 0: a = 0.491
  Demo 1: a = 0.281
  Demo 2: a = 0.821

-- score: -7.50 (accuracy -11.70, token simplicity 2.20, parameter simplicity 2.00) --
diff.y += params.a
diff.y += params.b * data.x
diff.y += params.c * data.y
diff.y += params.d * data.z
  Demo 0: a = 0.040, b = -0.004, c = -0.045, d = -0.050
  Demo 1: a = -0.185, b = 0.238, c = 0.162, d = 0.184
  Demo 2: a = -0.158, b = 0.209, c = 0.112, d = 0.146

-- score: -6.61 (accuracy -7.71, token simplicity 0.60, parameter simplicity 0.50) --
diff.z += params.a * data.y
  Demo 0: a = 0.103
  Demo 1: a = 0.050
  Demo 2: a = 0.243

-- score: -6.16 (accuracy -7.46, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.y
  Demo 0: a = 0.239
  Demo 1: a = 0.158
  Demo 2: a = 0.230

-- score: -5.78 (accuracy -6.88, token simplicity 0.60, parameter simplicity 0.50) --
diff.x -= params.a * data.x
  Demo 0: a = 0.057
  Demo 1: a = 0.058
  Demo 2: a = 0.103

-- score: -5.78 (accuracy -7.08, token simplicity 0.80, parameter simplicity 0.50) --
diff.z += params.a * data.y * data.y
  Demo 0: a = 0.255
  Demo 1: a = 0.109
  Demo 2: a = 0.880

-- score: -5.77 (accuracy -9.97, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
  Demo 0: a = -0.108, b = 0.073, c = 0.008, d = 0.118
  Demo 1: a = 0.122, b = -0.169, c = -0.154, d = -0.119
  Demo 2: a = 0.428, b = -0.496, c = -0.609, d = -0.415

-- score: -5.54 (accuracy -6.64, token simplicity 0.60, parameter simplicity 0.50) --
diff.y += params.a * data.x
  Demo 0: a = 0.034
  Demo 1: a = 0.038
  Demo 2: a = 0.035

-- score: -4.54 (accuracy -5.84, token simplicity 0.80, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.x
  Demo 0: a = 0.035
  Demo 1: a = 0.045
  Demo 2: a = 0.046

## Round 1 | 0.19s | best score: -22.38

+344 new programs (344 actually scored)
* add_terms: +302
* delete_lines: +18
* delete_near_zeros: +0
* relate_parameters: +18
* snap_to_one: +0
* tie_parameters: +6

### 10 parents for the next round

-- score: -22.38 (accuracy -35.68, token simplicity 7.80, parameter simplicity 5.50) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.x * data.z
diff.y += params.g * data.y
diff.y += params.h * data.y * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.y += params.k * data.z * data.z
  Demo 0: a = 0.491, b = 0.431, c = 0.939, d = -0.509, e = -0.518, f = 0.941, g = 0.870, h = -0.507, i = -0.848, j = 0.737, k = -0.305
  Demo 1: a = 0.281, b = 0.014, c = 0.344, d = -0.336, e = 0.328, f = 0.143, g = -0.426, h = 0.372, i = 0.462, j = -0.053, k = 0.068
  Demo 2: a = 0.821, b = 0.021, c = -0.088, d = 0.106, e = 1.194, f = 0.029, g = -0.372, h = 0.214, i = 0.297, j = -0.087, k = 0.121

-- score: -20.70 (accuracy -23.10, token simplicity 1.40, parameter simplicity 1.00) --
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
  Demo 0: a = 0.501, b = 0.101
  Demo 1: a = 0.295, b = 0.052
  Demo 2: a = 0.810, b = 0.251

-- score: -19.18 (accuracy -21.78, token simplicity 1.60, parameter simplicity 1.00) --
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y * data.z
  Demo 0: a = 0.334, b = 0.145
  Demo 1: a = 0.201, b = 0.079
  Demo 2: a = 0.463, b = 0.325

-- score: -18.91 (accuracy -32.01, token simplicity 7.60, parameter simplicity 5.50) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.x * data.z
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.y * data.z
diff.y += params.i * data.z
diff.y += params.j * data.z * data.z
diff.z += params.k * data.y
  Demo 0: a = 0.431, b = 0.939, c = -0.509, d = -0.518, e = 0.941, f = 0.870, g = -0.507, h = -0.848, i = 0.737, j = -0.305, k = 0.103
  Demo 1: a = 0.014, b = 0.344, c = -0.336, d = 0.328, e = 0.143, f = -0.426, g = 0.372, h = 0.462, i = -0.053, j = 0.068, k = 0.050
  Demo 2: a = 0.021, b = -0.088, c = 0.106, d = 1.194, e = 0.029, f = -0.372, g = 0.214, h = 0.297, i = -0.087, j = 0.121, k = 0.243

-- score: -18.25 (accuracy -23.75, token simplicity 3.00, parameter simplicity 2.50) --
diff.y += params.a
diff.y += params.b * data.x
diff.y += params.c * data.x * data.y
diff.y += params.d * data.y
diff.y += params.e * data.z
  Demo 0: a = 0.001, b = -0.001, c = 0.499, d = -0.103, e = -0.001
  Demo 1: a = -0.126, b = 0.141, c = 0.241, d = 0.075, e = 0.127
  Demo 2: a = -0.058, b = 0.055, c = 0.839, d = -0.200, e = 0.060

-- score: -18.08 (accuracy -31.18, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.x * data.z
diff.y += params.g * data.y
diff.y += params.h * data.y * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.y += params.k * data.z * data.z
  Demo 0: a = 0.057, b = 0.431, c = 0.939, d = -0.509, e = -0.518, f = 0.941, g = 0.870, h = -0.507, i = -0.848, j = 0.737, k = -0.305
  Demo 1: a = 0.058, b = 0.014, c = 0.344, d = -0.336, e = 0.328, f = 0.143, g = -0.426, h = 0.372, i = 0.462, j = -0.053, k = 0.068
  Demo 2: a = 0.103, b = 0.021, c = -0.088, d = 0.106, e = 1.194, f = 0.029, g = -0.372, h = 0.214, i = 0.297, j = -0.087, k = 0.121

-- score: -18.08 (accuracy -31.38, token simplicity 7.80, parameter simplicity 5.50) --
diff.y -= params.a
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.x * data.z
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.y * data.z
diff.y += params.i * data.z
diff.y += params.j * data.z * data.z
diff.z += params.k * data.y * data.y
  Demo 0: a = 0.431, b = 0.939, c = -0.509, d = -0.518, e = 0.941, f = 0.870, g = -0.507, h = -0.848, i = 0.737, j = -0.305, k = 0.255
  Demo 1: a = 0.014, b = 0.344, c = -0.336, d = 0.328, e = 0.143, f = -0.426, g = 0.372, h = 0.462, i = -0.053, j = 0.068, k = 0.109
  Demo 2: a = 0.021, b = -0.088, c = 0.106, d = 1.194, e = 0.029, f = -0.372, g = 0.214, h = 0.297, i = -0.087, j = 0.121, k = 0.880

-- score: -18.07 (accuracy -34.27, token simplicity 9.20, parameter simplicity 7.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y -= params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.x * data.z
diff.y += params.j * data.y
diff.y += params.k * data.y * data.y
diff.y += params.l * data.y * data.z
diff.y += params.m * data.z
diff.y += params.n * data.z * data.z
  Demo 0: a = -0.108, b = 0.073, c = 0.008, d = 0.118, e = 0.431, f = 0.939, g = -0.509, h = -0.518, i = 0.941, j = 0.870, k = -0.507, l = -0.848, m = 0.737, n = -0.305
  Demo 1: a = 0.122, b = -0.169, c = -0.154, d = -0.119, e = 0.014, f = 0.344, g = -0.336, h = 0.328, i = 0.143, j = -0.426, k = 0.372, l = 0.462, m = -0.053, n = 0.068
  Demo 2: a = 0.428, b = -0.496, c = -0.609, d = -0.415, e = 0.021, f = -0.088, g = 0.106, h = 1.194, i = 0.029, j = -0.372, k = 0.214, l = 0.297, m = -0.087, n = 0.121

-- score: -17.57 (accuracy -23.07, token simplicity 3.00, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.y
diff.y += params.e * data.z
  Demo 0: a = 0.491, b = 0.040, c = -0.004, d = -0.045, e = -0.050
  Demo 1: a = 0.281, b = -0.185, c = 0.238, d = 0.162, e = 0.184
  Demo 2: a = 0.821, b = -0.158, c = 0.209, d = 0.112, e = 0.146

-- score: -17.51 (accuracy -20.11, token simplicity 1.60, parameter simplicity 1.00) --
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y * data.y
  Demo 0: a = 0.470, b = 0.234
  Demo 1: a = 0.286, b = 0.113
  Demo 2: a = 0.697, b = 0.782

## Round 2 | 0.49s | best score: -30.78

+431 new programs (431 actually scored)
* add_terms: +264
* delete_lines: +63
* delete_near_zeros: +0
* relate_parameters: +93
* snap_to_one: +0
* tie_parameters: +11

### 10 parents for the next round

-- score: -30.78 (accuracy -34.48, token simplicity 2.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101
  Demo 1: a = 0.281, b = 0.295, c = 0.052
  Demo 2: a = 0.821, b = 0.810, c = 0.251

-- score: -29.25 (accuracy -33.15, token simplicity 2.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
  Demo 0: a = 0.491, b = 0.334, c = 0.145
  Demo 1: a = 0.281, b = 0.201, c = 0.079
  Demo 2: a = 0.821, b = 0.463, c = 0.325

-- score: -28.99 (accuracy -43.39, token simplicity 8.40, parameter simplicity 6.00) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.x * data.z
diff.y += params.g * data.y
diff.y += params.h * data.y * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.y += params.k * data.z * data.z
diff.z += params.l * data.y
  Demo 0: a = 0.491, b = 0.431, c = 0.939, d = -0.509, e = -0.518, f = 0.941, g = 0.870, h = -0.507, i = -0.848, j = 0.737, k = -0.305, l = 0.103
  Demo 1: a = 0.281, b = 0.014, c = 0.344, d = -0.336, e = 0.328, f = 0.143, g = -0.426, h = 0.372, i = 0.462, j = -0.053, k = 0.068, l = 0.050
  Demo 2: a = 0.821, b = 0.021, c = -0.088, d = 0.106, e = 1.194, f = 0.029, g = -0.372, h = 0.214, i = 0.297, j = -0.087, k = 0.121, l = 0.243

-- score: -28.33 (accuracy -35.13, token simplicity 3.80, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y
diff.y += params.f * data.z
  Demo 0: a = 0.491, b = 0.001, c = -0.001, d = 0.499, e = -0.103, f = -0.001
  Demo 1: a = 0.281, b = -0.126, c = 0.141, d = 0.241, e = 0.075, f = 0.127
  Demo 2: a = 0.821, b = -0.058, c = 0.055, d = 0.839, e = -0.200, f = 0.060

-- score: -28.16 (accuracy -42.76, token simplicity 8.60, parameter simplicity 6.00) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.x * data.z
diff.y += params.g * data.y
diff.y += params.h * data.y * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.y += params.k * data.z * data.z
diff.z += params.l * data.y * data.y
  Demo 0: a = 0.491, b = 0.431, c = 0.939, d = -0.509, e = -0.518, f = 0.941, g = 0.870, h = -0.507, i = -0.848, j = 0.737, k = -0.305, l = 0.255
  Demo 1: a = 0.281, b = 0.014, c = 0.344, d = -0.336, e = 0.328, f = 0.143, g = -0.426, h = 0.372, i = 0.462, j = -0.053, k = 0.068, l = 0.109
  Demo 2: a = 0.821, b = 0.021, c = -0.088, d = 0.106, e = 1.194, f = 0.029, g = -0.372, h = 0.214, i = 0.297, j = -0.087, k = 0.121, l = 0.880

-- score: -27.59 (accuracy -31.49, token simplicity 2.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.y
  Demo 0: a = 0.491, b = 0.470, c = 0.234
  Demo 1: a = 0.281, b = 0.286, c = 0.113
  Demo 2: a = 0.821, b = 0.697, c = 0.782

-- score: -27.31 (accuracy -30.81, token simplicity 2.00, parameter simplicity 1.50) --
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.501, b = 0.101, c = 0.103
  Demo 1: a = 0.295, b = 0.052, c = 0.050
  Demo 2: a = 0.810, b = 0.251, c = 0.243

-- score: -26.59 (accuracy -41.19, token simplicity 8.60, parameter simplicity 6.00) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.x * data.z
diff.y += params.g * data.y
diff.y += params.h * data.y * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.y += params.k * data.z * data.z
diff.z += params.l * data.y * data.z
  Demo 0: a = 0.491, b = 0.431, c = 0.939, d = -0.509, e = -0.518, f = 0.941, g = 0.870, h = -0.507, i = -0.848, j = 0.737, k = -0.305, l = 0.174
  Demo 1: a = 0.281, b = 0.014, c = 0.344, d = -0.336, e = 0.328, f = 0.143, g = -0.426, h = 0.372, i = 0.462, j = -0.053, k = 0.068, l = 0.091
  Demo 2: a = 0.821, b = 0.021, c = -0.088, d = 0.106, e = 1.194, f = 0.029, g = -0.372, h = 0.214, i = 0.297, j = -0.087, k = 0.121, l = 0.446

-- score: -26.48 (accuracy -29.98, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.057, b = 0.501, c = 0.101
  Demo 1: a = 0.058, b = 0.295, c = 0.052
  Demo 2: a = 0.103, b = 0.810, c = 0.251

-- score: -26.48 (accuracy -30.18, token simplicity 2.20, parameter simplicity 1.50) --
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y * data.y
  Demo 0: a = 0.501, b = 0.101, c = 0.255
  Demo 1: a = 0.295, b = 0.052, c = 0.109
  Demo 2: a = 0.810, b = 0.251, c = 0.880

## Round 3 | 0.39s | best score: -37.39

+398 new programs (398 actually scored)
* add_terms: +281
* delete_lines: +35
* delete_near_zeros: +0
* relate_parameters: +74
* snap_to_one: +0
* tie_parameters: +8

### 10 parents for the next round

-- score: -37.39 (accuracy -42.19, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -36.55 (accuracy -41.55, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.255
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.109
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.880

-- score: -35.87 (accuracy -40.87, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.103
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.050
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.243

-- score: -35.03 (accuracy -40.23, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.y * data.y
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.255
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.109
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.880

-- score: -34.99 (accuracy -39.99, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y * data.z
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.174
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.091
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.446

-- score: -34.94 (accuracy -42.84, token simplicity 4.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y
diff.y += params.f * data.z
diff.z += params.g * data.y
  Demo 0: a = 0.491, b = 0.001, c = -0.001, d = 0.499, e = -0.103, f = -0.001, g = 0.103
  Demo 1: a = 0.281, b = -0.126, c = 0.141, d = 0.241, e = 0.075, f = 0.127, g = 0.050
  Demo 2: a = 0.821, b = -0.058, c = 0.055, d = 0.839, e = -0.200, f = 0.060, g = 0.243

-- score: -34.56 (accuracy -39.56, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.z
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.514
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.355
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.518

-- score: -34.47 (accuracy -42.37, token simplicity 4.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d
diff.z += params.e * data.x
diff.z += params.f * data.y
diff.z += params.g * data.z
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.082, e = -0.088, f = 0.030, g = -0.083
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.043, e = -0.041, f = 0.004, g = -0.043
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = -0.191, e = 0.194, f = 0.432, g = 0.190

-- score: -34.20 (accuracy -39.20, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.470, c = 0.234, d = 0.103
  Demo 1: a = 0.281, b = 0.286, c = 0.113, d = 0.050
  Demo 2: a = 0.821, b = 0.697, c = 0.782, d = 0.243

-- score: -34.12 (accuracy -39.12, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.284
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.141
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.588

## Round 4 | 0.27s | best score: -37.88

+411 new programs (411 actually scored)
* add_terms: +283
* delete_lines: +23
* delete_near_zeros: +0
* relate_parameters: +92
* snap_to_one: +0
* tie_parameters: +13

### 10 parents for the next round

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -37.39 (accuracy -42.19, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -37.24 (accuracy -41.74, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a + params.b) * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.431, b = 0.100, c = 0.107
  Demo 1: a = 0.264, b = 0.049, c = 0.055
  Demo 2: a = 0.660, b = 0.227, c = 0.275

-- score: -37.15 (accuracy -41.65, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a + params.b) * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.423, b = 0.105, c = 0.103
  Demo 1: a = 0.259, b = 0.054, c = 0.050
  Demo 2: a = 0.611, b = 0.269, c = 0.243

-- score: -37.13 (accuracy -41.63, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a - params.b) * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.555, b = 0.092, c = 0.103
  Demo 1: a = 0.308, b = 0.045, c = 0.050
  Demo 2: a = 0.951, b = 0.223, c = 0.243

-- score: -37.10 (accuracy -41.60, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.465, b = 0.099, c = 0.094
  Demo 1: a = 0.264, b = 0.048, c = 0.046
  Demo 2: a = 0.739, b = 0.229, c = 0.229

-- score: -37.04 (accuracy -41.54, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.255
  Demo 1: a = 0.288, b = 0.051, c = 0.109
  Demo 2: a = 0.813, b = 0.252, c = 0.880

-- score: -36.64 (accuracy -41.34, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += (params.a * params.b) * data.y * data.y
  Demo 0: a = 0.497, b = 0.504, c = 0.101
  Demo 1: a = 0.298, b = 0.311, c = 0.055
  Demo 2: a = 0.896, b = 0.847, c = 0.263

-- score: -36.55 (accuracy -41.55, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.255
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.109
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.880

## Round 5 | 0.22s | best score: -38.37

+272 new programs (272 actually scored)
* add_terms: +251
* delete_lines: +16
* delete_near_zeros: +0
* relate_parameters: +4
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -38.37 (accuracy -42.17, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -37.63 (accuracy -41.63, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a - params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.526, b = 0.104
  Demo 1: a = 0.309, b = 0.052
  Demo 2: a = 0.859, b = 0.259

-- score: -37.61 (accuracy -41.61, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.470, b = 0.096
  Demo 1: a = 0.266, b = 0.047
  Demo 2: a = 0.739, b = 0.229

-- score: -37.39 (accuracy -42.19, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -37.24 (accuracy -41.74, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a + params.b) * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.431, b = 0.100, c = 0.107
  Demo 1: a = 0.264, b = 0.049, c = 0.055
  Demo 2: a = 0.660, b = 0.227, c = 0.275

-- score: -37.15 (accuracy -41.65, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a + params.b) * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.423, b = 0.105, c = 0.103
  Demo 1: a = 0.259, b = 0.054, c = 0.050
  Demo 2: a = 0.611, b = 0.269, c = 0.243

-- score: -37.13 (accuracy -41.63, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a - params.b) * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.555, b = 0.092, c = 0.103
  Demo 1: a = 0.308, b = 0.045, c = 0.050
  Demo 2: a = 0.951, b = 0.223, c = 0.243

-- score: -37.10 (accuracy -41.60, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.465, b = 0.099, c = 0.094
  Demo 1: a = 0.264, b = 0.048, c = 0.046
  Demo 2: a = 0.739, b = 0.229, c = 0.229

## Round 6 | 0.06s | best score: -38.37 (stable)

+99 new programs (99 actually scored)
* add_terms: +96
* delete_lines: +3
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -38.37 (accuracy -42.17, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -37.63 (accuracy -41.63, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a - params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.526, b = 0.104
  Demo 1: a = 0.309, b = 0.052
  Demo 2: a = 0.859, b = 0.259

-- score: -37.61 (accuracy -41.61, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.470, b = 0.096
  Demo 1: a = 0.266, b = 0.047
  Demo 2: a = 0.739, b = 0.229

-- score: -37.48 (accuracy -42.18, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101, c = -0.000
  Demo 1: a = 0.286, b = 0.049, c = 0.001
  Demo 2: a = 0.810, b = 0.250, c = -0.001

-- score: -37.48 (accuracy -42.18, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.000, c = 0.102
  Demo 1: a = 0.288, b = -0.000, c = 0.050
  Demo 2: a = 0.807, b = 0.000, c = 0.250

-- score: -37.47 (accuracy -42.17, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.000, b = 0.499, c = 0.101
  Demo 1: a = 0.000, b = 0.288, c = 0.050
  Demo 2: a = 0.001, b = 0.804, c = 0.248

-- score: -37.39 (accuracy -42.19, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -37.32 (accuracy -42.22, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.496, b = 0.001, c = 0.101
  Demo 1: a = 0.278, b = 0.004, c = 0.051
  Demo 2: a = 0.820, b = -0.003, c = 0.249

## Round 7 | 0.08s | best score: -38.37 (stable)

+131 new programs (131 actually scored)
* add_terms: +115
* delete_lines: +16
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -38.37 (accuracy -42.17, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -37.88 (accuracy -42.18, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -37.63 (accuracy -41.63, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a - params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.526, b = 0.104
  Demo 1: a = 0.309, b = 0.052
  Demo 2: a = 0.859, b = 0.259

-- score: -37.61 (accuracy -41.61, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.470, b = 0.096
  Demo 1: a = 0.266, b = 0.047
  Demo 2: a = 0.739, b = 0.229

-- score: -37.48 (accuracy -42.18, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101, c = -0.000
  Demo 1: a = 0.286, b = 0.049, c = 0.001
  Demo 2: a = 0.810, b = 0.250, c = -0.001

-- score: -37.48 (accuracy -42.18, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.000, c = 0.102
  Demo 1: a = 0.288, b = -0.000, c = 0.050
  Demo 2: a = 0.807, b = 0.000, c = 0.250

-- score: -37.47 (accuracy -42.17, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.000, b = 0.499, c = 0.101
  Demo 1: a = 0.000, b = 0.288, c = 0.050
  Demo 2: a = 0.001, b = 0.804, c = 0.248

-- score: -37.39 (accuracy -42.19, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -37.32 (accuracy -42.22, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.496, b = 0.001, c = 0.101
  Demo 1: a = 0.278, b = 0.004, c = 0.051
  Demo 2: a = 0.820, b = -0.003, c = 0.249

