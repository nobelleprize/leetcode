# https://leetcode.com/problems/design-snake-game/
from collections import deque

class SnakeGame:

    def __init__(self, width, height, food):
        self.food = food
        self.bounds = (height, width)
        self.snake = [(0,0)]

    def move(self, direction: str) -> int:
        move = self.getMove(direction)
        if move == [-1,-1]:
            return -1

        tail = self.snake[-1]
        head = self.snake[0]

        new_head = [head[0] + move[0], head[1] + move[1]]
        if new_head[0] < 0 or new_head[0] >= self.bounds[0]:
            return -1
        if new_head[1] < 0 or new_head[1] >= self.bounds[1]:
            return -1

        self.snake.pop()


        if new_head in self.snake:
            return -1

        if len(self.food) > 0 and new_head == self.food[0]:
            self.food.pop(0)
            self.snake.append(tail)
            self.snake.insert(0, new_head)
        else:
            self.snake.insert(0, new_head)


        return len(self.snake) -1

    def getMove(self, direction: str) -> tuple:
        if direction == "R":
            move = [0,1]
        elif direction == "L":
            move = [0,-1]
        elif direction == "U":
            move = [-1,0]
        elif direction == "D":
            move = [1,0]
        else:
            return [-1,-1]
        return move

[[3,3,[[2,0],[0,0],[0,2],[0,1],[2,2],[0,1]]],["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["L"],["D"],["R"],["U"]]

obj = SnakeGame(3,3,[[2,0],[0,0],[0,2],[0,1],[2,2],[0,1]])
print(obj.move("D"))
print(obj.move("D"))
print(obj.move("R"))
print(obj.move("U"))
print(obj.move("U"))
print(obj.move("L"))
print(obj.move("D"))
print(obj.move("R"))
print(obj.move("R"))
print(obj.move("U"))
print(obj.move("L"))
print(obj.move("L"))
print(obj.move("D"))
print(obj.move("R"))
print(obj.move("U"))
