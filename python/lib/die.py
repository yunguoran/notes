from random import randint

class Die:
    """一个表示骰子的类。"""

    def __init__(self, num_sides=6):
        """初始化骰子的属性。"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个随机的骰子点数。"""
        return randint(1, self.num_sides)
