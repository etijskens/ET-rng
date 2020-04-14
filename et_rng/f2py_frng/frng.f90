!-------------------------------------------------------------------------------------------------
! Fortran source code for module et_rng.frng
!-------------------------------------------------------------------------------------------------
! Remarks:
!   . Enter Python documentation for this module in ``./frng.rst``.
!     You might want to check the f2py output for the interfaces of the C-wrapper functions.
!     It will be autmatically included in the et_rng documentation.
!   . Documument the Fortran routines in this file. This documentation will not be included
!     in the et_rng documentation (because there is no recent sphinx
!     extension for modern fortran.
module f90
    implicit none
    integer*8, parameter :: a=2147483629_8
    integer*8, parameter :: b=2147483629_8
    integer*8, parameter :: m=2_8**31-1
    integer*8            :: seed = 0_8
    integer*8            :: x    = 0_8

    contains
        subroutine set_seed(s)
            integer*8, intent(in) :: s
            seed = s
            x = s
        end subroutine set_seed

        function lcg1()
          ! Compute the
          !
          ! Python use:
          !    import ET-rng.frng as f90
          !    a      = np.array([1,2,3],dtype=np.float64)
          !    result = np.ndarray((2,), np.float64)
          !    f90.mean_and_stddev(result,a)
          !    avg = result[0]
          !    std = result[1]
            implicit none
            integer*8 :: lcg1
          !-------------------------------------------------------------------------------------------------
          ! declare local variables
          !-------------------------------------------------------------------------------------------------
            x = modulo( a * x + b, m )
            lcg1 = x

        end function lcg1

end module f90
