"""
DIFFICULTY : easy
TAGS : math, geometry, rejection sampling, randomized
"""

import random
import math


class Solution:
    def __init__(self, radius, x_center, y_center):
        self.r, self.x, self.y = radius, x_center, y_center

    def randPoint(self):
        theta = random.uniform(0, 2 * math.pi)
        temp = random.random() + random.random()
        if temp > 1:
            temp = 2 - temp
        R = self.r * temp
        return [self.x + R * cos(theta), self.y + R * sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
