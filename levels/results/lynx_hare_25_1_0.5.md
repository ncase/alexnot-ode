# lynx_hare_25_1_0.5

Solved in 1.24 seconds. 1509 programs considered, over 9 rounds.

## Winner

-- score: -82.93 (accuracy -109.93, token simplicity 26.00, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.618, b = 0.028

## Runner-ups

-- score: -82.87 (accuracy -110.37, token simplicity 26.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -80.99 (accuracy -110.49, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.638, b = 0.029, c = 1.047

-- score: -80.87 (accuracy -110.37, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.028, c = 1.054

-- score: -80.87 (accuracy -110.37, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += (params.b * params.c) * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.949

# The Search

## Round 0 | 0.00s | best score: -74.10

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

-- score: -74.10 (accuracy -126.10, token simplicity 48.00, parameter simplicity 4.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 12.122, b = 0.968, c = 0.043, d = 0.481, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -53.02 (accuracy -130.52, token simplicity 72.00, parameter simplicity 5.50) --
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

-- score: -35.27 (accuracy -57.27, token simplicity 20.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.y
diff.y -= params.c
diff.y += params.d * data.x
  Demo 0: a = 19.471, b = 0.946, c = 18.665, d = 0.549

-- score: -23.84 (accuracy -58.84, token simplicity 32.00, parameter simplicity 3.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.y
diff.y -= params.d
diff.y += params.e * data.x
diff.y -= params.f * data.y
  Demo 0: a = 16.896, b = 0.082, c = 0.958, d = 16.983, e = 0.556, f = 0.093

-- score: -6.20 (accuracy -14.70, token simplicity 8.00, parameter simplicity 0.50) --
diff.x -= params.a * data.y * data.y
  Demo 0: a = 0.010

-- score: -2.17 (accuracy -10.67, token simplicity 8.00, parameter simplicity 0.50) --
diff.y += params.a * data.x * data.x
  Demo 0: a = 0.003

-- score: -0.84 (accuracy -7.34, token simplicity 6.00, parameter simplicity 0.50) --
diff.x -= params.a * data.y
  Demo 0: a = 0.328

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

-- score: 1.38 (accuracy -7.12, token simplicity 8.00, parameter simplicity 0.50) --
diff.x -= params.a * data.x * data.y
  Demo 0: a = 0.008

-- score: 1.83 (accuracy -4.67, token simplicity 6.00, parameter simplicity 0.50) --
diff.y += params.a * data.x
  Demo 0: a = 0.140

## Round 1 | 0.13s | best score: -76.54

+358 new programs (358 actually scored)
* linear_fit: +9
* quadratic_fit: +18
* add_single_terms: +71
* delete_interactions: +51
* delete_lines: +28
* delete_near_zeros: +3
* relate_parameters: +168
* snap_to_one: +0
* tie_parameters: +10

### 10 parents for the next round

-- score: -76.54 (accuracy -126.04, token simplicity 46.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 13.176, b = 0.044, c = 0.525, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -75.93 (accuracy -121.43, token simplicity 42.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 2.519, b = 0.705, c = 0.030, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -74.59 (accuracy -126.09, token simplicity 48.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 11.801, b = 0.958, c = 0.042, d = 0.465, e = 11.713, f = 0.320, g = 1.516

-- score: -74.59 (accuracy -126.09, token simplicity 48.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.a
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 11.748, b = 0.958, c = 0.042, d = 0.466, e = 0.320, f = 0.042, g = 1.515

-- score: -74.10 (accuracy -126.10, token simplicity 48.00, parameter simplicity 4.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.e
diff.y -= params.f * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.h * data.y
  Demo 0: a = 12.122, b = 0.968, c = 0.043, d = 0.481, e = 11.505, f = 0.313, g = 0.042, h = 1.505

-- score: -72.69 (accuracy -120.19, token simplicity 44.00, parameter simplicity 3.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.x -= params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 0.646, b = 0.029, c = 0.013, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -72.60 (accuracy -126.10, token simplicity 50.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.d * params.e) * data.y
diff.y += params.d
diff.y -= params.f * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 12.122, b = 0.968, c = 0.043, d = 11.504, e = 0.042, f = 0.313, g = 1.505

-- score: -72.60 (accuracy -126.10, token simplicity 50.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.a - params.d) * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 12.039, b = 0.965, c = 0.043, d = 11.561, e = 0.315, f = 0.042, g = 1.508

-- score: -72.60 (accuracy -126.10, token simplicity 50.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += (params.a * params.b)
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 11.997, b = 0.964, c = 0.042, d = 0.476, e = 0.315, f = 0.042, g = 1.508

-- score: -72.60 (accuracy -126.10, token simplicity 50.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += (params.d * params.e) * data.y
diff.y += params.f
diff.y -= params.d * data.x
diff.y += params.g * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 12.026, b = 0.965, c = 0.042, d = 0.316, e = 1.509, f = 11.585, g = 0.042

## Round 2 | 0.31s | best score: -79.17

+409 new programs (409 actually scored)
* linear_fit: +1
* quadratic_fit: +8
* add_single_terms: +36
* delete_interactions: +115
* delete_lines: +59
* delete_near_zeros: +8
* relate_parameters: +176
* snap_to_one: +0
* tie_parameters: +6

### 10 parents for the next round

-- score: -79.17 (accuracy -120.17, token simplicity 38.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.647, b = 0.030, c = 11.505, d = 0.313, e = 0.042, f = 1.505

-- score: -76.85 (accuracy -125.85, token simplicity 46.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 13.166, b = 0.044, c = 0.511, d = 12.676, e = 0.349, f = 1.563

-- score: -76.85 (accuracy -125.85, token simplicity 46.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.a
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 12.889, b = 0.044, c = 0.516, d = 0.350, e = 0.043, f = 1.562

-- score: -76.54 (accuracy -126.04, token simplicity 46.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 13.176, b = 0.044, c = 0.525, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -75.93 (accuracy -121.43, token simplicity 42.00, parameter simplicity 3.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.g * data.y
  Demo 0: a = 2.519, b = 0.705, c = 0.030, d = 11.505, e = 0.313, f = 0.042, g = 1.505

-- score: -75.09 (accuracy -126.09, token simplicity 48.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.a
diff.y -= params.e * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 11.748, b = 0.957, c = 0.042, d = 0.464, e = 0.320, f = 1.516

-- score: -75.04 (accuracy -126.04, token simplicity 48.00, parameter simplicity 3.00) --
diff.x -= (params.a + params.b)
diff.x += data.x
diff.x -= params.c * data.x * data.y
diff.x += params.d * data.y
diff.y += params.a
diff.y -= params.e * data.x
diff.y += params.f * data.x * data.y
diff.y -= params.b * data.y
  Demo 0: a = 11.638, b = 1.511, c = 0.044, d = 0.524, e = 0.317, f = 0.042

-- score: -75.03 (accuracy -126.03, token simplicity 48.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += (params.b * params.c) * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 13.121, b = 0.044, c = 11.859, d = 0.323, e = 0.042, f = 1.520

-- score: -75.00 (accuracy -126.00, token simplicity 48.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += (params.c * params.d) * data.y
diff.y += params.c
diff.y -= params.e * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 13.098, b = 0.044, c = 12.131, d = 0.043, e = 0.330, f = 1.532

-- score: -74.98 (accuracy -125.98, token simplicity 48.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += (params.a * params.c) * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.c * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 13.127, b = 0.044, c = 0.041, d = 11.075, e = 0.300, f = 1.484

## Round 3 | 0.18s | best score: -79.17 (stable)

+270 new programs (270 actually scored)
* linear_fit: +1
* quadratic_fit: +7
* add_single_terms: +32
* delete_interactions: +89
* delete_lines: +47
* delete_near_zeros: +5
* relate_parameters: +83
* snap_to_one: +0
* tie_parameters: +6

### 10 parents for the next round

-- score: -79.17 (accuracy -120.17, token simplicity 38.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.647, b = 0.030, c = 11.505, d = 0.313, e = 0.042, f = 1.505

-- score: -77.31 (accuracy -125.81, token simplicity 46.00, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.a
diff.y -= params.d * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 12.997, b = 0.044, c = 0.512, d = 0.356, e = 1.572

-- score: -77.26 (accuracy -119.76, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= (params.b * params.c) * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.635, b = 0.029, c = 11.022, d = 0.042, e = 1.491

-- score: -77.01 (accuracy -119.51, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += (params.a * params.b) * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.a
diff.y -= params.d * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 14.199, b = 0.045, c = 0.029, d = 0.388, e = 1.621

-- score: -77.01 (accuracy -119.51, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.615, b = 0.028, c = 11.296, d = 0.321, e = 1.493

-- score: -76.95 (accuracy -119.45, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += (params.a * params.b) * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y -= params.a * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.b * data.y
  Demo 0: a = 0.394, b = 1.624, c = 0.029, d = 14.200, e = 0.045

-- score: -76.94 (accuracy -119.44, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= (params.a * params.b) * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.654, b = 0.045, c = 13.912, d = 0.387, e = 1.625

-- score: -76.85 (accuracy -125.85, token simplicity 46.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.d
diff.y -= params.e * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 13.166, b = 0.044, c = 0.511, d = 12.676, e = 0.349, f = 1.563

-- score: -76.85 (accuracy -125.85, token simplicity 46.00, parameter simplicity 3.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.a
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 12.889, b = 0.044, c = 0.516, d = 0.350, e = 0.043, f = 1.562

-- score: -76.82 (accuracy -111.32, token simplicity 32.00, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.647, b = 0.030, c = 1.301, d = 0.029, e = 1.077

## Round 4 | 0.44s | best score: -80.55

+193 new programs (193 actually scored)
* linear_fit: +12
* quadratic_fit: +8
* add_single_terms: +35
* delete_interactions: +75
* delete_lines: +33
* delete_near_zeros: +4
* relate_parameters: +22
* snap_to_one: +0
* tie_parameters: +4

### 10 parents for the next round

-- score: -80.55 (accuracy -110.55, token simplicity 28.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.029, d = 1.034

-- score: -79.17 (accuracy -120.17, token simplicity 38.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.647, b = 0.030, c = 11.505, d = 0.313, e = 0.042, f = 1.505

-- score: -78.61 (accuracy -110.61, token simplicity 30.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.632, d = 0.028

-- score: -77.31 (accuracy -125.81, token simplicity 46.00, parameter simplicity 2.50) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.y
diff.x += params.c * data.y
diff.y += params.a
diff.y -= params.d * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 12.997, b = 0.044, c = 0.512, d = 0.356, e = 1.572

-- score: -77.29 (accuracy -111.29, token simplicity 32.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.647, b = 0.030, c = 1.070, d = 0.029

-- score: -77.26 (accuracy -111.26, token simplicity 32.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.b * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.639, b = 0.029, c = 1.309, d = 1.090

-- score: -77.26 (accuracy -119.76, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= (params.b * params.c) * data.x
diff.y += params.d * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.635, b = 0.029, c = 11.022, d = 0.042, e = 1.491

-- score: -77.01 (accuracy -119.51, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += (params.a * params.b) * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.a
diff.y -= params.d * data.x
diff.y += params.b * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 14.199, b = 0.045, c = 0.029, d = 0.388, e = 1.621

-- score: -77.01 (accuracy -119.51, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += (params.b * params.e) * data.x * data.y
diff.y -= params.e * data.y
  Demo 0: a = 0.615, b = 0.028, c = 11.296, d = 0.321, e = 1.493

-- score: -76.95 (accuracy -119.45, token simplicity 40.00, parameter simplicity 2.50) --
diff.x += (params.a * params.b) * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d
diff.y -= params.a * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.b * data.y
  Demo 0: a = 0.394, b = 1.624, c = 0.029, d = 14.200, e = 0.045

## Round 5 | 0.03s | best score: -82.87

+109 new programs (109 actually scored)
* linear_fit: +6
* quadratic_fit: +6
* add_single_terms: +25
* delete_interactions: +34
* delete_lines: +13
* delete_near_zeros: +3
* relate_parameters: +20
* snap_to_one: +0
* tie_parameters: +2

### 10 parents for the next round

-- score: -82.87 (accuracy -110.37, token simplicity 26.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -80.99 (accuracy -110.49, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.638, b = 0.029, c = 1.047

-- score: -80.55 (accuracy -110.55, token simplicity 28.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.029, d = 1.034

-- score: -79.17 (accuracy -120.17, token simplicity 38.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.647, b = 0.030, c = 11.505, d = 0.313, e = 0.042, f = 1.505

-- score: -79.11 (accuracy -110.61, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.a
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -79.05 (accuracy -110.55, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.648, b = 0.029, c = 1.030

-- score: -78.61 (accuracy -110.61, token simplicity 30.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.d * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.632, d = 0.028

-- score: -78.52 (accuracy -110.02, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += (params.b * params.c) * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.616, b = 0.028, c = 1.023

-- score: -78.48 (accuracy -109.98, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.615, b = 0.028, c = 0.240

-- score: -77.74 (accuracy -111.24, token simplicity 32.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.639, b = 0.029, c = 1.083

## Round 6 | 0.10s | best score: -82.93

+140 new programs (140 actually scored)
* linear_fit: +12
* quadratic_fit: +8
* add_single_terms: +46
* delete_interactions: +53
* delete_lines: +16
* delete_near_zeros: +2
* relate_parameters: +2
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -82.93 (accuracy -109.93, token simplicity 26.00, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.618, b = 0.028

-- score: -82.87 (accuracy -110.37, token simplicity 26.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -80.99 (accuracy -110.49, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.638, b = 0.029, c = 1.047

-- score: -80.87 (accuracy -110.37, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.028, c = 1.054

-- score: -80.55 (accuracy -110.55, token simplicity 28.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.029, d = 1.034

-- score: -79.62 (accuracy -111.62, token simplicity 30.00, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= data.y
  Demo 0: a = 2.519, b = 0.705, c = 0.030, d = 0.028

-- score: -79.17 (accuracy -120.17, token simplicity 38.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.647, b = 0.030, c = 11.505, d = 0.313, e = 0.042, f = 1.505

-- score: -79.11 (accuracy -110.61, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.a
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -79.05 (accuracy -110.55, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.648, b = 0.029, c = 1.030

-- score: -78.90 (accuracy -109.90, token simplicity 30.00, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.a
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.610, b = 0.028

## Round 7 | 0.03s | best score: -82.93 (stable)

+74 new programs (74 actually scored)
* linear_fit: +5
* quadratic_fit: +5
* add_single_terms: +27
* delete_interactions: +26
* delete_lines: +8
* delete_near_zeros: +1
* relate_parameters: +1
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -82.93 (accuracy -109.93, token simplicity 26.00, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.618, b = 0.028

-- score: -82.87 (accuracy -110.37, token simplicity 26.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -80.99 (accuracy -110.49, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.638, b = 0.029, c = 1.047

-- score: -80.87 (accuracy -110.37, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.028, c = 1.054

-- score: -80.55 (accuracy -110.55, token simplicity 28.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.029, d = 1.034

-- score: -79.62 (accuracy -111.62, token simplicity 30.00, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= data.y
  Demo 0: a = 2.519, b = 0.705, c = 0.030, d = 0.028

-- score: -79.57 (accuracy -111.07, token simplicity 30.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 2.419, b = 0.672, c = 0.028

-- score: -79.17 (accuracy -120.17, token simplicity 38.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.647, b = 0.030, c = 11.505, d = 0.313, e = 0.042, f = 1.505

-- score: -79.11 (accuracy -110.61, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.a
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -79.05 (accuracy -110.55, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.648, b = 0.029, c = 1.030

## Round 8 | 0.01s | best score: -82.93 (stable)

+17 new programs (17 actually scored)
* linear_fit: +1
* quadratic_fit: +2
* add_single_terms: +6
* delete_interactions: +6
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -82.93 (accuracy -109.93, token simplicity 26.00, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.618, b = 0.028

-- score: -82.87 (accuracy -110.37, token simplicity 26.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -80.99 (accuracy -110.49, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.638, b = 0.029, c = 1.047

-- score: -80.87 (accuracy -110.37, token simplicity 28.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.028, c = 1.054

-- score: -80.55 (accuracy -110.55, token simplicity 28.00, parameter simplicity 2.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= params.d * data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.029, d = 1.034

-- score: -79.62 (accuracy -111.62, token simplicity 30.00, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.d * data.x * data.y
diff.y -= data.y
  Demo 0: a = 2.519, b = 0.705, c = 0.030, d = 0.028

-- score: -79.57 (accuracy -111.07, token simplicity 30.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.y
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 2.419, b = 0.672, c = 0.028

-- score: -79.17 (accuracy -120.17, token simplicity 38.00, parameter simplicity 3.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.c
diff.y -= params.d * data.x
diff.y += params.e * data.x * data.y
diff.y -= params.f * data.y
  Demo 0: a = 0.647, b = 0.030, c = 11.505, d = 0.313, e = 0.042, f = 1.505

-- score: -79.11 (accuracy -110.61, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.y
diff.y += params.a
diff.y += params.c * data.x * data.y
diff.y -= data.y
  Demo 0: a = 0.647, b = 0.030, c = 0.028

-- score: -79.05 (accuracy -110.55, token simplicity 30.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= (params.b * params.c) * data.x * data.y
diff.y += params.b * data.x * data.y
diff.y -= params.c * data.y
  Demo 0: a = 0.648, b = 0.029, c = 1.030

