'''
sigmoid & relu
https://neetcode.io/problems/sigmoid-and-relu/question
'''
import numpy as np
from numpy.typing import NDArray


class Solution:
    '''
    solution class for sigmoid and relu functions.
    '''

    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # formula: 1 / (1 + e^(-z))
        return np.round(1 / (1 + np.exp(-z)), 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # formula: max(0, z) element-wise
        return np.maximum(0, z)


if __name__ == '__main__':
    sol = Solution()
    print(sol.sigmoid(np.array([0.0])))              # [0.5]
    print(sol.sigmoid(np.array([-1.0, 0.0, 1.0])))   # [0.26894 0.5 0.73106]
    print(sol.relu(np.array([-1.0, 0.0, 1.0])))      # [0. 0. 1.]
    assert np.allclose(sol.sigmoid(np.array([0.0])), [0.5])
    assert np.allclose(sol.relu(np.array([-1.0, 0.0, 1.0])), [0.0, 0.0, 1.0])