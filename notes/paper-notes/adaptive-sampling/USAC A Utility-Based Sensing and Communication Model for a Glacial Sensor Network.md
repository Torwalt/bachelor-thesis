# USAC A Utility-Based Sensing and Communication Model for a Glacial Sensor Network

## Problem/Goal

- an application was deployed for sensing glacial environment
  - a wireless sensor network was used to collect data
  - researchers needed sampling and routing algorithms to implement application

## Basics of Algorithm

- sampling algorithm
  - uses a linear regression model at sensor nodes
  - sensed values are predicted and checked against the real sensed values
  - confidence interval is used as the error metric
    - lower confidence interval better => min(ci)
  - when predicted value not in CI => phase shift in observed phenomenon
    - sensor node increases sampling rate to incorporate change in model
  - otherwise prediction model good enough

## Experimental Results

- experiments were conducted to test authors algorithm against the currently
  deployed protocol GLACSWEB
- tests were conducted in a simulated environment using a tool
- data was taken from a real sensor testbed (Glacial monitoring)
- factors analyzed:
  - network topology
  - number of agents within the network
  - type of environment
- metrics tested:
  - efficiency (value of data gained versus energy consumed)
- experiments:
  - agents (or sensor nodes) are distributed randomly around a center
    - 470% efficiency gain in comparison the other technique
  - agents numbers vary between 1 and 20
    - 250% efficiency gain in comparison the other technique
  - number of phase changes was varyied between 0 and 25 while keeping topology
    and number of nodes constant
    - 300% efficiency gain in comparison the other technique

## Use Cases

## Advantages/Disadvantages

- confidence interval has to be set manually (domain knowledge required)

## Compability

- authors state that other information metrics than CI could be used

## Notes

- two algorithms given, sampling (or sensing) and routing
- interesting point: sensor networks could have multiple *stakeholders*,
  meaning that subsets of sensor nodes in such a network belong to different
  people
  - one such example could be IoT applications where mobile phones of different
    people are the "sensor nodes"
- **CITABLE** Multihop vs Singlehop
  - As a result, the total energy spent by transmitting data directly to the
    centre via a single hop is more than the energy spent when the data is
    relayed via successive intermediaries to the centre
- disadvantages of multihop (as stated by the auhtors):
  - opportunity costs for transmitting sensor nodes 
    - they could be sensing at that time but they need to transmit
      - personal remark: isn't this dependent on the sensor node hardware?
  - transferring nodes expend energy and have to be in a listening mode