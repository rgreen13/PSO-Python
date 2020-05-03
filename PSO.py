from random import random
import math

def fitFunc(xVals):
    fitness = 10*len(xVals)
    for i in range(len(xVals)):
        fitness += xVals[i]**2 - (10*math.cos(2*math.pi*xVals[i]))
    return fitness

def initPosition(Np, Nd, xMin, xMax):
    R = [[xMin + random()*(xMax-xMin) for i in range(0, Nd)] for p in range(0, Np)]

    return R

def updatePosition(R, Np, Nd, xMin, xMax, V):
    for p in range(0, Np):
        for i in range(0, Nd):

            R[p][i] = R[p][i] + V[p][i]
            if R[p][i] > xMax: R[p][i] = xMax
            if R[p][i] < xMin: R[p][i] = xMin

    return R

def initVelocity(Np, Nd, vMin, vMax):
    V =[[vMin + random()*(vMax-vMin) for i in range(0,Nd)] for p in range(0, Np)]

    return V

def updateVelocity(R, V, Np, Nd, j, w, vMin, vMax, chi, pBestPos, gBestPos, c1, c2):

    for p in range(0, Np):
        for i in range(0, Nd):

            r1 = random()
            r2 = random()

            V[p][i] = chi * (w * V[p][i] + r1 * c1 * (pBestPos[p][i] - R[p][i])
                             + r2 * c2 * (gBestPos[i] - R[p][i]))

            if V[p][i] > vMax: V[p][i] = vMax
            if V[p][i] < vMin: V[p][i] = vMin

    return V


def updateFitness(R, M, Np, pBestPos, pBestValue, gBestPos, gBestValue):

    for p in range(0, Np):
        M[p] = fitFunc(R[p])

        # print(M[p])         #### updated print statement format
        if M[p] < gBestValue:
            gBestValue = M[p]
            print("Global Best: {}".format(gBestValue))   #### updated print statement format
            gBestPos = R[p]

        if M[p] < pBestValue[p]:
            pBestValue[p] = M[p]
            pBestPos[p] = R[p]

    return gBestValue, gBestPos, pBestPos, pBestValue, M   #### added return for gBestPos, didn't seem to be updating

def main():

    Np, Nd, Nt    = 50, 20, 100
    c1, c2        = 2.05, 2.05
    w, wMin, wMax = 0.0, 0.4, 0.9 

    phi = c1+c2
    chi = 2.0/abs(2.0-phi-math.sqrt(pow(phi, 2)-4*phi))

    xMin, xMax = -5.12, 5.12
    vMin, vMax = 0.25*xMin, 0.25*xMax
    
    gBestValue = float("inf")
    pBestValue = [float("inf")] * Np

    pBestPos   = [[0]*Nd] * Np
    gBestPos   = [0] * Nd

    history    = []
    
    R = initPosition(Np, Nd, xMin, xMax)
    V = initVelocity(Np, Nd, vMin, vMax)
    M = [fitFunc(R[p]) for p in range(0, Np)]

    for j in range(0, Nt):
        # print statement optional, used as a progress tracker
        if j % 100 == 0:
            print("Iteration #{} out of {}".format(j, Nt))

        #### added R to make it explicit and match new return
        R = updatePosition(R, Np, Nd, xMin, xMax, V)
    

        gBestValue, gBestPos, pBestPos, pBestValue, M = updateFitness(R, M, Np, pBestPos, pBestValue,
                                                                      gBestPos, gBestValue)
        history.append(gBestValue)
        
        w = wMax - ((wMax-wMin)/Nt)*j
        V = updateVelocity(R, V, Np, Nd, j, w, vMin, vMax, chi, pBestPos, gBestPos, c1, c2)

    for h in history:
        print(h)

if __name__ == "__main__":
    main()