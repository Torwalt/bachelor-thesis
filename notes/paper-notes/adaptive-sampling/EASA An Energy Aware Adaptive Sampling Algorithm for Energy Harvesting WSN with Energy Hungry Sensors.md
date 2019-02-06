# EASA An Energy Aware Adaptive Sampling Algorithm for Energy Harvesting WSN with Energy Hungry Sensors

## Problem/Goal

- some sensor nodes consume more energy with sensing than with transmission
  - especially when the acquisition time of sensor data is higher than the data
    transmission time
- algorithm for managing (effectivly) node activity (sampling rate of the
  sensors) according to the energy levels of the nodes and the dynamics of the
  phenomenon observed
- when sensing task are reduced, communication volume is reduced, too

## Basics of Algorithm

- nodes sense phenomenon and send sensed values to base station
- base station will respond with an adapted sensing rate if it detects a change
  in the frequency of the signal
- the node will adapts it's sampling frequency to that value according to some
  constraints (like it's own power level)
- cycles of a sensor node:
  - sleeping
  - listening for base station
  - adapting sensing rate
  - sensing
  - transmitting

## Experimental Results

- preliminaries
  - experimental evalutation of the algorithm was conducted on two different
    application scenarios => different platform, application space and
    different sensors
  - custom sensor board developed to monitor wind speeds
    - equipped with a wind turbine to generate power from wind
  - off the shelf gas monitoring microcontroller to monitor primarily CO2 in a
    Beehive
    - equipped with a solar panel
  - for both sensors, the energy collection characteristics (e.g. collection
    speed) are known
  - Basestation is a wireless node too
    - receives data from sensor node and forwards it to wired server
- postive outcomes for EASA, however some alialising may occure if the
    frequency is below the nyquist criterion (what ever that means)
  - authors classify this as a tradeoff for staying in the network and not
    letting the node discharge down to 0 energy ○ below nyquist probably means
    that at this sensing rate, not all information about the phenomenon can be
    captured by the sensor

## Use Cases

- WSNs with enough processing power
- RSNs -> perpetual operation possible

## Advantages/Disadvantages

- advantage:
  - a perpetual service can be provided in the network
- disadvatange:
  - user has to set critical energy/power level
  - when energy is low, sensing results may not capture all developments of phenomenon

## Compability

## Notes
