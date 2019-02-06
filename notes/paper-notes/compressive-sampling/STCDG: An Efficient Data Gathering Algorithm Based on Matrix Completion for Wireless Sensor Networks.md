# STCDG: An Efficient Data Gathering Algorithm Based on Matrix Completion for Wireless Sensor Networks

## Problem/Goal

Goal: efficiency and adaptability in data gathering with CS

## Basics of Algorithm

user sets sampling ratio

low sampling ratios => many values missing in X

missing values are replaced by 0

assuming sensing values are positive, real numbers (zero is thus not included)

check for low-rank and short term stability:

data has to be checked whether it has a good low rank approximation

determined by a fraction of the nuclear form

this is captured by the top d singular values

data has to be checked if it has short term stability

calculate gap between adjacent sensor readings and compare difference of adjacend pair of gaps

"The smaller the resulting dif(n, t), the stabler the sensor readings for node n around the time slot t"

STCDG

rank minization problem has to be solved 

is NP-hard 

thus nuclear norm minimization heuristic is used 

into the optimization problem, two tuning parameters are introduced 

they allow a tradeoff between the optimization targets: 

satisfying the sampling equation  

maintaining the low-rank feature 

achieving short-term stability 

the convex optimization problem can be solved by alternating least square procedure from EDCA 

empty columns 

when sink receives no readings during some timeslots 

could lead to high recovery errors 

the algorithm first recovers the non-empty columns and applies the algorithm as if there were no empty columns 

the empty columns are then filled by the short term stability feature 

sequence of the colums is preserved 

abnormal readings are always forwarded to the sink 

 
## Experimental Results

assumptions 

all subtrees are roughly of the same size 

the number of the measurements from each subtree is approximately equal to the total number of required measurements divided by the number of subtrees all the time 

experiments were done analytically and using real data 

capacity gain was analized, however, interpretation of that gain is hard 

TDMA based scheduling is prooven to be NP-complete for STCDG 

authors introduce their own scheduling algorithm MNIS (Maximum Non-Interference Set) 

a set of nodes is determined which can send packages simultaniously (in the same time slot) without collision 

experimental steps: 

sink node/ base station broadcasts a fixed sampling ratio (5% - 90% in the experiments) 

nodes sample with sampling ratio and forward readings to parent/sink nodes 

sink nodes select randomly the readings over a t-slot time window 

sink node recovers missing readings 

data origins 

own data generated from a wsn in a residential building 

data and traces from berkely research test lab 

kpi's 

recovery error, power consumption, lifespan 

error matrix E which is the difference between the original matrix and the recovered one 

Normalized Mean Absolute Error 

takes only the recovery errors about the missing  

results 

dumping ratios  = the inverse of a sampling ratio (1 - sampling ratio) 

there exists a critical dumping ratio for each algorithm 

when dumping ratio is exceeded the results of the precision metric ( 

Normalized Mean Absolute Error (NMAE)) worsens rapidly 

STCDG and EDCA outperform CDG in terms of highest possible dumping ratios 

reason: CDG requires sensor readings to be sparse enough 

interesting to note is, that the schemes perform worse in the intel light data than in the temperature data 

reason for that may be, that temperature is spacially and temporaly more tighter correlated than the light data 

temperature tends to go up/down in in different rooms simultaneously 

light can be switched on/off especially during the night, individually 

results for intel/light and house/light are similiar 

lower dumping ratios (higher sampling ratios) needed in house/light for the same NMAE 

=> fewer number of sensor nodes in the residental building 

power usage 

measured in units of power (32 bit consumes 1 unit of power) 

with higher dumping ratio, the total power consumption decreases 

STCDG performs best, while CDG gets outperformed by centrelized Exact 

other power usage metric relative lifespan 

lifespan of network = lifetime of first sensor node to run out of energy (M0) 

Mmax = lifetime of first sensor node to run out of energy in specific scheme 

relative lifespan = M0/Mmax 

STCDG outperforms CDG and centralized exact in relative lifespan, too 

number of packets transmitted is the same for STCDG and EDCA, thus relative lifespan and powerconsumption measured by packets transmitted is the same 

authors propose a scheduling algorithm for their sampling scheme 


## Use Cases

authors argue that real WSNs applications often exhibit the low-rank and short-term stability features approximately 

## Advantages/Disadvantages


does not rely on sparsity of the signal 

takes advantage of low rank feature 

thus, does not have to be adapted to specific sensor networks 

disadvanatges: 

data has to exhibit low-rank and short term stability 

## Compability

## Notes

STCDG is a contiunation of CDG (from the same author) 

CDG has low adaptability, because the relevant transform to reproduce the sparse signal is dependent on the type of sensor network 

CDG assumes the ordering of data reconstruction is fixed all the time  

authors argue that CDG and EDCA both suffer from precision loss when sampling ratio is extremely low or the packet loss is very high 

probability of empty columns increases 

STCDG = Spatio-Temporal Compressive Data Gathering 
