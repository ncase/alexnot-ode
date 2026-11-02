# lorenz

Solved in 11.04 seconds. 5984 programs considered, over 12 rounds.

## Winner

-- score: -235.03 (accuracy -241.23, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.962
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 3.537

## Runner-ups

-- score: -234.97 (accuracy -241.87, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.063, e = 3.748

-- score: -234.90 (accuracy -240.40, token simplicity 4.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.c * data.z
  Demo 0: a = 9.688, b = 28.073, c = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.962
  Demo 2: a = 8.704, b = 40.022, c = 3.537

-- score: -234.87 (accuracy -241.67, token simplicity 4.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.339, c = -0.199, d = 2.586
  Demo 1: a = 13.263, b = 34.445, c = 0.002, d = 1.962
  Demo 2: a = 8.704, b = 40.084, c = -0.017, d = 3.537

-- score: -234.83 (accuracy -241.03, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.000, d = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.020, d = 2.005
  Demo 2: a = 8.704, b = 40.022, c = 1.063, d = 3.748

# The Search

## Round 0 | 0.03s | best score: -226.62

+39 new programs (39 actually scored)
* linear_fit: +2
* quadratic_fit: +7
* add_single_terms: +30
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -226.62 (accuracy -248.32, token simplicity 12.20, parameter simplicity 9.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i
diff.y += params.j * data.x
diff.y -= params.k * data.x * data.z
diff.y += params.l * data.y
diff.y += params.m * data.y * data.z
diff.y += params.n * data.z
diff.z += params.o
diff.z += params.p * data.x
diff.z += params.q * data.x * data.y
diff.z += params.r * data.y
diff.z -= params.s * data.z
  Demo 0: a = 9.986, b = -3.334, c = 0.314, d = -0.254, e = 0.211, f = 6.429, g = 0.139, h = -0.789, i = -13.410, j = 28.135, k = 0.986, l = 2.754, m = -0.166, n = 0.586, o = -4.509, p = 1.665, q = 0.900, r = 0.336, s = 2.685
  Demo 1: a = 37.489, b = 34.105, c = 0.558, d = -0.368, e = 1.119, f = -17.234, g = 0.717, h = -1.331, i = -9.417, j = 47.153, k = 1.314, l = -9.268, m = 0.216, n = 0.363, o = -5.632, p = -0.801, q = 1.010, r = 0.783, s = 1.796
  Demo 2: a = -16.145, b = -4.196, c = -0.163, d = 0.049, e = 0.105, f = 5.395, g = 0.088, h = 0.817, i = 0.606, j = 38.933, k = 0.979, l = -0.692, m = -0.002, n = -0.090, o = 3.226, p = 0.507, q = 1.069, r = -0.519, s = 3.858

-- score: -225.17 (accuracy -249.87, token simplicity 14.20, parameter simplicity 10.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.y
diff.x -= params.c * data.x * data.z
diff.x += params.d * data.y
diff.x += params.e * data.y * data.y
diff.x += params.f * data.y * data.z
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
diff.z += params.q * data.x * data.y
diff.z += params.r * data.y
diff.z += params.s * data.y * data.y
diff.z += params.t * data.y * data.z
diff.z -= params.u * data.z
  Demo 0: a = -7.598, b = -0.081, c = 0.050, d = 8.845, e = -0.036, f = 0.088, g = -0.278, h = 17.715, i = 27.304, j = -0.194, k = 0.921, l = 3.199, m = -0.139, n = 0.698, o = -6.350, p = -0.304, q = 1.191, r = 2.350, s = -0.222, t = -0.022, u = 2.506
  Demo 1: a = 26.722, b = 0.526, c = 0.917, d = -10.312, e = -0.376, f = 0.524, g = 0.073, h = 9.012, i = 47.392, j = 0.007, k = 1.319, l = -9.410, m = 0.218, n = 0.337, o = -27.807, p = -1.155, q = 0.415, r = -1.540, s = 0.481, t = 0.077, u = 1.116
  Demo 2: a = -3.996, b = -0.067, c = 0.103, d = 5.480, e = 0.025, f = 0.084, g = -0.032, h = 1.820, i = 38.829, j = -0.019, k = 0.978, l = -0.674, m = -0.001, n = 0.052, o = 0.153, p = 0.279, q = 1.013, r = -1.346, s = 0.036, t = 0.028, u = 3.772

-- score: -219.05 (accuracy -251.15, token simplicity 18.60, parameter simplicity 13.50) --
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
diff.y -= params.n * data.x * data.z
diff.y += params.o * data.y
diff.y += params.p * data.y * data.y
diff.y += params.q * data.y * data.z
diff.y += params.r * data.z
diff.y += params.s * data.z * data.z
diff.z += params.t
diff.z += params.u * data.x
diff.z -= params.v * data.x * data.x
diff.z += params.w * data.x * data.y
diff.z += params.x * data.x * data.z
diff.z += params.y * data.y
diff.z += params.z * data.y * data.z
diff.z -= params.p26 * data.z
  Demo 0: a = 4.977, b = -3.866, c = 0.342, d = -0.287, e = 0.182, f = 6.604, g = 0.011, h = 0.128, i = -0.162, j = -0.018, k = -20.473, l = 23.782, m = -0.239, n = 0.783, o = 3.996, p = 0.068, q = -0.203, r = 1.398, s = -0.021, t = 10.157, u = -0.951, v = 0.118, w = 0.864, x = 0.125, y = 0.185, z = 0.052, p26 = 3.445
  Demo 1: a = -17.492, b = 31.899, c = 0.384, d = 0.230, e = 1.035, f = -13.406, g = -0.377, h = 0.593, i = 2.920, j = -0.070, k = 30.774, l = 50.573, m = 0.013, n = 1.405, o = -11.914, p = -0.011, q = 0.288, r = -2.410, s = 0.044, t = -27.080, u = 5.268, v = 0.343, w = 1.274, x = -0.120, y = -3.680, z = 0.095, p26 = 0.916
  Demo 2: a = 48.960, b = -0.365, c = -0.626, d = 0.193, e = 0.187, f = 4.259, g = 0.045, h = 0.111, i = -5.037, j = 0.123, k = 42.682, l = 42.484, m = -0.359, n = 1.052, o = -1.865, p = 0.108, q = 0.022, r = -4.419, s = 0.095, t = -15.679, u = 0.113, v = 0.161, w = 1.143, x = -0.003, y = -1.441, z = 0.033, p26 = 2.934

-- score: -217.82 (accuracy -252.52, token simplicity 20.20, parameter simplicity 14.50) --
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
diff.y += params.p * data.y
diff.y += params.q * data.y * data.y
diff.y += params.r * data.y * data.z
diff.y += params.s * data.z
diff.y += params.t * data.z * data.z
diff.z += params.u
diff.z += params.v * data.x
diff.z += params.w * data.x * data.y
diff.z += params.x * data.x * data.z
diff.z += params.y * data.y
diff.z += params.z * data.y * data.y
diff.z += params.p26 * data.y * data.z
diff.z += params.p27 * data.z
diff.z += params.p28 * data.z * data.z
  Demo 0: a = 4.977, b = -3.866, c = 0.342, d = -0.287, e = 0.182, f = 6.604, g = 0.011, h = 0.128, i = -0.162, j = -0.018, k = -18.726, l = 26.219, m = -0.127, n = -0.444, o = 0.758, p = 0.864, q = 0.258, r = -0.094, s = 2.032, t = -0.066, u = 30.401, v = 3.017, w = 1.344, x = -0.202, y = 1.085, z = -0.266, p26 = 0.018, p27 = -6.556, p28 = 0.111
  Demo 1: a = -17.492, b = 31.899, c = 0.384, d = 0.230, e = 1.035, f = -13.406, g = -0.377, h = 0.593, i = 2.920, j = -0.070, k = 19.448, l = 52.208, m = 0.202, n = -0.287, o = 1.451, p = -13.123, q = 0.103, r = 0.324, s = -1.456, t = 0.024, u = 5.709, v = 7.608, w = 0.383, x = -0.212, y = -7.734, z = 0.509, p26 = 0.230, p27 = -3.524, p28 = 0.040
  Demo 2: a = 48.960, b = -0.365, c = -0.626, d = 0.193, e = 0.187, f = 4.259, g = 0.045, h = 0.111, i = -5.037, j = 0.123, k = 49.541, l = 42.915, m = -0.476, n = 0.082, o = 1.064, p = -2.012, q = 0.090, r = 0.025, s = -5.105, t = 0.114, u = -60.422, v = -2.094, w = 1.139, x = 0.040, y = -0.867, z = -0.046, p26 = 0.023, p27 = 0.755, p28 = -0.067

-- score: -217.52 (accuracy -252.22, token simplicity 20.20, parameter simplicity 14.50) --
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
diff.y += params.p * data.y
diff.y += params.q * data.y * data.y
diff.y += params.r * data.y * data.z
diff.y += params.s * data.z
diff.y += params.t * data.z * data.z
diff.z -= params.u
diff.z += params.v * data.x
diff.z += params.w * data.x * data.x
diff.z += params.x * data.x * data.y
diff.z += params.y * data.x * data.z
diff.z += params.z * data.y
diff.z += params.p26 * data.y * data.y
diff.z += params.p27 * data.y * data.z
diff.z -= params.p28 * data.z
  Demo 0: a = 4.977, b = -3.866, c = 0.342, d = -0.287, e = 0.182, f = 6.604, g = 0.011, h = 0.128, i = -0.162, j = -0.018, k = -18.726, l = 26.219, m = -0.127, n = -0.444, o = 0.758, p = 0.864, q = 0.258, r = -0.094, s = 2.032, t = -0.066, u = 8.756, v = -4.296, w = -0.141, x = 1.306, y = 0.134, z = 4.400, p26 = -0.234, p27 = -0.095, p28 = 2.322
  Demo 1: a = -17.492, b = 31.899, c = 0.384, d = 0.230, e = 1.035, f = -13.406, g = -0.377, h = 0.593, i = 2.920, j = -0.070, k = 19.448, l = 52.208, m = 0.202, n = -0.287, o = 1.451, p = -13.123, q = 0.103, r = 0.324, s = -1.456, t = 0.024, u = 20.417, v = 9.292, w = 0.204, x = 0.149, y = -0.255, z = -8.491, p26 = 0.571, p27 = 0.249, p28 = 1.404
  Demo 2: a = 48.960, b = -0.365, c = -0.626, d = 0.193, e = 0.187, f = 4.259, g = 0.045, h = 0.111, i = -5.037, j = 0.123, k = 49.541, l = 42.915, m = -0.476, n = 0.082, o = 1.064, p = -2.012, q = 0.090, r = 0.025, s = -5.105, t = 0.114, u = 15.695, v = 0.152, w = -0.157, x = 1.134, y = -0.004, z = -1.455, p26 = 0.005, p27 = 0.033, p28 = 2.946

-- score: -216.96 (accuracy -252.96, token simplicity 21.00, parameter simplicity 15.00) --
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
diff.z += params.p27 * data.y * data.z
diff.z += params.p28 * data.z
diff.z += params.p29 * data.z * data.z
  Demo 0: a = 4.977, b = -3.866, c = 0.342, d = -0.287, e = 0.182, f = 6.604, g = 0.011, h = 0.128, i = -0.162, j = -0.018, k = -18.726, l = 26.219, m = -0.127, n = -0.444, o = 0.758, p = 0.864, q = 0.258, r = -0.094, s = 2.032, t = -0.066, u = 56.518, v = 2.691, w = -0.492, x = 1.714, y = -0.248, z = 1.974, p26 = -0.362, p27 = 0.053, p28 = -10.441, p29 = 0.237
  Demo 1: a = -17.492, b = 31.899, c = 0.384, d = 0.230, e = 1.035, f = -13.406, g = -0.377, h = 0.593, i = 2.920, j = -0.070, k = 19.448, l = 52.208, m = 0.202, n = -0.287, o = 1.451, p = -13.123, q = 0.103, r = 0.324, s = -1.456, t = 0.024, u = -8.868, v = 9.169, w = 0.158, x = 0.188, y = -0.253, z = -8.617, p26 = 0.568, p27 = 0.253, p28 = -2.302, p29 = 0.016
  Demo 2: a = 48.960, b = -0.365, c = -0.626, d = 0.193, e = 0.187, f = 4.259, g = 0.045, h = 0.111, i = -5.037, j = 0.123, k = 49.541, l = 42.915, m = -0.476, n = 0.082, o = 1.064, p = -2.012, q = 0.090, r = 0.025, s = -5.105, t = 0.114, u = -105.086, v = -5.273, w = 0.461, x = 0.973, y = 0.111, z = 0.165, p26 = -0.077, p27 = 0.002, p28 = 5.148, p29 = -0.168

-- score: -206.50 (accuracy -233.10, token simplicity 15.60, parameter simplicity 11.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.y
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
diff.z += params.r * data.x * data.x
diff.z += params.s * data.x * data.y
diff.z += params.t * data.y
diff.z += params.u * data.y * data.y
diff.z -= params.v * data.z
  Demo 0: a = 10.048, b = -3.323, c = 0.315, d = -0.255, e = 0.211, f = 6.415, g = 0.001, h = 0.139, i = -0.792, j = 10.078, k = -0.397, l = -0.835, m = 3.175, n = 0.654, o = 0.248, p = 3.209, q = -0.159, r = 0.019, s = 1.141, t = 1.545, u = -0.193, v = 2.796
  Demo 1: a = 32.953, b = 31.365, c = 0.186, d = 0.398, e = 1.027, f = -13.959, g = -0.389, h = 0.613, i = -0.999, j = -8.197, k = -0.757, l = 0.848, m = 26.109, n = -0.224, o = 0.630, p = -1.366, q = 0.045, r = 0.088, s = 0.524, t = -0.153, u = 0.349, v = 2.060
  Demo 2: a = -16.096, b = -4.313, c = -0.176, d = 0.076, e = 0.104, f = 5.438, g = -0.014, h = 0.088, i = 0.854, j = -7.826, k = 0.812, l = -0.228, m = 22.858, n = -0.115, o = 0.538, p = 5.055, q = -0.153, r = -0.071, s = 1.107, t = -0.274, u = -0.004, v = 3.569

-- score: -110.47 (accuracy -121.97, token simplicity 6.00, parameter simplicity 5.50) --
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
  Demo 0: a = -2.483, b = 9.657, c = 9.810, d = 162.549, e = 0.291, f = 0.584, g = 7.265, h = 50.302, i = 8.224, j = 7.943, k = -2.346
  Demo 1: a = 0.848, b = 13.287, c = 13.278, d = 43.101, e = -15.377, f = 11.675, g = 1.317, h = 24.929, i = -5.012, j = 8.931, k = 0.963
  Demo 2: a = -0.717, b = 8.747, c = 8.699, d = 57.026, e = -13.521, f = 7.813, g = 0.948, h = 19.347, i = -2.384, j = 2.887, k = 0.293

-- score: -109.49 (accuracy -122.09, token simplicity 6.60, parameter simplicity 6.00) --
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
  Demo 0: a = -2.894, b = 9.695, c = 9.829, d = 0.022, e = 162.549, f = 0.291, g = 0.584, h = 7.265, i = 50.302, j = 8.224, k = 7.943, l = -2.346
  Demo 1: a = 5.897, b = 13.101, c = 13.117, d = -0.165, e = 43.101, f = -15.377, g = 11.675, h = 1.317, i = 24.929, j = -5.012, k = 8.931, l = 0.963
  Demo 2: a = 7.688, b = 8.693, c = 8.690, d = -0.271, e = 57.026, f = -13.521, g = 7.813, h = 0.948, i = 19.347, j = -2.384, k = 2.887, l = 0.293

-- score: -33.90 (accuracy -35.20, token simplicity 0.80, parameter simplicity 0.50) --
diff.z += params.a * data.x * data.y
  Demo 0: a = 0.583
  Demo 1: a = 0.691
  Demo 2: a = 0.650

## Round 1 | 3.20s | best score: -229.50

+907 new programs (907 actually scored)
* linear_fit: +6
* quadratic_fit: +33
* add_single_terms: +93
* delete_interactions: +407
* delete_lines: +198
* delete_near_zeros: +20
* relate_parameters: +145
* snap_to_one: +0
* tie_parameters: +5

### 10 parents for the next round

-- score: -229.50 (accuracy -242.90, token simplicity 7.40, parameter simplicity 6.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x
diff.z += params.j * data.x * data.y
diff.z += params.k * data.y
diff.z -= params.l * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = -4.509, i = 1.665, j = 0.900, k = 0.336, l = 2.685
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = -5.632, i = -0.801, j = 1.010, k = 0.783, l = 1.796
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = 3.226, i = 0.507, j = 1.069, k = -0.519, l = 3.858

-- score: -228.23 (accuracy -249.23, token simplicity 12.00, parameter simplicity 9.00) --
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
diff.y += params.l * data.z
diff.z -= params.m
diff.z += params.n * data.x
diff.z += params.o * data.x * data.y
diff.z += params.p * data.y
diff.z += params.q * data.y * data.y
diff.z -= params.r * data.z
  Demo 0: a = -10.522, b = 0.126, c = 0.003, d = 10.291, e = -0.098, f = 0.005, g = -13.410, h = 28.135, i = 0.986, j = 2.754, k = -0.166, l = 0.586, m = 3.490, n = 0.119, o = 1.132, p = 1.771, q = -0.194, r = 2.674
  Demo 1: a = 25.703, b = 0.533, c = 0.889, d = -9.596, e = -0.372, f = 0.502, g = -9.417, h = 47.153, i = 1.314, j = -9.268, k = 0.216, l = 0.363, m = 29.203, n = -0.493, o = 0.511, p = 0.330, q = 0.412, r = 1.118
  Demo 2: a = -4.261, b = -0.068, c = 0.099, d = 5.601, e = 0.024, f = 0.082, g = 0.606, h = 38.933, i = 0.979, j = -0.692, k = -0.002, l = -0.090, m = 0.883, n = 0.558, o = 1.014, p = -0.548, q = 0.037, r = 3.758

-- score: -227.50 (accuracy -248.10, token simplicity 11.60, parameter simplicity 9.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i
diff.y += params.j * data.x
diff.y -= params.k * data.x * data.z
diff.y += params.l * data.y
diff.y += params.m * data.y * data.z
diff.y += params.n * data.z
diff.z += params.o
diff.z += params.p * data.x
diff.z += params.q * data.x * data.y
diff.z -= params.r * data.z
  Demo 0: a = 9.986, b = -3.334, c = 0.314, d = -0.254, e = 0.211, f = 6.429, g = 0.139, h = -0.789, i = -13.410, j = 28.135, k = 0.986, l = 2.754, m = -0.166, n = 0.586, o = -2.098, p = 1.603, q = 0.927, r = 2.741
  Demo 1: a = 37.489, b = 34.105, c = 0.558, d = -0.368, e = 1.119, f = -17.234, g = 0.717, h = -1.331, i = -9.417, j = 47.153, k = 1.314, l = -9.268, m = 0.216, n = 0.363, o = -1.569, p = -0.044, q = 1.022, r = 1.961
  Demo 2: a = -16.145, b = -4.196, c = -0.163, d = 0.049, e = 0.105, f = 5.395, g = 0.088, h = 0.817, i = 0.606, j = 38.933, k = 0.979, l = -0.692, m = -0.002, n = -0.090, o = 3.053, p = -0.005, q = 1.064, r = 3.832

-- score: -227.49 (accuracy -248.09, token simplicity 11.60, parameter simplicity 9.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i
diff.y += params.j * data.x
diff.y -= params.k * data.x * data.z
diff.y += params.l * data.y
diff.y += params.m * data.y * data.z
diff.z += params.n
diff.z += params.o * data.x
diff.z += params.p * data.x * data.y
diff.z += params.q * data.y
diff.z -= params.r * data.z
  Demo 0: a = 9.986, b = -3.334, c = 0.314, d = -0.254, e = 0.211, f = 6.429, g = 0.139, h = -0.789, i = -0.861, j = 27.588, k = 0.953, l = 2.178, m = -0.148, n = -4.509, o = 1.665, p = 0.900, q = 0.336, r = 2.685
  Demo 1: a = 37.489, b = 34.105, c = 0.558, d = -0.368, e = 1.119, f = -17.234, g = 0.717, h = -1.331, i = 1.646, j = 46.092, k = 1.283, l = -8.988, m = 0.206, n = -5.632, o = -0.801, p = 1.010, q = 0.783, r = 1.796
  Demo 2: a = -16.145, b = -4.196, c = -0.163, d = 0.049, e = 0.105, f = 5.395, g = 0.088, h = 0.817, i = -2.270, j = 39.037, k = 0.981, l = -0.735, m = -0.001, n = 3.226, o = 0.507, p = 1.069, q = -0.519, r = 3.858

-- score: -227.46 (accuracy -248.26, token simplicity 11.80, parameter simplicity 9.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i
diff.y += params.j * data.x
diff.y -= params.k * data.x * data.z
diff.y += params.l * data.y
diff.y += params.m * data.y * data.z
diff.y += params.n * data.z
diff.z += params.o * data.x
diff.z += params.p * data.x * data.y
diff.z += params.q * data.y
diff.z -= params.r * data.z
  Demo 0: a = 9.986, b = -3.334, c = 0.314, d = -0.254, e = 0.211, f = 6.429, g = 0.139, h = -0.789, i = -13.410, j = 28.135, k = 0.986, l = 2.754, m = -0.166, n = 0.586, o = 1.715, p = 0.924, q = -0.016, r = 2.839
  Demo 1: a = 37.489, b = 34.105, c = 0.558, d = -0.368, e = 1.119, f = -17.234, g = 0.717, h = -1.331, i = -9.417, j = 47.153, k = 1.314, l = -9.268, m = 0.216, n = 0.363, o = -0.623, p = 1.011, q = 0.617, r = 1.968
  Demo 2: a = -16.145, b = -4.196, c = -0.163, d = 0.049, e = 0.105, f = 5.395, g = 0.088, h = 0.817, i = 0.606, j = 38.933, k = 0.979, l = -0.692, m = -0.002, n = -0.090, o = 0.506, p = 1.069, q = -0.517, r = 3.770

-- score: -227.40 (accuracy -248.00, token simplicity 11.60, parameter simplicity 9.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i
diff.y += params.j * data.x
diff.y -= params.k * data.x * data.z
diff.y += params.l * data.y
diff.y += params.m * data.y * data.z
diff.y += params.n * data.z
diff.z += params.o
diff.z += params.p * data.x * data.y
diff.z += params.q * data.y
diff.z -= params.r * data.z
  Demo 0: a = 9.986, b = -3.334, c = 0.314, d = -0.254, e = 0.211, f = 6.429, g = 0.139, h = -0.789, i = -13.410, j = 28.135, k = 0.986, l = 2.754, m = -0.166, n = 0.586, o = -5.852, p = 0.992, q = 0.096, r = 2.366
  Demo 1: a = 37.489, b = 34.105, c = 0.558, d = -0.368, e = 1.119, f = -17.234, g = 0.717, h = -1.331, i = -9.417, j = 47.153, k = 1.314, l = -9.268, m = 0.216, n = 0.363, o = -1.850, p = 1.015, q = 0.122, r = 1.944
  Demo 2: a = -16.145, b = -4.196, c = -0.163, d = 0.049, e = 0.105, f = 5.395, g = 0.088, h = 0.817, i = 0.606, j = 38.933, k = 0.979, l = -0.692, m = -0.002, n = -0.090, o = 3.210, p = 1.066, q = -0.226, r = 3.825

-- score: -227.32 (accuracy -248.12, token simplicity 11.80, parameter simplicity 9.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i * data.x
diff.y -= params.j * data.x * data.z
diff.y += params.k * data.y
diff.y += params.l * data.y * data.z
diff.y += params.m * data.z
diff.z += params.n
diff.z += params.o * data.x
diff.z += params.p * data.x * data.y
diff.z += params.q * data.y
diff.z -= params.r * data.z
  Demo 0: a = 9.986, b = -3.334, c = 0.314, d = -0.254, e = 0.211, f = 6.429, g = 0.139, h = -0.789, i = 27.673, j = 0.958, k = 1.963, l = -0.141, m = 0.004, n = -4.509, o = 1.665, p = 0.900, q = 0.336, r = 2.685
  Demo 1: a = 37.489, b = 34.105, c = 0.558, d = -0.368, e = 1.119, f = -17.234, g = 0.717, h = -1.331, i = 46.880, j = 1.303, k = -9.475, l = 0.220, m = 0.081, n = -5.632, o = -0.801, p = 1.010, q = 0.783, r = 1.796
  Demo 2: a = -16.145, b = -4.196, c = -0.163, d = 0.049, e = 0.105, f = 5.395, g = 0.088, h = 0.817, i = 38.991, j = 0.980, k = -0.718, l = -0.001, m = -0.075, n = 3.226, o = 0.507, p = 1.069, q = -0.519, r = 3.858

-- score: -227.27 (accuracy -245.47, token simplicity 10.20, parameter simplicity 8.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.x += params.c * data.z
diff.y -= params.d
diff.y += params.e * data.x
diff.y += params.f * data.x * data.x
diff.y -= params.g * data.x * data.z
diff.y += params.h * data.y
diff.y += params.i * data.y * data.z
diff.y += params.j * data.z
diff.z -= params.k
diff.z += params.l * data.x
diff.z += params.m * data.x * data.y
diff.z += params.n * data.y
diff.z += params.o * data.y * data.y
diff.z -= params.p * data.z
  Demo 0: a = 9.499, b = 9.696, c = -0.105, d = 17.715, e = 27.304, f = -0.194, g = 0.921, h = 3.199, i = -0.139, j = 0.698, k = 3.490, l = 0.119, m = 1.132, n = 1.771, o = -0.194, p = 2.674
  Demo 1: a = 13.282, b = 13.282, c = 0.012, d = 9.012, e = 47.392, f = 0.007, g = 1.319, h = -9.410, i = 0.218, j = 0.337, k = 29.203, l = -0.493, m = 0.511, n = 0.330, o = 0.412, p = 1.118
  Demo 2: a = 8.691, b = 8.693, c = -0.063, d = 1.820, e = 38.829, f = -0.019, g = 0.978, h = -0.674, i = -0.001, j = 0.052, k = 0.883, l = 0.558, m = 1.014, n = -0.548, o = 0.037, p = 3.758

-- score: -227.21 (accuracy -247.81, token simplicity 11.60, parameter simplicity 9.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.y
diff.x -= params.e * data.x * data.z
diff.x += params.f * data.y
diff.x += params.g * data.y * data.z
diff.x += params.h * data.z
diff.y += params.i
diff.y += params.j * data.x
diff.y -= params.k * data.x * data.z
diff.y -= params.l * data.y * data.z
diff.y += params.m * data.z
diff.z += params.n
diff.z += params.o * data.x
diff.z += params.p * data.x * data.y
diff.z += params.q * data.y
diff.z -= params.r * data.z
  Demo 0: a = 9.986, b = -3.334, c = 0.314, d = -0.254, e = 0.211, f = 6.429, g = 0.139, h = -0.789, i = -7.542, j = 31.050, k = 1.079, l = 0.071, m = 0.388, n = -4.509, o = 1.665, p = 0.900, q = 0.336, r = 2.685
  Demo 1: a = 37.489, b = 34.105, c = 0.558, d = -0.368, e = 1.119, f = -17.234, g = 0.717, h = -1.331, i = -10.487, j = 33.630, k = 1.004, l = 0.002, m = 0.326, n = -5.632, o = -0.801, p = 1.010, q = 0.783, r = 1.796
  Demo 2: a = -16.145, b = -4.196, c = -0.163, d = 0.049, e = 0.105, f = 5.395, g = 0.088, h = 0.817, i = 1.354, j = 37.853, k = 0.956, l = 0.018, m = -0.097, n = 3.226, o = 0.507, p = 1.069, q = -0.519, r = 3.858

-- score: -227.09 (accuracy -243.79, token simplicity 9.20, parameter simplicity 7.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
diff.x += params.d * data.x * data.z
diff.x += params.e * data.y
diff.x += params.f * data.z
diff.y += params.g
diff.y += params.h * data.x
diff.y -= params.i * data.x * data.z
diff.y -= params.j * data.y
diff.z += params.k
diff.z += params.l * data.x
diff.z += params.m * data.x * data.y
diff.z += params.n * data.y
diff.z -= params.o * data.z
  Demo 0: a = 7.837, b = 9.604, c = 0.158, d = -0.032, e = 8.961, f = -0.381, g = 1.712, h = 32.057, i = 1.112, j = 1.804, k = -4.509, l = 1.665, m = 0.900, n = 0.336, o = 2.685
  Demo 1: a = 7.906, b = 7.908, c = 0.094, d = -0.106, e = 11.465, f = -0.435, g = -0.568, h = 34.396, i = 1.009, j = 0.602, k = -5.632, l = -0.801, m = 1.010, n = 0.783, o = 1.796
  Demo 2: a = -1.731, b = 9.151, c = -0.073, d = 0.005, e = 8.860, f = 0.284, g = -2.293, h = 39.083, i = 0.982, j = 0.766, k = 3.226, l = 0.507, m = 1.069, n = -0.519, o = 3.858

## Round 2 | 1.87s | best score: -230.62

+891 new programs (891 actually scored)
* linear_fit: +10
* quadratic_fit: +34
* add_single_terms: +120
* delete_interactions: +329
* delete_lines: +158
* delete_near_zeros: +12
* relate_parameters: +217
* snap_to_one: +0
* tie_parameters: +11

### 10 parents for the next round

-- score: -230.62 (accuracy -242.72, token simplicity 6.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = -4.509, h = 1.665, i = 0.900, j = 0.336, k = 2.685
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -5.632, h = -0.801, i = 1.010, j = 0.783, k = 1.796
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = 3.226, h = 0.507, i = 1.069, j = -0.519, k = 3.858

-- score: -230.39 (accuracy -242.69, token simplicity 6.80, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x
diff.z += params.j * data.x * data.y
diff.z -= params.k * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = -2.098, i = 1.603, j = 0.927, k = 2.741
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = -1.569, i = -0.044, j = 1.022, k = 1.961
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = 3.053, i = -0.005, j = 1.064, k = 3.832

-- score: -230.35 (accuracy -242.85, token simplicity 7.00, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = 1.715, i = 0.924, j = -0.016, k = 2.839
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = -0.623, i = 1.011, j = 0.617, k = 1.968
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = 0.506, i = 1.069, j = -0.517, k = 3.770

-- score: -230.33 (accuracy -242.83, token simplicity 7.00, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 32.380, e = 1.117, f = 1.783, g = -4.509, h = 1.665, i = 0.900, j = 0.336, k = 2.685
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = 34.336, e = 1.008, f = 0.582, g = -5.632, h = -0.801, i = 1.010, j = 0.783, k = 1.796
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = 38.684, e = 0.976, f = 0.705, g = 3.226, h = 0.507, i = 1.069, j = -0.519, k = 3.858

-- score: -230.29 (accuracy -242.59, token simplicity 6.80, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = -5.852, i = 0.992, j = 0.096, k = 2.366
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = -1.850, i = 1.015, j = 0.122, k = 1.944
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = 3.210, i = 1.066, j = -0.226, k = 3.825

-- score: -229.89 (accuracy -242.59, token simplicity 7.20, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= data.y
diff.z += params.g
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.355, e = 30.053, f = 1.071, g = -4.509, h = 1.665, i = 0.900, j = 0.336, k = 2.685
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.685, e = 35.437, f = 1.026, g = -5.632, h = -0.801, i = 1.010, j = 0.783, k = 1.796
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.625, e = 39.741, f = 0.992, g = 3.226, h = 0.507, i = 1.069, j = -0.519, k = 3.858

-- score: -229.83 (accuracy -244.53, token simplicity 8.20, parameter simplicity 6.50) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.x += params.d * data.y * data.z
diff.y += params.e
diff.y += params.f * data.x
diff.y -= params.g * data.x * data.z
diff.y -= params.h * data.y
diff.z += params.i
diff.z += params.j * data.x
diff.z += params.k * data.x * data.y
diff.z += params.l * data.y
diff.z -= params.m * data.z
  Demo 0: a = -10.158, b = 0.004, c = 9.420, d = 0.019, e = 1.712, f = 32.057, g = 1.112, h = 1.804, i = -4.509, j = 1.665, k = 0.900, l = 0.336, m = 2.685
  Demo 1: a = 14.113, b = -0.622, c = -4.475, d = 0.408, e = -0.568, f = 34.396, g = 1.009, h = 0.602, i = -5.632, j = -0.801, k = 1.010, l = 0.783, m = 1.796
  Demo 2: a = -4.862, b = -0.087, c = 5.931, d = 0.071, e = -2.293, f = 39.083, g = 0.982, h = 0.766, i = 3.226, j = 0.507, k = 1.069, l = -0.519, m = 3.858

-- score: -229.82 (accuracy -242.72, token simplicity 7.40, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x -= params.b * data.x * data.z
diff.x += params.a * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z += params.j * data.y
diff.z -= params.k * data.z
  Demo 0: a = 9.682, b = 0.002, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = -4.509, h = 1.665, i = 0.900, j = 0.336, k = 2.685
  Demo 1: a = 13.240, b = 0.002, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -5.632, h = -0.801, i = 1.010, j = 0.783, k = 1.796
  Demo 2: a = 8.687, b = 0.002, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = 3.226, h = 0.507, i = 1.069, j = -0.519, k = 3.858

-- score: -229.80 (accuracy -242.90, token simplicity 7.60, parameter simplicity 5.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z -= (params.a * params.h)
diff.z += params.i * data.x
diff.z += params.j * data.x * data.y
diff.z += params.h * data.y
diff.z -= params.k * data.z
  Demo 0: a = 10.808, b = 0.026, c = 9.934, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = 0.395, i = 1.714, j = 0.894, k = 2.707
  Demo 1: a = 9.442, b = -0.075, c = 12.255, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = 0.738, i = -0.763, j = 1.011, k = 1.760
  Demo 2: a = 8.559, b = -0.004, c = 8.667, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = -0.501, i = 0.487, j = 1.069, k = 3.887

-- score: -229.76 (accuracy -244.46, token simplicity 8.20, parameter simplicity 6.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z -= params.h
diff.z += params.i * data.x
diff.z += params.j * data.x * data.y
diff.z += params.k * data.y
diff.z += params.l * data.y * data.y
diff.z -= params.m * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = 3.490, i = 0.119, j = 1.132, k = 1.771, l = -0.194, m = 2.674
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = 29.203, i = -0.493, j = 0.511, k = 0.330, l = 0.412, m = 1.118
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = 0.883, i = 0.558, j = 1.014, k = -0.548, l = 0.037, m = 3.758

## Round 3 | 1.56s | best score: -232.44

+855 new programs (855 actually scored)
* linear_fit: +25
* quadratic_fit: +42
* add_single_terms: +168
* delete_interactions: +219
* delete_lines: +98
* delete_near_zeros: +4
* relate_parameters: +283
* snap_to_one: +0
* tie_parameters: +16

### 10 parents for the next round

-- score: -232.44 (accuracy -242.34, token simplicity 5.40, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = -5.133, h = 0.999, i = 2.385
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -1.474, h = 1.021, i = 1.963
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = 3.051, h = 1.064, i = 3.832

-- score: -232.39 (accuracy -242.49, token simplicity 5.60, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g * data.x
diff.z += params.h * data.x * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = 1.724, h = 0.923, i = 2.841
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -0.038, h = 1.021, i = 2.006
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = -0.003, h = 1.063, i = 3.748

-- score: -231.51 (accuracy -242.51, token simplicity 6.00, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = -2.098, h = 1.603, i = 0.927, j = 2.741
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -1.569, h = -0.044, i = 1.022, j = 1.961
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = 3.053, h = -0.005, i = 1.064, j = 3.832

-- score: -231.47 (accuracy -242.67, token simplicity 6.20, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g * data.x
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = 1.715, h = 0.924, i = -0.016, j = 2.839
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -0.623, h = 1.011, i = 0.617, j = 1.968
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = 0.506, h = 1.069, i = -0.517, j = 3.770

-- score: -231.45 (accuracy -242.65, token simplicity 6.20, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.791, b = 9.704, c = 32.380, d = 1.117, e = 1.783, f = -4.509, g = 1.665, h = 0.900, i = 0.336, j = 2.685
  Demo 1: a = 13.253, b = 13.263, c = 34.336, d = 1.008, e = 0.582, f = -5.632, g = -0.801, h = 1.010, i = 0.783, j = 1.796
  Demo 2: a = 8.772, b = 8.702, c = 38.684, d = 0.976, e = 0.705, f = 3.226, g = 0.507, h = 1.069, i = -0.519, j = 3.858

-- score: -231.41 (accuracy -242.41, token simplicity 6.00, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = -5.852, h = 0.992, i = 0.096, j = 2.366
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -1.850, h = 1.015, i = 0.122, j = 1.944
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = 3.210, h = 1.066, i = -0.226, j = 3.825

-- score: -231.32 (accuracy -242.52, token simplicity 6.20, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h
diff.z += params.i * data.x * data.y
diff.z -= params.j * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = -5.133, i = 0.999, j = 2.385
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = -1.474, i = 1.021, j = 1.963
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = 3.051, i = 1.064, j = 3.832

-- score: -231.27 (accuracy -242.67, token simplicity 6.40, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d
diff.y += params.e * data.x
diff.y -= params.f * data.x * data.z
diff.y -= params.g * data.y
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z -= params.j * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 1.712, e = 32.057, f = 1.112, g = 1.804, h = 1.724, i = 0.923, j = 2.841
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = -0.568, e = 34.396, f = 1.009, g = 0.602, h = -0.038, i = 1.021, j = 2.006
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = -2.293, e = 39.083, f = 0.982, g = 0.766, h = -0.003, i = 1.063, j = 3.748

-- score: -231.21 (accuracy -242.61, token simplicity 6.40, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x
diff.z += params.i * data.x * data.y
diff.z -= params.j * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 32.380, e = 1.117, f = 1.783, g = -2.098, h = 1.603, i = 0.927, j = 2.741
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = 34.336, e = 1.008, f = 0.582, g = -1.569, h = -0.044, i = 1.022, j = 1.961
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = 38.684, e = 0.976, f = 0.705, g = 3.053, h = -0.005, i = 1.064, j = 3.832

-- score: -231.18 (accuracy -242.78, token simplicity 6.60, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.x * data.z
diff.x += params.c * data.y
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g * data.x
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y
diff.z -= params.j * data.z
  Demo 0: a = 10.801, b = 0.026, c = 9.932, d = 32.380, e = 1.117, f = 1.783, g = 1.715, h = 0.924, i = -0.016, j = 2.839
  Demo 1: a = 9.491, b = -0.074, c = 12.270, d = 34.336, e = 1.008, f = 0.582, g = -0.623, h = 1.011, i = 0.617, j = 1.968
  Demo 2: a = 8.565, b = -0.004, c = 8.668, d = 38.684, e = 0.976, f = 0.705, g = 0.506, h = 1.069, i = -0.517, j = 3.770

## Round 4 | 0.88s | best score: -233.27

+760 new programs (760 actually scored)
* linear_fit: +3
* quadratic_fit: +3
* add_single_terms: +175
* delete_interactions: +176
* delete_lines: +78
* delete_near_zeros: +0
* relate_parameters: +305
* snap_to_one: +0
* tie_parameters: +20

### 10 parents for the next round

-- score: -233.27 (accuracy -242.27, token simplicity 5.00, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = 1.000, h = 2.586
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = 1.020, h = 2.005
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = 1.063, h = 3.748

-- score: -233.27 (accuracy -242.27, token simplicity 5.00, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.791, b = 9.704, c = 32.380, d = 1.117, e = 1.783, f = -5.133, g = 0.999, h = 2.385
  Demo 1: a = 13.253, b = 13.263, c = 34.336, d = 1.008, e = 0.582, f = -1.474, g = 1.021, h = 1.963
  Demo 2: a = 8.772, b = 8.702, c = 38.684, d = 0.976, e = 0.705, f = 3.051, g = 1.064, h = 3.832

-- score: -233.21 (accuracy -242.41, token simplicity 5.20, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.791, b = 9.704, c = 32.380, d = 1.117, e = 1.783, f = 1.724, g = 0.923, h = 2.841
  Demo 1: a = 13.253, b = 13.263, c = 34.336, d = 1.008, e = 0.582, f = -0.038, g = 1.021, h = 2.006
  Demo 2: a = 8.772, b = 8.702, c = 38.684, d = 0.976, e = 0.705, f = -0.003, g = 1.063, h = 3.748

-- score: -232.92 (accuracy -242.32, token simplicity 5.40, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.688, b = 1.712, c = 32.057, d = 1.112, e = 1.804, f = -5.133, g = 0.999, h = 2.385
  Demo 1: a = 13.263, b = -0.568, c = 34.396, d = 1.009, e = 0.602, f = -1.474, g = 1.021, h = 1.963
  Demo 2: a = 8.704, b = -2.293, c = 39.083, d = 0.982, e = 0.766, f = 3.051, g = 1.064, h = 3.832

-- score: -232.87 (accuracy -242.47, token simplicity 5.60, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.688, b = 1.712, c = 32.057, d = 1.112, e = 1.804, f = 1.724, g = 0.923, h = 2.841
  Demo 1: a = 13.263, b = -0.568, c = 34.396, d = 1.009, e = 0.602, f = -0.038, g = 1.021, h = 2.006
  Demo 2: a = 8.704, b = -2.293, c = 39.083, d = 0.982, e = 0.766, f = -0.003, g = 1.063, h = 3.748

-- score: -232.83 (accuracy -242.03, token simplicity 5.20, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= data.y
diff.z += params.f
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.355, d = 30.053, e = 1.071, f = -5.133, g = 0.999, h = 2.385
  Demo 1: a = 13.253, b = 13.263, c = -0.685, d = 35.437, e = 1.026, f = -1.474, g = 1.021, h = 1.963
  Demo 2: a = 8.772, b = 8.702, c = -2.625, d = 39.741, e = 0.992, f = 3.051, g = 1.064, h = 3.832

-- score: -232.77 (accuracy -242.17, token simplicity 5.40, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= data.y
diff.z += params.f * data.x
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.355, d = 30.053, e = 1.071, f = 1.724, g = 0.923, h = 2.841
  Demo 1: a = 13.253, b = 13.263, c = -0.685, d = 35.437, e = 1.026, f = -0.038, g = 1.021, h = 2.006
  Demo 2: a = 8.772, b = 8.702, c = -2.625, d = 39.741, e = 0.992, f = -0.003, g = 1.063, h = 3.748

-- score: -232.73 (accuracy -243.93, token simplicity 6.20, parameter simplicity 5.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= params.f * data.y
diff.z += params.g
diff.z += params.h * data.x * data.y
diff.z += params.i * data.y * data.y
diff.z -= params.j * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.712, d = 32.057, e = 1.112, f = 1.804, g = 4.491, h = 1.173, i = -0.126, j = 2.797
  Demo 1: a = 13.253, b = 13.263, c = -0.568, d = 34.396, e = 1.009, f = 0.602, g = -27.266, h = 0.508, i = 0.414, j = 1.192
  Demo 2: a = 8.772, b = 8.702, c = -2.293, d = 39.083, e = 0.982, f = 0.766, g = -0.240, h = 1.020, i = 0.030, j = 3.749

-- score: -232.67 (accuracy -242.27, token simplicity 5.60, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += (params.a - params.b) * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.796, b = 0.091, c = 32.363, d = 1.117, e = 1.784, f = -5.133, g = 0.999, h = 2.385
  Demo 1: a = 13.248, b = -0.015, c = 34.337, d = 1.008, e = 0.583, f = -1.474, g = 1.021, h = 1.963
  Demo 2: a = 8.765, b = 0.063, c = 38.673, d = 0.976, e = 0.703, f = 3.051, g = 1.064, h = 3.832

-- score: -232.67 (accuracy -242.27, token simplicity 5.60, parameter simplicity 4.00) --
diff.x -= (params.a - params.b) * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.703, b = -0.082, c = 32.396, d = 1.118, e = 1.782, f = -5.133, g = 0.999, h = 2.385
  Demo 1: a = 13.263, b = 0.006, c = 34.335, d = 1.008, e = 0.582, f = -1.474, g = 1.021, h = 1.963
  Demo 2: a = 8.702, b = -0.077, c = 38.698, d = 0.976, e = 0.707, f = 3.051, g = 1.064, h = 3.832

## Round 5 | 0.67s | best score: -234.10

+611 new programs (611 actually scored)
* linear_fit: +25
* quadratic_fit: +33
* add_single_terms: +179
* delete_interactions: +149
* delete_lines: +70
* delete_near_zeros: +0
* relate_parameters: +146
* snap_to_one: +0
* tie_parameters: +9

### 10 parents for the next round

-- score: -234.10 (accuracy -242.20, token simplicity 4.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.791, b = 9.704, c = 32.380, d = 1.117, e = 1.783, f = 1.000, g = 2.586
  Demo 1: a = 13.253, b = 13.263, c = 34.336, d = 1.008, e = 0.582, f = 1.020, g = 2.005
  Demo 2: a = 8.772, b = 8.702, c = 38.684, d = 0.976, e = 0.705, f = 1.063, g = 3.748

-- score: -233.76 (accuracy -242.26, token simplicity 5.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.688, b = 1.712, c = 32.057, d = 1.112, e = 1.804, f = 1.000, g = 2.586
  Demo 1: a = 13.263, b = -0.568, c = 34.396, d = 1.009, e = 0.602, f = 1.020, g = 2.005
  Demo 2: a = 8.704, b = -2.293, c = 39.083, d = 0.982, e = 0.766, f = 1.063, g = 3.748

-- score: -233.75 (accuracy -242.25, token simplicity 5.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = -5.133, f = 0.999, g = 2.385
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = -1.474, f = 1.021, g = 1.963
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 3.051, f = 1.064, g = 3.832

-- score: -233.69 (accuracy -242.39, token simplicity 5.20, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 1.724, f = 0.923, g = 2.841
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = -0.038, f = 1.021, g = 2.006
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = -0.003, f = 1.063, g = 3.748

-- score: -233.66 (accuracy -241.96, token simplicity 4.80, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c
diff.y += params.d * data.x
diff.y -= params.e * data.x * data.z
diff.y -= data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.791, b = 9.704, c = 1.355, d = 30.053, e = 1.071, f = 1.000, g = 2.586
  Demo 1: a = 13.253, b = 13.263, c = -0.685, d = 35.437, e = 1.026, f = 1.020, g = 2.005
  Demo 2: a = 8.772, b = 8.702, c = -2.625, d = 39.741, e = 0.992, f = 1.063, g = 3.748

-- score: -233.65 (accuracy -241.95, token simplicity 4.80, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.791, b = 9.704, c = 30.352, d = 1.077, e = -5.133, f = 0.999, g = 2.385
  Demo 1: a = 13.253, b = 13.263, c = 35.427, d = 1.026, e = -1.474, f = 1.021, g = 1.963
  Demo 2: a = 8.772, b = 8.702, c = 39.471, d = 0.988, e = 3.051, f = 1.064, g = 3.832

-- score: -233.60 (accuracy -242.10, token simplicity 5.00, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e * data.x
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.791, b = 9.704, c = 30.352, d = 1.077, e = 1.724, f = 0.923, g = 2.841
  Demo 1: a = 13.253, b = 13.263, c = 35.427, d = 1.026, e = -0.038, f = 1.021, g = 2.006
  Demo 2: a = 8.772, b = 8.702, c = 39.471, d = 0.988, e = -0.003, f = 1.063, g = 3.748

-- score: -233.56 (accuracy -243.86, token simplicity 5.80, parameter simplicity 4.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f
diff.z += params.g * data.x * data.y
diff.z += params.h * data.y * data.y
diff.z -= params.i * data.z
  Demo 0: a = 9.791, b = 9.704, c = 32.380, d = 1.117, e = 1.783, f = 4.491, g = 1.173, h = -0.126, i = 2.797
  Demo 1: a = 13.253, b = 13.263, c = 34.336, d = 1.008, e = 0.582, f = -27.266, g = 0.508, h = 0.414, i = 1.192
  Demo 2: a = 8.772, b = 8.702, c = 38.684, d = 0.976, e = 0.705, f = -0.240, g = 1.020, h = 0.030, i = 3.749

-- score: -233.50 (accuracy -242.20, token simplicity 5.20, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += (params.a - params.b) * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.796, b = 0.091, c = 32.363, d = 1.117, e = 1.784, f = 1.000, g = 2.586
  Demo 1: a = 13.248, b = -0.015, c = 34.337, d = 1.008, e = 0.583, f = 1.020, g = 2.005
  Demo 2: a = 8.765, b = 0.063, c = 38.673, d = 0.976, e = 0.703, f = 1.063, g = 3.748

-- score: -233.50 (accuracy -242.20, token simplicity 5.20, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += (params.a + params.b) * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.785, b = -0.082, c = 32.396, d = 1.118, e = 1.782, f = 1.000, g = 2.586
  Demo 1: a = 13.257, b = 0.006, c = 34.335, d = 1.008, e = 0.582, f = 1.020, g = 2.005
  Demo 2: a = 8.779, b = -0.077, c = 38.698, d = 0.976, e = 0.707, f = 1.063, g = 3.748

## Round 6 | 0.50s | best score: -234.58

+541 new programs (541 actually scored)
* linear_fit: +9
* quadratic_fit: +12
* add_single_terms: +202
* delete_interactions: +135
* delete_lines: +62
* delete_near_zeros: +0
* relate_parameters: +112
* snap_to_one: +0
* tie_parameters: +9

### 10 parents for the next round

-- score: -234.58 (accuracy -242.18, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 1.000, f = 2.586
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = 1.020, f = 2.005
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 1.063, f = 3.748

-- score: -234.49 (accuracy -241.89, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.791, b = 9.704, c = 30.352, d = 1.077, e = 1.000, f = 2.586
  Demo 1: a = 13.253, b = 13.263, c = 35.427, d = 1.026, e = 1.020, f = 2.005
  Demo 2: a = 8.772, b = 8.702, c = 39.471, d = 0.988, e = 1.063, f = 3.748

-- score: -234.18 (accuracy -241.98, token simplicity 4.80, parameter simplicity 3.00) --
diff.x -= (params.a * params.b) * data.x
diff.x += params.a * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.b * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.700, b = 1.007, c = 32.380, d = 1.117, e = 1.783, f = 2.606
  Demo 1: a = 13.261, b = 1.004, c = 34.336, d = 1.008, e = 0.582, f = 1.971
  Demo 2: a = 8.685, b = 1.031, c = 38.684, d = 0.976, e = 0.705, f = 3.642

-- score: -234.16 (accuracy -241.56, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.791, b = 9.704, c = 32.380, d = 1.117, e = 1.783, f = 2.586
  Demo 1: a = 13.253, b = 13.263, c = 34.336, d = 1.008, e = 0.582, f = 1.962
  Demo 2: a = 8.772, b = 8.702, c = 38.684, d = 0.976, e = 0.705, f = 3.537

-- score: -234.14 (accuracy -241.94, token simplicity 4.80, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 1.355, c = 30.053, d = 1.071, e = 1.000, f = 2.586
  Demo 1: a = 13.263, b = -0.685, c = 35.437, d = 1.026, e = 1.020, f = 2.005
  Demo 2: a = 8.704, b = -2.625, c = 39.741, d = 0.992, e = 1.063, f = 3.748

-- score: -234.14 (accuracy -241.94, token simplicity 4.80, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = -5.133, e = 0.999, f = 2.385
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = -1.474, e = 1.021, f = 1.963
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 3.051, e = 1.064, f = 3.832

-- score: -234.10 (accuracy -242.20, token simplicity 4.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.f * data.x * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.791, b = 9.704, c = 32.380, d = 1.117, e = 1.783, f = 1.000, g = 2.586
  Demo 1: a = 13.253, b = 13.263, c = 34.336, d = 1.008, e = 0.582, f = 1.020, g = 2.005
  Demo 2: a = 8.772, b = 8.702, c = 38.684, d = 0.976, e = 0.705, f = 1.063, g = 3.748

-- score: -234.08 (accuracy -242.08, token simplicity 5.00, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.724, e = 0.923, f = 2.841
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = -0.038, e = 1.021, f = 2.006
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = -0.003, e = 1.063, f = 3.748

-- score: -234.07 (accuracy -241.87, token simplicity 4.80, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += (params.a * params.b) * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= params.e * data.y
diff.z += params.b * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.764, b = 0.993, c = 32.380, d = 1.117, e = 1.783, f = 2.567
  Demo 1: a = 13.188, b = 1.006, c = 34.336, d = 1.008, e = 0.582, f = 1.974
  Demo 2: a = 8.506, b = 1.023, c = 38.684, d = 0.976, e = 0.705, f = 3.614

-- score: -234.04 (accuracy -243.84, token simplicity 5.80, parameter simplicity 4.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e
diff.z += params.f * data.x * data.y
diff.z += params.g * data.y * data.y
diff.z -= params.h * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 4.491, f = 1.173, g = -0.126, h = 2.797
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = -27.266, f = 0.508, g = 0.414, h = 1.192
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = -0.240, f = 1.020, g = 0.030, h = 3.749

## Round 7 | 0.87s | best score: -234.97

+452 new programs (452 actually scored)
* linear_fit: +29
* quadratic_fit: +33
* add_single_terms: +181
* delete_interactions: +117
* delete_lines: +46
* delete_near_zeros: +0
* relate_parameters: +39
* snap_to_one: +0
* tie_parameters: +7

### 10 parents for the next round

-- score: -234.97 (accuracy -241.87, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.063, e = 3.748

-- score: -234.65 (accuracy -241.55, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 2.586
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = 1.962
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 3.537

-- score: -234.58 (accuracy -242.18, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 1.000, f = 2.586
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = 1.020, f = 2.005
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 1.063, f = 3.748

-- score: -234.56 (accuracy -241.66, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= (params.a * params.b) * data.x
diff.x += params.a * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.b * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.700, b = 1.007, c = 30.352, d = 1.077, e = 2.606
  Demo 1: a = 13.261, b = 1.004, c = 35.427, d = 1.026, e = 1.971
  Demo 2: a = 8.685, b = 1.031, c = 39.471, d = 0.988, e = 3.642

-- score: -234.55 (accuracy -241.25, token simplicity 4.20, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.791, b = 9.704, c = 30.352, d = 1.077, e = 2.586
  Demo 1: a = 13.253, b = 13.263, c = 35.427, d = 1.026, e = 1.962
  Demo 2: a = 8.772, b = 8.702, c = 39.471, d = 0.988, e = 3.537

-- score: -234.49 (accuracy -241.89, token simplicity 4.40, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.791, b = 9.704, c = 30.352, d = 1.077, e = 1.000, f = 2.586
  Demo 1: a = 13.253, b = 13.263, c = 35.427, d = 1.026, e = 1.020, f = 2.005
  Demo 2: a = 8.772, b = 8.702, c = 39.471, d = 0.988, e = 1.063, f = 3.748

-- score: -234.45 (accuracy -241.55, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += (params.a * params.b) * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.b * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.764, b = 0.993, c = 30.352, d = 1.077, e = 2.567
  Demo 1: a = 13.188, b = 1.006, c = 35.427, d = 1.026, e = 1.974
  Demo 2: a = 8.506, b = 1.023, c = 39.471, d = 0.988, e = 3.614

-- score: -234.43 (accuracy -243.53, token simplicity 5.60, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d
diff.z += params.e * data.x * data.y
diff.z += params.f * data.y * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 4.491, e = 1.173, f = -0.126, g = 2.797
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = -27.266, e = 0.508, f = 0.414, g = 1.192
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = -0.240, e = 1.020, f = 0.030, g = 3.749

-- score: -234.41 (accuracy -243.31, token simplicity 5.40, parameter simplicity 3.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z += params.f * data.y * data.y
diff.z -= params.g * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 1.138, f = -0.101, g = 2.614
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = 0.687, f = 0.267, g = 1.986
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 1.021, f = 0.029, g = 3.756

-- score: -234.35 (accuracy -241.05, token simplicity 4.20, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.b * data.y
diff.y += params.c * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.791, b = 9.704, c = 28.073, d = 1.000, e = 2.586
  Demo 1: a = 13.253, b = 13.263, c = 34.455, d = 1.020, e = 2.005
  Demo 2: a = 8.772, b = 8.702, c = 40.022, d = 1.063, e = 3.748

## Round 8 | 0.75s | best score: -235.03

+404 new programs (404 actually scored)
* linear_fit: +33
* quadratic_fit: +33
* add_single_terms: +160
* delete_interactions: +101
* delete_lines: +42
* delete_near_zeros: +0
* relate_parameters: +31
* snap_to_one: +0
* tie_parameters: +4

### 10 parents for the next round

-- score: -235.03 (accuracy -241.23, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.962
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 3.537

-- score: -234.97 (accuracy -241.87, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.063, e = 3.748

-- score: -234.83 (accuracy -241.03, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.000, d = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.020, d = 2.005
  Demo 2: a = 8.704, b = 40.022, c = 1.063, d = 3.748

-- score: -234.80 (accuracy -243.00, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z += params.e * data.y * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.138, e = -0.101, f = 2.614
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 0.687, e = 0.267, f = 1.986
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.021, e = 0.029, f = 3.756

-- score: -234.68 (accuracy -241.08, token simplicity 4.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 29.139, c = 1.036, d = 2.693
  Demo 1: a = 13.263, b = 35.311, c = 1.023, d = 2.011
  Demo 2: a = 8.704, b = 41.124, c = 1.025, d = 3.620

-- score: -234.65 (accuracy -241.55, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 2.586
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = 1.962
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 3.537

-- score: -234.58 (accuracy -242.18, token simplicity 4.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += params.e * data.x * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 1.000, f = 2.586
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = 1.020, f = 2.005
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 1.063, f = 3.748

-- score: -234.56 (accuracy -241.66, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= (params.a * params.b) * data.x
diff.x += params.a * data.y
diff.y += params.c * data.x
diff.y -= params.d * data.x * data.z
diff.y -= data.y
diff.z += params.b * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.700, b = 1.007, c = 30.352, d = 1.077, e = 2.606
  Demo 1: a = 13.261, b = 1.004, c = 35.427, d = 1.026, e = 1.971
  Demo 2: a = 8.685, b = 1.031, c = 39.471, d = 0.988, e = 3.642

-- score: -234.56 (accuracy -243.16, token simplicity 5.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.d - params.e) * data.y
diff.z += params.d * data.x * data.y
diff.z += params.e * data.y * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 31.062, c = 1.091, d = 1.158, e = -0.115, f = 2.622
  Demo 1: a = 13.263, b = 33.932, c = 1.001, d = 0.691, e = 0.264, f = 1.987
  Demo 2: a = 8.704, b = 39.394, c = 0.986, d = 1.008, e = 0.037, f = 3.755

-- score: -234.55 (accuracy -243.15, token simplicity 5.60, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= (params.c * params.d) * data.y
diff.z += params.d * data.x * data.y
diff.z += params.e * data.y * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 31.085, c = 1.092, d = 1.153, e = -0.111, f = 2.622
  Demo 1: a = 13.263, b = 34.622, c = 1.013, d = 0.685, e = 0.269, f = 1.986
  Demo 2: a = 8.704, b = 39.426, c = 0.987, d = 1.012, e = 0.034, f = 3.754

## Round 9 | 0.44s | best score: -235.03 (stable)

+299 new programs (299 actually scored)
* linear_fit: +26
* quadratic_fit: +30
* add_single_terms: +122
* delete_interactions: +79
* delete_lines: +32
* delete_near_zeros: +0
* relate_parameters: +9
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -235.03 (accuracy -241.23, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.962
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 3.537

-- score: -234.97 (accuracy -241.87, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.063, e = 3.748

-- score: -234.90 (accuracy -240.40, token simplicity 4.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.c * data.z
  Demo 0: a = 9.688, b = 28.073, c = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.962
  Demo 2: a = 8.704, b = 40.022, c = 3.537

-- score: -234.83 (accuracy -241.03, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.000, d = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.020, d = 2.005
  Demo 2: a = 8.704, b = 40.022, c = 1.063, d = 3.748

-- score: -234.80 (accuracy -242.30, token simplicity 5.00, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.339, c = -0.199, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 34.445, c = 0.002, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 40.084, c = -0.017, d = 1.063, e = 3.748

-- score: -234.80 (accuracy -243.00, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z += params.e * data.y * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.138, e = -0.101, f = 2.614
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 0.687, e = 0.267, f = 1.986
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.021, e = 0.029, f = 3.756

-- score: -234.68 (accuracy -241.08, token simplicity 4.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 29.139, c = 1.036, d = 2.693
  Demo 1: a = 13.263, b = 35.311, c = 1.023, d = 2.011
  Demo 2: a = 8.704, b = 41.124, c = 1.025, d = 3.620

-- score: -234.67 (accuracy -242.17, token simplicity 5.00, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z += params.d * data.y * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.138, d = -0.101, e = 2.614
  Demo 1: a = 13.263, b = 34.455, c = 0.687, d = 0.267, e = 1.986
  Demo 2: a = 8.704, b = 40.022, c = 1.021, d = 0.029, e = 3.756

-- score: -234.66 (accuracy -242.56, token simplicity 5.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += (params.c - params.d) * data.x * data.y
diff.z += params.d * data.y * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 29.840, c = 1.060, d = -0.124, e = 2.666
  Demo 1: a = 13.263, b = 34.258, c = 0.995, d = 0.209, e = 2.048
  Demo 2: a = 8.704, b = 40.414, c = 1.009, d = 0.069, e = 3.693

-- score: -234.65 (accuracy -241.55, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= params.d * data.y
diff.z += data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 32.380, c = 1.117, d = 1.783, e = 2.586
  Demo 1: a = 13.263, b = 34.336, c = 1.008, d = 0.582, e = 1.962
  Demo 2: a = 8.704, b = 38.684, c = 0.976, d = 0.705, e = 3.537

## Round 10 | 0.18s | best score: -235.03 (stable)

+207 new programs (207 actually scored)
* linear_fit: +21
* quadratic_fit: +17
* add_single_terms: +86
* delete_interactions: +54
* delete_lines: +25
* delete_near_zeros: +0
* relate_parameters: +4
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -235.03 (accuracy -241.23, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.962
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 3.537

-- score: -234.97 (accuracy -241.87, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.063, e = 3.748

-- score: -234.90 (accuracy -240.40, token simplicity 4.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.c * data.z
  Demo 0: a = 9.688, b = 28.073, c = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.962
  Demo 2: a = 8.704, b = 40.022, c = 3.537

-- score: -234.87 (accuracy -241.67, token simplicity 4.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.339, c = -0.199, d = 2.586
  Demo 1: a = 13.263, b = 34.445, c = 0.002, d = 1.962
  Demo 2: a = 8.704, b = 40.084, c = -0.017, d = 3.537

-- score: -234.83 (accuracy -241.03, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.000, d = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.020, d = 2.005
  Demo 2: a = 8.704, b = 40.022, c = 1.063, d = 3.748

-- score: -234.80 (accuracy -242.30, token simplicity 5.00, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.339, c = -0.199, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 34.445, c = 0.002, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 40.084, c = -0.017, d = 1.063, e = 3.748

-- score: -234.80 (accuracy -243.00, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z += params.e * data.y * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.138, e = -0.101, f = 2.614
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 0.687, e = 0.267, f = 1.986
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.021, e = 0.029, f = 3.756

-- score: -234.77 (accuracy -241.87, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 0.077, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 0.006, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = -0.076, e = 3.748

-- score: -234.68 (accuracy -241.08, token simplicity 4.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 29.139, c = 1.036, d = 2.693
  Demo 1: a = 13.263, b = 35.311, c = 1.023, d = 2.011
  Demo 2: a = 8.704, b = 41.124, c = 1.025, d = 3.620

-- score: -234.67 (accuracy -242.17, token simplicity 5.00, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z += params.d * data.y * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.138, d = -0.101, e = 2.614
  Demo 1: a = 13.263, b = 34.455, c = 0.687, d = 0.267, e = 1.986
  Demo 2: a = 8.704, b = 40.022, c = 1.021, d = 0.029, e = 3.756

## Round 11 | 0.10s | best score: -235.03 (stable)

+105 new programs (105 actually scored)
* linear_fit: +10
* quadratic_fit: +9
* add_single_terms: +45
* delete_interactions: +27
* delete_lines: +12
* delete_near_zeros: +0
* relate_parameters: +2
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -235.03 (accuracy -241.23, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.962
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 3.537

-- score: -234.97 (accuracy -241.87, token simplicity 4.40, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.063, e = 3.748

-- score: -234.90 (accuracy -240.40, token simplicity 4.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.c * data.z
  Demo 0: a = 9.688, b = 28.073, c = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.962
  Demo 2: a = 8.704, b = 40.022, c = 3.537

-- score: -234.87 (accuracy -241.67, token simplicity 4.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 30.339, c = -0.199, d = 2.586
  Demo 1: a = 13.263, b = 34.445, c = 0.002, d = 1.962
  Demo 2: a = 8.704, b = 40.084, c = -0.017, d = 3.537

-- score: -234.83 (accuracy -241.03, token simplicity 4.20, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.000, d = 2.586
  Demo 1: a = 13.263, b = 34.455, c = 1.020, d = 2.005
  Demo 2: a = 8.704, b = 40.022, c = 1.063, d = 3.748

-- score: -234.80 (accuracy -242.30, token simplicity 5.00, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y += params.c * data.x * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.339, c = -0.199, d = 1.000, e = 2.586
  Demo 1: a = 13.263, b = 34.445, c = 0.002, d = 1.020, e = 2.005
  Demo 2: a = 8.704, b = 40.084, c = -0.017, d = 1.063, e = 3.748

-- score: -234.80 (accuracy -243.00, token simplicity 5.20, parameter simplicity 3.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.d * data.x * data.y
diff.z += params.e * data.y * data.y
diff.z -= params.f * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 1.138, e = -0.101, f = 2.614
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 0.687, e = 0.267, f = 1.986
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = 1.021, e = 0.029, f = 3.756

-- score: -234.77 (accuracy -241.87, token simplicity 4.60, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += (params.c - params.d) * data.x * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 30.352, c = 1.077, d = 0.077, e = 2.586
  Demo 1: a = 13.263, b = 35.427, c = 1.026, d = 0.006, e = 2.005
  Demo 2: a = 8.704, b = 39.471, c = 0.988, d = -0.076, e = 3.748

-- score: -234.68 (accuracy -241.08, token simplicity 4.40, parameter simplicity 2.00) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= params.c * data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z -= params.d * data.z
  Demo 0: a = 9.688, b = 29.139, c = 1.036, d = 2.693
  Demo 1: a = 13.263, b = 35.311, c = 1.023, d = 2.011
  Demo 2: a = 8.704, b = 41.124, c = 1.025, d = 3.620

-- score: -234.67 (accuracy -242.17, token simplicity 5.00, parameter simplicity 2.50) --
diff.x -= params.a * data.x
diff.x += params.a * data.y
diff.y += params.b * data.x
diff.y -= data.x * data.z
diff.y -= data.y
diff.z += params.c * data.x * data.y
diff.z += params.d * data.y * data.y
diff.z -= params.e * data.z
  Demo 0: a = 9.688, b = 28.073, c = 1.138, d = -0.101, e = 2.614
  Demo 1: a = 13.263, b = 34.455, c = 0.687, d = 0.267, e = 1.986
  Demo 2: a = 8.704, b = 40.022, c = 1.021, d = 0.029, e = 3.756

