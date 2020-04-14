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
"""
2147483629 2147483629
306 306
2147478121 2147478121
99450 99450
2145693529 2145693529
32222106 32222106
1567485721 1567485721
1850028062 1850028062
1059233218 1059233218
261154881 261154881
"""
UINT = int
UINT = np.uint64

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
            self.seed = UINT(time_ns())
        else:
            self.seed = UINT(seed)
        self.a = UINT(a)
        self.b = UINT(b)
        self.m = UINT(m)
        self.x = self.seed

    def __call__(self):
        """

        :return: a random number
        """
        self.x = (self.a * self.x + self.b) % self.m
        return self.x