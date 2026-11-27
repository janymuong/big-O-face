# ml/foundations/losses.py
'''
Cross-entropy loss: binary and categorical.

Binary:      L = -mean(y*ln(p) + (1-y)*ln(1-p))
Categorical: L = -mean over samples of sum over classes of y_c*ln(p_c)

- Clip predictions to [eps, 1 - eps] so ln(0) never happens. A model that is
  confidently wrong (p = 0 for the true class) would otherwise give inf.
- With one-hot labels, the categorical sum has exactly one nonzero term per
  sample: -ln(p of the true class). Low when the model puts high probability
  on the right class, large when it is confidently wrong.
- Binary CE is categorical CE with two classes, p and 1-p.
- Average over samples (axis 0), sum over classes (axis 1). Mixing these up
  is the classic bug here.
- Round once at the end.

Complexity: O(n) for binary, O(n * C) for categorical.
'''

import numpy as np
from numpy.typing import NDArray

EPS = 1e-7


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        p = np.clip(y_pred, EPS, 1 - EPS)
        loss = -np.mean(y_true * np.log(p) + (1 - y_true) * np.log(1 - p))
        return round(float(loss), 4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        p = np.clip(y_pred, EPS, 1 - EPS)
        per_sample = -np.sum(y_true * np.log(p), axis=1)
        return round(float(np.mean(per_sample)), 4)


# sol = Solution()
# assert sol.binary_cross_entropy(np.array([1, 0, 1]), np.array([0.9, 0.1, 0.8])) == 0.1446
# assert sol.categorical_cross_entropy(
#     np.array([[1, 0, 0], [0, 1, 0]]),
#     np.array([[0.9, 0.05, 0.05], [0.1, 0.8, 0.1]]),
# ) == 0.1643