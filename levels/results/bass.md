# bass

Solved in 0.01 seconds. 17 programs considered, over 3 rounds.

## Winner

-- score: -32.32 (accuracy -35.62, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

## Runner-ups

-- score: -32.30 (accuracy -35.30, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += (params.b - params.a) * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.025, b = 0.397
  Demo 1: a = 0.005, b = 0.361
  Demo 2: a = 0.264, b = 0.448

-- score: -32.30 (accuracy -35.30, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= (params.a + params.b) * data.x * data.x
  Demo 0: a = 0.025, b = 0.372
  Demo 1: a = 0.005, b = 0.356
  Demo 2: a = 0.264, b = 0.184

-- score: -29.76 (accuracy -31.66, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.462
  Demo 1: a = 0.376
  Demo 2: a = 1.044

-- score: -29.52 (accuracy -31.92, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

# The Search

## Round 0 | 0.00s | best score: -32.32

+5 new programs (5 actually scored)
* add_terms: +5
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -32.32 (accuracy -35.62, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -27.06 (accuracy -29.06, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x
  Demo 0: a = 0.088, b = 0.053
  Demo 1: a = 0.039, b = 0.004
  Demo 2: a = 0.378, b = 0.357

-- score: -16.63 (accuracy -17.53, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 0.053
  Demo 1: a = 0.037
  Demo 2: a = 0.086

-- score: -6.56 (accuracy -7.66, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.050
  Demo 1: a = 0.045
  Demo 2: a = 0.061

-- score: -2.78 (accuracy -4.08, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.041
  Demo 1: a = 0.036
  Demo 2: a = 0.047

## Round 1 | 0.00s | best score: -32.32

+10 new programs (10 actually scored)
* add_terms: +3
* delete_lines: +3
* relate_parameters: +2
* snap_to_one: +0
* tie_parameters: +2

### 5 parents for the next round

-- score: -32.32 (accuracy -35.62, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -32.30 (accuracy -35.30, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += (params.b - params.a) * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.025, b = 0.397
  Demo 1: a = 0.005, b = 0.361
  Demo 2: a = 0.264, b = 0.448

-- score: -29.52 (accuracy -31.92, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

-- score: -29.40 (accuracy -32.20, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.017, b = 0.373
  Demo 1: a = 0.000, b = 0.376
  Demo 2: a = 0.010, b = 0.985

-- score: -28.69 (accuracy -30.89, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.087, b = 0.061
  Demo 1: a = 0.046, b = 0.023
  Demo 2: a = 0.305, b = 0.296

## Round 2 | 0.00s | best score: -32.32

+5 new programs (5 actually scored)
* add_terms: +0
* delete_lines: +4
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +1

### 5 parents for the next round

-- score: -32.32 (accuracy -35.62, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.c * data.x * data.x
  Demo 0: a = 0.028, b = 0.335, c = 0.349
  Demo 1: a = 0.005, b = 0.369, c = 0.379
  Demo 2: a = 0.269, b = 0.154, c = 0.417

-- score: -32.30 (accuracy -35.30, token simplicity 2.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += (params.b - params.a) * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.025, b = 0.397
  Demo 1: a = 0.005, b = 0.361
  Demo 2: a = 0.264, b = 0.448

-- score: -29.76 (accuracy -31.66, token simplicity 1.40, parameter simplicity 0.50) --
diff.x += params.a * data.x
diff.x -= params.a * data.x * data.x
  Demo 0: a = 0.462
  Demo 1: a = 0.376
  Demo 2: a = 1.044

-- score: -29.52 (accuracy -31.92, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.442, b = 0.431
  Demo 1: a = 0.388, b = 0.394
  Demo 2: a = 1.061, b = 1.068

-- score: -29.40 (accuracy -32.20, token simplicity 1.80, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
diff.x -= params.b * data.x * data.x
  Demo 0: a = 0.017, b = 0.373
  Demo 1: a = 0.000, b = 0.376
  Demo 2: a = 0.010, b = 0.985

