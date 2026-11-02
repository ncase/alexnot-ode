# exponential

Solved in 0.02 seconds. 43 programs considered, over 4 rounds.

## Winner

-- score: -49.50 (accuracy -50.60, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.303
  Demo 1: a = -0.506
  Demo 2: a = 0.154

## Runner-ups

-- score: -49.10 (accuracy -50.60, token simplicity 1.00, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x
  Demo 0: a = 0.697
  Demo 1: a = 1.506
  Demo 2: a = 0.846

-- score: -49.10 (accuracy -50.60, token simplicity 1.00, parameter simplicity 0.50) --
diff.x -= params.a * data.x
diff.x += data.x
  Demo 0: a = 0.697
  Demo 1: a = 1.506
  Demo 2: a = 0.846

-- score: -48.62 (accuracy -50.62, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.004, b = 0.303
  Demo 1: a = -0.012, b = -0.504
  Demo 2: a = -0.110, b = 0.161

-- score: -48.40 (accuracy -50.60, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x
  Demo 0: a = 0.309, b = -0.006
  Demo 1: a = -0.478, b = -0.027
  Demo 2: a = 0.142, b = 0.012

# The Search

## Round 0 | 0.00s | best score: -49.50

+5 new programs (5 actually scored)
* linear_fit: +2
* quadratic_fit: +1
* add_single_terms: +2
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -49.50 (accuracy -50.60, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.303
  Demo 1: a = -0.506
  Demo 2: a = 0.154

-- score: -48.62 (accuracy -50.62, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.004, b = 0.303
  Demo 1: a = -0.012, b = -0.504
  Demo 2: a = -0.110, b = 0.161

-- score: -47.46 (accuracy -50.76, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.081, b = 0.335, c = -0.002
  Demo 1: a = -0.074, b = -0.415, c = -0.012
  Demo 2: a = 0.192, b = 0.099, c = 0.002

-- score: -40.37 (accuracy -41.67, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.020
  Demo 1: a = -0.069
  Demo 2: a = 0.007

-- score: -19.59 (accuracy -20.49, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 1.940
  Demo 1: a = -1.016
  Demo 2: a = 1.712

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -49.50 (stable)

+10 new programs (10 actually scored)
* linear_fit: +1
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +8
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -49.50 (accuracy -50.60, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.303
  Demo 1: a = -0.506
  Demo 2: a = 0.154

-- score: -48.62 (accuracy -50.62, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.004, b = 0.303
  Demo 1: a = -0.012, b = -0.504
  Demo 2: a = -0.110, b = 0.161

-- score: -48.31 (accuracy -50.71, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.315, b = -0.001
  Demo 1: a = -0.458, b = -0.007
  Demo 2: a = 0.131, b = 0.001

-- score: -47.52 (accuracy -50.62, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 0.004, b = 0.320, c = -0.017
  Demo 1: a = -0.012, b = -0.453, c = -0.050
  Demo 2: a = -0.110, b = 0.129, c = 0.032

-- score: -47.46 (accuracy -50.76, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.081, b = 0.335, c = -0.002
  Demo 1: a = -0.074, b = -0.415, c = -0.012
  Demo 2: a = 0.192, b = 0.099, c = 0.002

-- score: -45.55 (accuracy -47.75, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.881, b = 0.015
  Demo 1: a = -0.413, b = -0.060
  Demo 2: a = 0.714, b = 0.006

-- score: -44.65 (accuracy -47.75, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x * data.x
  Demo 0: a = 0.232, b = 0.649, c = 0.015
  Demo 1: a = -0.036, b = -0.377, c = -0.060
  Demo 2: a = 0.403, b = 0.311, c = 0.006

-- score: -40.37 (accuracy -41.67, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.020
  Demo 1: a = -0.069
  Demo 2: a = 0.007

-- score: -23.97 (accuracy -26.57, token simplicity 1.60, parameter simplicity 1.00) --
diff.x -= params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.986, b = 0.036
  Demo 1: a = 1.233, b = 0.178
  Demo 2: a = 4.533, b = 0.028

-- score: -19.59 (accuracy -20.49, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 1.940
  Demo 1: a = -1.016
  Demo 2: a = 1.712

## Round 2 | 0.00s | best score: -49.50 (stable)

+14 new programs (14 actually scored)
* linear_fit: +1
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +10
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -49.50 (accuracy -50.60, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.303
  Demo 1: a = -0.506
  Demo 2: a = 0.154

-- score: -48.62 (accuracy -50.62, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.004, b = 0.303
  Demo 1: a = -0.012, b = -0.504
  Demo 2: a = -0.110, b = 0.161

-- score: -48.40 (accuracy -50.60, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x
  Demo 0: a = 0.309, b = -0.006
  Demo 1: a = -0.478, b = -0.027
  Demo 2: a = 0.142, b = 0.012

-- score: -48.31 (accuracy -50.71, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.315, b = -0.001
  Demo 1: a = -0.458, b = -0.007
  Demo 2: a = 0.131, b = 0.001

-- score: -48.22 (accuracy -50.62, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 0.004, b = 0.697
  Demo 1: a = -0.012, b = 1.504
  Demo 2: a = -0.110, b = 0.839

-- score: -47.72 (accuracy -50.62, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
  Demo 0: a = -0.156, b = 0.160, c = 0.303
  Demo 1: a = 0.215, b = -0.227, c = -0.504
  Demo 2: a = -0.175, b = 0.065, c = 0.161

-- score: -47.52 (accuracy -50.62, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 0.004, b = 0.320, c = -0.017
  Demo 1: a = -0.012, b = -0.453, c = -0.050
  Demo 2: a = -0.110, b = 0.129, c = 0.032

-- score: -47.46 (accuracy -50.76, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.081, b = 0.335, c = -0.002
  Demo 1: a = -0.074, b = -0.415, c = -0.012
  Demo 2: a = 0.192, b = 0.099, c = 0.002

-- score: -46.56 (accuracy -50.76, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = -0.249, b = 0.168, c = 0.335, d = -0.002
  Demo 1: a = 0.134, b = -0.207, c = -0.415, d = -0.012
  Demo 2: a = 0.142, b = 0.050, c = 0.099, d = 0.002

-- score: -46.36 (accuracy -50.76, token simplicity 2.40, parameter simplicity 2.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x
diff.x += params.d * data.x * data.x
  Demo 0: a = -0.081, b = 0.336, c = -0.001, d = -0.002
  Demo 1: a = -0.074, b = -0.409, c = -0.006, d = -0.012
  Demo 2: a = 0.192, b = 0.098, c = 0.001, d = 0.002

## Round 3 | 0.01s | best score: -49.50 (stable)

+19 new programs (19 actually scored)
* linear_fit: +0
* quadratic_fit: +1
* add_single_terms: +1
* delete_interactions: +14
* delete_lines: +2
* delete_near_zeros: +0
* relate_parameters: +1
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -49.50 (accuracy -50.60, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.303
  Demo 1: a = -0.506
  Demo 2: a = 0.154

-- score: -49.10 (accuracy -50.60, token simplicity 1.00, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x
  Demo 0: a = 0.697
  Demo 1: a = 1.506
  Demo 2: a = 0.846

-- score: -48.62 (accuracy -50.62, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.004, b = 0.303
  Demo 1: a = -0.012, b = -0.504
  Demo 2: a = -0.110, b = 0.161

-- score: -48.40 (accuracy -50.60, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x
  Demo 0: a = 0.309, b = -0.006
  Demo 1: a = -0.478, b = -0.027
  Demo 2: a = 0.142, b = 0.012

-- score: -48.31 (accuracy -50.71, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.315, b = -0.001
  Demo 1: a = -0.458, b = -0.007
  Demo 2: a = 0.131, b = 0.001

-- score: -48.22 (accuracy -50.62, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x
  Demo 0: a = 0.004, b = 0.697
  Demo 1: a = -0.012, b = 1.504
  Demo 2: a = -0.110, b = 0.839

-- score: -48.02 (accuracy -50.62, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b
diff.x += (params.b - params.a) * data.x
  Demo 0: a = -0.149, b = 0.153
  Demo 1: a = 0.246, b = -0.258
  Demo 2: a = -0.136, b = 0.025

-- score: -47.72 (accuracy -50.62, token simplicity 1.40, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x += params.c * data.x
  Demo 0: a = -0.156, b = 0.160, c = 0.303
  Demo 1: a = 0.215, b = -0.227, c = -0.504
  Demo 2: a = -0.175, b = 0.065, c = 0.161

-- score: -47.52 (accuracy -50.62, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x
  Demo 0: a = 0.004, b = 0.320, c = -0.017
  Demo 1: a = -0.012, b = -0.453, c = -0.050
  Demo 2: a = -0.110, b = 0.129, c = 0.032

-- score: -47.46 (accuracy -50.76, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.081, b = 0.335, c = -0.002
  Demo 1: a = -0.074, b = -0.415, c = -0.012
  Demo 2: a = 0.192, b = 0.099, c = 0.002

