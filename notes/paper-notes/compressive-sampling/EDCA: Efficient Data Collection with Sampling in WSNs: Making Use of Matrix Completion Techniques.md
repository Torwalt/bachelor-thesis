# EDCA: Efficient Data Collection with Sampling in WSNs: Making Use of Matrix Completion Techniques

## Problem/Goal

energy efficiency in WSNs

Problem: cost of sensing different physical quantities, i.e. images, sound..

signals those signals are sparse in different domains 

different algorithms will be applied by the sensors then which increases computational overhead 

Goal:  

minimize the rank of a transmission matrix, which has null values 

achieve measurement equations 

"recover original data matrix based on a incomplete one" 

## Basics of Algorithm

uses nuclear norm heuristic 

nuclear norm = sum of nonzero, singular values of a matrix 

input: a matrix X which is N x T  

sensors send uniformly random readings 

nodes sample with a specified sampling ratio and choose randomly which and when a reading is forwarded 

T = number of samples of each node 

N = number of nodes 

decompose input matrix (X) into three elements 

U = uniary matrix N x N 

V = unitary matrix T x T 

E = diagonal matrix N x T 

find matrix t(L*R) which equals X 

initialize L and R randomly  

fix L and optimize R with linear least squared 

at the next iteration, swap R and L => fix R and optimize L 

continue until convergeance 

## Experimental Results

data used:  

real world data  

temperature information collected 

54 sensor nodes 

Matrix = 54 * 2880 

sythetic data 

matrices with sizes varying from 100 x 100 to 3000 x 3000 

"jitter" (noise) is added to the matrices 

real world data 

with decrease of the sampling ratio, the error (standard deviation) increase, however, the error is very small (from 0.05 to 0.15 °C) 

synth data 

with a fixed sampling ratio (15%) the error is not higher than 0.3 °C 

with increase of nodes the error decreases; authors argue it is because with a fixed sampling rate, more data is availiable to reconstruct the original data more reliably 

even with high discard (1 - sampling ratio), the error is low 

thus, higher discard can enable higher network lifetime (lifetime of the first node to die) through lower power consumption 

with high dicard values (0.8) power cost can be reduced by a factor of 7 (in comparison to a scheme, where all values are transmitted to the sink node), while lifetime increases by a factor of 5 ceteris paribus 

## Use Cases


multihop sensor network with N nodes 

lossy transmissions 

spatial and temporal correlation 

## Advantages/Disadvantages

authors define the power consumtion as the transmission of packets

computation overhead and sampling costs are omitted

## Compability

## Notes

low rank completion is an extension of compressed sensing, based on nuclear norm minimization

another formulation of the goal of the algorithm is the minization of the nuclear form

different algorithms can solve the problem e.g.:

Interior point methods
    (+) numerically efficient and precise
    (-) high memory requirements for bigger problems

subgradient methods
    (+) can be used for larger problems
    (-) lower accuracy then interior point methods
