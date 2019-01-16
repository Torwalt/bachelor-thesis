# An Adaptive and Autonomous Sensor Sampling Frequency Control Scheme for Energy-Efficient Data Acquisition in Wireless Sensor Networks

## Problem/Goal

- change the sensing frequency based on variance of a signal

## Basics of Algorithm

- time series forecasting is used to predict future sensor readings
  - if signal trend is fairly constant, sensing frequencies are decreased and
    vice versa
    - nodes are allowed to adjust various parameters autonomously
    - nodes readjust their sampling rates automatically, if topology changes
      are reported by the MAC layer
    - user queries have a time inverval t, specifying the time after each
      successive sensor reading
    - once the first r readings are acquired, the r+1 reading is acquired and
      predicted
    - if the error is not high, it is assumed, that the next readings will not
        change
      - thus the following epoch is skipped
    - further samples may be skipped
    - if prediciton is not true, no samples are skipped
    - a limit for skipping samples is specifed, so that, in case of a node
      predicts values correctly many times in a row, skipping samples is not
      continued indefinitely
    - the sink node stores the prediction parameters, too
      - if no updates on the parameters are sent, the sink predicts the
        readings
        - no actual values are transmitted, only model parameters

## Experimental Results

- no real life data sets used, although extensive explanation of technique to
  generate sythetic data sets with temporal and spatial correlation

## Use Cases

- applications with energy hungry sensors
- non-critical applications, where no anomalous event may be missed
- probably also where the signal has high temporal correlation
  - authors state, that the algorithms are specifically designed for
    environmental monitoring purposses
  - only if an event has occured is detected

## Advantages/Disadvantages

## Compability

## Notes

- algorithm is run locally at every node
- specific MAC protocol LMAC is used
- classifying is not straight forward:
  - algorithm adapts sampling epochs based on predictions
  - prediction values are used to answer user queries
