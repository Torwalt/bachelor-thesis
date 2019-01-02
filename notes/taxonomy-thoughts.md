# Categories for sampling algorithms

- adaptive sampling
- compressive sampling
- data sharing 
  - possibly other names:
    - collaboritive sampling
    - maybe not part of the sampling domain, rather at the aggregation
      domain/level
    - or something inbetween, as sampling is deliberately done in such a way to
      serve multiple queries 

- paper Energy minimization by exploiting data redundancy in real-time wireless
  sensor networks by Benazir Fateh and Manimaran Govindarasu
  - suggest a grouping of data acquisition methods in their related work:
    - adaptive sampling
    - model based schemes
    - data aggregation schemes

## Adaptive Sampling

- Sampling and filtering at the node
  - AdAM
  - ADMIN
  - ASA
  - HDASA
    - builds on ASA
    - HIBAS
- Model at the sink and the source which predicts values of the source
  - SIP
    - original algorithm
  - G-SIP
    - same as SIP but with Heartbeat
  - LSIP
    - G-SIP but with dEWMA as state estimator
- Sampling and filtering at the node while sink reconstructs original data
  - MuSA
  - maybe look into related work of data fusion, data compression and
    collaborative processing
- Some authors defferentiate between sampling and sensing
  - EASA
    - adapt sensing rate  to the dynamics of observed phenomenon
    - focus lies on the sensing

Adaptive Sampling is the process of changing the sampling rate according to
statistics of the observed phenomenon. 

Approximate Data Collection is the technique, in which sensed values of a
source/sensor node are predicted at a sink node, thus eliminating the need of
sending those values across the network

Potentiell eine andere main category finden als adaptive sampling, da adaptive
sampling nicht der parent für approximate data collection ist

- Possible classification of algorithm
  - Works independent on source node and does not communicate with sink nodes
  - Algorithm works with source and sink nodes

- another possible distinction would be:
  - adaptive sampling 
  - model based schemes
  - compressive sampling
  - data sharing

- another possible domain to divide the algorithms (taken from ASAP):
  - event based
  - periodic

- Possible subcategories for model based schemes: (from ASAP)
  - inter node modelling
    - In inter-node modeling, correlations among the readings of same type
      sensors on different but spatially close-by nodes are modeled
    - e.g. building models for each correlated cluster of nodes (different
      sensors)
    - further division into
      - centralized model construction:
        - probabilistic models are contructed on the server/base station side 
      - localized model construction
        - probabilistic models are discovered locally 
        - ASAP is such an algorithm
  - intra node modelling
    - In intra-node modeling, correlations among the readings of different type
      sensors on the same node are modeled
    - e.g. correlation between voltage and temperature on the same sensor

Another possibility, would be having filtering as a main category and model
based schemes as one sub category

- Zu dem Punkt, dass der Bachelor Thesis Titel potentiell nicht passend gewählt
  ist:
  - sampling kann als ein prozess definiert werden, bei welchen ein Zustand
    (State) eines zu observierenden Phänomens festgehalten wird
  - dieser Zustand kann über ein bestimmtes interval sein, jedoch sind immer
    nur diskrete Ausprägungen des Zustandes zu erfassen
  - somit kann filtering, compressive sampling, adaptive sampling und data
    sharing alles aus der Kategorie sampling gesehen werden, da alle techniques
    den Zustand eines Phenomäns in einer bestimmten Zeit erfassen wollen

- Possible taxonomy categories:
  - sampling
    - adaptive sampling
    - compressive sampling
  - filtering
    - model based schemes
    - adaptive filtering
    - or:
      - temoral suppression
      - spatio suppression
      - spatiotemporal suppression
  - Data Sharing

- But how do I rationalize the split in sampling and filtering?
  - if I take filtering, into the "sampling algorithms for sensor data"
    taxonomy with the reasoning, that filtering is part of sampling, as it is
    the process of acquiring data ... (see above) then I must rationalize
    why sampling is part of the classification categories
  - no it makes sense to divide it like that
    - => sampling rate adaptation and suppression
  - so I have to still rationalize why the title is sampling algorithms for
    sensor data
