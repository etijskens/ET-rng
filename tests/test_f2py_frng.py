#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for f2py module `et_rng.frng`."""

import et_rng
# create an alias for the binary extension fortran module
f90 = et_rng.frng.f90


def test_f90_seed():
    """Test the default seed and the corresponding initial state"""
    assert f90.seed==0
    assert f90.x==0

def test_f90_set_seed():
    """Test setting a seed and the corresponding initial state"""
    f90.set_seed(1)
    assert f90.seed==1
    assert f90.x==1

def test_f90_lcg1():
    """test the fortran version against the python version, using a seed """
    # set the seed
    seed = 1
    lcg1 = et_rng.LCG1(seed=seed)
    f90.set_seed(seed)
    # test 10 successive random numbrs
    for i in range(10):
        r = lcg1()
        fr = f90.lcg1()
        print(r,fr)
        assert r == fr

#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_f90_lcg1

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
