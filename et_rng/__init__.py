# -*- coding: utf-8 -*-

"""
Package et_rng
==============

Top-level package for et_rng.

Check https://numpy.org/devdocs/user/basics.types.html for unsigned integer data types.
"""

__version__ = "0.0.0"

try:
    import et_rng.frng
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'frng')
    if not msg:
        import et_rng.frng
    else:
        click.secho(msg, fg='bright_red')

from time import time_ns
import numpy as np


class LCG1:
    """`Linear congruential generator <https://en.wikipedia.org/wiki/Random_number_generation>`_

    This class describes a function object. This is basically a function with a state. As a random
    number generator is a deterministic function in which the new value depends on the previous
    value, it must remember the previous value to compute the new value. The previous value is
    part of the state of the function. Also the parameters of the LCG, a, b and m and the seed
    are part of the state. The __init__ method initializes the state.

    :param seed: the seed. The default seed uses the current time value, so that different
        LCG1 objects with the default seed generate different sequences of random numbers.
    :param a: a parameter for LCG
    :param b: b parameter for LCG
    :param m: m parameter for LCG

    Typical use:

    * create a LCG1 object::

        from et_rng import LCG1
        lcg = LCG1()

    * create a random number::

        random_number = lcg()
        # this is equivalent to
        random_number = lcg.__call__()
    """

    # an alias for numpy's unsigned integer type. As the LCG creates random numbers as positive
    # integers, we better use an appropriate type for it.
    UINT = np.uint64

    def __init__(self, seed=None, a=2147483629, b=2147483629, m=2**31-1):
        # set the seed
        if seed is None:
            # use a seed based on the current time value.
            self.seed = LCG1.UINT(time_ns())
        else:
            self.seed = LCG1.UINT(seed)

        # store the parameters
        self.a = LCG1.UINT(a)
        self.b = LCG1.UINT(b)
        self.m = LCG1.UINT(m)

        # initialize the random number sequence
        self.x = self.seed

    def __call__(self):
        """
        :return: a random number
        """
        self.x = (self.a * self.x + self.b) % self.m
        return self.x