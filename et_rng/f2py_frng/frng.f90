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

    ! The Fortrtan version store the state of the function as module variables. Note that this way
    ! we can have only one random number generator, as there is only a single state.
    integer*8, parameter :: a=2147483629_8
    integer*8, parameter :: b=2147483629_8
    integer*8, parameter :: m=2_8**31-1
    integer*8            :: seed = 0_8
    integer*8            :: x    = 0_8
    ! REMARK: Fortran has no standard support for unsigned integers. So we use signed
    ! integers. As a consequence the Python version and the Fortran version are not
    ! entirely equivalent, since the range of allowed numbers in the Fortran version
    ! is only half of that in Python (half of the range is for negative numbers).

    contains
        subroutine set_seed(s)
            integer*8, intent(in) :: s
            seed = s
            x = s
        end subroutine set_seed

        function lcg1()
          ! Compute the next random number in the sequence
            implicit none
            integer*8 :: lcg1 ! result type

            ! modify the state
            x = modulo( a*x+b, m )
            ! assign result
            lcg1 = x

        end function lcg1

end module f90
