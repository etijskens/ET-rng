This file documents a python module built from Fortran code with f2py.
You should document the Python interfaces, *NOT* the Fortran interfaces.

Module et_rng.frng
*********************************************************************

Module :py:mod:`frng` built from fortran code in :file:`f2py_frng/frng.f90`.

.. function:: set_seed(seed)
   :module: et_rng.frng
   
   Initialize the LCG random number generator with a seed. Note, that the
   Fortran version allows for just one generator.

.. function:: lcg1()
   :module: et_rng.frng

   Return the next random number in the sequence
