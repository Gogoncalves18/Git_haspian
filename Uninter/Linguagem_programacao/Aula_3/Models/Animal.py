#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age: int, height: int, weight: int, position: int):
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position

    @abstractmethod
    def move_x(self):
        pass

    @abstractmethod
    def move_y(self):
        pass

    @abstractmethod
    def move_z(self):
        pass
