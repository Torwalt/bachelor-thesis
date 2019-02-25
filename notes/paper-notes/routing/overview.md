Source: https://ieeexplore.ieee.org/abstract/document/1368893/ 

 

Topics: 

Routing challenges and design issues in WSNs 

Node deployment 

manual or randomized 

if randomized, network building should be automated 

energy consumption without loosing accuracy 

time-driven, event-driven, query-driven, or a hybrid 

Node/link heterogeneity 

different parameters for nodes in one network 

Fault tolerance 

if nodes fail routing protocols must establish new links 

Scalability 

routing scheme has to be able to manage 100 or 1000 sensor nodes 

Network dynamics 

if node or phenomenon which is being sensed is mobile 

Transmission Media 

has to be energy conserving 

Connectivity 

high node density enables connectivity 

Coverage 

nodes are limited in range and accuracy 

Data Aggregation 

duplicates elimination, reduction in number of transfers 

Quality of Service (QoS) 

in some use cases, data has to be delivered within a certain period of time from the moment it was sensed or it will become useless 

bounded latency for data delivery 

 

Types of routing: 

flat-based routing: 

all nodes are typically assigned equal roles or functionality 

Routing is data centric 

attributes have to be named 

hierarchical-based routing: 

nodes play different roles in the network 

higher-energy nodes can be used to process and send the information, while low-energy nodes can be used to perform the sensing in the proximity of the target 

the creation of clusters and choosing of clusterheads plays an important role in that 

location-based routing: 

sensor nodes’ positions are exploited to route data in the network 

 

Further classification: 

proactive 

all routes are computed before they are really needed 

good for static sensor networks 

reactive 

routes are computed on demand 

hybrid 

combination of the two ideas 

cooperative 

sensor nodes send data to a central nodes where aggregation is happening 

 

Different Flat-Routing techniques 

SPIN (already covered) 

 

directed diffusion: 

data generated by sensor nodes is named by attribute-value pairs 

BS propagates (flooding) interest (what kind of data) through the network 

network path is build from node to node (gradients) 

a gradient specifies an attribute value and a direction 

energy preservance is achieved by selecting empirically good paths, caching and processing data in-network 

aggregation techniques are dependent on the model of source placement 

Event-Radius (ER) 

point in the network is defined as location of event 

all nodes (not BSs) within a range of the point are defined as sources 

Random Sources (RS) 

k of the nodes (not BSs) are randomly selected to be sources 

not necessarily clustered near each other 

 

rumor routing 

event based routing 

when a node senses an event, it propagates that information through a path to the BS 

when a node issues a query for that event, nodes knowing the path can look the event up 

feasible only if there are few events and a lot of queries for the events 

 

Minimum Cost Forwarding Algorithm 

each node has a least cost past estimate from itself to the BS 

BS send message with cost set to 0 

receiving nodes check cost in message and link on which it received to message are less than the current estimate 

if true: update own estimates and the message and broadcast it 

if false: nothing is done and message is deleted 

 

Gradient Based Routing (GBR) 

interest is diffused through network 

nodes each node can calculated their height, i.e. the number of hops to reach the BS 

nodes which are neighbors (i.e. they have the same height) are differentiated by the gradient of the link (to the next node) 

packets are forwarded on a link with the highest gradient 

nodes can aggregate in-network 

to increase network lifetime, different dissemination techniques have been discussed 

stochastic scheme: nodes pick next step randomly if gradient of link is the same  

energy-based scheme: node increases it's height when energy drops below certain threshold 

stream based scheme: new streams are not routed through nodes that are currently part of a stream 

 

CADR and IDSQ 

both are extensions to directed diffusion 

CADR: 

activates only the sensors that are close to the particular event -> dynamically adjusts routing paths  

each node evaluates and information/cost objective  

IDSQ 

complementary optimization  

querying node determines which nodes can provide the most useful information while preserving energy 

COUGAR 

like tinyDB -> views sensor network as a distributed database 

BS generates a query plan which specifies the dataflow and in-network aggregation and sends that plan to the relevant nodes 

nodes choose leader to send data to for aggregation 

disadvantages: 

nodes have to synchronize between each other 

leader nodes have to be maintained to not become hot spots 

additional query layer produces more overhead which leads to higher energy consumption 

ACQUIRE 

also a routing solution which views the network like a distributed db 

BS sends a query through the network 

nodes try to partially answer the query if their data is up to date  

if not, they try gather information from neighboring nodes, d hops away  

CADR, IDSQ and rumor routing can be added to ACQUIRE 

 

Energy-Aware Routing 

chooses beforehand multiple possible paths for query processing 

no one optimal path, thus increasing overall network life by distributing routing to all nodes 

location information of the nodes is needed. also an addressing mechanism has to be implemented 

 

Different Hierarchical-Routing Techniques 

LEACH (already covered) 

PEGASIS 

enhancement over LEACH 

nodes take turn in communicating with the BS and nodes only communicate with their closest neighbor 

when all nodes have communicated with the BS, another round is started 

thus achieving maximal network lifetime 

nodes adjust signal strength so that only one node can be heard 

nodes still need to know the power status of their neighbors 

-> overhead 

nodes contain a database of location of all nodes 

nodes have to be static 

in hierarchical PEGASIS, nodes form a hierarchal chain structure to transport data parallelly 

TEEN 

Parameters 
Cluster change 
time 
Attribute > threshold 
Time 
Clusterhead receives 
message 
data is sensed continuously, but transmitted less frequently 

CH send their members a hard and a soft threshold 

hard 

a sensed value has to be smaller/higher than threshold which is set by the user 

soft 

the difference a sensed value has to have to the previous value 

user can control the tradeoff between energy consumption and QoS 

APTEEN 

same as with teen, but an additional Count time is sent by the CH 

If a node does not send data for a time period equal to CT, it is forced to sense and retransmit the data 

MECN 

computes an energy efficient subnetwork 

which is a relay region for every node 

a relay region can transmit data from a node to another one (e.g. basestation) more energy-efficiently than on a direct path 

global minimum power paths are found without considering all nodes 

SMECN 

extension of MECN which finds minimum energy paths while taking into account, that not all nodes can communicate with each other 

SOP (Self Organizing Protocol) 

mobile and stationary nodes (sensing and routing nodes) 

a sensing node has to be connected to a routing node to be part of the network 

routing nodes are connected to a more powerful basestation 

through the Local Markov Loops Algorithm, fault tolerance and broadcasting means is achieved 

random walk on spanning trees of a graph 

sensor nodes can be addressed directly  

Sensor aggregates routing  

objective: collectively monitor target activity in a certain environment 

three algorithms were proposed: 

Distributed aggregate management (DAM) 

forms sensor aggregates for a target monitoring task 

each node a predicate P for deciding if it should participate in an aggregate  

and a messaging scheme M for applying the grouping predicate  

Energy-based acitivty monitoring (EBAM) 

estimates energy levels of every node by computing signal impact area (?) 

Expectation-Maximization Like Activity Monitoring (EMLAM) 

estimates target position and signal energy by using received signals  

predicts how signals of the target might be mixed at each sensor 

together they form a scaleable system that can track multiple targets  

can recover from intertarget interference 

Virtual Grid Architercture routing 

nodes are arranged in a fixed topology 

clusters are build with a gps-free approach  

clusters are fixed, equal, adjacent, and nonoverlapping with symmetric shapes (e.g. rectangles) 

inside each cluster a cluster head (LA = Local aggregator) is chosen 

subset of LA become Master aggregators (MA) 

this determination is NP-hard 

data is thus aggreagted on two levels 

algorithms for choosing of MA's while maximizing network lifetime: 

Integer Linear Program (ILP) 

genetics-algorithm-based heuristic 

k-means heuristic 

greedy-based heuristic 

Clustering-based Aggregation Heuristic 

the algorithms produce not satisfying results 

Hierarchical power aware routing 

Q. Li, J. Aslam and D. Rus, “Hierarchical Power-Aware Routing in Sensor Networks,” Proc. DIMACS Wksp. Pervasive Net., May, 2001. 

sensors are divided by their geographic location into zones and clustered accordingly 

zones are treated as entities and they are allowed to decide how it will route a message accross the other zones for maximum battery life 

max-min zPmin 

trade-off between minimizing total power consumption and maximizing the minmal residual power of the network 

Zone-based routing  

sensor network is divided into small number of zones 

global path from zone to zone is found to send a message through the whole network 

power levels are estimated on zone level 

a node with the highest power is assigned a controller role to manage the zones 

Two-Tier Data Dissemination 

data delivery to multiple mobile BS 

sensors are stationary and location aware 

a grid is build from a source node which sends a message to it's adjacent nodes which subsequentally send messages to their neighbor 

BSs can flood the network with a query and receive data while moving 

longer network life and shorter data delay than with directed diffusion 

problems 

assumes a very accurate positioning system  

not compatible with moving sensors 

high overhead 

 

Location-Based Routing protocols 

Geographic Adaptive Fidelity 

area is divided into different zones 

nodes elect a node to stay awake a certain amount of time for monitoring and reporting data to the BS while the other nodes sleep  

nodes are considered to be costing the same in the term of packet routing when they are in the same zone 

=> lifetime can be increased substantionally if number of nodes increases 

nodes estimate their time as active nodes and the other nodes adjust their sleeping time accordingly => no routing downtime  

can be used in stationary and mobile networks  

Geographic and Energy Aware Routing (GEAR) 

similiar to directed diffusion, but interest are send only to a specific region 

nodes keep estimated cost of reaching destination 

residual energy and distance to destination 

additionaly a learned cost is kept which is a refinement of the estimated cost  

accounts for routing around holes  

hole: no closer node to the target region than itself 

when a message reaches the target region, it is diffused 

restricted flooding or recursive geographic forwarding 

compared to GPSR which uses a different algorithm to handle holes 

GEAR delivers more packets than GPSR 

MFR, DIR and GEDIR 

Most Forward within Radius (MFR) 

has most of the time the same path to the destination as GEDIR 

A greedy algorithm that moves the packet to the currently closest neighbor 

DIR 

the best neighbor has the best angle toward the destination 

dot product is minimized 

Greedy Other Adaptive Face Routing (GOAFR) 

combination of Face Routing (FR) and Adaptive Face Routing in adhoc geometric networks 

FR 

if source and destination are connected -> success; else cost of routing proportional of size of network 

… 

SPAN 

coordinator nodes connect nodes who cant reach each other via maximum of three hops 

 

Multipath Routing Protocols 

more than just the optimal path is maintained between source and sink nodes 

such backup-paths are used when the primary path gets low on energy 

that is however chained to tradeoffs, like minimizing the total power consumed and the residual energy of the network. 

e.g. directed diffusion 

 

 

Query-Based Routing 

user issues a data sensing task by a query which propagates through the network 

e.g. rumor routing 

 

Negotiation-Based Routing Protocols 

high level data descriptors to eliminate data redundancy 

e.g. SPIN 

 

QoS-Based Routing 

QoS Metrics and energy consumption have to be balanced 

like delay, bandwith, etc. 

e.g. SAR, SPEED (look it up) 

 

Coherent and Noncoherent Processing 

coherent processing 

data is forwarded to aggregators after it was minimaly processed by the nodes 

like timestamping and duplicate-supression 

Noncoherent processing 

also processes data locally but differetly (?) 

Algorithms like SWE and MWE (look them up) 

 