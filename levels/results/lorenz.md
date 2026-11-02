# lorenz

Solved in 11.63 seconds. 6250 programs considered, over 11 rounds.

## Winner

-- score: -385.86 (accuracy -392.76, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = 1.052, e = 3.690

## Runner-ups

-- score: -385.77 (accuracy -392.87, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = 1.052, e = 3.690

-- score: -385.66 (accuracy -392.76, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 0.046, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 0.008, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -0.033, e = 3.690

-- score: -385.66 (accuracy -392.76, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= (params.c * params.d) * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.046, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.008, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 0.969, d = 1.052, e = 3.690

-- score: -385.66 (accuracy -393.26, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 1.011, f = 2.650
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = 1.028, f = 2.042
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = 1.052, f = 3.690

# The Search

## Round 0 | 0.04s | best score: -374.75

+38 new programs (38 actually scored)
* linear_fit: +2
* quadratic_fit: +6
* add_single_terms: +30
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -374.75 (accuracy -397.75, token simplicity 13.00, parameter simplicity 10.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.z
diff.y -= params.h
diff.y += params.i * data.x
diff.y += params.j * data.x * data.x
diff.y -= params.k * data.x * data.z
diff.y += params.l * data.y
diff.y += params.m * data.y * data.z
diff.y += params.n * data.z
diff.z += params.o
diff.z += params.p * data.x
diff.z += params.q * data.x * data.x
diff.z += params.r * data.x * data.y
diff.z += params.s * data.y
diff.z -= params.t * data.z
  Demo 0: a = 3.021, b = 9.201, c = 0.118, d = -0.035, e = -0.035, f = 9.584, g = -0.216, h = 12.016, i = 29.348, j = -0.071, k = 1.022, l = 0.645, m = -0.062, n = 0.492, o = 5.794, p = 0.175, q = 0.096, r = 0.959, s = -0.225, t = 3.001
  Demo 1: a = 3.790, b = 12.378, c = 0.057, d = -0.014, e = -0.034, f = 13.449, g = -0.194, h = 4.019, i = 48.101, j = 0.011, k = 1.312, l = -8.936, m = 0.183, n = 0.162, o = -18.892, p = 0.015, q = -0.224, r = 1.195, s = 0.116, t = 1.318
  Demo 2: a = -7.456, b = 9.046, c = -0.090, d = 0.026, e = 0.008, f = 8.597, g = 0.455, h = 1.084, i = 41.915, j = 0.002, k = 1.039, l = -1.526, m = 0.010, n = -0.044, o = -19.289, p = 0.079, q = -0.170, r = 1.133, s = -0.247, t = 2.758

-- score: -373.63 (accuracy -400.93, token simplicity 15.80, parameter simplicity 11.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
diff.x += params.c * data.x * data.y
diff.x -= params.d * data.x * data.z
diff.x += params.e * data.y
diff.x -= params.f * data.y * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y -= params.i
diff.y += params.j * data.x
diff.y += params.k * data.x * data.x
diff.y -= params.l * data.x * data.z
diff.y += params.m * data.y
diff.y += params.n * data.y * data.y
diff.y += params.o * data.y * data.z
diff.y += params.p * data.z
diff.z -= params.q
diff.z -= params.r * data.x
diff.z -= params.s * data.x * data.x
diff.z += params.t * data.x * data.y
diff.z += params.u * data.y
diff.z += params.v * data.y * data.y
diff.z -= params.w * data.z
  Demo 0: a = -6.683, b = 0.158, c = -0.022, d = 0.132, e = 8.728, f = 0.058, g = 0.053, h = -0.114, i = 9.121, j = 27.340, k = -0.142, l = 0.941, m = 0.951, n = 0.053, o = -0.089, p = 0.412, q = 1.467, r = 0.546, s = 0.002, t = 1.137, u = 0.930, v = -0.124, w = 2.621
  Demo 1: a = 6.096, b = -0.057, c = 0.351, d = 0.446, e = 2.195, f = 0.221, g = 0.249, h = 0.053, i = 0.447, j = 50.018, k = 0.047, l = 1.356, m = -10.005, n = -0.025, o = 0.207, p = 0.046, q = 18.727, r = 0.094, s = 0.171, t = 1.080, u = 0.161, v = 0.060, w = 1.354
  Demo 2: a = -6.578, b = -0.053, c = 0.030, d = 0.045, e = 6.890, f = 0.013, g = 0.044, h = 0.134, i = 4.187, j = 42.011, k = -0.016, l = 1.041, m = -1.591, n = 0.007, o = 0.011, p = 0.076, q = 20.046, r = 0.016, s = 0.205, t = 1.200, u = -0.218, v = -0.034, w = 2.639

-- score: -370.70 (accuracy -404.10, token simplicity 19.40, parameter simplicity 14.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.x += params.i * data.z * data.z
diff.y += params.j
diff.y += params.k * data.x
diff.y += params.l * data.x * data.x
diff.y += params.m * data.x * data.y
diff.y -= params.n * data.x * data.z
diff.y -= params.o * data.y
diff.y += params.p * data.y * data.y
diff.y += params.q * data.y * data.z
diff.y += params.r * data.z
diff.y += params.s * data.z * data.z
diff.z += params.t
diff.z -= params.u * data.x
diff.z += params.v * data.x * data.x
diff.z += params.w * data.x * data.y
diff.z += params.x * data.y
diff.z += params.y * data.y * data.y
diff.z += params.z * data.y * data.z
diff.z += params.p26 * data.z
diff.z += params.p27 * data.z * data.z
  Demo 0: a = -3.214, b = -6.848, c = 0.205, d = -0.149, e = 0.091, f = 8.216, g = 0.063, h = 0.549, i = -0.026, j = -10.056, k = 28.494, l = -0.061, m = -0.310, n = 0.900, o = 0.983, p = 0.190, q = -0.026, r = 1.112, s = -0.039, t = 7.071, u = 2.891, v = -0.172, w = 1.470, x = 3.298, y = -0.236, z = -0.078, p26 = -4.143, p27 = 0.060
  Demo 1: a = -22.341, b = 14.947, c = 0.477, d = -0.333, e = 0.657, f = -3.732, g = 0.392, h = 2.670, i = -0.062, j = -13.139, k = 55.357, l = 0.420, m = -0.585, n = 1.494, o = 13.986, p = 0.213, q = 0.313, r = 1.295, s = -0.029, t = -8.627, u = 0.742, v = -0.134, w = 0.932, x = -0.923, y = 0.152, z = 0.049, p26 = -2.049, p27 = 0.011
  Demo 2: a = 35.738, b = -3.613, c = -0.516, d = 0.218, e = 0.107, f = 5.752, g = 0.068, h = -3.692, i = 0.094, j = 53.043, k = 45.434, l = -0.403, m = 0.067, n = 1.108, o = 2.728, p = 0.076, q = 0.033, r = -5.149, s = 0.108, t = -51.314, u = 0.291, v = 0.001, w = 1.151, x = -1.032, y = -0.063, z = 0.027, p26 = 0.121, p27 = -0.057

-- score: -370.39 (accuracy -403.79, token simplicity 19.40, parameter simplicity 14.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.y
diff.x += params.h * data.y * data.z
diff.x += params.i * data.z
diff.x += params.j * data.z * data.z
diff.y += params.k
diff.y += params.l * data.x
diff.y += params.m * data.x * data.x
diff.y += params.n * data.x * data.y
diff.y -= params.o * data.x * data.z
diff.y -= params.p * data.y
diff.y += params.q * data.y * data.y
diff.y += params.r * data.y * data.z
diff.y += params.s * data.z
diff.y += params.t * data.z * data.z
diff.z += params.u
diff.z -= params.v * data.x
diff.z -= params.w * data.x * data.x
diff.z += params.x * data.x * data.y
diff.z += params.y * data.y
diff.z += params.z * data.y * data.y
diff.z -= params.p26 * data.z
diff.z += params.p27 * data.z * data.z
  Demo 0: a = -5.090, b = -7.205, c = 0.202, d = -0.070, e = 0.099, f = 8.829, g = -0.042, h = 0.042, i = 0.594, j = -0.022, k = -10.056, l = 28.494, m = -0.061, n = -0.310, o = 0.900, p = 0.983, q = 0.190, r = -0.026, s = 1.112, t = -0.039, u = 14.889, v = 1.375, w = 0.201, x = 1.281, y = 1.415, z = -0.139, p26 = 4.660, p27 = 0.061
  Demo 1: a = -16.742, b = 13.027, c = 0.308, d = -0.035, e = 0.605, f = -2.088, g = -0.135, h = 0.345, i = 2.168, j = -0.050, k = -13.139, l = 55.357, m = 0.420, n = -0.585, o = 1.494, p = 13.986, q = 0.213, r = 0.313, s = 1.295, t = -0.029, u = -34.427, v = 0.121, w = 0.083, x = 0.978, y = 0.216, z = 0.087, p26 = 0.108, p27 = -0.023
  Demo 2: a = 52.655, b = -2.420, c = -0.612, d = 0.194, e = 0.129, f = 5.358, g = 0.044, h = 0.075, i = -5.306, j = 0.126, k = 53.043, l = 45.434, m = -0.403, n = 0.067, o = 1.108, p = 2.728, q = 0.076, r = 0.033, s = -5.149, t = 0.108, u = -34.597, v = 0.013, w = 0.094, x = 1.169, y = -0.240, z = -0.045, p26 = 1.348, p27 = -0.028

-- score: -368.92 (accuracy -404.92, token simplicity 21.00, parameter simplicity 15.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.y
diff.x += params.h * data.y * data.z
diff.x += params.i * data.z
diff.x += params.j * data.z * data.z
diff.y += params.k
diff.y += params.l * data.x
diff.y += params.m * data.x * data.x
diff.y += params.n * data.x * data.y
diff.y -= params.o * data.x * data.z
diff.y -= params.p * data.y
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
diff.z += params.p27 * data.y * data.z
diff.z += params.p28 * data.z
diff.z += params.p29 * data.z * data.z
  Demo 0: a = -5.090, b = -7.205, c = 0.202, d = -0.070, e = 0.099, f = 8.829, g = -0.042, h = 0.042, i = 0.594, j = -0.022, k = -10.056, l = 28.494, m = -0.061, n = -0.310, o = 0.900, p = 0.983, q = 0.190, r = -0.026, s = 1.112, t = -0.039, u = 21.844, v = 0.661, w = -0.216, x = 1.524, y = -0.154, z = 1.805, p26 = -0.267, p27 = -0.004, p28 = -6.080, p29 = 0.117
  Demo 1: a = -16.742, b = 13.027, c = 0.308, d = -0.035, e = 0.605, f = -2.088, g = -0.135, h = 0.345, i = 2.168, j = -0.050, k = -13.139, l = 55.357, m = 0.420, n = -0.585, o = 1.494, p = 13.986, q = 0.213, r = 0.313, s = 1.295, t = -0.029, u = -10.576, v = 9.299, w = 0.046, x = 0.720, y = -0.232, z = -7.334, p26 = 0.213, p27 = 0.197, p28 = -1.623, p29 = -0.001
  Demo 2: a = 52.655, b = -2.420, c = -0.612, d = 0.194, e = 0.129, f = 5.358, g = 0.044, h = 0.075, i = -5.306, j = 0.126, k = 53.043, l = 45.434, m = -0.403, n = 0.067, o = 1.108, p = 2.728, q = 0.076, r = 0.033, s = -5.149, t = 0.108, u = -69.037, v = -3.197, w = 0.152, x = 1.114, y = 0.059, z = 0.281, p26 = -0.083, p27 = -0.002, p28 = 1.887, p29 = -0.095

-- score: -334.97 (accuracy -360.97, token simplicity 15.00, parameter simplicity 11.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x -= params.g * data.y * data.y
diff.x += params.h * data.y * data.z
diff.x += params.i * data.z
diff.y += params.j * data.x
diff.y += params.k * data.x * data.x
diff.y += params.l * data.x * data.y
diff.y += params.m * data.y
diff.y += params.n * data.y * data.y
diff.y -= params.o * data.y * data.z
diff.y += params.p * data.z
diff.y += params.q * data.z * data.z
diff.z += params.r
diff.z += params.s * data.x
diff.z += params.t * data.x * data.y
diff.z += params.u * data.y
diff.z -= params.v * data.z
  Demo 0: a = 0.821, b = -6.585, c = 0.159, d = -0.036, e = 0.132, f = 8.583, g = 0.050, h = 0.058, i = -0.160, j = 11.103, k = -0.361, l = -0.994, m = 0.873, n = 0.756, o = 0.169, p = 3.550, q = -0.180, r = -2.137, s = 0.409, t = 0.991, u = 0.018, v = 2.629
  Demo 1: a = 17.777, b = 11.802, c = 0.128, d = 0.138, e = 0.580, f = -1.890, g = 0.163, h = 0.347, i = -0.563, j = -9.246, k = -0.736, l = 0.778, m = 27.251, n = -0.184, o = 0.636, p = -1.487, q = 0.049, r = -3.451, s = -0.521, t = 1.022, u = 0.480, v = 1.914
  Demo 2: a = -11.144, b = -6.302, c = -0.120, d = 0.065, e = 0.053, f = 6.684, g = 0.016, h = 0.049, i = 0.599, j = -8.099, k = 1.053, l = -0.350, m = 24.110, n = -0.101, o = 0.575, p = 5.496, q = -0.176, r = 2.007, s = 0.231, t = 1.054, u = -0.253, v = 3.754

-- score: -172.14 (accuracy -183.64, token simplicity 6.00, parameter simplicity 5.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y += params.f * data.y
diff.y -= params.g * data.z
diff.z -= params.h
diff.z += params.i * data.x
diff.z += params.j * data.y
diff.z += params.k * data.z
  Demo 0: a = -1.605, b = 9.874, c = 9.987, d = 161.451, e = 0.350, f = 0.624, g = 7.279, h = 52.269, i = 7.878, j = 8.288, k = -2.303
  Demo 1: a = 0.593, b = 14.080, c = 14.051, d = 37.904, e = -16.418, f = 12.603, g = 1.130, h = 26.940, i = -5.484, j = 9.351, k = 1.006
  Demo 2: a = -0.224, b = 8.522, c = 8.488, d = 50.167, e = -13.487, f = 7.641, g = 0.710, h = 19.788, i = -2.269, j = 2.652, k = 0.326

-- score: -171.13 (accuracy -183.73, token simplicity 6.60, parameter simplicity 6.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y += params.e
diff.y += params.f * data.x
diff.y += params.g * data.y
diff.y -= params.h * data.z
diff.z -= params.i
diff.z += params.j * data.x
diff.z += params.k * data.y
diff.z += params.l * data.z
  Demo 0: a = -1.616, b = 9.875, c = 9.987, d = 0.001, e = 161.451, f = 0.350, g = 0.624, h = 7.279, i = 52.269, j = 7.878, k = 8.288, l = -2.303
  Demo 1: a = 0.607, b = 14.079, c = 14.051, d = -0.000, e = 37.904, f = -16.418, g = 12.603, h = 1.130, i = 26.940, j = -5.484, k = 9.351, l = 1.006
  Demo 2: a = 3.725, b = 8.492, c = 8.481, d = -0.127, e = 50.167, f = -13.487, g = 7.641, h = 0.710, i = 19.788, j = -2.269, k = 2.652, l = 0.326

-- score: -38.57 (accuracy -39.87, token simplicity 0.80, parameter simplicity 0.50) --
diff.z += params.a * data.x * data.y
  Demo 0: a = 0.585
  Demo 1: a = 0.695
  Demo 2: a = 0.649

-- score: -36.04 (accuracy -37.34, token simplicity 0.80, parameter simplicity 0.50) --
diff.z += params.a * data.y * data.y
  Demo 0: a = 0.429
  Demo 1: a = 0.549
  Demo 2: a = 0.390

## Round 1 | 3.22s | best score: -382.18

+936 new programs (936 actually scored)
* linear_fit: +7
* quadratic_fit: +31
* add_single_terms: +118
* delete_interactions: +347
* delete_lines: +173
* delete_near_zeros: +18
* relate_parameters: +237
* snap_to_one: +0
* tie_parameters: +5

### 10 parents for the next round

-- score: -382.18 (accuracy -395.58, token simplicity 7.40, parameter simplicity 6.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x * data.x
diff.z += params.j * data.x * data.y
diff.z += params.k * data.y
diff.z -= params.l * data.z
  Demo 0: a = 9.766, b = 9.913, c = -0.070, d = 0.128, e = 31.006, f = 1.083, g = 1.536, h = 6.197, i = 0.102, j = 0.966, k = -0.265, l = 2.994
  Demo 1: a = 14.098, b = 14.068, c = 0.018, d = -0.164, e = 36.273, f = 1.040, g = 1.091, h = -18.905, i = -0.223, j = 1.195, k = 0.129, l = 1.317
  Demo 2: a = 8.494, b = 8.484, c = -0.026, d = -1.938, e = 41.323, f = 1.027, g = 1.126, h = -19.745, i = -0.173, j = 1.134, k = -0.204, l = 2.732

-- score: -381.36 (accuracy -395.66, token simplicity 7.80, parameter simplicity 6.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y += params.e
diff.y += params.f * data.x
diff.y -= params.g * data.x * data.z
diff.y -= params.h * data.y
diff.z += params.i
diff.z += params.j * data.x * data.x
diff.z += params.k * data.x * data.y
diff.z += params.l * data.y
diff.z -= params.m * data.z
  Demo 0: a = -1.616, b = 9.875, c = 9.987, d = 0.001, e = 0.128, f = 31.006, g = 1.083, h = 1.536, i = 6.197, j = 0.102, k = 0.966, l = -0.265, m = 2.994
  Demo 1: a = 0.607, b = 14.079, c = 14.051, d = -0.000, e = -0.164, f = 36.273, g = 1.040, h = 1.091, i = -18.905, j = -0.223, k = 1.195, l = 0.129, m = 1.317
  Demo 2: a = 3.725, b = 8.492, c = 8.481, d = -0.127, e = -1.938, f = 41.323, g = 1.027, h = 1.126, i = -19.745, j = -0.173, k = 1.134, l = -0.204, m = 2.732

-- score: -380.59 (accuracy -399.39, token simplicity 10.80, parameter simplicity 8.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.y
diff.x -= params.c * data.x * data.z
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.x += params.f * data.y * data.z
diff.y += params.g
diff.y += params.h * data.x
diff.y -= params.i * data.x * data.z
diff.y += params.j * data.y
diff.y += params.k * data.y * data.z
diff.z += params.l
diff.z += params.m * data.x * data.x
diff.z += params.n * data.x * data.y
diff.z += params.o * data.y
diff.z -= params.p * data.z
  Demo 0: a = -9.894, b = 0.075, c = 0.017, d = 9.897, e = -0.055, f = 0.013, g = -0.850, h = 29.141, i = 1.017, j = 0.109, k = -0.061, l = 6.197, m = 0.102, n = 0.966, o = -0.265, p = 2.994
  Demo 1: a = 6.682, b = 0.254, c = 0.462, d = 1.730, e = -0.175, f = 0.261, g = 1.576, h = 46.885, i = 1.282, j = -8.405, k = 0.171, l = -18.905, m = -0.223, n = 1.195, o = 0.129, p = 1.317
  Demo 2: a = -6.181, b = -0.033, c = 0.051, d = 6.778, e = 0.011, f = 0.045, g = -2.222, h = 41.919, i = 1.040, j = -1.529, k = 0.010, l = -19.745, m = -0.173, n = 1.134, o = -0.204, p = 2.732

-- score: -380.18 (accuracy -396.88, token simplicity 9.20, parameter simplicity 7.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.y
diff.x += params.d * data.z
diff.y -= params.e
diff.y += params.f * data.x
diff.y -= params.g * data.x * data.z
diff.y += params.h * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.z += params.k
diff.z += params.l * data.x * data.x
diff.z += params.m * data.x * data.y
diff.z += params.n * data.y
diff.z -= params.o * data.z
  Demo 0: a = -1.616, b = 9.875, c = 9.987, d = 0.001, e = 10.355, f = 29.657, g = 1.046, h = 0.464, i = -0.072, j = 0.448, k = 6.197, l = 0.102, m = 0.966, n = -0.265, o = 2.994
  Demo 1: a = 0.607, b = 14.079, c = 14.051, d = -0.000, e = 4.782, f = 47.459, g = 1.298, h = -8.557, i = 0.177, j = 0.207, k = -18.905, l = -0.223, m = 1.195, n = 0.129, o = 1.317
  Demo 2: a = 3.725, b = 8.492, c = 8.481, d = -0.127, e = 1.374, f = 41.900, g = 1.039, h = -1.522, i = 0.010, j = -0.027, k = -19.745, l = -0.173, m = 1.134, n = -0.204, o = 2.732

-- score: -378.27 (accuracy -394.77, token simplicity 9.00, parameter simplicity 7.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.y
diff.x += params.e * data.z
diff.y -= params.f
diff.y += params.g * data.x
diff.y -= params.h * data.x * data.z
diff.y -= params.i * data.y
diff.y += params.j * data.z
diff.z += params.k
diff.z += params.l * data.x
diff.z += params.m * data.x * data.y
diff.z += params.n * data.y
diff.z -= params.o * data.z
  Demo 0: a = 3.190, b = 10.115, c = 0.048, d = 9.731, e = -0.192, f = 7.319, g = 31.669, h = 1.115, i = 1.475, j = 0.357, k = -2.137, l = 0.409, m = 0.991, n = 0.018, o = 2.629
  Demo 1: a = 3.521, b = 14.033, c = 0.034, d = 13.880, e = -0.164, f = 5.692, g = 36.485, h = 1.048, i = 1.027, j = 0.179, k = -3.451, l = -0.521, m = 1.022, n = 0.480, o = 1.914
  Demo 2: a = -1.671, b = 8.572, c = -0.040, d = 8.534, e = 0.179, f = 1.040, g = 41.311, h = 1.026, i = 1.124, j = -0.029, k = 2.007, l = 0.231, m = 1.054, n = -0.253, o = 3.754

-- score: -377.14 (accuracy -397.54, token simplicity 11.40, parameter simplicity 9.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.y
diff.x += params.f * data.z
diff.y -= params.g
diff.y += params.h * data.x
diff.y -= params.i * data.x * data.z
diff.y += params.j * data.y
diff.y += params.k * data.y * data.z
diff.y += params.l * data.z
diff.z += params.m
diff.z += params.n * data.x
diff.z += params.o * data.x * data.x
diff.z += params.p * data.x * data.y
diff.z += params.q * data.y
diff.z -= params.r * data.z
  Demo 0: a = 3.275, b = 10.006, c = 0.060, d = -0.022, e = 9.853, f = -0.233, g = 10.355, h = 29.657, i = 1.046, j = 0.464, k = -0.072, l = 0.448, m = 5.794, n = 0.175, o = 0.096, p = 0.959, q = -0.225, r = 3.001
  Demo 1: a = 3.843, b = 14.047, c = 0.038, d = -0.004, e = 13.891, f = -0.176, g = 4.782, h = 47.459, i = 1.298, j = -8.557, k = 0.177, l = 0.207, m = -18.892, n = 0.015, o = -0.224, p = 1.195, q = 0.116, r = 1.318
  Demo 2: a = -7.619, b = 8.607, c = -0.088, d = 0.026, e = 8.525, f = 0.446, g = 1.374, h = 41.900, i = 1.039, j = -1.522, k = 0.010, l = -0.027, m = -19.289, n = 0.079, o = -0.170, p = 1.133, q = -0.247, r = 2.758

-- score: -376.73 (accuracy -396.23, token simplicity 11.00, parameter simplicity 8.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.x
diff.x += params.c * data.x * data.z
diff.x += params.d * data.y
diff.x += params.e * data.z
diff.y -= params.f
diff.y += params.g * data.x
diff.y += params.h * data.x * data.x
diff.y -= params.i * data.x * data.z
diff.y -= params.j * data.y
diff.y += params.k * data.z
diff.z += params.l
diff.z += params.m * data.x
diff.z += params.n * data.x * data.y
diff.z += params.o * data.y
diff.z += params.p * data.y * data.y
diff.z -= params.q * data.z
  Demo 0: a = 9.631, b = 0.057, c = -0.021, d = 9.687, e = -0.044, f = 10.956, g = 30.652, h = -0.125, i = 1.057, j = 0.699, k = 0.456, l = -1.322, m = -0.543, n = 1.135, o = 0.918, p = -0.123, q = 2.628
  Demo 1: a = 12.372, b = 0.037, c = -0.034, d = 13.484, e = -0.067, f = 5.731, g = 36.471, h = -0.001, i = 1.048, j = 1.021, k = 0.181, l = -13.342, m = -0.471, n = 0.813, o = 0.361, p = 0.171, q = 1.618
  Demo 2: a = 9.015, b = -0.038, c = 0.008, d = 8.602, e = 0.132, f = 0.731, g = 41.330, h = 0.002, i = 1.027, j = 1.130, k = -0.047, l = 1.280, m = 0.244, n = 1.044, o = -0.258, p = 0.007, q = 3.736

-- score: -376.37 (accuracy -400.67, token simplicity 13.80, parameter simplicity 10.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y -= params.i
diff.y += params.j * data.x
diff.y += params.k * data.x * data.x
diff.y -= params.l * data.x * data.z
diff.y += params.m * data.y
diff.y += params.n * data.y * data.z
diff.y += params.o * data.z
diff.z += params.p
diff.z += params.q * data.x
diff.z += params.r * data.x * data.x
diff.z += params.s * data.x * data.y
diff.z += params.t * data.y
diff.z -= params.u * data.z
  Demo 0: a = 4.514, b = -5.998, c = 0.153, d = -0.127, e = 0.128, f = 7.760, g = 0.089, h = -0.388, i = 12.016, j = 29.348, k = -0.071, l = 1.022, m = 0.645, n = -0.062, o = 0.492, p = 5.794, q = 0.175, r = 0.096, s = 0.959, t = -0.225, u = 3.001
  Demo 1: a = 20.733, b = 13.873, c = 0.290, d = -0.189, e = 0.639, f = -3.912, g = 0.406, h = -0.723, i = 4.019, j = 48.101, k = 0.011, l = 1.312, m = -8.936, n = 0.183, o = 0.162, p = -18.892, q = 0.015, r = -0.224, s = 1.195, t = 0.116, u = 1.318
  Demo 2: a = -10.819, b = -6.192, c = -0.104, d = 0.033, e = 0.054, f = 6.654, g = 0.049, h = 0.542, i = 1.084, j = 41.915, k = 0.002, l = 1.039, m = -1.526, n = 0.010, o = -0.044, p = -19.289, q = 0.079, r = -0.170, s = 1.133, t = -0.247, u = 2.758

-- score: -375.97 (accuracy -397.67, token simplicity 12.20, parameter simplicity 9.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x += params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.z
diff.y -= params.h
diff.y += params.i * data.x
diff.y -= params.j * data.x * data.z
diff.y += params.k * data.y
diff.y += params.l * data.y * data.z
diff.y += params.m * data.z
diff.z += params.n
diff.z += params.o * data.x
diff.z += params.p * data.x * data.x
diff.z += params.q * data.x * data.y
diff.z += params.r * data.y
diff.z -= params.s * data.z
  Demo 0: a = 3.021, b = 9.201, c = 0.118, d = -0.035, e = -0.035, f = 9.584, g = -0.216, h = 10.355, i = 29.657, j = 1.046, k = 0.464, l = -0.072, m = 0.448, n = 5.794, o = 0.175, p = 0.096, q = 0.959, r = -0.225, s = 3.001
  Demo 1: a = 3.790, b = 12.378, c = 0.057, d = -0.014, e = -0.034, f = 13.449, g = -0.194, h = 4.782, i = 47.459, j = 1.298, k = -8.557, l = 0.177, m = 0.207, n = -18.892, o = 0.015, p = -0.224, q = 1.195, r = 0.116, s = 1.318
  Demo 2: a = -7.456, b = 9.046, c = -0.090, d = 0.026, e = 0.008, f = 8.597, g = 0.455, h = 1.374, i = 41.900, j = 1.039, k = -1.522, l = 0.010, m = -0.027, n = -19.289, o = 0.079, p = -0.170, q = 1.133, r = -0.247, s = 2.758

-- score: -375.93 (accuracy -397.63, token simplicity 12.20, parameter simplicity 9.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.z
diff.x += params.e * data.y
diff.x += params.f * data.z
diff.y -= params.g
diff.y += params.h * data.x
diff.y += params.i * data.x * data.x
diff.y -= params.j * data.x * data.z
diff.y += params.k * data.y
diff.y += params.l * data.y * data.z
diff.y += params.m * data.z
diff.z += params.n
diff.z += params.o * data.x
diff.z += params.p * data.x * data.x
diff.z += params.q * data.x * data.y
diff.z += params.r * data.y
diff.z -= params.s * data.z
  Demo 0: a = 3.028, b = 9.716, c = 0.075, d = -0.019, e = 9.550, f = -0.170, g = 12.016, h = 29.348, i = -0.071, j = 1.022, k = 0.645, l = -0.062, m = 0.492, n = 5.794, o = 0.175, p = 0.096, q = 0.959, r = -0.225, s = 3.001
  Demo 1: a = 2.746, b = 12.413, c = 0.040, d = -0.032, e = 13.432, f = -0.155, g = 4.019, h = 48.101, i = 0.011, j = 1.312, k = -8.936, l = 0.183, m = 0.162, n = -18.892, o = 0.015, p = -0.224, q = 1.195, r = 0.116, s = 1.318
  Demo 2: a = -1.473, b = 9.002, c = -0.041, d = 0.008, e = 8.604, f = 0.185, g = 1.084, h = 41.915, i = 0.002, j = 1.039, k = -1.526, l = 0.010, m = -0.044, n = -19.289, o = 0.079, p = -0.170, q = 1.133, r = -0.247, s = 2.758

## Round 2 | 2.89s | best score: -383.16

+1380 new programs (1380 actually scored)
* linear_fit: +7
* quadratic_fit: +45
* add_single_terms: +126
* delete_interactions: +313
* delete_lines: +160
* delete_near_zeros: +11
* relate_parameters: +695
* snap_to_one: +0
* tie_parameters: +23

### 10 parents for the next round

-- score: -383.16 (accuracy -395.46, token simplicity 6.80, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.963, b = 9.919, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = 6.197, h = 0.102, i = 0.966, j = -0.265, k = 2.994
  Demo 1: a = 14.056, b = 14.041, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = -18.905, h = -0.223, i = 1.195, j = 0.129, k = 1.317
  Demo 2: a = 8.530, b = 8.488, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = -19.745, h = -0.173, i = 1.134, j = -0.204, k = 2.732

-- score: -383.04 (accuracy -395.34, token simplicity 6.80, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x * data.x
diff.z += params.j * data.x * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.766, b = 9.913, c = -0.070, d = 0.128, e = 31.006, f = 1.083, g = 1.536, h = 3.560, i = 0.092, j = 0.953, k = 2.901
  Demo 1: a = 14.098, b = 14.068, c = 0.018, d = -0.164, e = 36.273, f = 1.040, g = 1.091, h = -18.064, i = -0.218, j = 1.196, k = 1.354
  Demo 2: a = 8.494, b = 8.484, c = -0.026, d = -1.938, e = 41.323, f = 1.027, g = 1.126, h = -17.614, i = -0.155, j = 1.124, k = 2.844

-- score: -382.98 (accuracy -395.48, token simplicity 7.00, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.766, b = 9.913, c = -0.070, d = 31.031, e = 1.083, f = 1.534, g = 6.197, h = 0.102, i = 0.966, j = -0.265, k = 2.994
  Demo 1: a = 14.098, b = 14.068, c = 0.018, d = 36.254, e = 1.040, f = 1.085, g = -18.905, h = -0.223, i = 1.195, j = 0.129, k = 1.317
  Demo 2: a = 8.494, b = 8.484, c = -0.026, d = 40.988, e = 1.022, f = 1.075, g = -19.745, h = -0.173, i = 1.134, j = -0.204, k = 2.732

-- score: -382.64 (accuracy -395.54, token simplicity 7.40, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.x += params.b * data.z
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.922, b = -0.029, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = 6.197, h = 0.102, i = 0.966, j = -0.265, k = 2.994
  Demo 1: a = 14.066, b = 0.016, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = -18.905, h = -0.223, i = 1.195, j = 0.129, k = 1.317
  Demo 2: a = 8.484, b = -0.027, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = -19.745, h = -0.173, i = 1.134, j = -0.204, k = 2.732

-- score: -382.45 (accuracy -395.55, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += (params.a - params.b) * data.y
diff.x += params.b * data.z
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.875, b = -0.045, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = 6.197, h = 0.102, i = 0.966, j = -0.265, k = 2.994
  Demo 1: a = 14.086, b = 0.018, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = -18.905, h = -0.223, i = 1.195, j = 0.129, k = 1.317
  Demo 2: a = 8.458, b = -0.027, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = -19.745, h = -0.173, i = 1.134, j = -0.204, k = 2.732

-- score: -382.45 (accuracy -395.55, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= (params.f - params.g) * data.y
diff.z += params.h
diff.z += params.i * data.x * data.x
diff.z += params.j * data.x * data.y
diff.z += params.g * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.766, b = 9.913, c = -0.070, d = 0.112, e = 30.934, f = 1.082, g = -0.423, h = 7.760, i = 0.107, j = 0.973, k = 3.049
  Demo 1: a = 14.098, b = 14.068, c = 0.018, d = -0.122, e = 35.847, f = 1.033, g = 0.104, h = -18.745, i = -0.222, j = 1.195, k = 1.324
  Demo 2: a = 8.494, b = 8.484, c = -0.026, d = -2.038, e = 41.525, f = 1.030, g = -0.170, h = -19.394, i = -0.170, j = 1.133, k = 2.750

-- score: -382.42 (accuracy -395.52, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= (params.a - params.b) * data.x
diff.x += params.a * data.y
diff.x += params.b * data.z
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.923, b = -0.020, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = 6.197, h = 0.102, i = 0.966, j = -0.265, k = 2.994
  Demo 1: a = 14.061, b = 0.013, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = -18.905, h = -0.223, i = 1.195, j = 0.129, k = 1.317
  Demo 2: a = 8.484, b = -0.024, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = -19.745, h = -0.173, i = 1.134, j = -0.204, k = 2.732

-- score: -382.41 (accuracy -395.51, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= (params.g - params.h) * data.y
diff.z += params.i
diff.z += params.j * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z += params.h * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.766, b = 9.913, c = -0.070, d = 0.111, e = 30.888, f = 1.081, g = 0.979, h = -0.508, i = 8.456, j = 0.108, k = 3.070
  Demo 1: a = 14.098, b = 14.068, c = 0.018, d = -0.159, e = 36.214, f = 1.039, g = 1.195, h = 0.126, i = -18.907, j = -0.224, k = 1.317
  Demo 2: a = 8.494, b = 8.484, c = -0.026, d = -2.142, e = 41.730, f = 1.033, g = 1.128, h = -0.139, i = -18.440, j = -0.162, k = 2.795

-- score: -382.38 (accuracy -395.48, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += (params.a + params.b) * data.y
diff.x += params.c * data.z
diff.y += params.b
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.767, b = 0.146, c = -0.070, d = 31.002, e = 1.083, f = 1.536, g = 6.197, h = 0.102, i = 0.966, j = -0.265, k = 2.994
  Demo 1: a = 14.099, b = -0.031, c = 0.018, d = 36.258, e = 1.040, f = 1.086, g = -18.905, h = -0.223, i = 1.195, j = 0.129, k = 1.317
  Demo 2: a = 8.500, b = -0.016, c = -0.026, d = 40.991, e = 1.022, f = 1.075, g = -19.745, h = -0.173, i = 1.134, j = -0.204, k = 2.732

-- score: -382.38 (accuracy -395.58, token simplicity 7.20, parameter simplicity 6.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x * data.x
diff.z += params.j * data.x * data.y
diff.z += params.k * data.y
diff.z -= params.l * data.z
  Demo 0: a = -1.605, b = 9.874, c = 9.987, d = 0.128, e = 31.006, f = 1.083, g = 1.536, h = 6.197, i = 0.102, j = 0.966, k = -0.265, l = 2.994
  Demo 1: a = 0.593, b = 14.080, c = 14.051, d = -0.164, e = 36.273, f = 1.040, g = 1.091, h = -18.905, i = -0.223, j = 1.195, k = 0.129, l = 1.317
  Demo 2: a = -0.224, b = 8.522, c = 8.488, d = -1.938, e = 41.323, f = 1.027, g = 1.126, h = -19.745, i = -0.173, j = 1.134, k = -0.204, l = 2.732

## Round 3 | 1.25s | best score: -384.03

+927 new programs (927 actually scored)
* linear_fit: +14
* quadratic_fit: +49
* add_single_terms: +170
* delete_interactions: +205
* delete_lines: +103
* delete_near_zeros: +2
* relate_parameters: +367
* snap_to_one: +0
* tie_parameters: +17

### 10 parents for the next round

-- score: -384.03 (accuracy -395.23, token simplicity 6.20, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.963, b = 9.919, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = 3.560, h = 0.092, i = 0.953, j = 2.901
  Demo 1: a = 14.056, b = 14.041, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = -18.064, h = -0.218, i = 1.196, j = 1.354
  Demo 2: a = 8.530, b = 8.488, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = -17.614, h = -0.155, i = 1.124, j = 2.844

-- score: -383.96 (accuracy -395.36, token simplicity 6.40, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.963, b = 9.919, c = 31.031, d = 1.083, e = 1.534, f = 6.197, g = 0.102, h = 0.966, i = -0.265, j = 2.994
  Demo 1: a = 14.056, b = 14.041, c = 36.254, d = 1.040, e = 1.085, f = -18.905, g = -0.223, h = 1.195, i = 0.129, j = 1.317
  Demo 2: a = 8.530, b = 8.488, c = 40.988, d = 1.022, e = 1.075, f = -19.745, g = -0.173, h = 1.134, i = -0.204, j = 2.732

-- score: -383.84 (accuracy -395.24, token simplicity 6.40, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.766, b = 9.913, c = -0.070, d = 31.031, e = 1.083, f = 1.534, g = 3.560, h = 0.092, i = 0.953, j = 2.901
  Demo 1: a = 14.098, b = 14.068, c = 0.018, d = 36.254, e = 1.040, f = 1.085, g = -18.064, h = -0.218, i = 1.196, j = 1.354
  Demo 2: a = 8.494, b = 8.484, c = -0.026, d = 40.988, e = 1.022, f = 1.075, g = -17.614, h = -0.155, i = 1.124, j = 2.844

-- score: -383.76 (accuracy -395.36, token simplicity 6.60, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += (params.a + params.b) * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.963, b = -0.043, c = 31.031, d = 1.083, e = 1.534, f = 6.197, g = 0.102, h = 0.966, i = -0.265, j = 2.994
  Demo 1: a = 14.056, b = -0.015, c = 36.254, d = 1.040, e = 1.085, f = -18.905, g = -0.223, h = 1.195, i = 0.129, j = 1.317
  Demo 2: a = 8.530, b = -0.041, c = 40.988, d = 1.022, e = 1.075, f = -19.745, g = -0.173, h = 1.134, i = -0.204, j = 2.732

-- score: -383.64 (accuracy -395.44, token simplicity 6.80, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.912, b = 0.128, c = 31.006, d = 1.083, e = 1.536, f = 6.197, g = 0.102, h = 0.966, i = -0.265, j = 2.994
  Demo 1: a = 14.041, b = -0.164, c = 36.273, d = 1.040, e = 1.091, f = -18.905, g = -0.223, h = 1.195, i = 0.129, j = 1.317
  Demo 2: a = 8.490, b = -1.938, c = 41.323, d = 1.027, e = 1.126, f = -19.745, g = -0.173, h = 1.134, i = -0.204, j = 2.732

-- score: -383.56 (accuracy -393.46, token simplicity 5.40, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.963, b = 9.919, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = -2.696, h = 1.010, i = 2.544
  Demo 1: a = 14.056, b = 14.041, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = -0.864, h = 1.028, i = 2.017
  Demo 2: a = 8.530, b = 8.488, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = 1.872, h = 1.052, i = 3.741

-- score: -383.50 (accuracy -395.30, token simplicity 6.80, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.x += params.b * data.z
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.922, b = -0.029, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = 3.560, h = 0.092, i = 0.953, j = 2.901
  Demo 1: a = 14.066, b = 0.016, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = -18.064, h = -0.218, i = 1.196, j = 1.354
  Demo 2: a = 8.484, b = -0.027, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = -17.614, h = -0.155, i = 1.124, j = 2.844

-- score: -383.44 (accuracy -395.44, token simplicity 7.00, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.x += params.b * data.z
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.922, b = -0.029, c = 31.031, d = 1.083, e = 1.534, f = 6.197, g = 0.102, h = 0.966, i = -0.265, j = 2.994
  Demo 1: a = 14.066, b = 0.016, c = 36.254, d = 1.040, e = 1.085, f = -18.905, g = -0.223, h = 1.195, i = 0.129, j = 1.317
  Demo 2: a = 8.484, b = -0.027, c = 40.988, d = 1.022, e = 1.075, f = -19.745, g = -0.173, h = 1.134, i = -0.204, j = 2.732

-- score: -383.43 (accuracy -395.43, token simplicity 7.00, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= (params.e + params.f) * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.g
diff.z += params.h * data.x * data.x
diff.z += params.i * data.x * data.y
diff.z += params.f * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.963, b = 9.919, c = 0.112, d = 30.934, e = 1.504, f = -0.423, g = 7.760, h = 0.107, i = 0.973, j = 3.049
  Demo 1: a = 14.056, b = 14.041, c = -0.122, d = 35.847, e = 0.929, f = 0.104, g = -18.745, h = -0.222, i = 1.195, j = 1.324
  Demo 2: a = 8.530, b = 8.488, c = -2.038, d = 41.525, e = 1.200, f = -0.170, g = -19.394, h = -0.170, i = 1.133, j = 2.750

-- score: -383.39 (accuracy -395.39, token simplicity 7.00, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= (params.f - params.g) * data.y
diff.z += params.h
diff.z += params.i * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z += params.g * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.963, b = 9.919, c = 0.111, d = 30.888, e = 1.081, f = 0.979, g = -0.508, h = 8.456, i = 0.108, j = 3.070
  Demo 1: a = 14.056, b = 14.041, c = -0.159, d = 36.214, e = 1.039, f = 1.195, g = 0.126, h = -18.907, i = -0.224, j = 1.317
  Demo 2: a = 8.530, b = 8.488, c = -2.142, d = 41.730, e = 1.033, f = 1.128, g = -0.139, h = -18.440, i = -0.162, j = 2.795

## Round 4 | 0.93s | best score: -384.83

+791 new programs (791 actually scored)
* linear_fit: +10
* quadratic_fit: +23
* add_single_terms: +175
* delete_interactions: +180
* delete_lines: +89
* delete_near_zeros: +1
* relate_parameters: +296
* snap_to_one: +0
* tie_parameters: +17

### 10 parents for the next round

-- score: -384.83 (accuracy -395.13, token simplicity 5.80, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.963, b = 9.919, c = 31.031, d = 1.083, e = 1.534, f = 3.560, g = 0.092, h = 0.953, i = 2.901
  Demo 1: a = 14.056, b = 14.041, c = 36.254, d = 1.040, e = 1.085, f = -18.064, g = -0.218, h = 1.196, i = 1.354
  Demo 2: a = 8.530, b = 8.488, c = 40.988, d = 1.022, e = 1.075, f = -17.614, g = -0.155, h = 1.124, i = 2.844

-- score: -384.63 (accuracy -395.13, token simplicity 6.00, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += (params.a + params.b) * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.963, b = -0.043, c = 31.031, d = 1.083, e = 1.534, f = 3.560, g = 0.092, h = 0.953, i = 2.901
  Demo 1: a = 14.056, b = -0.015, c = 36.254, d = 1.040, e = 1.085, f = -18.064, g = -0.218, h = 1.196, i = 1.354
  Demo 2: a = 8.530, b = -0.041, c = 40.988, d = 1.022, e = 1.075, f = -17.614, g = -0.155, h = 1.124, i = 2.844

-- score: -384.51 (accuracy -395.21, token simplicity 6.20, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.912, b = 0.128, c = 31.006, d = 1.083, e = 1.536, f = 3.560, g = 0.092, h = 0.953, i = 2.901
  Demo 1: a = 14.041, b = -0.164, c = 36.273, d = 1.040, e = 1.091, f = -18.064, g = -0.218, h = 1.196, i = 1.354
  Demo 2: a = 8.490, b = -1.938, c = 41.323, d = 1.027, e = 1.126, f = -17.614, g = -0.155, h = 1.124, i = 2.844

-- score: -384.44 (accuracy -395.34, token simplicity 6.40, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e
diff.z += params.f * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z += params.h * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 6.197, f = 0.102, g = 0.966, h = -0.265, i = 2.994
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = -18.905, f = -0.223, g = 1.195, h = 0.129, i = 1.317
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = -19.745, f = -0.173, g = 1.134, h = -0.204, i = 2.732

-- score: -384.38 (accuracy -393.38, token simplicity 5.00, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.963, b = 9.919, c = 0.128, d = 31.006, e = 1.083, f = 1.536, g = 1.011, h = 2.650
  Demo 1: a = 14.056, b = 14.041, c = -0.164, d = 36.273, e = 1.040, f = 1.091, g = 1.028, h = 2.042
  Demo 2: a = 8.530, b = 8.488, c = -1.938, d = 41.323, e = 1.027, f = 1.126, g = 1.052, h = 3.690

-- score: -384.36 (accuracy -393.36, token simplicity 5.00, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.963, b = 9.919, c = 31.031, d = 1.083, e = 1.534, f = -2.696, g = 1.010, h = 2.544
  Demo 1: a = 14.056, b = 14.041, c = 36.254, d = 1.040, e = 1.085, f = -0.864, g = 1.028, h = 2.017
  Demo 2: a = 8.530, b = 8.488, c = 40.988, d = 1.022, e = 1.075, f = 1.872, g = 1.052, h = 3.741

-- score: -384.30 (accuracy -395.20, token simplicity 6.40, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.x += params.b * data.z
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.922, b = -0.029, c = 31.031, d = 1.083, e = 1.534, f = 3.560, g = 0.092, h = 0.953, i = 2.901
  Demo 1: a = 14.066, b = 0.016, c = 36.254, d = 1.040, e = 1.085, f = -18.064, g = -0.218, h = 1.196, i = 1.354
  Demo 2: a = 8.484, b = -0.027, c = 40.988, d = 1.022, e = 1.075, f = -17.614, g = -0.155, h = 1.124, i = 2.844

-- score: -384.23 (accuracy -395.13, token simplicity 6.40, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += (params.a + params.b) * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.963, b = -0.043, c = 31.040, d = 1.084, e = 1.534, f = 3.560, g = 0.092, h = 0.953, i = 2.901
  Demo 1: a = 14.057, b = -0.016, c = 36.256, d = 1.040, e = 1.086, f = -18.064, g = -0.218, h = 1.196, i = 1.354
  Demo 2: a = 8.534, b = -0.046, c = 40.996, d = 1.022, e = 1.076, f = -17.614, g = -0.155, h = 1.124, i = 2.844

-- score: -384.22 (accuracy -395.12, token simplicity 6.40, parameter simplicity 4.50) --
diff.x -= (params.a + params.b) * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.920, b = 0.044, c = 31.023, d = 1.083, e = 1.535, f = 3.560, g = 0.092, h = 0.953, i = 2.901
  Demo 1: a = 14.041, b = 0.014, c = 36.253, d = 1.040, e = 1.085, f = -18.064, g = -0.218, h = 1.196, i = 1.354
  Demo 2: a = 8.489, b = 0.036, c = 40.981, d = 1.022, e = 1.074, f = -17.614, g = -0.155, h = 1.124, i = 2.844

-- score: -384.22 (accuracy -395.32, token simplicity 6.60, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= (params.d + params.e) * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z += params.e * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.963, b = 9.919, c = 30.956, d = 1.503, e = -0.421, f = 7.748, g = 0.107, h = 0.973, i = 3.048
  Demo 1: a = 14.056, b = 14.041, c = 35.844, d = 0.928, e = 0.105, f = -18.749, g = -0.222, h = 1.195, i = 1.324
  Demo 2: a = 8.530, b = 8.488, c = 41.260, d = 1.180, e = -0.155, f = -19.230, g = -0.169, h = 1.132, i = 2.759

## Round 5 | 0.70s | best score: -385.31

+664 new programs (664 actually scored)
* linear_fit: +6
* quadratic_fit: +17
* add_single_terms: +180
* delete_interactions: +161
* delete_lines: +76
* delete_near_zeros: +2
* relate_parameters: +203
* snap_to_one: +0
* tie_parameters: +19

### 10 parents for the next round

-- score: -385.31 (accuracy -395.11, token simplicity 5.80, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e
diff.z += params.f * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 3.560, f = 0.092, g = 0.953, h = 2.901
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = -18.064, f = -0.218, g = 1.196, h = 1.354
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = -17.614, f = -0.155, g = 1.124, h = 2.844

-- score: -385.18 (accuracy -393.28, token simplicity 4.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.963, b = 9.919, c = 31.031, d = 1.083, e = 1.534, f = 1.011, g = 2.650
  Demo 1: a = 14.056, b = 14.041, c = 36.254, d = 1.040, e = 1.085, f = 1.028, g = 2.042
  Demo 2: a = 8.530, b = 8.488, c = 40.988, d = 1.022, e = 1.075, f = 1.052, g = 3.690

-- score: -385.03 (accuracy -394.63, token simplicity 5.60, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e
diff.z += params.f * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.963, b = 9.919, c = 29.691, d = 1.057, e = 3.560, f = 0.092, g = 0.953, h = 2.901
  Demo 1: a = 14.056, b = 14.041, c = 36.028, d = 1.036, e = -18.064, f = -0.218, g = 1.196, h = 1.354
  Demo 2: a = 8.530, b = 8.488, c = 40.784, d = 1.019, e = -17.614, f = -0.155, g = 1.124, h = 2.844

-- score: -384.94 (accuracy -394.74, token simplicity 5.80, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e
diff.z += params.f * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.963, b = 9.919, c = 29.891, d = 1.062, e = 3.560, f = 0.092, g = 0.953, h = 2.901
  Demo 1: a = 14.056, b = 14.041, c = 36.131, d = 1.038, e = -18.064, f = -0.218, g = 1.196, h = 1.354
  Demo 2: a = 8.530, b = 8.488, c = 40.845, d = 1.020, e = -17.614, f = -0.155, g = 1.124, h = 2.844

-- score: -384.86 (accuracy -393.36, token simplicity 5.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 0.128, c = 31.006, d = 1.083, e = 1.536, f = 1.011, g = 2.650
  Demo 1: a = 14.041, b = -0.164, c = 36.273, d = 1.040, e = 1.091, f = 1.028, g = 2.042
  Demo 2: a = 8.490, b = -1.938, c = 41.323, d = 1.027, e = 1.126, f = 1.052, g = 3.690

-- score: -384.84 (accuracy -393.34, token simplicity 5.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = -2.696, f = 1.010, g = 2.544
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = -0.864, f = 1.028, g = 2.017
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = 1.872, f = 1.052, g = 3.741

-- score: -384.84 (accuracy -394.84, token simplicity 6.00, parameter simplicity 4.00) --
diff.x -= (params.a - params.b) * data.x
diff.x += params.a * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z -= params.f
diff.z += params.b * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.908, b = 0.030, c = 31.031, d = 1.083, e = 1.534, f = 0.664, g = 0.991, h = 2.660
  Demo 1: a = 14.039, b = -0.169, c = 36.254, d = 1.040, e = 1.085, f = 14.194, g = 1.158, h = 1.504
  Demo 2: a = 8.486, b = -0.114, c = 40.988, d = 1.022, e = 1.075, f = 12.478, g = 1.105, h = 3.080

-- score: -384.83 (accuracy -394.63, token simplicity 5.80, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += (params.a + params.b) * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e
diff.z += params.f * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.963, b = -0.043, c = 29.691, d = 1.057, e = 3.560, f = 0.092, g = 0.953, h = 2.901
  Demo 1: a = 14.056, b = -0.015, c = 36.028, d = 1.036, e = -18.064, f = -0.218, g = 1.196, h = 1.354
  Demo 2: a = 8.530, b = -0.041, c = 40.784, d = 1.019, e = -17.614, f = -0.155, g = 1.124, h = 2.844

-- score: -384.83 (accuracy -395.13, token simplicity 5.80, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.963, b = 9.919, c = 31.031, d = 1.083, e = 1.534, f = 3.560, g = 0.092, h = 0.953, i = 2.901
  Demo 1: a = 14.056, b = 14.041, c = 36.254, d = 1.040, e = 1.085, f = -18.064, g = -0.218, h = 1.196, i = 1.354
  Demo 2: a = 8.530, b = 8.488, c = 40.988, d = 1.022, e = 1.075, f = -17.614, g = -0.155, h = 1.124, i = 2.844

-- score: -384.82 (accuracy -394.82, token simplicity 6.00, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= (params.d + params.e) * data.y
diff.z += params.f
diff.z += params.e * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.963, b = 9.919, c = 30.193, d = 1.067, e = 0.119, f = 5.425, g = 0.935, h = 3.008
  Demo 1: a = 14.056, b = 14.041, c = 35.549, d = 1.028, e = -0.213, f = -17.679, g = 1.192, h = 1.369
  Demo 2: a = 8.530, b = 8.488, c = 40.474, d = 1.014, e = -0.138, f = -15.532, g = 1.116, h = 2.940

## Round 6 | 0.61s | best score: -385.66

+571 new programs (571 actually scored)
* linear_fit: +19
* quadratic_fit: +45
* add_single_terms: +168
* delete_interactions: +137
* delete_lines: +61
* delete_near_zeros: +0
* relate_parameters: +127
* snap_to_one: +0
* tie_parameters: +14

### 10 parents for the next round

-- score: -385.66 (accuracy -393.26, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 1.011, f = 2.650
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = 1.028, f = 2.042
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = 1.052, f = 3.690

-- score: -385.51 (accuracy -394.61, token simplicity 5.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 3.560, e = 0.092, f = 0.953, g = 2.901
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -18.064, e = -0.218, f = 1.196, g = 1.354
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -17.614, e = -0.155, f = 1.124, g = 2.844

-- score: -385.42 (accuracy -394.72, token simplicity 5.80, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 3.560, e = 0.092, f = 0.953, g = 2.901
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = -18.064, e = -0.218, f = 1.196, g = 1.354
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = -17.614, e = -0.155, f = 1.124, g = 2.844

-- score: -385.38 (accuracy -392.78, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.963, b = 9.919, c = 29.691, d = 1.057, e = 1.011, f = 2.650
  Demo 1: a = 14.056, b = 14.041, c = 36.028, d = 1.036, e = 1.028, f = 2.042
  Demo 2: a = 8.530, b = 8.488, c = 40.784, d = 1.019, e = 1.052, f = 3.690

-- score: -385.31 (accuracy -395.11, token simplicity 5.80, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e
diff.z += params.f * data.x * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 3.560, f = 0.092, g = 0.953, h = 2.901
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = -18.064, f = -0.218, g = 1.196, h = 1.354
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = -17.614, f = -0.155, g = 1.124, h = 2.844

-- score: -385.30 (accuracy -394.80, token simplicity 6.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.c + params.d) * data.y
diff.z += params.e
diff.z += params.d * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 30.193, c = 1.067, d = 0.119, e = 5.425, f = 0.935, g = 3.008
  Demo 1: a = 14.041, b = 35.549, c = 1.028, d = -0.213, e = -17.679, f = 1.192, g = 1.369
  Demo 2: a = 8.490, b = 40.474, c = 1.014, d = -0.138, e = -15.532, f = 1.116, g = 2.940

-- score: -385.29 (accuracy -392.89, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.963, b = 9.919, c = 29.891, d = 1.062, e = 1.011, f = 2.650
  Demo 1: a = 14.056, b = 14.041, c = 36.131, d = 1.038, e = 1.028, f = 2.042
  Demo 2: a = 8.530, b = 8.488, c = 40.845, d = 1.020, e = 1.052, f = 3.690

-- score: -385.27 (accuracy -394.77, token simplicity 6.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= (params.c * params.d) * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.e
diff.z += params.f * data.x * data.x
diff.z += params.d * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 30.077, c = 1.138, d = 0.936, e = 5.155, f = 0.116, g = 2.989
  Demo 1: a = 14.041, b = 35.671, c = 0.863, d = 1.194, e = -17.886, f = -0.215, g = 1.361
  Demo 2: a = 8.490, b = 40.548, c = 0.906, d = 1.121, e = -16.960, f = -0.150, g = 2.873

-- score: -385.24 (accuracy -394.14, token simplicity 5.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 0.056, f = 0.975, g = 2.718
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = -0.102, f = 1.105, g = 1.962
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = -0.053, f = 1.077, g = 3.566

-- score: -385.18 (accuracy -394.68, token simplicity 6.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.d + params.e) * data.y
diff.z += params.f
diff.z += params.d * data.x * data.x
diff.z += params.e * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.819, c = 1.059, d = 0.106, e = 0.945, f = 4.510, g = 2.959
  Demo 1: a = 14.041, b = 35.970, c = 1.035, d = -0.217, e = 1.196, f = -18.033, g = 1.356
  Demo 2: a = 8.490, b = 40.706, c = 1.018, d = -0.151, e = 1.122, f = -17.052, g = 2.871

## Round 7 | 0.93s | best score: -385.86

+493 new programs (493 actually scored)
* linear_fit: +25
* quadratic_fit: +48
* add_single_terms: +168
* delete_interactions: +134
* delete_lines: +52
* delete_near_zeros: +0
* relate_parameters: +57
* snap_to_one: +0
* tie_parameters: +9

### 10 parents for the next round

-- score: -385.86 (accuracy -392.76, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = 1.052, e = 3.690

-- score: -385.77 (accuracy -392.87, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = 1.052, e = 3.690

-- score: -385.66 (accuracy -393.26, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 1.011, f = 2.650
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = 1.028, f = 2.042
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = 1.052, f = 3.690

-- score: -385.60 (accuracy -392.90, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.c * params.d) * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.925, c = 1.062, d = 1.012, e = 2.655
  Demo 1: a = 14.041, b = 36.211, c = 1.039, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.986, c = 1.022, d = 1.052, e = 3.690

-- score: -385.54 (accuracy -392.84, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= (params.c * params.d) * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.865, c = 1.051, d = 1.009, e = 2.646
  Demo 1: a = 14.041, b = 36.053, c = 1.008, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.711, c = 0.968, d = 1.051, e = 3.689

-- score: -385.51 (accuracy -394.61, token simplicity 5.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 3.560, e = 0.092, f = 0.953, g = 2.901
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -18.064, e = -0.218, f = 1.196, g = 1.354
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -17.614, e = -0.155, f = 1.124, g = 2.844

-- score: -385.44 (accuracy -393.64, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.x
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 0.056, e = 0.975, f = 2.718
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -0.102, e = 1.105, f = 1.962
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -0.053, e = 1.077, f = 3.566

-- score: -385.42 (accuracy -394.72, token simplicity 5.80, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 3.560, e = 0.092, f = 0.953, g = 2.901
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = -18.064, e = -0.218, f = 1.196, g = 1.354
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = -17.614, e = -0.155, f = 1.124, g = 2.844

-- score: -385.38 (accuracy -392.78, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.963, b = 9.919, c = 29.691, d = 1.057, e = 1.011, f = 2.650
  Demo 1: a = 14.056, b = 14.041, c = 36.028, d = 1.036, e = 1.028, f = 2.042
  Demo 2: a = 8.530, b = 8.488, c = 40.784, d = 1.019, e = 1.052, f = 3.690

-- score: -385.35 (accuracy -393.75, token simplicity 5.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.x
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 0.056, e = 0.975, f = 2.718
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = -0.102, e = 1.105, f = 1.962
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = -0.053, e = 1.077, f = 3.566

## Round 8 | 0.66s | best score: -385.86 (stable)

+301 new programs (301 actually scored)
* linear_fit: +18
* quadratic_fit: +28
* add_single_terms: +122
* delete_interactions: +84
* delete_lines: +30
* delete_near_zeros: +0
* relate_parameters: +15
* snap_to_one: +0
* tie_parameters: +4

### 10 parents for the next round

-- score: -385.86 (accuracy -392.76, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = 1.052, e = 3.690

-- score: -385.77 (accuracy -392.87, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = 1.052, e = 3.690

-- score: -385.66 (accuracy -392.76, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= (params.c * params.d) * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.046, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.008, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 0.969, d = 1.052, e = 3.690

-- score: -385.66 (accuracy -393.26, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 1.011, f = 2.650
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = 1.028, f = 2.042
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = 1.052, f = 3.690

-- score: -385.60 (accuracy -392.90, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.c * params.d) * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.925, c = 1.062, d = 1.012, e = 2.655
  Demo 1: a = 14.041, b = 36.211, c = 1.039, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.986, c = 1.022, d = 1.052, e = 3.690

-- score: -385.54 (accuracy -392.84, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= (params.c * params.d) * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.865, c = 1.051, d = 1.009, e = 2.646
  Demo 1: a = 14.041, b = 36.053, c = 1.008, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.711, c = 0.968, d = 1.051, e = 3.689

-- score: -385.52 (accuracy -391.92, token simplicity 4.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.912, b = 28.982, c = 1.033, d = 2.717
  Demo 1: a = 14.041, b = 35.867, c = 1.032, d = 2.050
  Demo 2: a = 8.490, b = 41.527, c = 1.035, d = 3.636

-- score: -385.51 (accuracy -394.61, token simplicity 5.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 3.560, e = 0.092, f = 0.953, g = 2.901
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -18.064, e = -0.218, f = 1.196, g = 1.354
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -17.614, e = -0.155, f = 1.124, g = 2.844

-- score: -385.49 (accuracy -393.39, token simplicity 5.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.x
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.423, c = 1.048, d = 0.081, e = 2.773
  Demo 1: a = 14.041, b = 35.496, c = 1.022, d = -0.077, e = 2.009
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = -0.058, e = 3.550

-- score: -385.44 (accuracy -393.64, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.x
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 0.056, e = 0.975, f = 2.718
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -0.102, e = 1.105, f = 1.962
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -0.053, e = 1.077, f = 3.566

## Round 9 | 0.34s | best score: -385.86 (stable)

+162 new programs (162 actually scored)
* linear_fit: +14
* quadratic_fit: +21
* add_single_terms: +66
* delete_interactions: +40
* delete_lines: +17
* delete_near_zeros: +0
* relate_parameters: +3
* snap_to_one: +1
* tie_parameters: +0

### 10 parents for the next round

-- score: -385.86 (accuracy -392.76, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = 1.052, e = 3.690

-- score: -385.77 (accuracy -392.87, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = 1.052, e = 3.690

-- score: -385.66 (accuracy -392.76, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 0.046, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 0.008, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -0.033, e = 3.690

-- score: -385.66 (accuracy -393.26, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 1.011, f = 2.650
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = 1.028, f = 2.042
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = 1.052, f = 3.690

-- score: -385.60 (accuracy -392.90, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.c * params.d) * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.925, c = 1.062, d = 1.012, e = 2.655
  Demo 1: a = 14.041, b = 36.211, c = 1.039, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.986, c = 1.022, d = 1.052, e = 3.690

-- score: -385.54 (accuracy -392.84, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= (params.c * params.d) * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.865, c = 1.051, d = 1.009, e = 2.646
  Demo 1: a = 14.041, b = 36.053, c = 1.008, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.711, c = 0.968, d = 1.051, e = 3.689

-- score: -385.52 (accuracy -391.92, token simplicity 4.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.912, b = 28.982, c = 1.033, d = 2.717
  Demo 1: a = 14.041, b = 35.867, c = 1.032, d = 2.050
  Demo 2: a = 8.490, b = 41.527, c = 1.035, d = 3.636

-- score: -385.51 (accuracy -394.61, token simplicity 5.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 3.560, e = 0.092, f = 0.953, g = 2.901
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -18.064, e = -0.218, f = 1.196, g = 1.354
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -17.614, e = -0.155, f = 1.124, g = 2.844

-- score: -385.49 (accuracy -393.39, token simplicity 5.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.x
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.423, c = 1.048, d = 0.081, e = 2.773
  Demo 1: a = 14.041, b = 35.496, c = 1.022, d = -0.077, e = 2.009
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = -0.058, e = 3.550

-- score: -385.44 (accuracy -393.64, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.x
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 0.056, e = 0.975, f = 2.718
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -0.102, e = 1.105, f = 1.962
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -0.053, e = 1.077, f = 3.566

## Round 10 | 0.06s | best score: -385.86 (stable)

+54 new programs (54 actually scored)
* linear_fit: +4
* quadratic_fit: +7
* add_single_terms: +23
* delete_interactions: +13
* delete_lines: +6
* delete_near_zeros: +0
* relate_parameters: +1
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -385.86 (accuracy -392.76, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = 1.052, e = 3.690

-- score: -385.77 (accuracy -392.87, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.891, c = 1.062, d = 1.011, e = 2.650
  Demo 1: a = 14.041, b = 36.131, c = 1.038, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = 1.052, e = 3.690

-- score: -385.66 (accuracy -392.76, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 0.046, e = 2.650
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = 0.008, e = 2.042
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -0.033, e = 3.690

-- score: -385.66 (accuracy -393.26, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 31.031, c = 1.083, d = 1.534, e = 1.011, f = 2.650
  Demo 1: a = 14.041, b = 36.254, c = 1.040, d = 1.085, e = 1.028, f = 2.042
  Demo 2: a = 8.490, b = 40.988, c = 1.022, d = 1.075, e = 1.052, f = 3.690

-- score: -385.60 (accuracy -392.90, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.c * params.d) * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.925, c = 1.062, d = 1.012, e = 2.655
  Demo 1: a = 14.041, b = 36.211, c = 1.039, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.986, c = 1.022, d = 1.052, e = 3.690

-- score: -385.54 (accuracy -392.84, token simplicity 4.80, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= (params.c * params.d) * data.x * data.z
diff.y -= params.c * data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.865, c = 1.051, d = 1.009, e = 2.646
  Demo 1: a = 14.041, b = 36.053, c = 1.008, d = 1.028, e = 2.042
  Demo 2: a = 8.490, b = 40.711, c = 0.968, d = 1.051, e = 3.689

-- score: -385.52 (accuracy -391.92, token simplicity 4.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.912, b = 28.982, c = 1.033, d = 2.717
  Demo 1: a = 14.041, b = 35.867, c = 1.032, d = 2.050
  Demo 2: a = 8.490, b = 41.527, c = 1.035, d = 3.636

-- score: -385.51 (accuracy -394.61, token simplicity 5.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d
diff.z += params.e * data.x * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 3.560, e = 0.092, f = 0.953, g = 2.901
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -18.064, e = -0.218, f = 1.196, g = 1.354
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -17.614, e = -0.155, f = 1.124, g = 2.844

-- score: -385.49 (accuracy -393.39, token simplicity 5.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.x
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.912, b = 29.423, c = 1.048, d = 0.081, e = 2.773
  Demo 1: a = 14.041, b = 35.496, c = 1.022, d = -0.077, e = 2.009
  Demo 2: a = 8.490, b = 40.845, c = 1.020, d = -0.058, e = 3.550

-- score: -385.44 (accuracy -393.64, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.x
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.912, b = 29.691, c = 1.057, d = 0.056, e = 0.975, f = 2.718
  Demo 1: a = 14.041, b = 36.028, c = 1.036, d = -0.102, e = 1.105, f = 1.962
  Demo 2: a = 8.490, b = 40.784, c = 1.019, d = -0.053, e = 1.077, f = 3.566

