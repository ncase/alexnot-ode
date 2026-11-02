# sir

Solved in 9.14 seconds. 4578 programs considered, over 7 rounds.

## Winner

-- score: -158.30 (accuracy -162.10, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101
  Demo 1: a = 0.295, b = 0.050
  Demo 2: a = 0.805, b = 0.250

## Runner-ups

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.497, b = 0.504, c = 0.101
  Demo 1: a = 0.291, b = 0.297, c = 0.051
  Demo 2: a = 0.810, b = 0.803, c = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.100, c = 0.102
  Demo 1: a = 0.295, b = 0.051, c = 0.050
  Demo 2: a = 0.809, b = 0.252, c = 0.247

-- score: -157.41 (accuracy -162.11, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101, c = -0.000
  Demo 1: a = 0.294, b = 0.050, c = 0.000
  Demo 2: a = 0.807, b = 0.251, c = -0.000

-- score: -157.40 (accuracy -162.10, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.501, b = 0.000, c = 0.101
  Demo 1: a = 0.295, b = -0.000, c = 0.050
  Demo 2: a = 0.805, b = 0.000, c = 0.250

# The Search

## Round 0 | 0.03s | best score: -136.86

+42 new programs (42 actually scored)
* linear_fit: +4
* quadratic_fit: +8
* add_single_terms: +30
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -136.86 (accuracy -165.86, token simplicity 17.00, parameter simplicity 12.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.x * data.z
diff.x += params.e * data.y
diff.x += params.f * data.y * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.x += params.i * data.z * data.z
diff.y += params.j
diff.y += params.k * data.x
diff.y += params.l * data.x * data.x
diff.y += params.m * data.x * data.y
diff.y += params.n * data.x * data.z
diff.y += params.o * data.y
diff.y += params.p * data.y * data.y
diff.y += params.q * data.y * data.z
diff.y += params.r * data.z
diff.y += params.s * data.z * data.z
diff.z += params.t
diff.z -= params.u * data.x * data.x
diff.z += params.v * data.y
diff.z += params.w * data.y * data.y
diff.z -= params.x * data.z * data.z
  Demo 0: a = -0.053, b = 0.053, c = 0.214, d = 0.129, e = -0.252, f = 0.240, g = 0.222, h = 0.015, i = -0.014, j = -0.878, k = 1.832, l = -0.954, m = -1.414, n = -1.830, o = 1.772, p = -0.971, q = -1.749, r = 1.635, s = -0.755, t = 0.060, u = 0.064, v = -0.030, w = 0.059, x = 0.059
  Demo 1: a = -0.655, b = 0.672, c = 0.296, d = 0.694, e = 0.630, f = -0.642, g = -0.672, h = 0.041, i = -0.041, j = 0.002, k = 0.239, l = -0.241, m = 0.383, n = -0.045, o = -0.403, p = 0.337, q = 0.439, r = -0.087, s = 0.086, t = 0.035, u = 0.035, v = -0.022, w = 0.026, x = 0.036
  Demo 2: a = 1.200, b = -1.226, c = 7.252, d = -0.749, e = 5.269, f = -5.633, g = -5.208, h = -0.067, i = 0.046, j = 0.125, k = -0.392, l = 0.264, m = 1.385, n = 0.282, o = -0.565, p = 0.258, q = 0.493, r = -0.380, s = 0.267, t = 0.045, u = 0.048, v = 0.147, w = -0.012, x = 0.049

-- score: -135.40 (accuracy -166.40, token simplicity 18.00, parameter simplicity 13.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x -= params.d * data.x * data.y
diff.x += params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.y
diff.x += params.h * data.y * data.z
diff.x += params.i * data.z
diff.y += params.j
diff.y += params.k * data.x
diff.y += params.l * data.x * data.x
diff.y += params.m * data.x * data.y
diff.y += params.n * data.x * data.z
diff.y += params.o * data.y * data.y
diff.y += params.p * data.y * data.z
diff.y += params.q * data.z
diff.y += params.r * data.z * data.z
diff.z += params.s
diff.z += params.t * data.x
diff.z += params.u * data.x * data.x
diff.z += params.v * data.x * data.y
diff.z += params.w * data.y
diff.z += params.x * data.y * data.y
diff.z += params.y * data.z
diff.z += params.z * data.z * data.z
  Demo 0: a = 0.003, b = -0.063, c = 0.060, d = 0.213, e = 0.136, f = -0.245, g = 0.233, h = 0.226, i = -0.002, j = 0.046, k = -0.061, l = 0.014, m = 0.398, n = 0.064, o = -0.124, p = 0.016, q = -0.208, r = 0.162, s = 0.087, t = -0.133, u = 0.040, v = 0.038, w = 0.067, x = -0.013, y = -0.157, z = 0.072
  Demo 1: a = 0.040, b = -0.731, c = 0.707, d = 0.217, e = 0.771, f = 0.547, g = -0.599, h = -0.588, i = -0.041, j = -0.194, k = 0.609, l = -0.414, m = 0.002, n = -0.420, o = 0.130, p = 0.029, q = 0.312, r = -0.117, s = 0.084, t = 0.051, u = -0.139, v = -0.166, w = -0.006, x = -0.043, y = -0.114, z = 0.029
  Demo 2: a = -0.066, b = 1.333, c = -1.293, d = 7.446, e = -0.876, f = 5.470, g = -5.765, h = -5.384, i = 0.046, j = -0.146, k = 0.154, l = -0.011, m = 0.812, n = -0.260, o = -0.034, p = -0.072, q = 0.160, r = -0.002, s = -0.402, t = 0.557, u = -0.152, v = 0.306, w = -0.124, x = 0.481, y = 1.009, z = -0.643

-- score: -135.38 (accuracy -166.98, token simplicity 18.60, parameter simplicity 13.00) --
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
diff.y += params.k * data.x
diff.y += params.l * data.x * data.x
diff.y += params.m * data.x * data.y
diff.y += params.n * data.x * data.z
diff.y -= params.o * data.y
diff.y += params.p * data.y * data.z
diff.y -= params.q * data.z
diff.y += params.r * data.z * data.z
diff.z += params.s
diff.z -= params.t * data.x * data.x
diff.z += params.u * data.x * data.y
diff.z += params.v * data.x * data.z
diff.z += params.w * data.y
diff.z += params.x * data.y * data.y
diff.z += params.y * data.y * data.z
diff.z -= params.z * data.z * data.z
  Demo 0: a = -5.309, b = 10.822, c = -5.511, d = -10.589, e = -10.754, f = 9.886, g = 4.591, h = 9.881, i = 10.603, j = -5.289, k = 0.061, l = -0.063, m = 0.462, n = -0.073, o = 0.089, p = 0.082, q = 0.091, r = 0.092, s = 0.005, t = 0.010, u = -0.242, v = -0.111, w = 0.368, x = -0.224, y = -0.296, z = 0.003
  Demo 1: a = 0.258, b = -1.150, c = 0.907, d = 0.206, e = 1.196, f = 0.107, g = 0.376, h = 0.139, i = -0.486, j = 0.227, k = -0.086, l = 0.094, m = 0.359, n = 0.308, o = 0.061, p = 0.133, q = 0.122, r = 0.123, s = 0.045, t = 0.043, u = 0.030, v = -0.001, w = -0.084, x = 0.079, y = 0.043, z = 0.045
  Demo 2: a = -11.104, b = 23.626, c = -12.531, d = -30.160, e = -23.013, f = 27.808, g = 16.969, h = 27.776, i = 22.111, j = -11.028, k = -0.147, l = 0.145, m = 1.010, n = 0.047, o = 0.185, p = 0.121, q = 0.137, r = 0.148, s = 0.204, t = 0.207, u = 6.423, v = 0.160, w = -6.809, x = 6.681, y = 6.475, z = 0.228

-- score: -132.80 (accuracy -167.50, token simplicity 20.20, parameter simplicity 14.50) --
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
diff.y += params.p * data.y
diff.y += params.q * data.y * data.y
diff.y += params.r * data.y * data.z
diff.y += params.s * data.z
diff.y += params.t * data.z * data.z
diff.z += params.u
diff.z += params.v * data.x
diff.z += params.w * data.x * data.x
diff.z += params.x * data.x * data.y
diff.z += params.y * data.x * data.z
diff.z += params.z * data.y
diff.z += params.p26 * data.y * data.y
diff.z += params.p27 * data.z
diff.z += params.p28 * data.z * data.z
  Demo 0: a = -5.309, b = 10.822, c = -5.511, d = -10.589, e = -10.754, f = 9.886, g = 4.591, h = 9.881, i = 10.603, j = -5.289, k = -0.878, l = 1.832, m = -0.954, n = -1.414, o = -1.830, p = 1.772, q = -0.971, r = -1.749, s = 1.635, t = -0.755, u = 0.142, v = -0.270, w = 0.123, x = 0.055, y = 0.157, z = 0.069, p26 = -0.065, p27 = -0.271, p28 = 0.130
  Demo 1: a = 0.258, b = -1.150, c = 0.907, d = 0.206, e = 1.196, f = 0.107, g = 0.376, h = 0.139, i = -0.486, j = 0.227, k = 0.002, l = 0.239, m = -0.241, n = 0.383, o = -0.045, p = -0.403, q = 0.337, r = 0.439, s = -0.087, t = 0.086, u = -0.230, v = 1.718, w = -1.524, x = -1.064, y = -1.749, z = -0.086, p26 = 0.331, p27 = 0.606, p28 = -0.377
  Demo 2: a = -11.104, b = 23.626, c = -12.531, d = -30.160, e = -23.013, f = 27.808, g = 16.969, h = 27.776, i = 22.111, j = -11.028, k = 0.125, l = -0.392, m = 0.264, n = 1.385, o = 0.282, p = -0.565, q = 0.258, r = 0.493, s = -0.380, t = 0.267, u = -3.048, v = 6.586, w = -3.535, x = -0.160, y = -6.386, z = -0.351, p26 = 3.507, p27 = 6.504, p28 = -3.479

-- score: -131.70 (accuracy -167.70, token simplicity 21.00, parameter simplicity 15.00) --
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
diff.y += params.p * data.y
diff.y += params.q * data.y * data.y
diff.y += params.r * data.y * data.z
diff.y += params.s * data.z
diff.y += params.t * data.z * data.z
diff.z += params.u
diff.z += params.v * data.x
diff.z -= params.w * data.x * data.x
diff.z += params.x * data.x * data.y
diff.z += params.y * data.x * data.z
diff.z += params.z * data.y
diff.z += params.p26 * data.y * data.y
diff.z += params.p27 * data.y * data.z
diff.z += params.p28 * data.z
diff.z += params.p29 * data.z * data.z
  Demo 0: a = -5.309, b = 10.822, c = -5.511, d = -10.589, e = -10.754, f = 9.886, g = 4.591, h = 9.881, i = 10.603, j = -5.289, k = -0.878, l = 1.832, m = -0.954, n = -1.414, o = -1.830, p = 1.772, q = -0.971, r = -1.749, s = 1.635, t = -0.755, u = -5.455, v = 11.192, w = 5.739, x = -10.915, y = -11.310, z = 10.790, p26 = -5.187, p27 = -10.684, p28 = 10.892, p29 = -5.431
  Demo 1: a = 0.258, b = -1.150, c = 0.907, d = 0.206, e = 1.196, f = 0.107, g = 0.376, h = 0.139, i = -0.486, j = 0.227, k = 0.002, l = 0.239, m = -0.241, n = 0.383, o = -0.045, p = -0.403, q = 0.337, r = 0.439, s = -0.087, t = 0.086, u = 1.150, v = -0.888, w = 0.303, x = 1.616, y = 0.896, z = -2.914, p26 = 1.780, p27 = 2.879, p28 = -2.206, p29 = 1.055
  Demo 2: a = -11.104, b = 23.626, c = -12.531, d = -30.160, e = -23.013, f = 27.808, g = 16.969, h = 27.776, i = 22.111, j = -11.028, k = 0.125, l = -0.392, m = 0.264, n = 1.385, o = 0.282, p = -0.565, q = 0.258, r = 0.493, s = -0.380, t = 0.267, u = -5.407, v = 11.340, w = 5.927, x = -5.142, y = -11.099, z = 4.562, p26 = 0.971, p27 = -4.914, p28 = 11.211, p29 = -5.828

-- score: -115.22 (accuracy -119.12, token simplicity 2.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
  Demo 0: a = 0.497, b = 0.335, c = 0.148
  Demo 1: a = 0.291, b = 0.206, c = 0.080
  Demo 2: a = 0.810, b = 0.461, c = 0.328

-- score: -114.02 (accuracy -119.22, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.z
  Demo 0: a = 0.001, b = 0.493, c = 0.335, d = 0.148
  Demo 1: a = 0.003, b = 0.285, c = 0.206, d = 0.080
  Demo 2: a = 0.010, b = 0.775, c = 0.461, d = 0.328

-- score: -89.41 (accuracy -102.01, token simplicity 6.60, parameter simplicity 6.00) --
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
  Demo 0: a = -0.171, b = 0.136, c = 0.073, d = 0.181, e = 0.104, f = -0.068, g = -0.109, h = -0.114, i = 0.084, j = -0.087, k = 0.022, l = -0.085
  Demo 1: a = 0.203, b = -0.251, c = -0.236, d = -0.201, e = -0.264, f = 0.314, g = 0.245, h = 0.263, i = 0.045, j = -0.044, k = 0.004, l = -0.045
  Demo 2: a = 0.531, b = -0.592, c = -0.720, d = -0.518, e = -0.256, f = 0.309, g = 0.208, h = 0.244, i = -0.190, j = 0.191, k = 0.438, l = 0.190

-- score: -88.68 (accuracy -100.18, token simplicity 6.00, parameter simplicity 5.50) --
diff.x -= params.a
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y += params.d
diff.y += params.e * data.x
diff.y += params.f * data.y
diff.y += params.g * data.z
diff.z += params.h
diff.z += params.i * data.x
diff.z += params.j * data.y
diff.z += params.k * data.z
  Demo 0: a = 0.037, b = -0.055, c = 0.046, d = 0.104, e = -0.068, f = -0.109, g = -0.114, h = 0.084, i = -0.087, j = 0.022, k = -0.085
  Demo 1: a = 0.042, b = 0.005, c = 0.047, d = -0.264, e = 0.314, f = 0.245, g = 0.263, h = 0.045, i = -0.044, j = 0.004, k = -0.045
  Demo 2: a = 0.058, b = -0.135, c = 0.069, d = -0.256, e = 0.309, f = 0.208, g = 0.244, h = -0.190, i = 0.191, j = 0.438, k = 0.190

-- score: -84.72 (accuracy -95.32, token simplicity 5.60, parameter simplicity 5.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y += params.e * data.x
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x
diff.z += params.i * data.y
diff.z += params.j * data.z
  Demo 0: a = -0.171, b = 0.136, c = 0.073, d = 0.181, e = 0.040, f = 0.026, g = 0.084, h = -0.087, i = 0.022, j = -0.085
  Demo 1: a = 0.203, b = -0.251, c = -0.236, d = -0.201, e = 0.047, f = 0.023, g = 0.045, h = -0.044, i = 0.004, j = -0.045
  Demo 2: a = 0.531, b = -0.592, c = -0.720, d = -0.518, e = 0.053, f = 0.076, g = -0.190, h = 0.191, i = 0.438, j = 0.190

## Round 1 | 6.71s | best score: -153.31

+1997 new programs (1997 actually scored)
* linear_fit: +14
* quadratic_fit: +36
* add_single_terms: +117
* delete_interactions: +353
* delete_lines: +172
* delete_near_zeros: +23
* relate_parameters: +1226
* snap_to_one: +0
* tie_parameters: +56

### 10 parents for the next round

-- score: -153.31 (accuracy -162.51, token simplicity 5.20, parameter simplicity 4.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.y += params.d * data.y * data.z
diff.z += params.e
diff.z += params.f * data.x
diff.z += params.g * data.y
diff.z += params.h * data.z
  Demo 0: a = 0.497, b = 0.516, c = 0.109, d = 0.013, e = 0.084, f = -0.087, g = 0.022, h = -0.085
  Demo 1: a = 0.291, b = 0.316, c = 0.061, d = 0.016, e = 0.045, f = -0.044, g = 0.004, h = -0.045
  Demo 2: a = 0.810, b = 0.815, c = 0.256, d = 0.006, e = -0.190, f = 0.191, g = 0.438, h = 0.190

-- score: -152.31 (accuracy -162.61, token simplicity 5.80, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.z
diff.z += params.f
diff.z += params.g * data.x
diff.z += params.h * data.y
diff.z += params.i * data.z
  Demo 0: a = 0.001, b = 0.491, c = 0.516, d = 0.109, e = 0.013, f = 0.084, g = -0.087, h = 0.022, i = -0.085
  Demo 1: a = 0.003, b = 0.280, c = 0.316, d = 0.061, e = 0.016, f = 0.045, g = -0.044, h = 0.004, i = -0.045
  Demo 2: a = 0.010, b = 0.758, c = 0.815, d = 0.256, e = 0.006, f = -0.190, g = 0.191, h = 0.438, i = 0.190

-- score: -152.11 (accuracy -162.61, token simplicity 6.00, parameter simplicity 4.50) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.z
diff.z += params.f
diff.z += params.g * data.x
diff.z += params.h * data.y
diff.z += params.i * data.z
  Demo 0: a = 0.001, b = 0.493, c = 0.516, d = 0.109, e = 0.013, f = 0.084, g = -0.087, h = 0.022, i = -0.085
  Demo 1: a = 0.003, b = 0.285, c = 0.316, d = 0.061, e = 0.016, f = 0.045, g = -0.044, h = 0.004, i = -0.045
  Demo 2: a = 0.010, b = 0.775, c = 0.815, d = 0.256, e = 0.006, f = -0.190, g = 0.191, h = 0.438, i = 0.190

-- score: -150.15 (accuracy -163.55, token simplicity 7.40, parameter simplicity 6.00) --
diff.x -= params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y += params.e * data.x * data.y
diff.y += params.f * data.y
diff.y += params.g * data.y * data.z
diff.y += params.h * data.z
diff.z += params.i
diff.z += params.j * data.x
diff.z += params.k * data.y
diff.z += params.l * data.z
  Demo 0: a = 0.001, b = 0.491, c = 0.001, d = -0.001, e = 0.519, f = -0.111, g = 0.015, h = -0.001, i = 0.084, j = -0.087, k = 0.022, l = -0.085
  Demo 1: a = 0.003, b = 0.280, c = -0.126, d = 0.133, e = 0.273, f = 0.075, g = 0.000, h = 0.126, i = 0.045, j = -0.044, k = 0.004, l = -0.045
  Demo 2: a = 0.010, b = 0.758, c = -0.057, d = 0.055, e = 0.841, f = -0.209, g = 0.013, h = 0.058, i = -0.190, j = 0.191, k = 0.438, l = 0.190

-- score: -150.11 (accuracy -155.11, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.497, b = 0.335, c = 0.148, d = 0.102
  Demo 1: a = 0.291, b = 0.206, c = 0.080, d = 0.050
  Demo 2: a = 0.810, b = 0.461, c = 0.328, d = 0.247

-- score: -149.44 (accuracy -163.54, token simplicity 7.60, parameter simplicity 6.50) --
diff.x -= params.a
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.x * data.y
diff.y += params.h * data.y
diff.y += params.i * data.z
diff.z += params.j
diff.z += params.k * data.x
diff.z += params.l * data.y
diff.z += params.m * data.z
  Demo 0: a = 0.002, b = 0.486, c = 0.001, d = 0.002, e = 0.001, f = -0.001, g = 0.503, h = -0.102, i = -0.001, j = 0.084, k = -0.087, l = 0.022, m = -0.085
  Demo 1: a = 0.003, b = 0.273, c = 0.001, d = 0.004, e = -0.126, f = 0.133, g = 0.273, h = 0.075, i = 0.127, j = 0.045, k = -0.044, l = 0.004, m = -0.045
  Demo 2: a = 0.008, b = 0.776, c = 0.012, d = 0.008, e = -0.057, f = 0.055, g = 0.826, h = -0.199, i = 0.058, j = -0.190, k = 0.191, l = 0.438, m = 0.190

-- score: -148.91 (accuracy -155.21, token simplicity 3.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.001, b = 0.493, c = 0.335, d = 0.148, e = 0.102
  Demo 1: a = 0.003, b = 0.285, c = 0.206, d = 0.080, e = 0.050
  Demo 2: a = 0.010, b = 0.775, c = 0.461, d = 0.328, e = 0.247

-- score: -148.81 (accuracy -164.01, token simplicity 8.20, parameter simplicity 7.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.z
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.y
diff.y += params.i * data.y
diff.y += params.j * data.z
diff.z += params.k
diff.z += params.l * data.x
diff.z += params.m * data.y
diff.z += params.n * data.z
  Demo 0: a = -0.072, b = 0.071, c = 0.482, d = 0.067, e = 0.072, f = 0.001, g = -0.001, h = 0.503, i = -0.102, j = -0.001, k = 0.084, l = -0.087, m = 0.022, n = -0.085
  Demo 1: a = 0.071, b = -0.077, c = 0.261, d = -0.073, e = -0.071, f = -0.126, g = 0.133, h = 0.273, i = 0.075, j = 0.127, k = 0.045, l = -0.044, m = 0.004, n = -0.045
  Demo 2: a = 0.358, b = -0.372, c = 0.718, d = -0.367, e = -0.356, f = -0.057, g = 0.055, h = 0.826, i = -0.199, j = 0.058, k = -0.190, l = 0.191, m = 0.438, n = 0.190

-- score: -147.71 (accuracy -163.51, token simplicity 8.80, parameter simplicity 7.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.z
diff.y += params.f * data.x
diff.y -= params.g * data.x * data.x
diff.y += params.h * data.x * data.y
diff.y -= params.i * data.y
diff.y += params.j * data.y * data.z
diff.z += params.k
diff.z += params.l * data.x
diff.z += params.m * data.y
diff.z += params.n * data.z
  Demo 0: a = -0.072, b = 0.071, c = 0.482, d = 0.067, e = 0.072, f = 0.051, g = 0.051, h = 0.464, i = 0.119, j = 0.021, k = 0.084, l = -0.087, m = 0.022, n = -0.085
  Demo 1: a = 0.071, b = -0.077, c = 0.261, d = -0.073, e = -0.071, f = 0.150, g = 0.149, h = 0.142, i = 0.072, j = 0.024, k = 0.045, l = -0.044, m = 0.004, n = -0.045
  Demo 2: a = 0.358, b = -0.372, c = 0.718, d = -0.367, e = -0.356, f = 0.001, g = 0.003, h = 0.859, i = 0.280, j = 0.033, k = -0.190, l = 0.191, m = 0.438, n = 0.190

-- score: -147.62 (accuracy -164.32, token simplicity 9.20, parameter simplicity 7.50) --
diff.x += params.a
diff.x += params.b * data.x * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.x += params.e * data.z
diff.y += params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.y
diff.y += params.i * data.y
diff.y += params.j * data.y * data.z
diff.y += params.k * data.z
diff.z += params.l
diff.z += params.m * data.x
diff.z += params.n * data.y
diff.z += params.o * data.z
  Demo 0: a = -0.057, b = 0.056, c = 0.415, d = 0.057, e = 0.057, f = 0.001, g = -0.001, h = 0.519, i = -0.111, j = 0.015, k = -0.001, l = 0.084, m = -0.087, n = 0.022, o = -0.085
  Demo 1: a = 0.074, b = -0.080, c = 0.356, d = -0.080, e = -0.074, f = -0.126, g = 0.133, h = 0.273, i = 0.075, j = 0.000, k = 0.126, l = 0.045, m = -0.044, n = 0.004, o = -0.045
  Demo 2: a = 0.493, b = -0.508, c = 1.334, d = -0.610, e = -0.513, f = -0.057, g = 0.055, h = 0.841, i = -0.209, j = 0.013, k = 0.058, l = -0.190, m = 0.191, n = 0.438, o = 0.190

## Round 2 | 1.23s | best score: -157.33

+1026 new programs (1026 actually scored)
* linear_fit: +22
* quadratic_fit: +54
* add_single_terms: +191
* delete_interactions: +198
* delete_lines: +93
* delete_near_zeros: +14
* relate_parameters: +393
* snap_to_one: +0
* tie_parameters: +61

### 10 parents for the next round

-- score: -157.33 (accuracy -162.13, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.497, b = 0.503, c = 0.101, d = 0.102
  Demo 1: a = 0.291, b = 0.299, c = 0.051, d = 0.050
  Demo 2: a = 0.810, b = 0.809, c = 0.252, d = 0.247

-- score: -156.13 (accuracy -162.23, token simplicity 3.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.e * data.y
  Demo 0: a = 0.001, b = 0.493, c = 0.503, d = 0.101, e = 0.102
  Demo 1: a = 0.003, b = 0.285, c = 0.299, d = 0.051, e = 0.050
  Demo 2: a = 0.010, b = 0.775, c = 0.809, d = 0.252, e = 0.247

-- score: -156.12 (accuracy -162.22, token simplicity 3.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.y += params.d * data.y * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.497, b = 0.516, c = 0.109, d = 0.013, e = 0.102
  Demo 1: a = 0.291, b = 0.316, c = 0.061, d = 0.016, e = 0.050
  Demo 2: a = 0.810, b = 0.815, c = 0.256, d = 0.006, e = 0.247

-- score: -155.79 (accuracy -162.09, token simplicity 3.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y * data.y
diff.y -= params.d * data.y * data.z
diff.z += params.e * data.y
  Demo 0: a = 0.497, b = 0.404, c = 0.103, d = 0.097, e = 0.102
  Demo 1: a = 0.291, b = 0.255, c = 0.060, d = 0.045, e = 0.050
  Demo 2: a = 0.810, b = 0.558, c = 0.255, d = 0.250, e = 0.247

-- score: -155.11 (accuracy -162.31, token simplicity 4.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.001, b = 0.491, c = 0.516, d = 0.109, e = 0.013, f = 0.102
  Demo 1: a = 0.003, b = 0.280, c = 0.316, d = 0.061, e = 0.016, f = 0.050
  Demo 2: a = 0.010, b = 0.758, c = 0.815, d = 0.256, e = 0.006, f = 0.247

-- score: -155.05 (accuracy -162.25, token simplicity 4.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.y += params.d * data.y * data.z
diff.z += params.e * data.x
diff.z += params.f * data.y
  Demo 0: a = 0.497, b = 0.516, c = 0.109, d = 0.013, e = -0.002, f = 0.103
  Demo 1: a = 0.291, b = 0.316, c = 0.061, d = 0.016, e = 0.002, f = 0.049
  Demo 2: a = 0.810, b = 0.815, c = 0.256, d = 0.006, e = 0.000, f = 0.247

-- score: -154.92 (accuracy -162.32, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.y += params.e * data.y * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.001, b = 0.493, c = 0.516, d = 0.109, e = 0.013, f = 0.102
  Demo 1: a = 0.003, b = 0.285, c = 0.316, d = 0.061, e = 0.016, f = 0.050
  Demo 2: a = 0.010, b = 0.775, c = 0.815, d = 0.256, e = 0.006, f = 0.247

-- score: -154.59 (accuracy -162.19, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y * data.y
diff.y -= params.e * data.y * data.z
diff.z += params.f * data.y
  Demo 0: a = 0.001, b = 0.493, c = 0.404, d = 0.103, e = 0.097, f = 0.102
  Demo 1: a = 0.003, b = 0.285, c = 0.255, d = 0.060, e = 0.045, f = 0.050
  Demo 2: a = 0.010, b = 0.775, c = 0.558, d = 0.255, e = 0.250, f = 0.247

-- score: -154.52 (accuracy -162.42, token simplicity 4.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d
diff.z += params.e * data.x
diff.z += params.f * data.y
diff.z += params.g * data.z
  Demo 0: a = 0.497, b = 0.503, c = 0.101, d = 0.084, e = -0.087, f = 0.022, g = -0.085
  Demo 1: a = 0.291, b = 0.299, c = 0.051, d = 0.045, e = -0.044, f = 0.004, g = -0.045
  Demo 2: a = 0.810, b = 0.809, c = 0.252, d = -0.190, e = 0.191, f = 0.438, g = 0.190

-- score: -154.17 (accuracy -162.27, token simplicity 4.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.y += params.d * data.y * data.z
diff.z += params.e
diff.z += params.f * data.x
diff.z += params.g * data.y
  Demo 0: a = 0.497, b = 0.516, c = 0.109, d = 0.013, e = -0.000, f = -0.002, g = 0.103
  Demo 1: a = 0.291, b = 0.316, c = 0.061, d = 0.016, e = 0.001, f = 0.001, g = 0.048
  Demo 2: a = 0.810, b = 0.815, c = 0.256, d = 0.006, e = -0.000, f = 0.000, g = 0.248

## Round 3 | 0.49s | best score: -157.81

+671 new programs (671 actually scored)
* linear_fit: +27
* quadratic_fit: +48
* add_single_terms: +223
* delete_interactions: +133
* delete_lines: +33
* delete_near_zeros: +0
* relate_parameters: +181
* snap_to_one: +0
* tie_parameters: +26

### 10 parents for the next round

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.497, b = 0.504, c = 0.101
  Demo 1: a = 0.291, b = 0.297, c = 0.051
  Demo 2: a = 0.810, b = 0.803, c = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.100, c = 0.102
  Demo 1: a = 0.295, b = 0.051, c = 0.050
  Demo 2: a = 0.809, b = 0.252, c = 0.247

-- score: -157.33 (accuracy -162.13, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.497, b = 0.503, c = 0.101, d = 0.102
  Demo 1: a = 0.291, b = 0.299, c = 0.051, d = 0.050
  Demo 2: a = 0.810, b = 0.809, c = 0.252, d = 0.247

-- score: -156.62 (accuracy -162.22, token simplicity 3.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.001, b = 0.493, c = 0.504, d = 0.101
  Demo 1: a = 0.003, b = 0.285, c = 0.297, d = 0.051
  Demo 2: a = 0.010, b = 0.775, c = 0.803, d = 0.250

-- score: -156.55 (accuracy -162.15, token simplicity 3.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.001, b = 0.499, c = 0.100, d = 0.102
  Demo 1: a = 0.001, b = 0.294, c = 0.050, d = 0.050
  Demo 2: a = 0.008, b = 0.798, c = 0.249, d = 0.247

-- score: -156.53 (accuracy -162.13, token simplicity 3.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.y += params.d * data.y * data.z
diff.z += params.c * data.y
  Demo 0: a = 0.497, b = 0.504, c = 0.102, d = 0.002
  Demo 1: a = 0.291, b = 0.297, c = 0.051, d = 0.000
  Demo 2: a = 0.810, b = 0.803, c = 0.248, d = -0.005

-- score: -156.51 (accuracy -162.11, token simplicity 3.60, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.y += params.c * data.y * data.z
diff.z += params.d * data.y
  Demo 0: a = 0.501, b = 0.101, c = 0.001, d = 0.102
  Demo 1: a = 0.297, b = 0.052, c = 0.003, d = 0.050
  Demo 2: a = 0.811, b = 0.253, c = 0.003, d = 0.247

-- score: -156.45 (accuracy -162.15, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d
diff.z += params.e * data.y
  Demo 0: a = 0.497, b = 0.503, c = 0.101, d = -0.000, e = 0.103
  Demo 1: a = 0.291, b = 0.299, c = 0.051, d = 0.001, e = 0.048
  Demo 2: a = 0.810, b = 0.809, c = 0.252, d = -0.000, e = 0.248

-- score: -156.44 (accuracy -162.14, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.e * data.y
  Demo 0: a = 0.497, b = 0.000, c = 0.503, d = 0.102, e = 0.102
  Demo 1: a = 0.291, b = 0.000, c = 0.299, d = 0.051, e = 0.050
  Demo 2: a = 0.810, b = 0.000, c = 0.809, d = 0.253, e = 0.247

-- score: -156.43 (accuracy -162.13, token simplicity 3.20, parameter simplicity 2.50) --
diff.x -= params.a
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.e * data.y
  Demo 0: a = 0.000, b = 0.494, c = 0.503, d = 0.101, e = 0.102
  Demo 1: a = 0.000, b = 0.290, c = 0.299, d = 0.051, e = 0.050
  Demo 2: a = 0.000, b = 0.806, c = 0.809, d = 0.252, e = 0.247

## Round 4 | 0.32s | best score: -158.30

+475 new programs (475 actually scored)
* linear_fit: +40
* quadratic_fit: +41
* add_single_terms: +204
* delete_interactions: +86
* delete_lines: +23
* delete_near_zeros: +1
* relate_parameters: +75
* snap_to_one: +0
* tie_parameters: +5

### 10 parents for the next round

-- score: -158.30 (accuracy -162.10, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101
  Demo 1: a = 0.295, b = 0.050
  Demo 2: a = 0.805, b = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.497, b = 0.504, c = 0.101
  Demo 1: a = 0.291, b = 0.297, c = 0.051
  Demo 2: a = 0.810, b = 0.803, c = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.100, c = 0.102
  Demo 1: a = 0.295, b = 0.051, c = 0.050
  Demo 2: a = 0.809, b = 0.252, c = 0.247

-- score: -157.33 (accuracy -162.13, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.497, b = 0.503, c = 0.101, d = 0.102
  Demo 1: a = 0.291, b = 0.299, c = 0.051, d = 0.050
  Demo 2: a = 0.810, b = 0.809, c = 0.252, d = 0.247

-- score: -157.05 (accuracy -162.15, token simplicity 3.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.001, b = 0.501, c = 0.101
  Demo 1: a = 0.001, b = 0.294, c = 0.050
  Demo 2: a = 0.008, b = 0.797, c = 0.248

-- score: -157.00 (accuracy -162.10, token simplicity 3.60, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.y += params.c * data.y * data.z
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.102, c = 0.002
  Demo 1: a = 0.295, b = 0.050, c = 0.000
  Demo 2: a = 0.805, b = 0.248, c = -0.005

-- score: -156.93 (accuracy -162.13, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.d * data.y
  Demo 0: a = 0.500, b = 0.100, c = -0.000, d = 0.103
  Demo 1: a = 0.295, b = 0.051, c = 0.001, d = 0.048
  Demo 2: a = 0.809, b = 0.252, c = -0.000, d = 0.248

-- score: -156.92 (accuracy -162.12, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.497, b = 0.000, c = 0.503, d = 0.102
  Demo 1: a = 0.291, b = -0.000, c = 0.298, d = 0.050
  Demo 2: a = 0.810, b = 0.000, c = 0.803, d = 0.250

-- score: -156.92 (accuracy -162.12, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d
diff.z += params.c * data.y
  Demo 0: a = 0.497, b = 0.505, c = 0.102, d = -0.000
  Demo 1: a = 0.291, b = 0.296, c = 0.050, d = 0.000
  Demo 2: a = 0.810, b = 0.806, c = 0.251, d = -0.000

-- score: -156.92 (accuracy -162.12, token simplicity 3.20, parameter simplicity 2.00) --
diff.x -= params.a
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.000, b = 0.494, c = 0.504, d = 0.101
  Demo 1: a = 0.000, b = 0.290, c = 0.297, d = 0.051
  Demo 2: a = 0.000, b = 0.806, c = 0.803, d = 0.250

## Round 5 | 0.20s | best score: -158.30 (stable)

+307 new programs (307 actually scored)
* linear_fit: +30
* quadratic_fit: +27
* add_single_terms: +160
* delete_interactions: +54
* delete_lines: +7
* delete_near_zeros: +0
* relate_parameters: +28
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -158.30 (accuracy -162.10, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101
  Demo 1: a = 0.295, b = 0.050
  Demo 2: a = 0.805, b = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.497, b = 0.504, c = 0.101
  Demo 1: a = 0.291, b = 0.297, c = 0.051
  Demo 2: a = 0.810, b = 0.803, c = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.100, c = 0.102
  Demo 1: a = 0.295, b = 0.051, c = 0.050
  Demo 2: a = 0.809, b = 0.252, c = 0.247

-- score: -157.41 (accuracy -162.11, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101, c = -0.000
  Demo 1: a = 0.294, b = 0.050, c = 0.000
  Demo 2: a = 0.807, b = 0.251, c = -0.000

-- score: -157.40 (accuracy -162.10, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.501, b = 0.000, c = 0.101
  Demo 1: a = 0.295, b = -0.000, c = 0.050
  Demo 2: a = 0.805, b = 0.000, c = 0.250

-- score: -157.40 (accuracy -162.10, token simplicity 3.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = -0.000, b = 0.501, c = 0.101
  Demo 1: a = 0.000, b = 0.295, c = 0.050
  Demo 2: a = -0.000, b = 0.804, c = 0.250

-- score: -157.33 (accuracy -162.13, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.497, b = 0.503, c = 0.101, d = 0.102
  Demo 1: a = 0.291, b = 0.299, c = 0.051, d = 0.050
  Demo 2: a = 0.810, b = 0.809, c = 0.252, d = 0.247

-- score: -157.26 (accuracy -162.16, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.000, c = 0.101
  Demo 1: a = 0.290, b = 0.002, c = 0.050
  Demo 2: a = 0.811, b = -0.001, c = 0.250

-- score: -157.22 (accuracy -162.12, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.000, b = 0.501, c = 0.101
  Demo 1: a = 0.000, b = 0.294, c = 0.050
  Demo 2: a = 0.005, b = 0.796, c = 0.248

-- score: -157.22 (accuracy -162.12, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.x
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101, c = -0.001
  Demo 1: a = 0.294, b = 0.050, c = 0.001
  Demo 2: a = 0.806, b = 0.250, c = -0.001

## Round 6 | 0.15s | best score: -158.30 (stable)

+241 new programs (241 actually scored)
* linear_fit: +23
* quadratic_fit: +19
* add_single_terms: +127
* delete_interactions: +56
* delete_lines: +16
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -158.30 (accuracy -162.10, token simplicity 2.80, parameter simplicity 1.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101
  Demo 1: a = 0.295, b = 0.050
  Demo 2: a = 0.805, b = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.497, b = 0.504, c = 0.101
  Demo 1: a = 0.291, b = 0.297, c = 0.051
  Demo 2: a = 0.810, b = 0.803, c = 0.250

-- score: -157.81 (accuracy -162.11, token simplicity 2.80, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.100, c = 0.102
  Demo 1: a = 0.295, b = 0.051, c = 0.050
  Demo 2: a = 0.809, b = 0.252, c = 0.247

-- score: -157.41 (accuracy -162.11, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101, c = -0.000
  Demo 1: a = 0.294, b = 0.050, c = 0.000
  Demo 2: a = 0.807, b = 0.251, c = -0.000

-- score: -157.40 (accuracy -162.10, token simplicity 3.20, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.501, b = 0.000, c = 0.101
  Demo 1: a = 0.295, b = -0.000, c = 0.050
  Demo 2: a = 0.805, b = 0.000, c = 0.250

-- score: -157.40 (accuracy -162.10, token simplicity 3.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = -0.000, b = 0.501, c = 0.101
  Demo 1: a = 0.000, b = 0.295, c = 0.050
  Demo 2: a = -0.000, b = 0.804, c = 0.250

-- score: -157.33 (accuracy -162.13, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.497, b = 0.503, c = 0.101, d = 0.102
  Demo 1: a = 0.291, b = 0.299, c = 0.051, d = 0.050
  Demo 2: a = 0.810, b = 0.809, c = 0.252, d = 0.247

-- score: -157.26 (accuracy -162.16, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x
diff.y += params.a * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.500, b = 0.000, c = 0.101
  Demo 1: a = 0.290, b = 0.002, c = 0.050
  Demo 2: a = 0.811, b = -0.001, c = 0.250

-- score: -157.22 (accuracy -162.12, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.c * data.y
  Demo 0: a = 0.000, b = 0.501, c = 0.101
  Demo 1: a = 0.000, b = 0.294, c = 0.050
  Demo 2: a = 0.005, b = 0.796, c = 0.248

-- score: -157.22 (accuracy -162.12, token simplicity 3.40, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.x
diff.z += params.b * data.y
  Demo 0: a = 0.502, b = 0.101, c = -0.001
  Demo 1: a = 0.294, b = 0.050, c = 0.001
  Demo 2: a = 0.806, b = 0.250, c = -0.001

