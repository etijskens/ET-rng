import et_rng
f90 = et_rng.frng.f90
from et_stopwatch import Stopwatch
import numpy as np
import pprint
"""
here is the output on my mac:
Note that the Numpy version is returning an array of random numbers, whereas the Python and fortran
versions just create random numbers and store them in always the same variable. The creation and 
filling of the array consumes time too. However, for larger n the numpy version is significantly
faster.
 
(.venv) > python perf/rng.py
10
/Users/etijskens/software/dev/workspace/ET-rng/et_rng/__init__.py:84: RuntimeWarning: overflow encountered in ulong_scalars
  self.x = (self.a * self.x + self.b) % self.m
Generating 10 random numbers in Python :  : 0.001592 s
Generating 10 random numbers in Fortran:  : 7e-06 s
Generating 10 random numbers in Numpy:  : 0.000194 s
100
Generating 100 random numbers in Python :  : 8.7e-05 s
Generating 100 random numbers in Fortran:  : 6.6e-05 s
Generating 100 random numbers in Numpy:  : 5.2e-05 s
1000
Generating 1000 random numbers in Python :  : 0.000778 s
Generating 1000 random numbers in Fortran:  : 0.000361 s
Generating 1000 random numbers in Numpy:  : 4.6e-05 s
10000
Generating 10000 random numbers in Python :  : 0.006986 s
Generating 10000 random numbers in Fortran:  : 0.002862 s
Generating 10000 random numbers in Numpy:  : 0.000112 s
{   'Fortran-n=10': 7e-06,
    'Fortran-n=100': 6.6e-05,
    'Fortran-n=1000': 0.000361,
    'Fortran-n=10000': 0.002862,
    'Python-n=10': 0.001592,
    'Python-n=100': 8.7e-05,
    'Python-n=1000': 0.000778,
    'Python-n=10000': 0.006986,
    'Python/Fortran-n=10': 227.42857142857144,
    'Python/Fortran-n=100': 1.3181818181818181,
    'Python/Fortran-n=1000': 2.1551246537396125,
    'Python/Fortran-n=10000': 2.440950384346611,
    'numpy-n=10': 0.000194,
    'numpy-n=100': 5.2e-05,
    'numpy-n=1000': 4.6e-05,
    'numpy-n=10000': 0.000112}
(.venv) etijskens@MacOSX@local [94] ~/software/dev/workspace/ET-rng
>
"""
if __name__ == "__main__":
    results = {}
    rng = et_rng.LCG1()
    pp = pprint.PrettyPrinter(indent=4)
    for n in  [10,100,1000,10000]:
        print(n)
        with Stopwatch(message=f"Generating {n} random numbers in Python : ") as sw:
            for i in range(n):
                r = rng()
            results[f"Python-n={n}"] = sw.stop()

        with Stopwatch(message=f"Generating {n} random numbers in Fortran: ") as sw:
            for i in range(n):
                r = f90.lcg1()
            results[f"Fortran-n={n}"] = sw.stop()
            results[f"Python/Fortran-n={n}"] = results[f"Python-n={n}"] / results[f"Fortran-n={n}"]

        with Stopwatch(message=f"Generating {n} random numbers in Numpy: ") as sw:
            a = np.random.randint(0, rng.m, n, dtype=et_rng.LCG1.UINT)
            results[f"numpy-n={n}"] = sw.stop()

    pp.pprint(results)