# -*- coding: utf-8 -*-

"""
Package et_rng
==============

Top-level package for et_rng.
"""

__version__ = "0.0.0"

from time import time

class LCG1:
    """`Linear congruential generator <https://en.wikipedia.org/wiki/Random_number_generation>`_

    :param seed:
    :param a:
    :param b:
    :param m:
    """
    def __init__(self, seed=None, a=2147483629, b=2147483629, m=2**31-1):
        """

        """
        if seed is None:
            self.seed = integer()
        self.seed = seed
        self.a = a
        self.b = b
        self.m = m
        self.x = seed

    def __call__(self):
        """

        :return: a random number
        """
        self.x = (self.a * self.x + self.b) % self.m
        return self.x