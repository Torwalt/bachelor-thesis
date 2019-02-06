# BBQ Model-Driven Data Acquisition in Sensor Networks

## Problem/Goal

optimize the combination of data prediction and standard data acquistion, best
data to send (which should compliment "bad" predictions) must be chosen 

## Basics of Algorithm

The queries include error tolerances and target confidence bounds that specify
how much uncertainty the user is willing to tolerate 

system decides, based on the model, what sensors to ask 

afterwards an observation plan (how and in which order sensors are queried) is build 

the readings are used to update the model and answer the query in the specified
confidence intervals 

correlations between different attributes can be captured 

e.g. when voltage and temperature are highly correlated and sampling
temperature is much more energy consuming than sampling voltage, then sampling
voltage and inferring the value for the temperatur from a model makes much more
sense 

spatial and temporal corelations can be used too 

## Experimental Results

User would ask a query, with a fraction of results 1 - delta not deviating by an error margin epsilon 

i.e. users ask a query with error margin 0.5 degrees (temperature) with 95% confidence interval 

Results by BBQ are compared to tiny db and a approximate caching approach 

approximate caching: energy costs induced due to communication are lowered because values that do not change a lot are not send through the network 

however, the cost of sensing is not reduced because data is acquired continuosly  

with reasonable error boundary and confidence interval, energy reduction per query can be reduced by a factor of 40 (5.4 J to 150 mj) 

## Use Cases

## Advantages/Disadvantages

advantages: 

was the first to introduce model predictions in WSNs 

does decrease communication volumne and thus decrease energy expenditure 

saves sensing costs, as sensing is only done when a query is issued

disadvantages: 

outliers (are not easily detectable with a correlation based model as outliers are inherently uncorrelated events) 

support for dynamic networks (network topology can change, e.g. sensors get added or removed) 

model is computed centrally at the base station, thus additional communication overhead is caused while training/tuning (?) 

## Compability

## Notes

probably the first paper which incorporates model based prediction in WSNs 

specific model is used: based on time-varying multivariate Gaussians 

models for real world processes are introduced to deliver answers to queries and not bother the sensor 

sensor is only used when the models do not answer the query suffeciently good 

spacial coherency, i.e. a single sensor reading can improve the model induced accuracy for another sensor if it is in some proximity to the read one 

Opinions of other authors: 

ASAP captures correlations between different sensor node readings, while BBQ focusses on the correlation of different attribute reading on the same sensor 

ADC: BBQ is centralized and thus requires a complete sensor data set of a WSN 

not scalable for sensor networks with 1000+ sensor nodes 

long training phase 

complete data set of every sensor node within a sufficiently long period 

model must be updated periodically, thus this process has to be repeated 

updates of the model need to be propagated back to the network 