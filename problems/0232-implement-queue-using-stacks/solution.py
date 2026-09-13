"""
implement queue using stacks
https://leetcode.com/problems/implement-queue-using-stacks/
"""


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer_if_needed(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# if __name__ == "__main__":
#     q = MyQueue()
#     q.push(1)
#     q.push(2)
#     print(q.peek())   # 1
#     print(q.pop())    # 1
#     print(q.empty())  # False