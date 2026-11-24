"""ML pset
gradient descent
https://neetcode.io/problems/gradient-descent/question

-----
gradient descent: minimize f(x) = x^2.

update rule: x = x - lr * f'(x), with f'(x) = 2x.

closed form: each step is x * (1 - 2*lr), so after n steps
x_n = init * (1 - 2*lr)^n.
check: 5 * 0.98^10 ≈ 4.08536 (matches the example).

behavior by learning rate (0 < lr < 1):
- lr < 0.5: factor is in (0, 1), x decays smoothly toward 0 from one side.
- lr = 0.5: factor is 0, lands on the minimum in one step.
- 0.5 < lr < 1: factor is in (-1, 0), x overshoots and oscillates across 0
  while still shrinking.
- lr >= 1 would diverge (|factor| >= 1), which is why the problem bounds lr.

hotchas:
- iterations = 0 returns init unchanged.
- round once at the end, not each step, to avoid accumulating error.
- round(x, 5) on an int returns an int; use round(float(x), 5) to always
  return a float.

complexity: O(iterations) time with the loop (O(1) with the closed form),
O(1) space.

why it matters: this is the same rule that trains neural networks. Here the
gradient is a scalar derivative; in a network it becomes a vector of partial
derivatives, one per parameter.
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
