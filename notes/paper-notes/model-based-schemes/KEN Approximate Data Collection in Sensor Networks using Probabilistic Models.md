# KEN Approximate Data Collection in Sensor Networks using Probabilistic Models

## Problem/Goal

end users often want all information at a specific time from a sensor network, i.e. SELECT * 

no data reduction will be peformed in such a query => more costs 

another challange: 

tradeoff between: 

a multidimensional model in the network, which incorporates all spatial and temporal correlations => high communication costs as checking if a prediction is correct is high (nodes have to send their sensed values to a central place for accuracy computation) 

check if prediction is accurate locally at nodes (only checking for correctness of the atttribute they are sensing) => spatial correlation can not be incorporated 

## Basics of Algorithm

similiar to other model based schemes, the base station computes values asked for by the query 

the sensor nodes keep sensing values and computing query answers too 

if a sensor node detects a too high error, it sends the real sensed data to the base station 

when routing data to the base station, spation correlations are exploited 

## Experimental Results

## Use Cases

"SELECT * FREQ f WITHIN +-e"  Queries, i.e. all sensors are queried, with a frequency and an error margin 

it is usable in a query, SN-as-a-database environment 

## Advantages/Disadvantages

## Compability

## Notes

copys of the model are distributed in the SN and the Basestation 

model building is done server side, i.e. at the basestation and distributed to the network afterwards (taken from ASAP) 