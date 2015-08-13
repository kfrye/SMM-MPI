c NPROCS = 4096 CLASS = E
c  
c  
c  This file is generated automatically by the setparams utility.
c  It sets the number of processors and the class of the NPB
c  in this directory. Do not modify it by hand.
c  
        integer nprocs_compiled
        parameter (nprocs_compiled = 4096)
        integer nx_default, ny_default, nz_default
        parameter (nx_default=2048, ny_default=2048, nz_default=2048)
        integer nit_default, lm, lt_default
        parameter (nit_default=50, lm = 7, lt_default=11)
        integer debug_default
        parameter (debug_default=0)
        integer ndim1, ndim2, ndim3
        parameter (ndim1 = 7, ndim2 = 7, ndim3 = 7)
        logical  convertdouble
        parameter (convertdouble = .false.)
        character*11 compiletime
        parameter (compiletime='04 Aug 2015')
        character*5 npbversion
        parameter (npbversion='3.3.1')
        character*6 cs1
        parameter (cs1='mpif77')
        character*9 cs2
        parameter (cs2='$(MPIF77)')
        character*31 cs3
        parameter (cs3='-L/usr/lib64/openmpi/lib/ -lmpi')
        character*30 cs4
        parameter (cs4='-I/usr/include/openmpi-x86_64/')
        character*2 cs5
        parameter (cs5='-O')
        character*2 cs6
        parameter (cs6='-O')
        character*6 cs7
        parameter (cs7='randi8')
