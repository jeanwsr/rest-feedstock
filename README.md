# REST feedstock

## Support for dependencies

### MPI

Currently we use openmpi 4 from conda-forge. It does not include libraries for InfiniBand support.
If using in a device without InfiniBand, there's a warning (but not harmful). To suppress it, use
```
mpirun --mca btl ^openib -n 4 rest
```
If the user does want to enable InfiniBand, extra library needs to be installed, which is not tested yet.

todo: test openmpi 5.

## Math Library

Currently we use openblas. And it's default is pthreads. Should we use openmp?