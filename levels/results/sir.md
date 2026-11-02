# sir

Solved in 3.54 seconds. 2762 programs considered, over 13 rounds.

## Winner

-- score: -160.86 (accuracy -167.46, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y -= params.b * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.496, b = 0.000, c = 0.001, d = -0.101
  Demo 1: a = 0.269, b = -0.102, c = 0.111, d = 0.052
  Demo 2: a = 0.816, b = -0.063, c = 0.061, d = -0.186

## Runner-ups

-- score: -160.86 (accuracy -167.46, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += (params.b - params.d) * data.y
diff.y += params.b * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.496, b = -0.000, c = 0.001, d = 0.101
  Demo 1: a = 0.269, b = 0.102, c = 0.111, d = 0.050
  Demo 2: a = 0.816, b = 0.063, c = 0.061, d = 0.249

-- score: -160.86 (accuracy -167.46, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.b * data.z
diff.z += (params.b - params.d) * data.y
  Demo 0: a = 0.496, b = -0.000, c = 0.001, d = -0.101
  Demo 1: a = 0.269, b = 0.102, c = 0.111, d = 0.052
  Demo 2: a = 0.816, b = 0.063, c = 0.061, d = -0.186

-- score: -160.79 (accuracy -166.89, token simplicity 4.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y -= params.b * data.x
diff.y += params.a * data.x * data.y
diff.y += params.c * data.y
diff.y -= params.b * data.z
diff.z -= (params.b + params.c) * data.y
  Demo 0: a = 0.500, b = 0.001, c = -0.102
  Demo 1: a = 0.287, b = -0.086, c = 0.036
  Demo 2: a = 0.806, b = -0.065, c = -0.185

-- score: -160.68 (accuracy -167.28, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += (params.c - params.d) * data.y
diff.y -= params.b * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.494, b = 0.001, c = 0.001, d = 0.102
  Demo 1: a = 0.272, b = -0.097, c = 0.103, d = 0.053
  Demo 2: a = 0.819, b = -0.062, c = 0.060, d = 0.248

# The Search

## Round 0 | 0.01s | best score: -83.25

+36 new programs (36 actually scored)
* add_terms: +36
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -83.25 (accuracy -95.25, token simplicity 7.00, parameter simplicity 5.00) --
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

-- score: -43.30 (accuracy -44.60, token simplicity 0.80, parameter simplicity 0.50) --
diff.x -= params.a * data.x * data.y
  Demo 0: a = 0.491
  Demo 1: a = 0.281
  Demo 2: a = 0.821

-- score: -41.65 (accuracy -45.85, token simplicity 2.20, parameter simplicity 2.00) --
diff.y += params.a
diff.y += params.b * data.x
diff.y += params.c * data.y
diff.y += params.d * data.z
  Demo 0: a = 0.040, b = -0.004, c = -0.045, d = -0.050
  Demo 1: a = -0.185, b = 0.238, c = 0.162, d = 0.184
  Demo 2: a = -0.158, b = 0.209, c = 0.112, d = 0.146

-- score: -37.16 (accuracy -49.16, token simplicity 7.00, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.x * data.z
diff.x += params.f * data.y
diff.x -= params.g * data.y * data.y
diff.x -= params.h * data.y * data.z
diff.x += params.i * data.z
diff.x += params.j * data.z * data.z
  Demo 0: a = -2.380, b = 4.939, c = -2.555, d = -4.804, e = -4.853, f = 4.135, g = 1.776, h = 4.149, i = 4.755, j = -2.365
  Demo 1: a = 0.183, b = -0.918, c = 0.760, d = 0.029, e = 0.965, f = 0.205, g = 0.400, h = 0.245, i = -0.335, j = 0.151
  Demo 2: a = -5.505, b = 12.446, c = -6.959, d = -19.165, e = -11.805, f = 16.851, g = 11.672, h = 16.776, i = 10.907, j = -5.420

-- score: -34.88 (accuracy -39.08, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
  Demo 0: a = -0.108, b = 0.073, c = 0.008, d = 0.118
  Demo 1: a = 0.122, b = -0.169, c = -0.154, d = -0.119
  Demo 2: a = 0.428, b = -0.496, c = -0.609, d = -0.415

## Round 1 | 0.21s | best score: -126.55

+256 new programs (256 actually scored)
* add_terms: +142
* delete_lines: +28
* relate_parameters: +32
* snap_to_one: +0
* tie_parameters: +54

### 5 parents for the next round

-- score: -126.55 (accuracy -139.85, token simplicity 7.80, parameter simplicity 5.50) --
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

-- score: -120.41 (accuracy -144.41, token simplicity 14.00, parameter simplicity 10.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.x * data.z
diff.x += params.f * data.y
diff.x -= params.g * data.y * data.y
diff.x -= params.h * data.y * data.z
diff.x += params.i * data.z
diff.x += params.j * data.z * data.z
diff.y -= params.k
diff.y += params.l * data.x
diff.y += params.m * data.x * data.x
diff.y += params.n * data.x * data.y
diff.y -= params.o * data.x * data.z
diff.y += params.p * data.y
diff.y += params.q * data.y * data.y
diff.y += params.r * data.y * data.z
diff.y += params.s * data.z
diff.y += params.t * data.z * data.z
  Demo 0: a = -2.380, b = 4.939, c = -2.555, d = -4.804, e = -4.853, f = 4.135, g = 1.776, h = 4.149, i = 4.755, j = -2.365, k = 0.431, l = 0.939, m = -0.509, n = -0.518, o = 0.941, p = 0.870, q = -0.507, r = -0.848, s = 0.737, t = -0.305
  Demo 1: a = 0.183, b = -0.918, c = 0.760, d = 0.029, e = 0.965, f = 0.205, g = 0.400, h = 0.245, i = -0.335, j = 0.151, k = 0.014, l = 0.344, m = -0.336, n = 0.328, o = 0.143, p = -0.426, q = 0.372, r = 0.462, s = -0.053, t = 0.068
  Demo 2: a = -5.505, b = 12.446, c = -6.959, d = -19.165, e = -11.805, f = 16.851, g = 11.672, h = 16.776, i = 10.907, j = -5.420, k = 0.021, l = -0.088, m = 0.106, n = 1.194, o = 0.029, p = -0.372, q = 0.214, r = 0.297, s = -0.087, t = 0.121

-- score: -118.12 (accuracy -134.32, token simplicity 9.20, parameter simplicity 7.00) --
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

-- score: -112.38 (accuracy -125.48, token simplicity 7.60, parameter simplicity 5.50) --
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

-- score: -110.01 (accuracy -126.21, token simplicity 9.20, parameter simplicity 7.00) --
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
diff.z += params.k
diff.z += params.l * data.x
diff.z += params.m * data.y
diff.z += params.n * data.z
  Demo 0: a = 0.431, b = 0.939, c = -0.509, d = -0.518, e = 0.941, f = 0.870, g = -0.507, h = -0.848, i = 0.737, j = -0.305, k = 0.082, l = -0.088, m = 0.030, n = -0.083
  Demo 1: a = 0.014, b = 0.344, c = -0.336, d = 0.328, e = 0.143, f = -0.426, g = 0.372, h = 0.462, i = -0.053, j = 0.068, k = 0.043, l = -0.041, m = 0.004, n = -0.043
  Demo 2: a = 0.021, b = -0.088, c = 0.106, d = 1.194, e = 0.029, f = -0.372, g = 0.214, h = 0.297, i = -0.087, j = 0.121, k = -0.191, l = 0.194, m = 0.432, n = 0.190

## Round 2 | 0.76s | best score: -155.68

+426 new programs (426 actually scored)
* add_terms: +90
* delete_lines: +68
* relate_parameters: +90
* snap_to_one: +0
* tie_parameters: +178

### 5 parents for the next round

-- score: -155.68 (accuracy -170.08, token simplicity 8.40, parameter simplicity 6.00) --
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

-- score: -153.31 (accuracy -170.81, token simplicity 10.00, parameter simplicity 7.50) --
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
diff.z += params.l
diff.z += params.m * data.x
diff.z += params.n * data.y
diff.z += params.o * data.z
  Demo 0: a = 0.491, b = 0.431, c = 0.939, d = -0.509, e = -0.518, f = 0.941, g = 0.870, h = -0.507, i = -0.848, j = 0.737, k = -0.305, l = 0.082, m = -0.088, n = 0.030, o = -0.083
  Demo 1: a = 0.281, b = 0.014, c = 0.344, d = -0.336, e = 0.328, f = 0.143, g = -0.426, h = 0.372, i = 0.462, j = -0.053, k = 0.068, l = 0.043, m = -0.041, n = 0.004, o = -0.043
  Demo 2: a = 0.821, b = 0.021, c = -0.088, d = 0.106, e = 1.194, f = 0.029, g = -0.372, h = 0.214, i = 0.297, j = -0.087, k = 0.121, l = -0.191, m = 0.194, n = 0.432, o = 0.190

-- score: -153.00 (accuracy -167.60, token simplicity 8.60, parameter simplicity 6.00) --
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

-- score: -149.54 (accuracy -174.64, token simplicity 14.60, parameter simplicity 10.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.x * data.z
diff.x += params.f * data.y
diff.x -= params.g * data.y * data.y
diff.x -= params.h * data.y * data.z
diff.x += params.i * data.z
diff.x += params.j * data.z * data.z
diff.y -= params.k
diff.y += params.l * data.x
diff.y += params.m * data.x * data.x
diff.y += params.n * data.x * data.y
diff.y -= params.o * data.x * data.z
diff.y += params.p * data.y
diff.y += params.q * data.y * data.y
diff.y += params.r * data.y * data.z
diff.y += params.s * data.z
diff.y += params.t * data.z * data.z
diff.z += params.u * data.y
  Demo 0: a = -2.380, b = 4.939, c = -2.555, d = -4.804, e = -4.853, f = 4.135, g = 1.776, h = 4.149, i = 4.755, j = -2.365, k = 0.431, l = 0.939, m = -0.509, n = -0.518, o = 0.941, p = 0.870, q = -0.507, r = -0.848, s = 0.737, t = -0.305, u = 0.103
  Demo 1: a = 0.183, b = -0.918, c = 0.760, d = 0.029, e = 0.965, f = 0.205, g = 0.400, h = 0.245, i = -0.335, j = 0.151, k = 0.014, l = 0.344, m = -0.336, n = 0.328, o = 0.143, p = -0.426, q = 0.372, r = 0.462, s = -0.053, t = 0.068, u = 0.050
  Demo 2: a = -5.505, b = 12.446, c = -6.959, d = -19.165, e = -11.805, f = 16.851, g = 11.672, h = 16.776, i = 10.907, j = -5.420, k = 0.021, l = -0.088, m = 0.106, n = 1.194, o = 0.029, p = -0.372, q = 0.214, r = 0.297, s = -0.087, t = 0.121, u = 0.243

-- score: -149.29 (accuracy -174.59, token simplicity 14.80, parameter simplicity 10.50) --
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
diff.z += params.l
diff.z += params.m * data.x
diff.z -= params.n * data.x * data.x
diff.z += params.o * data.x * data.y
diff.z -= params.p * data.x * data.z
diff.z += params.q * data.y
diff.z += params.r * data.y * data.y
diff.z += params.s * data.y * data.z
diff.z += params.t * data.z
diff.z += params.u * data.z * data.z
  Demo 0: a = 0.491, b = 0.431, c = 0.939, d = -0.509, e = -0.518, f = 0.941, g = 0.870, h = -0.507, i = -0.848, j = 0.737, k = -0.305, l = -2.661, m = 5.605, n = 2.949, o = -5.318, p = 5.731, q = 5.214, r = -2.370, s = -5.124, t = 5.298, u = -2.625
  Demo 1: a = 0.281, b = 0.014, c = 0.344, d = -0.336, e = 0.328, f = 0.143, g = -0.426, h = 0.372, i = 0.462, j = -0.053, k = 0.068, l = 0.587, m = 0.126, n = 0.791, o = 0.635, p = 0.115, q = -1.739, r = 1.141, s = 1.713, t = -1.081, u = 0.491
  Demo 2: a = 0.821, b = 0.021, c = -0.088, d = 0.106, e = 1.194, f = 0.029, g = -0.372, h = 0.214, i = 0.297, j = -0.087, k = 0.121, l = -2.765, m = 6.040, n = 3.266, o = 0.163, p = 5.803, q = -0.787, r = 3.826, s = 0.281, t = 5.959, u = -3.210

## Round 3 | 1.04s | best score: -156.95

+487 new programs (487 actually scored)
* add_terms: +76
* delete_lines: +74
* relate_parameters: +118
* snap_to_one: +0
* tie_parameters: +219

### 5 parents for the next round

-- score: -156.95 (accuracy -170.05, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.x * data.z
diff.y += params.g * data.y
diff.y += params.h * data.y * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.z += params.k * data.y
  Demo 0: a = 0.491, b = 0.125, c = 0.296, d = 0.172, e = 0.065, f = 0.297, g = 0.316, h = -0.257, i = -0.295, j = 0.125, k = 0.103
  Demo 1: a = 0.281, b = 0.076, c = 0.458, d = 0.386, e = 0.212, f = 0.260, g = -0.299, h = 0.307, i = 0.330, j = 0.077, k = 0.050
  Demo 2: a = 0.821, b = 0.142, c = 0.158, d = 0.018, e = 0.939, f = 0.272, g = -0.129, h = 0.096, i = 0.050, j = 0.154, k = 0.243

-- score: -156.92 (accuracy -170.02, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.y * data.z
diff.y -= params.i * data.z
diff.y += params.j * data.z * data.z
diff.z += params.k * data.y
  Demo 0: a = 0.491, b = 0.015, c = 0.002, d = -0.018, e = 0.331, f = 0.061, g = -0.142, h = -0.045, i = 0.151, j = 0.135, k = 0.103
  Demo 1: a = 0.281, b = 0.054, c = 0.207, d = -0.266, e = 0.460, f = -0.557, g = 0.436, h = 0.600, i = 0.196, j = 0.143, k = 0.050
  Demo 2: a = 0.821, b = -0.007, c = -0.117, d = 0.121, e = 1.224, f = -0.401, g = 0.228, h = 0.325, i = 0.115, j = 0.135, k = 0.243

-- score: -156.89 (accuracy -169.99, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.x
diff.y -= params.e * data.x * data.z
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.y * data.z
diff.y += params.i * data.z
diff.y -= params.j * data.z * data.z
diff.z += params.k * data.y
  Demo 0: a = 0.491, b = 0.163, c = 0.377, d = 0.215, e = 0.379, f = 0.377, g = -0.281, h = -0.359, i = 0.205, j = 0.042, k = 0.103
  Demo 1: a = 0.281, b = 0.183, c = 0.660, d = 0.480, e = 0.467, f = -0.076, g = 0.190, h = 0.099, i = 0.298, j = 0.114, k = 0.050
  Demo 2: a = 0.821, b = 0.531, c = 0.951, d = 0.420, e = 1.045, f = 0.779, g = -0.411, h = -0.854, i = 0.925, j = 0.381, k = 0.243

-- score: -156.89 (accuracy -169.99, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.x * data.z
diff.y += params.g * data.y
diff.y += params.h * data.y * data.y
diff.y += params.i * data.z
diff.y += params.j * data.z * data.z
diff.z += params.k * data.y
  Demo 0: a = 0.491, b = 0.032, c = -0.030, d = 0.003, e = 0.376, f = 0.029, g = 0.016, h = -0.116, i = -0.184, j = 0.152, k = 0.103
  Demo 1: a = 0.281, b = -0.221, c = 0.696, d = 0.475, e = -0.060, f = -0.505, g = 0.021, h = 0.132, i = 0.377, j = -0.154, k = 0.050
  Demo 2: a = 0.821, b = -0.152, c = 0.176, d = 0.027, e = 0.888, f = -0.288, g = -0.076, h = 0.053, i = 0.173, j = -0.008, k = 0.243

-- score: -156.86 (accuracy -169.96, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.x * data.z
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.y * data.z
diff.y += params.i * data.z
diff.y += params.j * data.z * data.z
diff.z += params.k * data.y
  Demo 0: a = 0.491, b = 0.029, c = -0.030, d = 0.359, e = 0.030, f = 0.037, g = -0.131, h = -0.020, i = -0.180, j = 0.150, k = 0.103
  Demo 1: a = 0.281, b = 0.230, c = -0.231, d = 0.831, e = 0.451, f = -0.855, g = 0.562, h = 0.916, i = -0.570, j = 0.340, k = 0.050
  Demo 2: a = 0.821, b = -0.121, c = 0.119, d = 0.981, e = -0.233, f = -0.171, g = 0.117, h = 0.094, i = 0.113, j = 0.021, k = 0.243

## Round 4 | 0.33s | best score: -158.01

+279 new programs (279 actually scored)
* add_terms: +110
* delete_lines: +43
* relate_parameters: +33
* snap_to_one: +0
* tie_parameters: +93

### 5 parents for the next round

-- score: -158.01 (accuracy -169.81, token simplicity 6.80, parameter simplicity 5.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.z
diff.y += params.i * data.z * data.z
diff.z += params.j * data.y
  Demo 0: a = 0.491, b = 0.022, c = -0.005, d = -0.019, e = 0.373, f = 0.016, g = -0.108, h = -0.163, i = 0.141, j = 0.103
  Demo 1: a = 0.281, b = -0.129, c = 0.217, d = -0.072, e = 0.172, f = 0.046, g = 0.026, h = 0.159, i = -0.029, j = 0.050
  Demo 2: a = 0.821, b = -0.033, c = -0.097, d = 0.127, e = 0.913, f = -0.061, g = -0.098, h = -0.074, i = 0.119, j = 0.243

-- score: -158.00 (accuracy -169.80, token simplicity 6.80, parameter simplicity 5.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.x * data.z
diff.y += params.f * data.y
diff.y += params.g * data.y * data.y
diff.y += params.h * data.z
diff.y += params.i * data.z * data.z
diff.z += params.j * data.y
  Demo 0: a = 0.491, b = 0.034, c = -0.035, d = 0.377, e = 0.034, f = 0.016, g = -0.117, h = -0.187, i = 0.153, j = 0.103
  Demo 1: a = 0.281, b = -0.124, c = 0.145, d = 0.228, e = 0.064, f = 0.046, g = 0.024, h = 0.150, i = -0.024, j = 0.050
  Demo 2: a = 0.821, b = -0.133, c = 0.131, d = 0.895, e = -0.241, f = -0.074, g = 0.030, h = 0.134, i = 0.012, j = 0.243

-- score: -157.91 (accuracy -169.71, token simplicity 6.80, parameter simplicity 5.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.y
diff.y += params.g * data.y * data.z
diff.y += params.h * data.z
diff.y += params.i * data.z * data.z
diff.z += params.j * data.y
  Demo 0: a = 0.491, b = 0.038, c = -0.018, d = -0.021, e = 0.485, f = -0.113, g = 0.111, h = -0.179, i = 0.142, j = 0.103
  Demo 1: a = 0.281, b = -0.123, c = 0.219, d = -0.081, e = 0.151, f = 0.063, g = -0.009, h = 0.142, i = -0.018, j = 0.050
  Demo 2: a = 0.821, b = -0.022, c = -0.103, d = 0.121, e = 1.019, f = -0.176, g = 0.118, h = -0.097, i = 0.131, j = 0.243

-- score: -157.90 (accuracy -169.70, token simplicity 6.80, parameter simplicity 5.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.x * data.z
diff.y += params.f * data.y
diff.y += params.g * data.y * data.z
diff.y += params.h * data.z
diff.y += params.i * data.z * data.z
diff.z += params.j * data.y
  Demo 0: a = 0.491, b = 0.060, c = -0.062, d = 0.505, e = 0.054, f = -0.136, g = 0.134, h = -0.223, i = 0.163, j = 0.103
  Demo 1: a = 0.281, b = -0.117, c = 0.137, d = 0.213, e = 0.076, f = 0.061, g = -0.008, h = 0.130, i = -0.011, j = 0.050
  Demo 2: a = 0.821, b = -0.131, c = 0.128, d = 0.875, e = -0.236, f = -0.052, g = -0.016, h = 0.127, i = 0.016, j = 0.243

-- score: -157.89 (accuracy -169.89, token simplicity 7.00, parameter simplicity 5.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.x * data.z
diff.y += params.g * data.y * data.y
diff.y += params.h * data.z
diff.y += params.i * data.z * data.z
diff.z += params.j * data.y
  Demo 0: a = 0.491, b = 0.033, c = -0.027, d = -0.007, e = 0.382, f = 0.030, g = -0.104, h = -0.171, i = 0.138, j = 0.103
  Demo 1: a = 0.281, b = -0.239, c = 0.779, d = -0.542, e = -0.087, f = -0.599, g = 0.171, h = 0.434, i = -0.193, j = 0.050
  Demo 2: a = 0.821, b = -0.097, c = 0.062, d = 0.032, e = 0.856, f = -0.165, g = -0.115, h = 0.018, i = 0.092, j = 0.243

## Round 5 | 0.26s | best score: -158.93

+239 new programs (239 actually scored)
* add_terms: +112
* delete_lines: +44
* relate_parameters: +26
* snap_to_one: +0
* tie_parameters: +57

### 5 parents for the next round

-- score: -158.93 (accuracy -169.63, token simplicity 6.20, parameter simplicity 4.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.y * data.y
diff.y += params.g * data.z
diff.y += params.h * data.z * data.z
diff.z += params.i * data.y
  Demo 0: a = 0.491, b = 0.023, c = -0.001, d = -0.023, e = 0.379, f = -0.096, g = -0.150, h = 0.127, i = 0.103
  Demo 1: a = 0.281, b = -0.131, c = 0.203, d = -0.050, e = 0.218, f = 0.080, g = 0.206, h = -0.073, i = 0.050
  Demo 2: a = 0.821, b = -0.030, c = -0.095, d = 0.121, e = 0.876, f = -0.188, g = -0.117, h = 0.159, i = 0.243

-- score: -158.92 (accuracy -169.42, token simplicity 6.00, parameter simplicity 4.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y
diff.y += params.f * data.y * data.y
diff.y += params.g * data.z
diff.y += params.h * data.z * data.z
diff.z += params.i * data.y
  Demo 0: a = 0.491, b = 0.021, c = -0.023, d = 0.389, e = 0.024, f = -0.109, g = -0.171, h = 0.149, i = 0.103
  Demo 1: a = 0.281, b = -0.155, c = 0.177, d = 0.265, e = 0.036, f = 0.068, g = 0.222, h = -0.066, i = 0.050
  Demo 2: a = 0.821, b = 0.003, c = -0.009, d = 0.735, e = -0.042, f = -0.223, g = -0.165, h = 0.170, i = 0.243

-- score: -158.90 (accuracy -169.60, token simplicity 6.20, parameter simplicity 4.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.x * data.z
diff.y += params.f * data.y * data.y
diff.y += params.g * data.z
diff.y += params.h * data.z * data.z
diff.z += params.i * data.y
  Demo 0: a = 0.491, b = 0.037, c = -0.038, d = 0.384, e = 0.041, f = -0.107, g = -0.179, h = 0.142, i = 0.103
  Demo 1: a = 0.281, b = -0.136, c = 0.160, d = 0.265, e = 0.029, f = 0.087, g = 0.215, h = -0.078, i = 0.050
  Demo 2: a = 0.821, b = -0.119, c = 0.115, d = 0.847, e = -0.220, f = -0.092, g = 0.061, h = 0.071, i = 0.243

-- score: -158.87 (accuracy -169.37, token simplicity 6.00, parameter simplicity 4.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y
diff.y += params.f * data.y * data.z
diff.y += params.g * data.z
diff.y += params.h * data.z * data.z
diff.z += params.i * data.y
  Demo 0: a = 0.491, b = 0.037, c = -0.039, d = 0.504, e = -0.104, f = 0.111, g = -0.188, h = 0.151, i = 0.103
  Demo 1: a = 0.281, b = -0.169, c = 0.193, d = 0.195, e = 0.118, f = -0.078, g = 0.246, h = -0.075, i = 0.050
  Demo 2: a = 0.821, b = 0.022, c = -0.029, d = 0.965, e = -0.281, f = 0.236, g = -0.198, h = 0.184, i = 0.243

-- score: -158.86 (accuracy -169.36, token simplicity 6.00, parameter simplicity 4.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.y
diff.y += params.g * data.z
diff.y += params.h * data.z * data.z
diff.z += params.i * data.y
  Demo 0: a = 0.491, b = 0.019, c = 0.003, d = -0.022, e = 0.411, f = -0.066, g = -0.102, h = 0.084, i = 0.103
  Demo 1: a = 0.281, b = -0.117, c = 0.219, d = -0.088, e = 0.150, f = 0.056, g = 0.130, h = -0.011, i = 0.050
  Demo 2: a = 0.821, b = -0.044, c = -0.102, d = 0.145, e = 0.947, f = -0.099, g = -0.035, h = 0.091, i = 0.243

## Round 6 | 0.22s | best score: -159.89

+223 new programs (223 actually scored)
* add_terms: +111
* delete_lines: +40
* relate_parameters: +24
* snap_to_one: +0
* tie_parameters: +48

### 5 parents for the next round

-- score: -159.89 (accuracy -169.29, token simplicity 5.40, parameter simplicity 4.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y * data.y
diff.y += params.f * data.z
diff.y += params.g * data.z * data.z
diff.z += params.h * data.y
  Demo 0: a = 0.491, b = 0.023, c = -0.024, d = 0.405, e = -0.089, f = -0.152, g = 0.129, h = 0.103
  Demo 1: a = 0.281, b = -0.150, c = 0.175, d = 0.280, e = 0.102, f = 0.245, g = -0.094, h = 0.050
  Demo 2: a = 0.821, b = 0.004, c = -0.011, d = 0.716, e = -0.282, f = -0.192, g = 0.197, h = 0.243

-- score: -159.70 (accuracy -168.90, token simplicity 5.20, parameter simplicity 4.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.y
diff.y += params.g * data.z
diff.z += params.h * data.y
  Demo 0: a = 0.491, b = 0.007, c = 0.043, d = -0.049, e = 0.440, f = -0.112, g = -0.006, h = 0.103
  Demo 1: a = 0.281, b = -0.114, c = 0.222, d = -0.094, e = 0.136, f = 0.058, g = 0.116, h = 0.050
  Demo 2: a = 0.821, b = -0.083, c = -0.078, d = 0.160, e = 1.029, f = -0.141, g = 0.091, h = 0.243

-- score: -159.48 (accuracy -168.68, token simplicity 5.20, parameter simplicity 4.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y
diff.y += params.f * data.z
diff.y += params.g * data.z * data.z
diff.z += params.h * data.y
  Demo 0: a = 0.491, b = 0.019, c = -0.018, d = 0.429, e = -0.057, f = -0.111, g = 0.093, h = 0.103
  Demo 1: a = 0.281, b = -0.131, c = 0.147, d = 0.256, e = 0.067, f = 0.157, g = -0.025, h = 0.050
  Demo 2: a = 0.821, b = -0.013, c = 0.010, d = 0.758, e = -0.141, f = -0.094, g = 0.113, h = 0.243

-- score: -159.40 (accuracy -168.80, token simplicity 5.40, parameter simplicity 4.00) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.x * data.z
diff.y += params.f * data.z
diff.y += params.g * data.z * data.z
diff.z += params.h * data.y
  Demo 0: a = 0.491, b = 0.013, c = 0.014, d = 0.425, e = -0.074, f = -0.109, g = 0.123, h = 0.103
  Demo 1: a = 0.281, b = 0.064, c = 0.081, d = 0.228, e = 0.115, f = 0.078, g = -0.013, h = 0.050
  Demo 2: a = 0.821, b = 0.160, c = 0.158, d = 0.873, e = -0.282, f = 0.137, g = 0.038, h = 0.243

-- score: -159.39 (accuracy -169.59, token simplicity 6.20, parameter simplicity 4.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y * data.y
diff.y += params.g * data.z
diff.y += params.f * data.z * data.z
diff.z += params.h * data.y
  Demo 0: a = 0.491, b = 0.019, c = 0.009, d = -0.030, e = 0.382, f = 0.112, g = -0.131, h = 0.103
  Demo 1: a = 0.281, b = -0.130, c = 0.202, d = -0.051, e = 0.220, f = -0.075, g = 0.205, h = 0.050
  Demo 2: a = 0.821, b = -0.030, c = -0.099, d = 0.126, e = 0.875, f = 0.164, g = -0.121, h = 0.243

## Round 7 | 0.20s | best score: -160.28

+227 new programs (227 actually scored)
* add_terms: +119
* delete_lines: +38
* relate_parameters: +29
* snap_to_one: +0
* tie_parameters: +41

### 5 parents for the next round

-- score: -160.28 (accuracy -169.18, token simplicity 5.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y * data.y
diff.y += params.f * data.z
diff.y += params.e * data.z * data.z
diff.z += params.g * data.y
  Demo 0: a = 0.491, b = 0.018, c = -0.019, d = 0.420, e = 0.108, f = -0.127, g = 0.103
  Demo 1: a = 0.281, b = -0.148, c = 0.173, d = 0.283, e = -0.096, f = 0.245, g = 0.050
  Demo 2: a = 0.821, b = 0.007, c = -0.013, d = 0.690, e = 0.218, f = -0.215, g = 0.243

-- score: -160.03 (accuracy -167.93, token simplicity 4.40, parameter simplicity 3.50) --
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

-- score: -159.95 (accuracy -168.85, token simplicity 5.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y * data.y
diff.y += params.e * data.z
diff.y += params.f * data.z * data.z
diff.z += params.g * data.y
  Demo 0: a = 0.459, b = 0.001, c = -0.004, d = -0.104, e = -0.096, f = 0.095, g = 0.103
  Demo 1: a = 0.281, b = -0.150, c = 0.175, d = 0.102, e = 0.246, f = -0.094, g = 0.050
  Demo 2: a = 0.777, b = -0.012, c = 0.001, d = -0.331, e = -0.156, f = 0.176, g = 0.243

-- score: -159.89 (accuracy -169.29, token simplicity 5.40, parameter simplicity 4.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y * data.y
diff.y += params.f * data.z
diff.y += params.g * data.z * data.z
diff.z += params.h * data.y
  Demo 0: a = 0.491, b = 0.023, c = -0.024, d = 0.405, e = -0.089, f = -0.152, g = 0.129, h = 0.103
  Demo 1: a = 0.281, b = -0.150, c = 0.175, d = 0.280, e = 0.102, f = 0.245, g = -0.094, h = 0.050
  Demo 2: a = 0.821, b = 0.004, c = -0.011, d = 0.716, e = -0.282, f = -0.192, g = 0.197, h = 0.243

-- score: -159.89 (accuracy -168.79, token simplicity 5.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.x
diff.y += params.e * data.x * data.y
diff.y -= (params.b + params.f) * data.y
diff.y += params.g * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.491, b = 0.007, c = 0.039, d = -0.046, e = 0.441, f = 0.104, g = -0.007
  Demo 1: a = 0.281, b = -0.116, c = 0.205, d = -0.074, e = 0.148, f = 0.052, g = 0.118
  Demo 2: a = 0.821, b = -0.077, c = -0.060, d = 0.135, e = 1.019, f = 0.237, g = 0.084

## Round 8 | 0.14s | best score: -160.36

+165 new programs (165 actually scored)
* add_terms: +97
* delete_lines: +27
* relate_parameters: +18
* snap_to_one: +0
* tie_parameters: +23

### 5 parents for the next round

-- score: -160.36 (accuracy -167.76, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.e * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.495, b = 0.002, c = -0.001, d = -0.102, e = -0.001, f = 0.103
  Demo 1: a = 0.271, b = -0.118, c = 0.128, d = 0.064, e = 0.120, f = 0.050
  Demo 2: a = 0.829, b = -0.060, c = 0.057, d = -0.197, e = 0.061, f = 0.243

-- score: -160.31 (accuracy -167.71, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += params.e * data.y
diff.y += params.b * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.491, b = -0.002, c = -0.001, d = 0.497, e = -0.102, f = 0.103
  Demo 1: a = 0.281, b = 0.114, c = 0.129, d = 0.233, e = 0.067, f = 0.050
  Demo 2: a = 0.821, b = 0.063, c = 0.061, d = 0.822, e = -0.190, f = 0.243

-- score: -160.29 (accuracy -167.89, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= (params.b + params.e) * data.y
diff.y += params.f * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.491, b = 0.000, c = 0.000, d = 0.501, e = 0.102, f = -0.000
  Demo 1: a = 0.281, b = -0.126, c = 0.141, d = 0.239, e = 0.050, f = 0.127
  Demo 2: a = 0.821, b = -0.061, c = 0.059, d = 0.816, e = 0.251, f = 0.062

-- score: -160.29 (accuracy -168.69, token simplicity 5.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.d * data.y * data.y
diff.y += params.e * data.z
diff.y += params.d * data.z * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.457, b = 0.001, c = -0.005, d = 0.099, e = -0.101, f = 0.103
  Demo 1: a = 0.282, b = -0.148, c = 0.172, d = -0.096, e = 0.244, f = 0.050
  Demo 2: a = 0.753, b = -0.013, c = 0.004, d = 0.212, e = -0.188, f = 0.243

-- score: -160.28 (accuracy -169.18, token simplicity 5.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y * data.y
diff.y += params.f * data.z
diff.y += params.e * data.z * data.z
diff.z += params.g * data.y
  Demo 0: a = 0.491, b = 0.018, c = -0.019, d = 0.420, e = 0.108, f = -0.127, g = 0.103
  Demo 1: a = 0.281, b = -0.148, c = 0.173, d = 0.283, e = -0.096, f = 0.245, g = 0.050
  Demo 2: a = 0.821, b = 0.007, c = -0.013, d = 0.690, e = 0.218, f = -0.215, g = 0.243

## Round 9 | 0.12s | best score: -160.58

+152 new programs (152 actually scored)
* add_terms: +103
* delete_lines: +22
* relate_parameters: +12
* snap_to_one: +0
* tie_parameters: +15

### 5 parents for the next round

-- score: -160.58 (accuracy -167.68, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.e * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.497, b = 0.000, c = 0.001, d = -0.102, e = 0.000
  Demo 1: a = 0.268, b = -0.115, c = 0.125, d = 0.064, e = 0.117
  Demo 2: a = 0.818, b = -0.061, c = 0.059, d = -0.190, e = 0.061

-- score: -160.58 (accuracy -167.48, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.b * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.494, b = -0.002, c = -0.001, d = -0.102, e = 0.103
  Demo 1: a = 0.269, b = 0.102, c = 0.111, d = 0.051, e = 0.050
  Demo 2: a = 0.822, b = 0.063, c = 0.061, d = -0.190, e = 0.243

-- score: -160.57 (accuracy -167.67, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.d * data.x * data.y
diff.y += (params.b - params.e) * data.y
diff.y += params.b * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.491, b = -0.000, c = 0.000, d = 0.500, e = 0.101
  Demo 1: a = 0.281, b = 0.112, c = 0.126, d = 0.239, e = 0.049
  Demo 2: a = 0.821, b = 0.063, c = 0.061, d = 0.812, e = 0.249

-- score: -160.54 (accuracy -167.64, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.e * data.z
diff.z += (params.e - params.d) * data.y
  Demo 0: a = 0.497, b = 0.000, c = 0.001, d = -0.102, e = -0.000
  Demo 1: a = 0.268, b = -0.113, c = 0.122, d = 0.062, e = 0.114
  Demo 2: a = 0.818, b = -0.061, c = 0.059, d = -0.189, e = 0.062

-- score: -160.45 (accuracy -168.55, token simplicity 5.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.d * data.y * data.y
diff.y += params.e * data.z
diff.y += params.d * data.z * data.z
diff.z += (params.d - params.b) * data.y
  Demo 0: a = 0.462, b = -0.002, c = -0.001, d = 0.098, e = -0.096
  Demo 1: a = 0.280, b = -0.148, c = 0.173, d = -0.097, e = 0.246
  Demo 2: a = 0.766, b = -0.022, c = 0.013, d = 0.210, e = -0.177

## Round 10 | 0.13s | best score: -160.86

+189 new programs (189 actually scored)
* add_terms: +139
* delete_lines: +29
* relate_parameters: +6
* snap_to_one: +0
* tie_parameters: +15

### 5 parents for the next round

-- score: -160.86 (accuracy -167.46, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y -= params.b * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.496, b = 0.000, c = 0.001, d = -0.101
  Demo 1: a = 0.269, b = -0.102, c = 0.111, d = 0.052
  Demo 2: a = 0.816, b = -0.063, c = 0.061, d = -0.186

-- score: -160.68 (accuracy -167.28, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += (params.c - params.d) * data.y
diff.y -= params.b * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.494, b = 0.001, c = 0.001, d = 0.102
  Demo 1: a = 0.272, b = -0.097, c = 0.103, d = 0.053
  Demo 2: a = 0.819, b = -0.062, c = 0.060, d = 0.248

-- score: -160.60 (accuracy -167.20, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.c * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.499, b = 0.001, c = -0.000, d = -0.103
  Demo 1: a = 0.285, b = -0.104, c = 0.106, d = 0.053
  Demo 2: a = 0.806, b = -0.064, c = 0.064, d = -0.185

-- score: -160.58 (accuracy -167.68, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.e * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.497, b = 0.000, c = 0.001, d = -0.102, e = 0.000
  Demo 1: a = 0.268, b = -0.115, c = 0.125, d = 0.064, e = 0.117
  Demo 2: a = 0.818, b = -0.061, c = 0.059, d = -0.190, e = 0.061

-- score: -160.58 (accuracy -167.48, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y -= params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.b * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.494, b = -0.002, c = -0.001, d = -0.102, e = 0.103
  Demo 1: a = 0.269, b = 0.102, c = 0.111, d = 0.051, e = 0.050
  Demo 2: a = 0.822, b = 0.063, c = 0.061, d = -0.190, e = 0.243

## Round 11 | 0.07s | best score: -160.86

+103 new programs (103 actually scored)
* add_terms: +84
* delete_lines: +17
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +2

### 5 parents for the next round

-- score: -160.86 (accuracy -167.46, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y -= params.b * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.496, b = 0.000, c = 0.001, d = -0.101
  Demo 1: a = 0.269, b = -0.102, c = 0.111, d = 0.052
  Demo 2: a = 0.816, b = -0.063, c = 0.061, d = -0.186

-- score: -160.79 (accuracy -166.89, token simplicity 4.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y -= params.b * data.x
diff.y += params.a * data.x * data.y
diff.y += params.c * data.y
diff.y -= params.b * data.z
diff.z -= (params.b + params.c) * data.y
  Demo 0: a = 0.500, b = 0.001, c = -0.102
  Demo 1: a = 0.287, b = -0.086, c = 0.036
  Demo 2: a = 0.806, b = -0.065, c = -0.185

-- score: -160.68 (accuracy -167.28, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += (params.c - params.d) * data.y
diff.y -= params.b * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.494, b = 0.001, c = 0.001, d = 0.102
  Demo 1: a = 0.272, b = -0.097, c = 0.103, d = 0.053
  Demo 2: a = 0.819, b = -0.062, c = 0.060, d = 0.248

-- score: -160.60 (accuracy -167.20, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.c * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.499, b = 0.001, c = -0.000, d = -0.103
  Demo 1: a = 0.285, b = -0.104, c = 0.106, d = 0.053
  Demo 2: a = 0.806, b = -0.064, c = 0.064, d = -0.185

-- score: -160.58 (accuracy -167.68, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.e * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.497, b = 0.000, c = 0.001, d = -0.102, e = 0.000
  Demo 1: a = 0.268, b = -0.115, c = 0.125, d = 0.064, e = 0.117
  Demo 2: a = 0.818, b = -0.061, c = 0.059, d = -0.190, e = 0.061

## Round 12 | 0.03s | best score: -160.86

+34 new programs (34 actually scored)
* add_terms: +28
* delete_lines: +6
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -160.86 (accuracy -167.46, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y -= params.b * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.496, b = 0.000, c = 0.001, d = -0.101
  Demo 1: a = 0.269, b = -0.102, c = 0.111, d = 0.052
  Demo 2: a = 0.816, b = -0.063, c = 0.061, d = -0.186

-- score: -160.79 (accuracy -166.89, token simplicity 4.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y -= params.b * data.x
diff.y += params.a * data.x * data.y
diff.y += params.c * data.y
diff.y -= params.b * data.z
diff.z -= (params.b + params.c) * data.y
  Demo 0: a = 0.500, b = 0.001, c = -0.102
  Demo 1: a = 0.287, b = -0.086, c = 0.036
  Demo 2: a = 0.806, b = -0.065, c = -0.185

-- score: -160.68 (accuracy -167.28, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += (params.c - params.d) * data.y
diff.y -= params.b * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.494, b = 0.001, c = 0.001, d = 0.102
  Demo 1: a = 0.272, b = -0.097, c = 0.103, d = 0.053
  Demo 2: a = 0.819, b = -0.062, c = 0.060, d = 0.248

-- score: -160.60 (accuracy -167.20, token simplicity 4.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.c * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.499, b = 0.001, c = -0.000, d = -0.103
  Demo 1: a = 0.285, b = -0.104, c = 0.106, d = 0.053
  Demo 2: a = 0.806, b = -0.064, c = 0.064, d = -0.185

-- score: -160.58 (accuracy -167.68, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y += params.a * data.x * data.y
diff.y += params.d * data.y
diff.y += params.e * data.z
diff.z -= (params.b + params.d) * data.y
  Demo 0: a = 0.497, b = 0.000, c = 0.001, d = -0.102, e = 0.000
  Demo 1: a = 0.268, b = -0.115, c = 0.125, d = 0.064, e = 0.117
  Demo 2: a = 0.818, b = -0.061, c = 0.059, d = -0.190, e = 0.061

