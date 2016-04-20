# PSO-Python
A simple implementation of classic Particle Swarm Optimization in Python. 

###Usage###

1. Update the _fitFunc_ function to accurately reflect your fitness function
2. Adjust Np and Nd to reflect your fitness function
3. Adjust xMin, xMax, vMin, and vMax to reflect your fitness function
4. Adjust gBestValue and pBestValue initialization to reflect your fitness function
5. Run the code!


###Method Names###
_fitFunc_:        User defined fitness function

_initPosition_:   Initializes _R_ with random values

_initVelocity_:   Initializes _V_ with random values

_updatePosition_: Updates _R_ values based on _V_

_updateVelocity_: Updates _V_ values based on _gBestPos_, _pBestPos_, _w_, and _chi_

_udpateFitness_:  Updates _M_ values based on _R_


###Variable Names###

_R_: Position

_V_: Velocity

_M_: Fitness

_Np_: Number of Probes
_Nd_: Number of Dimensions
_Nt_: Number of Iterations

_w_: Omega
_wMin_: Omega Minimum Value
_wMax_: Omega Maximum Value

_chi_: Constriction Factor

_xMin_: Minimum value for any dimension in R
_xMax_: Maximum value for any dimension in R

_vMin_: Minimum value for any dimension in V
_vMax_: Maximum value for any dimension in V

_gBestValue_: Global best fitness value
_gBestPos_:   Global best fitness position

_pBestValue_: Personal best fitness value
_pBestPos_:   Personal best fitness position
