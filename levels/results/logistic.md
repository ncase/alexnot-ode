# logistic

Solved in 0.02 seconds. 66 programs considered, over 5 rounds.

## Winner

-- score: -32.11 (accuracy -34.51, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.787, b = 0.078
  Demo 1: a = 0.510, b = 0.017
  Demo 2: a = 1.197, b = 0.298

## Runner-ups

-- score: -31.71 (accuracy -34.51, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.213, b = 0.078
  Demo 1: a = -0.490, b = 0.017
  Demo 2: a = 0.197, b = 0.298

-- score: -31.71 (accuracy -34.51, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.213, b = 0.078
  Demo 1: a = -0.490, b = 0.017
  Demo 2: a = 0.197, b = 0.298

-- score: -31.71 (accuracy -34.51, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.787, b = 0.078
  Demo 1: a = 1.510, b = 0.017
  Demo 2: a = 2.197, b = 0.298

-- score: -31.22 (accuracy -34.52, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = 0.802, c = 0.079
  Demo 1: a = 0.143, b = 0.528, c = 0.018
  Demo 2: a = 0.018, b = 1.215, c = 0.301

# The Search

## Round 0 | 0.00s | best score: -31.22

+5 new programs (5 actually scored)
* linear_fit: +2
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +0
* delete_lines: +0
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 6 parents for the next round

-- score: -31.22 (accuracy -34.52, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = 0.802, c = 0.079
  Demo 1: a = 0.143, b = 0.528, c = 0.018
  Demo 2: a = 0.018, b = 1.215, c = 0.301

-- score: -18.63 (accuracy -20.63, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.529, b = 0.105
  Demo 1: a = 3.227, b = 0.082
  Demo 2: a = 0.905, b = 0.155

-- score: -15.10 (accuracy -16.00, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.808
  Demo 1: a = 1.504
  Demo 2: a = 0.479

-- score: -5.76 (accuracy -6.86, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.073
  Demo 1: a = 0.044
  Demo 2: a = 0.109

-- score: -2.19 (accuracy -3.49, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.006
  Demo 1: a = 0.001
  Demo 2: a = 0.022

-- score: 0.00 (accuracy 0.00, token simplicity 0.00, parameter simplicity 0.00) --
(blank program)

## Round 1 | 0.00s | best score: -32.11

+15 new programs (15 actually scored)
* linear_fit: +0
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +8
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -32.11 (accuracy -34.51, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.787, b = 0.078
  Demo 1: a = 0.510, b = 0.017
  Demo 2: a = 1.197, b = 0.298

-- score: -31.22 (accuracy -34.52, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = 0.802, c = 0.079
  Demo 1: a = 0.143, b = 0.528, c = 0.018
  Demo 2: a = 0.018, b = 1.215, c = 0.301

-- score: -29.32 (accuracy -31.92, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.415, b = 0.095
  Demo 1: a = -2.982, b = 0.031
  Demo 2: a = 0.142, b = 0.256

-- score: -21.46 (accuracy -23.66, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.484, b = 0.011
  Demo 1: a = 3.040, b = 0.003
  Demo 2: a = 0.887, b = 0.043

-- score: -20.56 (accuracy -23.66, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.321, b = 1.163, c = 0.011
  Demo 1: a = 1.185, b = 1.856, c = 0.003
  Demo 2: a = -0.173, b = 1.060, c = 0.043

-- score: -18.63 (accuracy -20.63, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.529, b = 0.105
  Demo 1: a = 3.227, b = 0.082
  Demo 2: a = 0.905, b = 0.155

-- score: -17.53 (accuracy -20.63, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
  Demo 0: a = 1.529, b = 0.388, c = 0.493
  Demo 1: a = 3.227, b = 0.232, c = 0.314
  Demo 2: a = 0.905, b = 0.681, c = 0.835

-- score: -15.10 (accuracy -16.00, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.808
  Demo 1: a = 1.504
  Demo 2: a = 0.479

-- score: -14.20 (accuracy -16.00, token simplicity 0.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b
  Demo 0: a = 1.221, b = 0.413
  Demo 1: a = 2.407, b = 0.903
  Demo 2: a = 0.770, b = 0.290

-- score: -5.76 (accuracy -6.86, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.073
  Demo 1: a = 0.044
  Demo 2: a = 0.109

## Round 2 | 0.01s | best score: -32.11 (stable)

+20 new programs (20 actually scored)
* linear_fit: +3
* quadratic_fit: +2
* add_single_terms: +1
* delete_interactions: +9
* delete_lines: +4
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -32.11 (accuracy -34.51, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.787, b = 0.078
  Demo 1: a = 0.510, b = 0.017
  Demo 2: a = 1.197, b = 0.298

-- score: -31.22 (accuracy -34.52, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = 0.802, c = 0.079
  Demo 1: a = 0.143, b = 0.528, c = 0.018
  Demo 2: a = 0.018, b = 1.215, c = 0.301

-- score: -30.32 (accuracy -34.52, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.797, b = 0.837, c = 0.802, d = 0.079
  Demo 1: a = 1.583, b = 1.726, c = 0.528, d = 0.018
  Demo 2: a = 0.521, b = 0.539, c = 1.215, d = 0.301

-- score: -30.12 (accuracy -34.52, token simplicity 2.40, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.040, b = 0.842, c = 0.039, d = 0.079
  Demo 1: a = 0.143, b = 0.537, c = 0.009, d = 0.018
  Demo 2: a = 0.018, b = 1.365, c = 0.151, d = 0.301

-- score: -29.32 (accuracy -31.92, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.415, b = 0.095
  Demo 1: a = -2.982, b = 0.031
  Demo 2: a = 0.142, b = 0.256

-- score: -22.90 (accuracy -24.60, token simplicity 1.20, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.100
  Demo 1: a = 0.035
  Demo 2: a = 0.245

-- score: -21.46 (accuracy -23.66, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 1.484, b = 0.011
  Demo 1: a = 3.040, b = 0.003
  Demo 2: a = 0.887, b = 0.043

-- score: -20.56 (accuracy -23.66, token simplicity 1.60, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.321, b = 1.163, c = 0.011
  Demo 1: a = 1.185, b = 1.856, c = 0.003
  Demo 2: a = -0.173, b = 1.060, c = 0.043

-- score: -18.63 (accuracy -20.63, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 1.529, b = 0.105
  Demo 1: a = 3.227, b = 0.082
  Demo 2: a = 0.905, b = 0.155

-- score: -18.23 (accuracy -20.63, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= data.x
  Demo 0: a = 1.529, b = 0.895
  Demo 1: a = 3.227, b = 0.918
  Demo 2: a = 0.905, b = 0.845

## Round 3 | 0.01s | best score: -32.11 (stable)

+19 new programs (19 actually scored)
* linear_fit: +0
* quadratic_fit: +1
* add_single_terms: +0
* delete_interactions: +14
* delete_lines: +3
* delete_near_zeros: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 10 parents for the next round

-- score: -32.11 (accuracy -34.51, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.787, b = 0.078
  Demo 1: a = 0.510, b = 0.017
  Demo 2: a = 1.197, b = 0.298

-- score: -31.22 (accuracy -34.52, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = 0.802, c = 0.079
  Demo 1: a = 0.143, b = 0.528, c = 0.018
  Demo 2: a = 0.018, b = 1.215, c = 0.301

-- score: -31.01 (accuracy -34.51, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.834, b = 0.047, c = 0.078
  Demo 1: a = 0.528, b = 0.018, c = 0.017
  Demo 2: a = 1.357, b = 0.160, c = 0.298

-- score: -30.82 (accuracy -34.52, token simplicity 2.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.x
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = -0.198, c = 0.079
  Demo 1: a = 0.143, b = -0.472, c = 0.018
  Demo 2: a = 0.018, b = 0.215, c = 0.301

-- score: -30.81 (accuracy -34.51, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.797, b = 0.787, c = 0.078
  Demo 1: a = 1.583, b = 0.510, c = 0.017
  Demo 2: a = 0.521, b = 1.197, c = 0.298

-- score: -30.32 (accuracy -34.52, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.797, b = 0.837, c = 0.802, d = 0.079
  Demo 1: a = 1.583, b = 1.726, c = 0.528, d = 0.018
  Demo 2: a = 0.521, b = 0.539, c = 1.215, d = 0.301

-- score: -30.12 (accuracy -34.52, token simplicity 2.40, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.040, b = 0.842, c = 0.039, d = 0.079
  Demo 1: a = 0.143, b = 0.537, c = 0.009, d = 0.018
  Demo 2: a = 0.018, b = 1.365, c = 0.151, d = 0.301

-- score: -29.32 (accuracy -31.92, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.415, b = 0.095
  Demo 1: a = -2.982, b = 0.031
  Demo 2: a = 0.142, b = 0.256

-- score: -28.42 (accuracy -31.92, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.b
diff.x += data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.609, b = 1.024, c = 0.095
  Demo 1: a = 0.163, b = 3.146, c = 0.031
  Demo 2: a = 0.601, b = 0.459, c = 0.256

-- score: -22.90 (accuracy -24.60, token simplicity 1.20, parameter simplicity 0.50) --
diff.x += data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.100
  Demo 1: a = 0.035
  Demo 2: a = 0.245

## Round 4 | 0.01s | best score: -32.11 (stable)

+23 new programs (23 actually scored)
* linear_fit: +1
* quadratic_fit: +0
* add_single_terms: +0
* delete_interactions: +15
* delete_lines: +6
* delete_near_zeros: +1
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 10 parents for the next round

-- score: -32.11 (accuracy -34.51, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.787, b = 0.078
  Demo 1: a = 0.510, b = 0.017
  Demo 2: a = 1.197, b = 0.298

-- score: -31.71 (accuracy -34.51, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += data.x
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.213, b = 0.078
  Demo 1: a = -0.490, b = 0.017
  Demo 2: a = 0.197, b = 0.298

-- score: -31.22 (accuracy -34.52, token simplicity 1.80, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = 0.802, c = 0.079
  Demo 1: a = 0.143, b = 0.528, c = 0.018
  Demo 2: a = 0.018, b = 1.215, c = 0.301

-- score: -31.01 (accuracy -34.51, token simplicity 2.00, parameter simplicity 1.50) --
diff.x += params.a * data.x
diff.x -= params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.834, b = 0.047, c = 0.078
  Demo 1: a = 0.528, b = 0.018, c = 0.017
  Demo 2: a = 1.357, b = 0.160, c = 0.298

-- score: -30.82 (accuracy -34.52, token simplicity 2.20, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += data.x
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.040, b = -0.198, c = 0.079
  Demo 1: a = 0.143, b = -0.472, c = 0.018
  Demo 2: a = 0.018, b = 0.215, c = 0.301

-- score: -30.81 (accuracy -34.51, token simplicity 2.20, parameter simplicity 1.50) --
diff.x += params.a
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.797, b = 0.787, c = 0.078
  Demo 1: a = 1.583, b = 0.510, c = 0.017
  Demo 2: a = 0.521, b = 1.197, c = 0.298

-- score: -30.32 (accuracy -34.52, token simplicity 2.20, parameter simplicity 2.00) --
diff.x += params.a
diff.x -= params.b
diff.x += params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.797, b = 0.837, c = 0.802, d = 0.079
  Demo 1: a = 1.583, b = 1.726, c = 0.528, d = 0.018
  Demo 2: a = 0.521, b = 0.539, c = 1.215, d = 0.301

-- score: -30.12 (accuracy -34.52, token simplicity 2.40, parameter simplicity 2.00) --
diff.x -= params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x
diff.x -= params.d * data.x * data.x
  Demo 0: a = 0.040, b = 0.842, c = 0.039, d = 0.079
  Demo 1: a = 0.143, b = 0.537, c = 0.009, d = 0.018
  Demo 2: a = 0.018, b = 1.365, c = 0.151, d = 0.301

-- score: -29.32 (accuracy -31.92, token simplicity 1.60, parameter simplicity 1.00) --
diff.x += params.a
diff.x += data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = -0.415, b = 0.095
  Demo 1: a = -2.982, b = 0.031
  Demo 2: a = 0.142, b = 0.256

-- score: -28.42 (accuracy -31.92, token simplicity 2.00, parameter simplicity 1.50) --
diff.x -= params.a
diff.x += params.b
diff.x += data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.129, b = -0.287, c = 0.095
  Demo 1: a = 1.327, b = -1.656, c = 0.031
  Demo 2: a = 0.046, b = 0.187, c = 0.256

