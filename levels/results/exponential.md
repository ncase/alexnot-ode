# exponential

Solved in 0.00 seconds. 8 programs considered, over 2 rounds.

## Winner

-- score: -49.03 (accuracy -50.13, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

## Runner-ups

-- score: -48.18 (accuracy -50.18, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

-- score: -48.02 (accuracy -50.42, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.329, b = -0.002
  Demo 1: a = -0.408, b = -0.016
  Demo 2: a = 0.110, b = 0.003

-- score: -47.29 (accuracy -50.59, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.144, b = 0.365, c = -0.003
  Demo 1: a = -0.159, b = -0.315, c = -0.025
  Demo 2: a = 0.424, b = 0.040, c = 0.005

-- score: -46.66 (accuracy -48.86, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.905, b = 0.015
  Demo 1: a = -0.417, b = -0.062
  Demo 2: a = 0.632, b = 0.006

# The Search

## Round 0 | 0.00s | best score: -49.03

+5 new programs (5 actually scored)
* add_terms: +5
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -49.03 (accuracy -50.13, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

-- score: -48.18 (accuracy -50.18, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

-- score: -47.29 (accuracy -50.59, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.144, b = 0.365, c = -0.003
  Demo 1: a = -0.159, b = -0.315, c = -0.025
  Demo 2: a = 0.424, b = 0.040, c = 0.005

-- score: -43.39 (accuracy -44.69, token simplicity 0.80, parameter simplicity 0.50) --
diff.x += params.a * data.x * data.x
  Demo 0: a = 0.019
  Demo 1: a = -0.071
  Demo 2: a = 0.008

-- score: -23.25 (accuracy -24.15, token simplicity 0.40, parameter simplicity 0.50) --
diff.x += params.a
  Demo 0: a = 1.972
  Demo 1: a = -1.039
  Demo 2: a = 1.725

## Round 1 | 0.00s | best score: -49.03

+2 new programs (2 actually scored)
* add_terms: +2
* delete_lines: +0
* relate_parameters: +0
* snap_to_one: +0
* tie_parameters: +0

### 5 parents for the next round

-- score: -49.03 (accuracy -50.13, token simplicity 0.60, parameter simplicity 0.50) --
diff.x += params.a * data.x
  Demo 0: a = 0.306
  Demo 1: a = -0.511
  Demo 2: a = 0.158

-- score: -48.18 (accuracy -50.18, token simplicity 1.00, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x
  Demo 0: a = 0.012, b = 0.305
  Demo 1: a = -0.027, b = -0.506
  Demo 2: a = -0.218, b = 0.172

-- score: -48.02 (accuracy -50.42, token simplicity 1.40, parameter simplicity 1.00) --
diff.x += params.a * data.x
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.329, b = -0.002
  Demo 1: a = -0.408, b = -0.016
  Demo 2: a = 0.110, b = 0.003

-- score: -47.29 (accuracy -50.59, token simplicity 1.80, parameter simplicity 1.50) --
diff.x += params.a
diff.x += params.b * data.x
diff.x += params.c * data.x * data.x
  Demo 0: a = -0.144, b = 0.365, c = -0.003
  Demo 1: a = -0.159, b = -0.315, c = -0.025
  Demo 2: a = 0.424, b = 0.040, c = 0.005

-- score: -46.66 (accuracy -48.86, token simplicity 1.20, parameter simplicity 1.00) --
diff.x += params.a
diff.x += params.b * data.x * data.x
  Demo 0: a = 0.905, b = 0.015
  Demo 1: a = -0.417, b = -0.062
  Demo 2: a = 0.632, b = 0.006

