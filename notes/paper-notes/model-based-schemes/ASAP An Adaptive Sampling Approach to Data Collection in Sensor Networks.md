# ASAP An Adaptive Sampling Approach to Data Collection in Sensor Networks

## Problem/Goal

increase network lifetime while keeping data quality at an acceptable level

## Basics of Algorithm

"The main idea behind ASAP is to use a dynamically changing subset of the nodes as samplers such that the sensor readings of the sampler nodes are directly collected, whereas the values of the non-sampler nodes are predicted through the use of probabilistic models that are locally and periodically constructed" 

nodes with same sensor readings are assigned to same clusters 

sampler nodes are determined and parameters of probabilistic models are calculated 

so the values of the non sampling nodes are predicted 

this sampling scheme is self optimizing, thus it adapts to changes in the data distribution (environmental dynamics) and energy levels of the sensors 

## Experimental Results

## Use Cases

SNs where…: 

data diversity is low so that not all observations are needed to be transmitted 

a tradeoff between data quality and network lifetime is possible 

## Advantages/Disadvantages

## Compability

## Notes



an analysis is given in respect to data collection techniques 

authors divide data collection into event based and periodic 

event based: 

less demanding in terms of wireless communication 

sensed data is filtered directly at the source node 

downside: no indepth analysis of raw sensor readings as they are not extracted 

periodic: 

most recent information sensed from the environment is sent to the base station periodically 

additional classification: 

query-based data acquisition 

like in the paper of Madden et al. (probably TAG, but also parts of TinyDB) queries are preinstalled and provide contiuous metrics like the average of a attribute 

downside: when values are sent in an aggregated way to the base station, deeper analysis, e.g. the comparison of the values from different sensors at different timestamps, is not possible 

 => trade-off between flexibility of data analysis and energy expenditure 

authors classify model based schemes into: 

inter node modelling 

In inter-node modeling, correlations among the readings of same type sensors on different but spatially close-by nodes are modeled 

e.g. building models for each correlated cluster of nodes (different sensors) 

further division into 

centralized model construction: 

probabilistic models are contructed on the server/base station side  

localized model construction 

probabilistic models are discovered locally  

ASAP is such an algorithm 

intra node modelling 

In intra-node modeling, correlations among the readings of different type sensors on the same node are modeled 

e.g. correlation between voltage and temperature on the same sensor 

authors discuss advantages of localized model construction: 

with high system dynamics, centralized model contruciton may introduce high communication overhead, as models need to be updated and potetially parameters communicated to the source nodes 

cluster heads need to be cycled as not to deplete individual nodes faster than the others (more general con of clustering in WSNs) 

authors give a quick summary of the algorithm 

"ASAP is designed for energy efficient periodic collection of raw sensor readings from the network, for the purpose of performing detailed data analysis that can not be done using in-network executed queries or locally detected events" 