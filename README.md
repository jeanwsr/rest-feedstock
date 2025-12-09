# REST feedstock

## REST components

Currently include executable `rest` only. No `rest_regression`.

Basis sets are placed at `$CONDA_PREFIX/share/rest`.

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

Currently we use openblas-openmp.