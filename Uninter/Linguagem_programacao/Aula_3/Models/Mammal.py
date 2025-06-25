#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

from Models.Mammal import Animal
# import Animal


class Mammal(Animal, ABC):
    def __init__(self, age: int, height: int, weight: int, position: int):
        super().__init__(age, height, weight, position)

    def fur_type(self, ):
        pass
