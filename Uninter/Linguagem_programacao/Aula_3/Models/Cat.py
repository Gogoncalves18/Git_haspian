#!/usr/bin/python
# -*- coding: utf-8 -*-

from Models.Mammal import Mammal


class Cat(Mammal):

    def __init__(self, age: int, height: int, weight: int, position: int):
        super().__init__(age, height, weight, position)

    def move_x(self):
        pass

    def move_y(self):
        pass

    def move_z(self):
        pass

    def tail_type(self, ):
        pass
