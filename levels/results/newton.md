# newton

Solved in 0.02 seconds. 45 programs considered, over 4 rounds.

## Winner

-- score: -56.72 (accuracy -58.72, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.375, b = 0.308
  Demo 1: a = 0.727, b = 0.151
  Demo 2: a = 10.702, b = 0.483

## Runner-ups

-- score: -56.32 (accuracy -58.72, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += data.x
  Demo 0: a = 6.375, b = 1.308
  Demo 1: a = 0.727, b = 1.151
  Demo 2: a = 10.702, b = 1.483

-- score: -56.32 (accuracy -58.72, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= data.x
diff.x += params.b * data.x
  Demo 0: a = 6.375, b = 0.692
  Demo 1: a = 0.727, b = 0.849
  Demo 2: a = 10.702, b = 0.517

-- score: -55.82 (accuracy -58.72, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 6.361, b = 0.014, c = 0.308
  Demo 1: a = 0.736, b = -0.009, c = 0.151
  Demo 2: a = 10.709, b = -0.007, c = 0.483

-- score: -55.62 (accuracy -58.72, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 6.375, b = 0.336, c = 0.029
  Demo 1: a = 0.727, b = 0.132, c = -0.019
  Demo 2: a = 10.702, b = 0.469, c = -0.014

# The Search

## Round 0 | 0.00s | best score: -56.72

+5 new programs (5 actually scored)
* linear_fit: +1
* quadratic_fit: +1
* add_single_terms: +3
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -56.72 (accuracy -58.72, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.375, b = 0.308
  Demo 1: a = 0.727, b = 0.151
  Demo 2: a = 10.702, b = 0.483

-- score: -55.53 (accuracy -58.83, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 7.462, b = 0.364, c = 0.001
  Demo 1: a = 0.434, b = 0.114, c = -0.001
  Demo 2: a = 10.528, b = 0.456, c = -0.001

-- score: -37.42 (accuracy -38.72, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

-- score: -33.24 (accuracy -34.34, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = -0.163
  Demo 1: a = -0.125
  Demo 2: a = 0.075

-- score: -15.44 (accuracy -16.34, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = -4.542
  Demo 1: a = -1.855
  Demo 2: a = 1.993

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -56.72 (stable)

+12 new programs (12 actually scored)
* linear_fit: +1
* quadratic_fit: +0
* add_single_terms: +1
* delete_interactions: +8
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -56.72 (accuracy -58.72, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.375, b = 0.308
  Demo 1: a = 0.727, b = 0.151
  Demo 2: a = 10.702, b = 0.483

-- score: -55.62 (accuracy -58.72, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 6.375, b = 0.336, c = 0.029
  Demo 1: a = 0.727, b = 0.132, c = -0.019
  Demo 2: a = 10.702, b = 0.469, c = -0.014

-- score: -55.53 (accuracy -58.83, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 7.462, b = 0.364, c = 0.001
  Demo 1: a = 0.434, b = 0.114, c = -0.001
  Demo 2: a = 10.528, b = 0.456, c = -0.001

-- score: -54.02 (accuracy -56.22, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.276, b = 0.003
  Demo 1: a = -0.555, b = 0.003
  Demo 2: a = 7.487, b = 0.016

-- score: -53.12 (accuracy -56.22, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 4.051, b = 3.775, c = 0.003
  Demo 1: a = -0.004, b = 0.552, c = 0.003
  Demo 2: a = 9.235, b = 1.748, c = 0.016

-- score: -50.81 (accuracy -53.21, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.002, b = 0.003
  Demo 1: a = -0.073, b = 0.001
  Demo 2: a = 1.014, b = 0.047

-- score: -37.42 (accuracy -38.72, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = -0.003
  Demo 1: a = -0.003
  Demo 2: a = 0.003

-- score: -33.24 (accuracy -34.34, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = -0.163
  Demo 1: a = -0.125
  Demo 2: a = 0.075

-- score: -32.72 (accuracy -35.32, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 20.017, b = 0.007
  Demo 1: a = 8.087, b = 0.015
  Demo 2: a = 14.162, b = 0.017

-- score: -15.44 (accuracy -16.34, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = -4.542
  Demo 1: a = -1.855
  Demo 2: a = 1.993

## Round 2 | 0.01s | best score: -56.72 (stable)

+19 new programs (19 actually scored)
* linear_fit: +2
* quadratic_fit: +0
* add_single_terms: +1
* delete_interactions: +11
* delete_lines: +4
* delete_near_zeros: +1
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -56.72 (accuracy -58.72, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.375, b = 0.308
  Demo 1: a = 0.727, b = 0.151
  Demo 2: a = 10.702, b = 0.483

-- score: -56.32 (accuracy -58.72, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += data.x
  Demo 0: a = 6.375, b = 1.308
  Demo 1: a = 0.727, b = 1.151
  Demo 2: a = 10.702, b = 1.483

-- score: -55.82 (accuracy -58.72, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 6.361, b = 0.014, c = 0.308
  Demo 1: a = 0.736, b = -0.009, c = 0.151
  Demo 2: a = 10.709, b = -0.007, c = 0.483

-- score: -55.62 (accuracy -58.72, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 6.375, b = 0.336, c = 0.029
  Demo 1: a = 0.727, b = 0.132, c = -0.019
  Demo 2: a = 10.702, b = 0.469, c = -0.014

-- score: -55.53 (accuracy -58.83, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 7.462, b = 0.364, c = 0.001
  Demo 1: a = 0.434, b = 0.114, c = -0.001
  Demo 2: a = 10.528, b = 0.456, c = -0.001

-- score: -54.63 (accuracy -58.83, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = 7.644, b = 0.182, c = 0.364, d = 0.001
  Demo 1: a = 0.491, b = 0.057, c = 0.114, d = -0.001
  Demo 2: a = 10.756, b = 0.228, c = 0.456, d = -0.001

-- score: -54.43 (accuracy -58.83, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = 7.462, b = 0.364, c = 0.000, d = 0.001
  Demo 1: a = 0.434, b = 0.114, c = -0.000, d = -0.001
  Demo 2: a = 10.528, b = 0.455, c = -0.000, d = -0.001

-- score: -54.02 (accuracy -56.22, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.276, b = 0.003
  Demo 1: a = -0.555, b = 0.003
  Demo 2: a = 7.487, b = 0.016

-- score: -53.12 (accuracy -56.22, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 4.051, b = 3.775, c = 0.003
  Demo 1: a = -0.004, b = 0.552, c = 0.003
  Demo 2: a = 9.235, b = 1.748, c = 0.016

-- score: -50.81 (accuracy -53.21, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.002, b = 0.003
  Demo 1: a = -0.073, b = 0.001
  Demo 2: a = 1.014, b = 0.047

## Round 3 | 0.01s | best score: -56.72 (stable)

+19 new programs (19 actually scored)
* linear_fit: +0
* quadratic_fit: +0
* add_single_terms: +2
* delete_interactions: +12
* delete_lines: +5
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -56.72 (accuracy -58.72, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 6.375, b = 0.308
  Demo 1: a = 0.727, b = 0.151
  Demo 2: a = 10.702, b = 0.483

-- score: -56.32 (accuracy -58.72, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += data.x
  Demo 0: a = 6.375, b = 1.308
  Demo 1: a = 0.727, b = 1.151
  Demo 2: a = 10.702, b = 1.483

-- score: -55.82 (accuracy -58.72, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
  Demo 0: a = 6.361, b = 0.014, c = 0.308
  Demo 1: a = 0.736, b = -0.009, c = 0.151
  Demo 2: a = 10.709, b = -0.007, c = 0.483

-- score: -55.62 (accuracy -58.72, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 6.375, b = 0.336, c = 0.029
  Demo 1: a = 0.727, b = 0.132, c = -0.019
  Demo 2: a = 10.702, b = 0.469, c = -0.014

-- score: -55.53 (accuracy -58.83, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 7.462, b = 0.364, c = 0.001
  Demo 1: a = 0.434, b = 0.114, c = -0.001
  Demo 2: a = 10.528, b = 0.456, c = -0.001

-- score: -55.13 (accuracy -58.83, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= data.x
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = 7.462, b = 0.636, c = 0.001
  Demo 1: a = 0.434, b = 0.886, c = -0.001
  Demo 2: a = 10.528, b = 0.544, c = -0.001

-- score: -54.72 (accuracy -58.72, token simplicity 2.00, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x
diff.x += params.d * data.x
  Demo 0: a = 7.101, b = -0.725, c = 0.336, d = 0.029
  Demo 1: a = 0.638, b = 0.090, c = 0.132, d = -0.019
  Demo 2: a = 10.843, b = -0.141, c = 0.469, d = -0.014

-- score: -54.63 (accuracy -58.83, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x -= params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = 7.644, b = 0.182, c = 0.364, d = 0.001
  Demo 1: a = 0.491, b = 0.057, c = 0.114, d = -0.001
  Demo 2: a = 10.756, b = 0.228, c = 0.456, d = -0.001

-- score: -54.52 (accuracy -58.72, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
diff.x += params.d * data.x
  Demo 0: a = 6.375, b = 0.346, c = 0.019, d = 0.019
  Demo 1: a = 0.727, b = 0.126, c = -0.012, d = -0.013
  Demo 2: a = 10.702, b = 0.464, c = -0.009, d = -0.010

-- score: -54.43 (accuracy -58.83, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b * data.x
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = 7.462, b = 0.364, c = 0.000, d = 0.001
  Demo 1: a = 0.434, b = 0.114, c = -0.000, d = -0.001
  Demo 2: a = 10.528, b = 0.455, c = -0.000, d = -0.001

