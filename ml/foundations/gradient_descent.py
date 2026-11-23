"""ML pset
gradient descent
https://neetcode.io/problems/gradient-descent/question
"""

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # objective function: f(x) = x^2
        # derivative:         f'(x) = 2x
        # rule:               x = x - learning_rate * f'(x)
        x = init
        for _ in range(iterations):
            grad = 2 * x
            x -= learning_rate * grad
        # 5 d.p.
        return round(x, 5)
