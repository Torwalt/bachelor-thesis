# Compressed Sensing based Signal and Data Acquisition in Wireless Sensor Networks and Internet of Things

## Problem/Goal

## Basics of Algorithm

## Experimental Results

## Use Cases

## Advantages/Disadvantages

## Compability

## Notes

 

Definitions: 

sparseness in the transformation process: capture all required information without loss of information 

Definition 4: Cluster-sparse. If a signal x can be accurately represented with k<<n nonzero components (or over some transform domains), these k nonzero elements can be clustered into c {1, … ,k} clusters 

 

Problem: Data compression for reduced network traffic without introducing unacceptable distortions 

 

Basics of algorithm(s): 

Adaptive Cluster Sparse Reconstruction Algorithm (ACSRA) 

Step 1) Estimate the residual of each iteration.  

Step 2) Compute the best clusters Ck,c support set of the errors (index set).  

number of neighbors in sparse data gets adjusted 

weights are computed to balance the cluster prior knowledge and the sparsity of signal 

Step 3) Merge the strongest support set.  

Step 4) Reconstruct the signals according to the given support sets.  

Step 5) Prune and computer residual for the next round. 

 

Experimenal evaluation: 

ecg (Electrocardiography Signal) where colllected through a small IoT network 

a bigger IoT network was simulated to demonstrate scalability of the algorithm 

quality of the signal compression is measured in a Recovery Error 

an observation Matrix M x N (N = number of observations in the original signal) has to be created 

with the authors algorithm, only 18.75% of the original data has to be transmitted through the network in order to perfectly reconstruct the original signal 

ACSRAs performance was compared to other CS algorithms: GPSR, LASSO, OMP  

ACSRA recovery error was the lowest with 0.0878 (with the others being in the range of 0.2634 - 0.3883) 

remark: 

overhead energy expenditure of the algorithms was not tested 

CS algorithms often produce a high computaional overhead when reconstructing signals 

 

 

Pros/Cons: 

possible limitation: employs an a priori data sparsity information 

if data stream is not know to be sparse, algorithm can not be employed 

 

 

 

Notes: 

Compressed Sensing (CS) is a new method which positions itself as a continuance of nyquist theory (which is an important theory in signal processing) 

An advantage of the nonparametric greedy algorithms is that it can produce a good approximation with a small number of iterations. Meanwhile, the convex programming-based algorithms have a better reconstruction accuracy (copied) 

both relate to parent compressive sampling 

The sensing data in most applications in IoT or WSNs often exhibits a certain degree of correlation, therefore, there is a large space to compress sensing reports to reduce transmissions 

 