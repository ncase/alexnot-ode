# sir

Solved in 7.39 seconds. 3559 programs considered, over 7 rounds.

## Winner

-- score: -63.67 (accuracy -67.47, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

## Runner-ups

-- score: -63.19 (accuracy -67.49, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -63.18 (accuracy -67.48, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -62.99 (accuracy -67.49, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a - params.b) * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = -0.013, c = 0.102
  Demo 1: a = 0.281, b = -0.011, c = 0.051
  Demo 2: a = 0.821, b = 0.019, c = 0.248

-- score: -62.98 (accuracy -67.48, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= (params.b - params.c) * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.498, b = 0.103, c = 0.003
  Demo 1: a = 0.288, b = 0.050, c = -0.001
  Demo 2: a = 0.813, b = 0.243, c = -0.009

# The Search

## Round 0 | 0.03s | best score: -49.25

+42 new programs (42 actually scored)
* linear_fit: +4
* quadratic_fit: +9
* add_single_terms: +29
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -49.25 (accuracy -70.45, token simplicity 12.20, parameter simplicity 9.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.z
diff.x += params.g * data.z * data.z
diff.y -= params.h
diff.y += params.i * data.x
diff.y += params.j * data.x * data.x
diff.y += params.k * data.x * data.y
diff.y += params.l * data.x * data.z
diff.y += params.m * data.y
diff.y -= params.n * data.y * data.y
diff.y += params.o * data.z * data.z
diff.z += params.p
diff.z -= params.q * data.x * data.x
diff.z -= params.r * data.z * data.z
  Demo 0: a = -0.076, b = 0.095, c = 0.021, d = 0.457, e = 0.040, f = 0.110, g = -0.033, h = 0.046, i = 0.162, j = -0.118, k = 0.371, l = -0.172, m = -0.003, n = 0.049, o = 0.046, p = 0.059, q = 0.068, r = 0.059
  Demo 1: a = 0.068, b = -0.011, c = 0.071, d = 0.272, e = -0.100, f = -0.031, g = -0.039, h = 0.062, i = 0.040, j = 0.038, k = 0.200, l = 0.188, m = 0.070, n = 0.064, o = 0.064, p = 0.029, q = 0.028, r = 0.029
  Demo 2: a = 0.596, b = 0.128, c = 0.758, d = 1.767, e = -0.484, f = -0.924, g = 0.315, h = 0.070, i = -0.003, j = 0.071, k = 0.896, l = -0.100, m = -0.061, n = 0.055, o = 0.082, p = 0.102, q = 0.108, r = 0.111

-- score: -49.15 (accuracy -53.05, token simplicity 2.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
  Demo 0: a = 0.491, b = 0.334, c = 0.145
  Demo 1: a = 0.281, b = 0.201, c = 0.079
  Demo 2: a = 0.821, b = 0.463, c = 0.325

-- score: -48.07 (accuracy -53.07, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.z
  Demo 0: a = 0.484, b = -0.002, c = 0.334, d = 0.145
  Demo 1: a = 0.273, b = -0.003, c = 0.201, d = 0.079
  Demo 2: a = 0.872, b = 0.022, c = 0.463, d = 0.325

-- score: -41.53 (accuracy -72.53, token simplicity 18.00, parameter simplicity 13.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i
diff.y += params.j * data.x
diff.y += params.k * data.x * data.x
diff.y += params.l * data.x * data.y
diff.y += params.m * data.y * data.y
diff.y += params.n * data.y * data.z
diff.y += params.o * data.z
diff.y += params.p * data.z * data.z
diff.z += params.q
diff.z += params.r * data.x
diff.z -= params.s * data.x * data.x
diff.z += params.t * data.x * data.y
diff.z -= params.u * data.x * data.z
diff.z += params.v * data.y
diff.z += params.w * data.y * data.y
diff.z += params.x * data.y * data.z
diff.z += params.y * data.z
diff.z += params.z * data.z * data.z
  Demo 0: a = -0.058, b = 0.060, c = 0.003, d = 0.390, e = -0.050, f = 0.127, g = 0.069, h = 0.060, i = 0.024, j = -0.005, k = -0.021, l = 0.384, m = -0.096, n = 0.010, o = -0.160, p = 0.136, q = -2.661, r = 5.605, s = 2.949, t = -5.318, u = 5.731, v = 5.214, w = -2.370, x = -5.124, y = 5.298, z = -2.625
  Demo 1: a = 0.070, b = 0.001, c = 0.090, d = 0.433, e = 0.072, f = -0.179, g = -0.135, h = -0.071, i = -0.113, j = 0.218, k = -0.090, l = 0.192, m = 0.055, n = 0.050, o = 0.126, p = -0.011, q = 0.587, r = 0.126, s = 0.791, t = 0.635, u = 0.115, v = -1.739, w = 1.141, x = 1.713, y = -1.081, z = 0.491
  Demo 2: a = 0.110, b = 0.577, c = 0.730, d = 7.242, e = 5.639, f = -6.346, g = -5.712, h = -0.147, i = -0.037, j = -0.094, k = 0.127, l = 0.861, m = -0.161, n = -0.049, o = -0.074, p = 0.123, q = -2.765, r = 6.040, s = 3.266, t = 0.163, u = 5.803, v = -0.787, w = 3.826, x = 0.281, y = 5.959, z = -3.210

-- score: -41.47 (accuracy -71.97, token simplicity 18.00, parameter simplicity 12.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.x * data.z
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i * data.x
diff.y += params.j * data.x * data.x
diff.y += params.k * data.x * data.y
diff.y += params.l * data.x * data.z
diff.y += params.m * data.y * data.z
diff.y -= params.n * data.z
diff.y += params.o * data.z * data.z
diff.z += params.p
diff.z += params.q * data.x
diff.z -= params.r * data.x * data.x
diff.z += params.s * data.x * data.y
diff.z -= params.t * data.x * data.z
diff.z += params.u * data.y
diff.z += params.v * data.y * data.y
diff.z += params.w * data.y * data.z
diff.z += params.x * data.z
diff.z += params.y * data.z * data.z
  Demo 0: a = -0.060, b = 0.060, c = 0.271, d = 0.153, e = -0.183, f = 0.178, g = 0.150, h = 0.002, i = 0.034, j = -0.034, k = 0.375, l = -0.091, m = 0.013, n = 0.153, o = 0.155, p = -2.661, q = 5.605, r = 2.949, s = -5.318, t = 5.731, u = 5.214, v = -2.370, w = -5.124, x = 5.298, y = -2.625
  Demo 1: a = -0.706, b = 0.740, c = 0.319, d = 0.768, e = 0.697, f = -0.701, g = -0.711, h = 0.001, i = -0.345, j = 0.384, k = 0.451, l = 0.584, m = 0.069, n = 0.157, o = 0.161, p = 0.587, q = 0.126, r = 0.791, s = 0.635, t = 0.115, u = -1.739, v = 1.141, w = 1.713, x = -1.081, y = 0.491
  Demo 2: a = 1.204, b = -1.254, c = 7.246, d = -0.740, e = 5.385, f = -5.947, g = -5.312, h = -0.026, i = -0.208, j = 0.211, k = 0.836, l = 0.069, m = -0.093, n = 0.151, o = 0.167, p = -2.765, q = 6.040, r = 3.266, s = 0.163, t = 5.803, u = -0.787, v = 3.826, w = 0.281, x = 5.959, y = -3.210

-- score: -38.72 (accuracy -72.32, token simplicity 19.60, parameter simplicity 14.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.x += params.i * data.z * data.z
diff.y -= params.j
diff.y += params.k * data.x
diff.y += params.l * data.x * data.x
diff.y += params.m * data.x * data.y
diff.y -= params.n * data.x * data.z
diff.y += params.o * data.y
diff.y += params.p * data.y * data.y
diff.y += params.q * data.y * data.z
diff.y += params.r * data.z
diff.y += params.s * data.z * data.z
diff.z += params.t
diff.z -= params.u * data.x * data.x
diff.z += params.v * data.x * data.y
diff.z += params.w * data.x * data.z
diff.z += params.x * data.y
diff.z += params.y * data.y * data.y
diff.z += params.z * data.y * data.z
diff.z += params.p26 * data.z
diff.z += params.p27 * data.z * data.z
  Demo 0: a = -0.352, b = 0.703, c = -0.351, d = -0.839, e = -0.621, f = 0.332, g = -0.388, h = 0.733, i = -0.377, j = 0.431, k = 0.939, l = -0.509, m = -0.518, n = 0.941, o = 0.870, p = -0.507, q = -0.848, r = 0.737, s = -0.305, t = 0.004, u = 0.013, v = -0.232, w = -0.117, x = 0.372, y = -0.181, z = -0.314, p26 = -0.013, p27 = 0.011
  Demo 1: a = 0.499, b = -1.421, c = 0.939, d = 0.626, e = 1.482, f = -0.511, g = 0.489, h = -0.984, i = 0.484, j = 0.014, k = 0.344, l = -0.336, m = 0.328, n = 0.143, o = -0.426, p = 0.372, q = 0.462, r = -0.053, s = 0.068, t = 0.650, u = 0.727, v = 0.757, w = 0.015, x = -1.860, y = 1.200, z = 1.840, p26 = -1.212, p27 = 0.560
  Demo 2: a = 1.911, b = -2.469, c = 0.504, d = 0.162, e = 2.638, f = -2.193, g = 2.001, h = -3.681, i = 1.753, j = 0.021, k = -0.088, l = 0.106, m = 1.194, n = 0.029, o = -0.372, p = 0.214, q = 0.297, r = -0.087, s = 0.121, t = 0.173, u = 0.180, v = 6.428, w = 0.148, x = -6.756, y = 6.731, z = 6.289, p26 = 0.095, p27 = -0.287

-- score: -38.18 (accuracy -73.08, token simplicity 20.40, parameter simplicity 14.50) --
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
diff.y += params.k
diff.y += params.l * data.x
diff.y += params.m * data.x * data.x
diff.y += params.n * data.x * data.y
diff.y += params.o * data.x * data.z
diff.y += params.p * data.y * data.y
diff.y += params.q * data.y * data.z
diff.y += params.r * data.z
diff.y += params.s * data.z * data.z
diff.z += params.t
diff.z += params.u * data.x
diff.z -= params.v * data.x * data.x
diff.z += params.w * data.x * data.y
diff.z -= params.x * data.x * data.z
diff.z += params.y * data.y
diff.z += params.z * data.y * data.y
diff.z += params.p26 * data.y * data.z
diff.z += params.p27 * data.z
diff.z += params.p28 * data.z * data.z
  Demo 0: a = -2.380, b = 4.939, c = -2.555, d = -4.804, e = -4.853, f = 4.135, g = 1.776, h = 4.149, i = 4.755, j = -2.365, k = 0.040, l = -0.045, m = 0.005, n = 0.391, o = 0.045, p = -0.108, q = 0.014, r = -0.197, s = 0.157, t = -2.661, u = 5.605, v = 2.949, w = -5.318, x = 5.731, y = 5.214, z = -2.370, p26 = -5.124, p27 = 5.298, p28 = -2.625
  Demo 1: a = 0.183, b = -0.918, c = 0.760, d = 0.029, e = 0.965, f = 0.205, g = 0.400, h = 0.245, i = -0.335, j = 0.151, k = -0.210, l = 0.674, m = -0.465, n = -0.040, o = -0.483, p = 0.142, q = 0.023, r = 0.352, s = -0.141, t = 0.587, u = 0.126, v = 0.791, w = 0.635, x = 0.115, y = -1.739, z = 1.141, p26 = 1.713, p27 = -1.081, p28 = 0.491
  Demo 2: a = -5.505, b = 12.446, c = -6.959, d = -19.165, e = -11.805, f = 16.851, g = 11.672, h = 16.776, i = 10.907, j = -5.420, k = -0.184, l = 0.241, m = -0.059, n = 0.811, o = -0.351, p = 0.009, q = -0.075, r = 0.235, s = -0.039, t = -2.765, u = 6.040, v = 3.266, w = 0.163, x = 5.803, y = -0.787, z = 3.826, p26 = 0.281, p27 = 5.959, p28 = -3.210

-- score: -37.12 (accuracy -73.12, token simplicity 21.00, parameter simplicity 15.00) --
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
diff.z += params.u
diff.z += params.v * data.x
diff.z -= params.w * data.x * data.x
diff.z += params.x * data.x * data.y
diff.z -= params.y * data.x * data.z
diff.z += params.z * data.y
diff.z += params.p26 * data.y * data.y
diff.z += params.p27 * data.y * data.z
diff.z += params.p28 * data.z
diff.z += params.p29 * data.z * data.z
  Demo 0: a = -2.380, b = 4.939, c = -2.555, d = -4.804, e = -4.853, f = 4.135, g = 1.776, h = 4.149, i = 4.755, j = -2.365, k = 0.431, l = 0.939, m = -0.509, n = -0.518, o = 0.941, p = 0.870, q = -0.507, r = -0.848, s = 0.737, t = -0.305, u = -2.661, v = 5.605, w = 2.949, x = -5.318, y = 5.731, z = 5.214, p26 = -2.370, p27 = -5.124, p28 = 5.298, p29 = -2.625
  Demo 1: a = 0.183, b = -0.918, c = 0.760, d = 0.029, e = 0.965, f = 0.205, g = 0.400, h = 0.245, i = -0.335, j = 0.151, k = 0.014, l = 0.344, m = -0.336, n = 0.328, o = 0.143, p = -0.426, q = 0.372, r = 0.462, s = -0.053, t = 0.068, u = 0.587, v = 0.126, w = 0.791, x = 0.635, y = 0.115, z = -1.739, p26 = 1.141, p27 = 1.713, p28 = -1.081, p29 = 0.491
  Demo 2: a = -5.505, b = 12.446, c = -6.959, d = -19.165, e = -11.805, f = 16.851, g = 11.672, h = 16.776, i = 10.907, j = -5.420, k = 0.021, l = -0.088, m = 0.106, n = 1.194, o = 0.029, p = -0.372, q = 0.214, r = 0.297, s = -0.087, t = 0.121, u = -2.765, v = 6.040, w = 3.266, x = 0.163, y = 5.803, z = -0.787, p26 = 3.826, p27 = 0.281, p28 = 5.959, p29 = -3.210

-- score: -34.70 (accuracy -47.30, token simplicity 6.60, parameter simplicity 6.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.y
diff.y += params.h * data.z
diff.z += params.i
diff.z += params.j * data.x
diff.z += params.k * data.y
diff.z += params.l * data.z
  Demo 0: a = -0.108, b = 0.073, c = 0.008, d = 0.118, e = 0.040, f = -0.004, g = -0.045, h = -0.050, i = 0.082, j = -0.088, k = 0.030, l = -0.083
  Demo 1: a = 0.122, b = -0.169, c = -0.154, d = -0.119, e = -0.185, f = 0.238, g = 0.162, h = 0.184, i = 0.043, j = -0.041, k = 0.004, l = -0.043
  Demo 2: a = 0.428, b = -0.496, c = -0.609, d = -0.415, e = -0.158, f = 0.209, g = 0.112, h = 0.146, i = -0.191, j = 0.194, k = 0.432, l = 0.190

-- score: -33.87 (accuracy -45.37, token simplicity 6.00, parameter simplicity 5.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y -= params.e
diff.y += params.f * data.x
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x
diff.z += params.j * data.y
diff.z += params.k * data.z
  Demo 0: a = -0.108, b = 0.073, c = 0.008, d = 0.118, e = 0.009, f = 0.046, g = 0.000, h = 0.082, i = -0.088, j = 0.030, k = -0.083
  Demo 1: a = 0.122, b = -0.169, c = -0.154, d = -0.119, e = 0.005, f = 0.050, g = 0.011, h = 0.043, i = -0.041, j = 0.004, k = -0.043
  Demo 2: a = 0.428, b = -0.496, c = -0.609, d = -0.415, e = 0.012, f = 0.062, g = 0.034, h = -0.191, i = 0.194, j = 0.432, k = 0.190

## Round 1 | 5.91s | best score: -60.39

+1681 new programs (1681 actually scored)
* linear_fit: +12
* quadratic_fit: +34
* add_single_terms: +104
* delete_interactions: +379
* delete_lines: +184
* delete_near_zeros: +25
* relate_parameters: +890
* snap_to_one: +0
* tie_parameters: +53

### 10 parents for the next round

-- score: -60.39 (accuracy -65.39, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.103
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.050
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.243

-- score: -59.31 (accuracy -65.41, token simplicity 3.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.484, b = -0.002, c = 0.334, d = 0.145, e = 0.103
  Demo 1: a = 0.273, b = -0.003, c = 0.201, d = 0.079, e = 0.050
  Demo 2: a = 0.872, b = 0.022, c = 0.463, d = 0.325, e = 0.243

-- score: -59.17 (accuracy -64.37, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.y * data.y
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.255
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.109
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.880

-- score: -58.10 (accuracy -64.40, token simplicity 3.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.z
diff.z += params.e * data.y * data.y
  Demo 0: a = 0.484, b = -0.002, c = 0.334, d = 0.145, e = 0.255
  Demo 1: a = 0.273, b = -0.003, c = 0.201, d = 0.079, e = 0.109
  Demo 2: a = 0.872, b = 0.022, c = 0.463, d = 0.325, e = 0.880

-- score: -56.67 (accuracy -61.87, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.y * data.z
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.174
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.091
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.446

-- score: -55.98 (accuracy -61.18, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.x * data.z
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.514
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.355
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.518

-- score: -55.59 (accuracy -61.89, token simplicity 3.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.z
diff.z += params.e * data.y * data.z
  Demo 0: a = 0.484, b = -0.002, c = 0.334, d = 0.145, e = 0.174
  Demo 1: a = 0.273, b = -0.003, c = 0.201, d = 0.079, e = 0.091
  Demo 2: a = 0.872, b = 0.022, c = 0.463, d = 0.325, e = 0.446

-- score: -55.28 (accuracy -60.48, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.x * data.y
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.284
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.141
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.588

-- score: -54.90 (accuracy -61.20, token simplicity 3.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.z
diff.z += params.e * data.x * data.z
  Demo 0: a = 0.484, b = -0.002, c = 0.334, d = 0.145, e = 0.514
  Demo 1: a = 0.273, b = -0.003, c = 0.201, d = 0.079, e = 0.355
  Demo 2: a = 0.872, b = 0.022, c = 0.463, d = 0.325, e = 0.518

-- score: -54.63 (accuracy -59.43, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.017
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.010
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.027

## Round 2 | 0.34s | best score: -62.70

+472 new programs (472 actually scored)
* linear_fit: +21
* quadratic_fit: +27
* add_single_terms: +226
* delete_interactions: +103
* delete_lines: +30
* delete_near_zeros: +0
* relate_parameters: +62
* snap_to_one: +0
* tie_parameters: +3

### 10 parents for the next round

-- score: -62.70 (accuracy -67.50, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -61.62 (accuracy -67.52, token simplicity 3.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.e * data.y
  Demo 0: a = 0.484, b = -0.002, c = 0.501, d = 0.101, e = 0.103
  Demo 1: a = 0.273, b = -0.003, c = 0.295, d = 0.052, e = 0.050
  Demo 2: a = 0.872, b = 0.022, c = 0.810, d = 0.251, e = 0.243

-- score: -61.51 (accuracy -67.61, token simplicity 3.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.y += params.d * data.y * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.491, b = 0.518, c = 0.111, d = 0.016, e = 0.103
  Demo 1: a = 0.281, b = 0.335, c = 0.075, d = 0.039, e = 0.050
  Demo 2: a = 0.821, b = 0.842, c = 0.275, d = 0.033, e = 0.243

-- score: -61.49 (accuracy -66.49, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.255
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.109
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.880

-- score: -61.16 (accuracy -67.46, token simplicity 3.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.y
diff.y -= params.d * data.y * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.491, b = 0.404, c = 0.104, d = 0.093, e = 0.103
  Demo 1: a = 0.281, b = 0.259, c = 0.071, d = 0.038, e = 0.050
  Demo 2: a = 0.821, b = 0.564, c = 0.265, d = 0.245, e = 0.243

-- score: -60.68 (accuracy -65.38, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y * data.z
diff.z += params.c * data.y
  Demo 0: a = 0.337, b = 0.146, c = 0.103
  Demo 1: a = 0.201, b = 0.080, c = 0.050
  Demo 2: a = 0.469, b = 0.329, c = 0.243

-- score: -60.44 (accuracy -65.14, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.b * data.y
  Demo 0: a = 0.345, b = 0.105, c = 0.147
  Demo 1: a = 0.212, b = 0.051, c = 0.081
  Demo 2: a = 0.480, b = 0.252, c = 0.332

-- score: -60.43 (accuracy -67.63, token simplicity 4.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.484, b = -0.002, c = 0.518, d = 0.111, e = 0.016, f = 0.103
  Demo 1: a = 0.273, b = -0.003, c = 0.335, d = 0.075, e = 0.039, f = 0.050
  Demo 2: a = 0.872, b = 0.022, c = 0.842, d = 0.275, e = 0.033, f = 0.243

-- score: -60.41 (accuracy -66.51, token simplicity 3.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.e * data.y * data.y
  Demo 0: a = 0.484, b = -0.002, c = 0.501, d = 0.101, e = 0.255
  Demo 1: a = 0.273, b = -0.003, c = 0.295, d = 0.052, e = 0.109
  Demo 2: a = 0.872, b = 0.022, c = 0.810, d = 0.251, e = 0.880

-- score: -60.39 (accuracy -65.39, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.334, c = 0.145, d = 0.103
  Demo 1: a = 0.281, b = 0.201, c = 0.079, d = 0.050
  Demo 2: a = 0.821, b = 0.463, c = 0.325, d = 0.243

## Round 3 | 0.35s | best score: -63.19

+468 new programs (468 actually scored)
* linear_fit: +20
* quadratic_fit: +34
* add_single_terms: +216
* delete_interactions: +94
* delete_lines: +22
* delete_near_zeros: +1
* relate_parameters: +68
* snap_to_one: +0
* tie_parameters: +13

### 10 parents for the next round

-- score: -63.19 (accuracy -67.49, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -63.18 (accuracy -67.48, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -62.70 (accuracy -67.50, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -62.29 (accuracy -66.79, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= (params.a - params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.530, b = 0.100, c = 0.107
  Demo 1: a = 0.313, b = 0.049, c = 0.055
  Demo 2: a = 0.887, b = 0.227, c = 0.275

-- score: -62.14 (accuracy -66.64, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= (params.a - params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.528, b = 0.105, c = 0.103
  Demo 1: a = 0.314, b = 0.054, c = 0.050
  Demo 2: a = 0.879, b = 0.269, c = 0.243

-- score: -62.11 (accuracy -67.51, token simplicity 3.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.484, b = -0.002, c = 0.503, d = 0.102
  Demo 1: a = 0.273, b = -0.003, c = 0.292, d = 0.051
  Demo 2: a = 0.872, b = 0.022, c = 0.802, d = 0.248

-- score: -62.10 (accuracy -66.60, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a - params.b) * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.555, b = 0.092, c = 0.103
  Demo 1: a = 0.308, b = 0.045, c = 0.050
  Demo 2: a = 0.951, b = 0.223, c = 0.243

-- score: -62.08 (accuracy -67.48, token simplicity 3.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.498, b = 0.000, c = 0.100, d = 0.103
  Demo 1: a = 0.287, b = -0.001, c = 0.050, d = 0.050
  Demo 2: a = 0.817, b = 0.005, c = 0.253, d = 0.243

-- score: -62.06 (accuracy -66.56, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.465, b = 0.099, c = 0.094
  Demo 1: a = 0.264, b = 0.048, c = 0.046
  Demo 2: a = 0.739, b = 0.229, c = 0.229

-- score: -61.97 (accuracy -66.47, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.255
  Demo 1: a = 0.288, b = 0.051, c = 0.109
  Demo 2: a = 0.813, b = 0.252, c = 0.880

## Round 4 | 0.30s | best score: -63.67

+397 new programs (397 actually scored)
* linear_fit: +22
* quadratic_fit: +39
* add_single_terms: +219
* delete_interactions: +77
* delete_lines: +20
* delete_near_zeros: +3
* relate_parameters: +15
* snap_to_one: +0
* tie_parameters: +2

### 10 parents for the next round

-- score: -63.67 (accuracy -67.47, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

-- score: -63.19 (accuracy -67.49, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -63.18 (accuracy -67.48, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -62.70 (accuracy -67.50, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -62.61 (accuracy -66.61, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a - params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.526, b = 0.104
  Demo 1: a = 0.309, b = 0.052
  Demo 2: a = 0.859, b = 0.259

-- score: -62.58 (accuracy -67.48, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.001, c = 0.101
  Demo 1: a = 0.287, b = -0.001, c = 0.050
  Demo 2: a = 0.809, b = 0.002, c = 0.250

-- score: -62.57 (accuracy -66.57, token simplicity 3.00, parameter simplicity 1.00) --
diff.x -= (params.a + params.b) * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.470, b = 0.096
  Demo 1: a = 0.266, b = 0.047
  Demo 2: a = 0.739, b = 0.229

-- score: -62.38 (accuracy -67.48, token simplicity 3.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += (params.a - params.b) * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = -0.000, c = 0.101
  Demo 1: a = 0.285, b = -0.002, c = 0.050
  Demo 2: a = 0.818, b = 0.008, c = 0.250

-- score: -62.38 (accuracy -67.48, token simplicity 3.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += (params.c - params.b) * data.y
  Demo 0: a = 0.498, b = -0.001, c = 0.101
  Demo 1: a = 0.287, b = -0.000, c = 0.050
  Demo 2: a = 0.817, b = 0.008, c = 0.253

-- score: -62.38 (accuracy -67.48, token simplicity 3.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.x += params.b * data.y
diff.y += params.a * data.x * data.y
diff.y -= (params.c - params.b) * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.001, c = 0.102
  Demo 1: a = 0.287, b = -0.001, c = 0.050
  Demo 2: a = 0.807, b = -0.003, c = 0.247

## Round 5 | 0.25s | best score: -63.67 (stable)

+305 new programs (305 actually scored)
* linear_fit: +14
* quadratic_fit: +37
* add_single_terms: +176
* delete_interactions: +61
* delete_lines: +15
* delete_near_zeros: +2
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -63.67 (accuracy -67.47, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

-- score: -63.19 (accuracy -67.49, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -63.18 (accuracy -67.48, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -62.99 (accuracy -67.49, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a - params.b) * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = -0.013, c = 0.102
  Demo 1: a = 0.281, b = -0.011, c = 0.051
  Demo 2: a = 0.821, b = 0.019, c = 0.248

-- score: -62.98 (accuracy -67.48, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= (params.b - params.c) * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.498, b = 0.103, c = 0.003
  Demo 1: a = 0.288, b = 0.050, c = -0.001
  Demo 2: a = 0.813, b = 0.243, c = -0.009

-- score: -62.79 (accuracy -67.49, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101, c = -0.000
  Demo 1: a = 0.286, b = 0.049, c = 0.001
  Demo 2: a = 0.810, b = 0.250, c = -0.001

-- score: -62.78 (accuracy -67.48, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.000, c = 0.102
  Demo 1: a = 0.288, b = -0.000, c = 0.050
  Demo 2: a = 0.807, b = 0.000, c = 0.250

-- score: -62.78 (accuracy -67.48, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.000, b = 0.499, c = 0.101
  Demo 1: a = 0.000, b = 0.288, c = 0.050
  Demo 2: a = 0.001, b = 0.804, c = 0.248

-- score: -62.70 (accuracy -67.50, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -62.65 (accuracy -67.55, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.496, b = 0.001, c = 0.101
  Demo 1: a = 0.278, b = 0.004, c = 0.051
  Demo 2: a = 0.820, b = -0.003, c = 0.249

## Round 6 | 0.19s | best score: -63.67 (stable)

+258 new programs (258 actually scored)
* linear_fit: +13
* quadratic_fit: +23
* add_single_terms: +146
* delete_interactions: +58
* delete_lines: +18
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -63.67 (accuracy -67.47, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101
  Demo 1: a = 0.288, b = 0.050
  Demo 2: a = 0.807, b = 0.249

-- score: -63.19 (accuracy -67.49, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = 0.503, c = 0.102
  Demo 1: a = 0.281, b = 0.292, c = 0.051
  Demo 2: a = 0.821, b = 0.802, c = 0.248

-- score: -63.18 (accuracy -67.48, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.103
  Demo 1: a = 0.288, b = 0.051, c = 0.050
  Demo 2: a = 0.813, b = 0.252, c = 0.243

-- score: -62.99 (accuracy -67.49, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += (params.a - params.b) * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.491, b = -0.013, c = 0.102
  Demo 1: a = 0.281, b = -0.011, c = 0.051
  Demo 2: a = 0.821, b = 0.019, c = 0.248

-- score: -62.98 (accuracy -67.48, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= (params.b - params.c) * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.498, b = 0.103, c = 0.003
  Demo 1: a = 0.288, b = 0.050, c = -0.001
  Demo 2: a = 0.813, b = 0.243, c = -0.009

-- score: -62.79 (accuracy -67.49, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.b * data.y
  Demo 0: a = 0.500, b = 0.101, c = -0.000
  Demo 1: a = 0.286, b = 0.049, c = 0.001
  Demo 2: a = 0.810, b = 0.250, c = -0.001

-- score: -62.78 (accuracy -67.48, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.498, b = 0.000, c = 0.102
  Demo 1: a = 0.288, b = -0.000, c = 0.050
  Demo 2: a = 0.807, b = 0.000, c = 0.250

-- score: -62.78 (accuracy -67.48, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.000, b = 0.499, c = 0.101
  Demo 1: a = 0.000, b = 0.288, c = 0.050
  Demo 2: a = 0.001, b = 0.804, c = 0.248

-- score: -62.70 (accuracy -67.50, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -62.65 (accuracy -67.55, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.496, b = 0.001, c = 0.101
  Demo 1: a = 0.278, b = 0.004, c = 0.051
  Demo 2: a = 0.820, b = -0.003, c = 0.249

