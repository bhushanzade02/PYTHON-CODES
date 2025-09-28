

# Traveling Salesman Problem - Simulated Annealing
# Student  : Bhushan Zade MS2421
# Date     : 2025-08-24
# Purpose  : Solves TSP using Simulated Annealing and plots results
# Github   : https://github.com/bhushanzade02/PYTHON-CODES/tree/main/16_OPTIMIZATION_CONCEPTS

"""
====================================================================
 Traveling Salesman Problem (TSP) - Solved using Simulated Annealing
====================================================================
"""
 

#******************************************************************

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
import time


#*******************************************************************


def Distance(P1, P2):
    # Euclidean distance between two points 
    if P1 == P2:
        return 0.0
    return math.sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2)


def TotalDistance(P, seq):
    # Total round-trip distance for visiting sequence seq
    dist = 0.0
    N = len(seq)
    for i in range(N - 1):
        dist += Distance(P[seq[i]], P[seq[i + 1]])
    dist += Distance(P[seq[N - 1]], P[seq[0]])
    return dist


#******************************************************************


def readCities(PNames):
    # Read city names from file and geocode coordinates
    P = []
    geolocator = Nominatim(user_agent="tsp_SA_solver")

    with open("India_cities.txt") as file:
        for line in file:
            city = line.strip()
            if not city:
                continue
            try:
                location = geolocator.geocode(city + ", India", timeout=10)
                if location:
                    print(f"City = {city} ({location.longitude:.2f}, {location.latitude:.2f})")
                    P.append([location.longitude, location.latitude])
                    PNames.append(city)
                    time.sleep(1) 
                else:
                    print(f"Could not locate {city}")
            except Exception as e:
                print(f"Error locating {city}: {e}")
    return P



#*******************************************************************

def Plot(seq, P, dist, PNames):
    
    Pt = [P[seq[i]] for i in range(len(seq))]
    Pt += [P[seq[0]]]  
    Pt = np.array(Pt)

    plt.figure(figsize=(8, 6))
    plt.title(f"Total distance = {dist:.2f}")
    plt.plot(Pt[:, 0], Pt[:, 1], '-o')

    for i in range(len(P)):
        plt.annotate(PNames[i], (P[i][0], P[i][1]))

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()


#*******************************************************************

def swap(P, seq, dist, N1, N2, temp, nCity):
    # Swap operation with acceptance criteria
    N1L = (N1 - 1) % nCity
    N1R = (N1 + 1) % nCity
    N2L = (N2 - 1) % nCity
    N2R = (N2 + 1) % nCity

    I1, I2 = seq[N1], seq[N2]
    I1L, I1R = seq[N1L], seq[N1R]
    I2L, I2R = seq[N2L], seq[N2R]

    delta = 0.0
    delta += Distance(P[I1L], P[I2])
    delta += Distance(P[I1], P[I2R])
    delta -= Distance(P[I1L], P[I1])
    delta -= Distance(P[I2], P[I2R])

    if N1 != N2L and N1R != N2 and N1R != N2L and N2 != N1L:
        delta += Distance(P[I2], P[I1R])
        delta += Distance(P[I2L], P[I1])
        delta -= Distance(P[I1], P[I1R])
        delta -= Distance(P[I2L], P[I2])

    prob = 1.0
    if delta > 0.0:
        prob = math.exp(-delta / temp)

    if random.random() < prob:
        dist += delta
        seq[N1], seq[N2] = I2, I1
        return dist, True
    else:
        return dist, False

#*******************************************************************


def reverse(P, seq, dist, N1, N2, temp, nCity):
    N1L = (N1 - 1) % nCity
    N2R = (N2 + 1) % nCity
    if N1 == N2R or N2 == N1L:
        return dist, False
    delta = Distance(P[seq[N1L]], P[seq[N2]]) \
          + Distance(P[seq[N1]], P[seq[N2R]]) \
          - Distance(P[seq[N1L]], P[seq[N1]]) \
          - Distance(P[seq[N2]], P[seq[N2R]])
    prob = 1.0
    if delta > 0.0:
        prob = math.exp(-delta / temp)

    if random.random() < prob:
        dist += delta
        seq[N1:N2+1] = reversed(seq[N1:N2+1])
        return dist, True
    else:
        return dist, False


#*******************************************************************


if __name__ == '__main__':
    PNames = [] 
    P = readCities(PNames)
    nCity = len(P)

    maxTsteps = 250
    fCool = 0.9
    maxSwaps = 2000

    seq = np.arange(0, nCity, 1).tolist()
    dist = TotalDistance(P, seq)
    temp = 10.0 * dist

    print("\nInitial sequence:", seq)
    print(f"\nnCity = {nCity}  dist = {dist:.2f}  temp = {temp:.2f}\n")

    Plot(seq, P, dist, PNames)

    oldDist = 0.0
    convergenceCount = 0

    for t in range(1, maxTsteps + 1):
        if temp < 1.0e-6:
            break
        accepted = 0
        iteration = 0
        while iteration <= maxSwaps:
            N1 = random.randrange(nCity)
            N2 = random.randrange(nCity)
            if N1 == N2:
                continue
            if N2 < N1:
                N1, N2 = N2, N1

            if random.random() < 0.5 and (N1 + 1 != N2) and (N1 != (N2 + 1) % nCity):
                dist, flag = swap(P, seq, dist, N1, N2, temp, nCity)
            else:
                dist, flag = reverse(P, seq, dist, N1, N2, temp, nCity)

            if flag:
                accepted += 1
            iteration += 1

        print(f"Iteration {t}, temp = {temp:.4f}, dist = {dist:.2f}")
        if abs(dist - oldDist) < 1.0e-4:
            convergenceCount += 1
        else:
            convergenceCount = 0

        if convergenceCount >= 4:
            break

        if (t % 25) == 0:
            Plot(seq, P, dist, PNames)

        temp *= fCool
        oldDist = dist

    
    Plot(seq, P, dist, PNames)


#**************************___END___*********************************