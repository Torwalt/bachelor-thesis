# An Overview of Compressive Sampling

- relies on two principles
  - sparsity
    - the full information of a natural signal, may be represented by far less
      values than it's bandwidth suggests, i.e. sampling at nyquist rate
      (Donoho et al., 2004)
  - incoherence
    - a sparse signal is very dense in another domain
- good designed algorithms can extract all relevant information from a sparse
  signal with a sub-nyquist rate
- "The theory of compressed sensing (CS) guarantees that, for certain matrices
  A, which are nonadaptive and often quite unstructured, x can be accurately
  recovered from y whenever x itself is compressible in some domain (e.g.,
  frequency, wavelet, time)." - taken from *Compressed sensing for networked data*
  by Haupt et al. [1]
- aliasing = same set of samples may describe many different signals
  - quote taken from [1]
- CS states that it is possible to reconstruct a discrete signal from a set of
  randomly chosen values selected from a vector computed by a linear transform
  of the discrete signal vector