Problem/Goal: 

approximate data collection in WSNs to simultaneously achieve low communication cost and guaranteed data quality (namely bounded data errors) 

design factors the authors find important: 

data collection approach should be scalable 

model should be lightweight 

data collection scheme should be self adaptive for environmental changes 

 

Basics of algorithm: 

SN is devided into clusters, local data correlations are discovered at each cluster head, cluster heads upload model parameters to sink for data approximation at sink 

data is first processed locally at each sensor, afterwards, cluster heads filter redundant data 

furthermore, cluster heads have estimation models of each child sensor node to further decrease communication cost 

sensor nodes sync a estimation model with their cluster heads while the cluster heads sync the approximation model with the sink 

thus error computation is distributed accross the network (estimation error is computed at the sensor nodes and the approximation error is computed at the cluster heads) 

the sink still recovers data from all sensors while using only a subset of sensor readings 

 

Experimental results: 

 

Use cases: 

"longterm continuous data gathering applications"  

 

Advantages/Disadvatages: 

authors do not elaborate on elevated work load on cluster  heads in comparison to the sensor nodes 

no cluster head cycling or similiar techniques 

Compability: 

 

Notes: 