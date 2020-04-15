# -*- coding: utf-8 -*-

"""Tests for et_rng package."""

import et_rng

def test_LCG1_init():
    """Test for et_rng.LCG1()"""
    lcg1 = et_rng.LCG1(seed=0)
    assert lcg1.seed == 0
    assert lcg1.a == 2147483629
    assert lcg1.b == 2147483629
    m = 2**31 - 1
    assert lcg1.m == m

def test_LCG1_call():
    """Test for et_rng.LCG1.__call__()"""
    seed = 0
    lcg1 = et_rng.LCG1(seed=seed)
    # values for manually computed random numbers
    a = lcg1.a
    b = lcg1.b
    m = lcg1.m
    x = et_rng.LCG1.UINT(seed)
    # test 10 successive random numbrs
    for i in range(10):
        x = (a*x+b)%m
        r = lcg1()
        # verify the type of the result
        assert type(r) == et_rng.LCG1.UINT
        # compare the result to the manually computed x
        assert r == x
        print(x,r)



# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (otherwise all tests are normally run with pytest)
# Make sure that you run this code with the project directory as CWD, and
# that the source directory is on the path
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_LCG1_call

    print("__main__ running", the_test_you_want_to_debug)
    the_test_you_want_to_debug()
    print('-*# finished #*-')
    
# eof