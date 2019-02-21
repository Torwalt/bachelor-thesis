# AdaM an Adaptive Monitoring Framework for Sampling and Filtering on IoT Devices

## Problem/Goal

## Basics of Algorithm

## Experimental Results

## Use Cases

## Advantages/Disadvantages

## Compability

## Notes

Adaptive sampling is the process of dynamically adjusting the sampling rate to
the current metric evolution, such that when stable phases in a metric stream
are detected, the sampling rate is reduced to ease processing and energy
consumption 

 

Adaptive filtering is the process of dynamically adapting the filter range to
follow the metric evolution without requiring beforehand for users to guess
what filter range should be applied 

 

algorithms discussed and compared in paper: 

FAST 

L-SIP 

 

AdaM 

is actually a framework implemented in java with no external dependencies which
can be deployed on an iot device 

Goal: 

find a sampling interval which produces a metric stream which differs from a
metric stream with a minimum fixed sampling interval by less than a user
specified imprecision value 

balance between efficiency and accuracy 

same thing with filter ranges: a fixed filter range would be inefficient and
thus an adaptive filter range should be found  

same algotithm/process as with the sampling interval 

 

Arguments against fixed sampling intervals 

small interval: a lot of data is generated and has to be send through the
network and processed which is linked with higher resource expenditure 

big interval: sudden events may be not sensed which would fail to produce
meaningful insights 

 

Metric stream evolution is computed by a moving average  

algorithm uses a expanded version of Exponential Weighted Moving Average (EWMA)
called Probabilistic Exponential Weighted Moving Average  (PEWMA) which detects
sudden spikes after long stable phases better then EWMA 

probabilistic means, that the evolution of the metric stream has a probability
to follow a modelled distribution 

 

Algorithm 

sample is taken of the data stream (one value) 

distance is computed between that value and the previous one 

pewma estimation is computed (for the next value) 

is essentialy the probability of the distance between current and previous
value to be of the gaussian distribution 

rare and unexpected spikes do not overestimate subsequent values 

estimated std is computed 

difference between pewma distance and actual distance is computed 

confidence = difference between estimated and observed std deviation 

the higher the confidence the higher the sampling period 

confidence gets compared to user defined imprecision value g 

after sample is processed, it gets filtered 

F = variance / mean 

if F < g 

filter range is widened to filter nearby values 

else  

filter range is shortend or restored to default to report abnormailities in the
data 

 

 

User interaction in algorithm 

aggressiveness in approach with lambda as a multiplicity factor 

alpha as the weighting factor in PEWMA 

imprecision value  

 

Testing of algorithm 

testing was conducted using the MAPE (Mean Absolute Percentage error),
cpu-cycles, outgoing network traffic and energy consumption  

tested on: AdAM, L-SIP, FAST and i-EWMA 

filtering in AdAM produces near to no overhead 

network traffic reduction of 69% is achieved 

Core statement: 

"AdaM succeeds in reducing data volume by 74%, energy consumption by at least
71%, while accuracy is, in all cases, greater than 89% and with filtering
enabled, greater than 83%." 

FAST samples more aggressivly, meaning it uses larger sampling intervals  

this reduces network traffic and energy expenditure 

however a great deal of accuracy is sacrificed 

 