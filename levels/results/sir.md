# sir

Solved in 0.67 seconds. 909 programs considered, over 8 rounds.

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

# The Search

## Round 0 | 0.01s | best score: -12.30

+36 new programs (36 actually scored)
* add_terms: +36
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

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

## Round 1 | 0.11s | best score: -22.38

+176 new programs (176 actually scored)
* add_terms: +153
* delete_lines: +14
* relate_parameters: +8
* snap_to_one: +0
* tie_parameters: +1

### 5 parents for the next round

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

## Round 2 | 0.16s | best score: -30.78

+181 new programs (181 actually scored)
* add_terms: +141
* delete_lines: +24
* relate_parameters: +16
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

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

## Round 3 | 0.17s | best score: -37.39

+179 new programs (179 actually scored)
* add_terms: +134
* delete_lines: +24
* relate_parameters: +19
* snap_to_one: +0
* tie_parameters: +2

### 5 parents for the next round

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

## Round 4 | 0.10s | best score: -37.88

+168 new programs (168 actually scored)
* add_terms: +149
* delete_lines: +8
* relate_parameters: +7
* snap_to_one: +0
* tie_parameters: +4

### 5 parents for the next round

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

-- score: -37.04 (accuracy -41.54, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.255
  Demo 1: a = 0.288, b = 0.051, c = 0.109
  Demo 2: a = 0.813, b = 0.252, c = 0.880

-- score: -36.55 (accuracy -41.55, token simplicity 3.00, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.255
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.109
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.880

## Round 5 | 0.06s | best score: -38.37

+99 new programs (99 actually scored)
* add_terms: +94
* delete_lines: +4
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 5 parents for the next round

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

-- score: -37.39 (accuracy -42.19, token simplicity 2.80, parameter simplicity 2.00) --
diff.x -= params.a * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
diff.z += params.d * data.y
  Demo 0: a = 0.491, b = 0.501, c = 0.101, d = 0.103
  Demo 1: a = 0.281, b = 0.295, c = 0.052, d = 0.050
  Demo 2: a = 0.821, b = 0.810, c = 0.251, d = 0.243

-- score: -37.04 (accuracy -41.54, token simplicity 3.00, parameter simplicity 1.50) --
diff.x -= params.a * data.x * data.y
diff.y += params.a * data.x * data.y
diff.y -= params.b * data.y
diff.z += params.c * data.y * data.y
  Demo 0: a = 0.498, b = 0.100, c = 0.255
  Demo 1: a = 0.288, b = 0.051, c = 0.109
  Demo 2: a = 0.813, b = 0.252, c = 0.880

## Round 6 | 0.02s | best score: -38.37

+32 new programs (32 actually scored)
* add_terms: +32
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

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

## Round 7 | 0.04s | best score: -38.37

+65 new programs (65 actually scored)
* add_terms: +57
* delete_lines: +8
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

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

