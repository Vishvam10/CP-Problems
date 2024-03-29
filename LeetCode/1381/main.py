"""
DIFFICULTY : medium
TAGS : array, stack, design
"""


class CustomStack:

    # The idea is to maintain a separate stack
    # for the increment information (say inc)
    # While popping the stack[] array, we will
    # simultaneously pop the inc[] array and add these two

    # inc[n-1] = value that has to added when stack[n-1] is popped
    #          = value that has to added to stack[] from index 0 to n-1
    #            while popping from stack

    # Now, when inc[n-1] is popped, we need to transfer the
    # information to inc[n-2] that

    # "stack[n-1] has the added result, but we need to add inc[n-1]
    # to all the elements from index 0 to n-2"

    # To do so, we can just say : inc[n-2] += inc[n-1]
    # Since we are dealing with stacks and inc[n-1] == inc[-1]
    # in Python, this can be represented as :

    # inc[-2] += inc[-1]

    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.increments = []

    def push(self, x):
        if len(self.increments) < self.n:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self):
        if not self.increments:
            return -1
        if len(self.increments) > 1:
            self.increments[-2] += self.increments[-1]
        return self.stack.pop() + self.increments.pop()

    def increment(self, k, val):
        if self.increments:
            self.increments[min(k, len(self.increments)) - 1] += val
