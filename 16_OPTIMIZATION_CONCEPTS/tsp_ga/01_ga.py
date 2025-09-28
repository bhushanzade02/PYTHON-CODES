"""Travelling salesman problem using genetic algorithm"""


import random as rnd , numpy as np , pandas as pd , operator
import matplotlib.pyplot as plt 
from pylab import * 
from geopy.geocoders import Nominatim


#-------------------------------------------------------------------
#-------------------------------------------------------------------

class City : 
    def __init__(self , xx ,yy , nm , j):
        self.x= xx 
        self.y = yy
        self.name = nm
        self.Position= j 
        
    def Distance(self , city):
        if(self == city ):
            return 0.0 
        d = np.sqrt( (self.x - city.x)**2 + (self.y - city.y)**2 )
        # print( "d = ", d)
        return d
    
    def getPosition(self):
        return [self.x , self.y]
    
    def getName(self):
        return self.name
    
    def __repr__(self):
        str = self.name + "[" + str(self.x) + "," + str(self.y)
        str += "]"
        return str
    
#-------------------------------------------------------------------
#-------------------------------------------------------------------

class Fitness:
    def __init__ (self, route):
        self.seq = route
        self.totalDistance = 0.0 
        self.fitness = 0.0
        
    def pathLength(self):
        self.totalDistance = 0.0
        
        for i in range(0 , len(self.seq)):
            fromCity =self.seq[i]
            toCity = None
            if((i + 1 ) < len(self.seq)):
                toCity = self.seq[i+1]
            else :
                toCity = self.seq[0]
            dist = fromCity.Distance(toCity)
            self.totalDistance += dist
        return self.totalDistance 
    
    def pathFitness(self):
        if(abs(self.totalDistance)< 1.0e-6):
            tmp = self.pathLength()
        self.fitness = 1.0 / self.totalDistance
        return self.fitness
    
#-------------------------------------------------------------------
#-------------------------------------------------------------------

def readCities():
    cityList = []
    
    geolocator = Nominatim(user_agent = "The_TSP_GA_APP")
    
    j = 0 
    with open("./India_cities_GA.txt") as file :
        for line in file :
            city = line.rstrip('\n')
            if(city == "" ):
                break
            
            theLocation = city + ", India"
            pt = geolocator.geocode(theLocation, timeout = 10000)
            y = round(pt.latitude, 2)
            x = round(pt.longitude, 2)
            print("City[%2d] = %s (%5.2f , %5.2f)" %(j , city , x,y))
            cityList.insert(j ,City(x , y , city, j))
            j += 1
    return cityList

#-------------------------------------------------------------------
#-------------------------------------------------------------------

def createPath(cityList):
    # print(rnd , type(rnd))
    path = rnd.sample(cityList, len(cityList))
    return path

#-------------------------------------------------------------------
#-------------------------------------------------------------------

def initialPopulation(populationSize , cityList):
    population = []
    for i in range(0 , populationSize):
        population.append(createPath(cityList))
    return population
#-------------------------------------------------------------------
#-------------------------------------------------------------------

def rankPaths(popualtion):
    fitnessRank = {}
    for i in range(0 , len(popualtion)):
        fitnessRank[i] = Fitness(popualtion[i]).pathFitness()
    return sorted(fitnessRank.items(),key = operator.itemgetter(1), reverse=True)
#-------------------------------------------------------------------
#-------------------------------------------------------------------

# def selection(popRanked , elliteSize):
#     selected = []
#     df = pd.DataFrame(np.array(popRanked), columns= ['Index', 'Fitness'])
#     df['cumul_sum' ]= df.Fitness.cumsum()
#     df['cumul_perc'] = 100 * df.cumul_sum / df.Fitness.sum()
    
    
#     for i in range(0 , elliteSize):
#         selected.append(popRanked[i][0])
        
#     for i in range(0 , len(popRanked) - elliteSize):
#         pick = 100 * rnd.random()
    
#     for i in range(0 , len(popRanked)):
#         if pick <= df.iat[i,3]:
#             selected.append(popRanked[i][0])
#             break
#     return selected




def selection(popRanked, eliteSize):
    selectionResults = []

    # Elitism: keep the best eliteSize individuals
    for i in range(eliteSize):
        selectionResults.append(popRanked[i][0])

    # Convert to DataFrame for cumulative probability
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    # Roulette wheel selection for the rest
    for _ in range(len(popRanked) - eliteSize):
        pick = 100 * rnd.random()
        for i in range(len(popRanked)):
            if pick <= df.iat[i, 3]:  
                selectionResults.append(popRanked[i][0])
                break

    return selectionResults


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def matingPool(population, selected):
    matingpool =[]
    for i in range(0 , len(selected)):
        index = selected[i]
        matingpool.append(population[index])
    return matingpool

#-------------------------------------------------------------------
#-------------------------------------------------------------------

def breed(parent1, parent2):
    child = []
    child_P1 = []
    child_P2 = []

    # Choose two random cut points
    geneA = int(rnd.random() * len(parent1))
    geneB = int(rnd.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    # Take the slice from parent1
    for i in range(startGene, endGene):
        child_P1.append(parent1[i])

    # Fill the remaining from parent2 in order
    child_P2 = [item for item in parent2 if item not in child_P1]

    # Final child = preserved slice + remaining from parent2
    child = child_P1 + child_P2
    return child

#-------------------------------------------------------------------
#-------------------------------------------------------------------


def breedNewChildren(matingpool , elliteSize):
    children = []
    length = len(matingpool) - elliteSize
    pool = rnd.sample(matingpool , len(matingpool))
    
    
    for i in range(0 , elliteSize):
        children.append(matingpool[i])
        
        
    for i in range(0 , length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    
    return children

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------


def mutate(items , mutationRate):
    for swapped in range(len(items)):
        if(rnd.random() < mutationRate):
            swapWith = int(rnd.random() * len(items))
            city1 = items[swapped]
            city2 = items[swapWith]
            
            items[swapped] = city2
            items[swapWith] = city1
    return items 

def mutatePopulation(population , mutationRate):
    mutatedPop = []
    
    for ind in range(0 , len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

#-------------------------------------------------------------------
#-------------------------------------------------------------------

def nextGeneration(currentGen, elliteSize , mutationRate):
    popRanked = rankPaths(currentGen)
    selectionResults = selection(popRanked, elliteSize)
    mating_pool = matingPool(currentGen, selectionResults)  
    children = breedNewChildren(mating_pool, elliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

#-------------------------------------------------------------------
#-------------------------------------------------------------------

def geneticAlgorithm(population, popSize ,elliteSize , mutationRate , generations):
    pop = initialPopulation(popSize , population)
    print("Intial distance : " + str (1 / rankPaths(pop)[0][1]))
    
    for i in range(0 , generations):
        pop = nextGeneration(pop , elliteSize , mutationRate)
        
    
    print("Final distance " + str(1 / rankPaths(pop)[0][1]))
    bestRouteIndex = rankPaths(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute
#-------------------------------------------------------------------
#-------------------------------------------------------------------

def plotRoute(cityList):
    # plot
    Pt = [cityList[i].getPosition() for i in range(len(cityList))]
    Pt += [cityList[0].getPosition()]
    Pt = array(Pt)
    plt.plot(Pt[:,0], Pt[:,1], '-o')
    
    for i in range(len(cityList)):
        coord = cityList[i].getPosition()
        annotate(cityList[i].getName(),(coord[0],coord[1]))
    plt.show()
        
#-------------------------------------------------------------------
#-------------------------------------------------------------------

def geneticAlgorithmPlot(population , popSize , elliteSize , mutationRate, generations ): # # ## ## ## # ## #
    pop = initialPopulation(popSize , population)
    print("Initial distance " + str (1 / rankPaths(pop)[0][1]))
    progress = []
    progress.append(1 / rankPaths(pop)[0][1])
    
    for i in range(0 , generations):
        pop = nextGeneration(pop , elliteSize , mutationRate)
        progress.append(1 / rankPaths(pop)[0][1])
        if (i % 50 == 0) :
            print(i)
            
            
    plt.plot(progress)
    plt.ylabel("distance")
    plt.xlabel("Generation")
    plt.show()
    
    print("Final distance " + str (1 / rankPaths(pop)[0][1]))
    bestRouteIndex = rankPaths(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


if __name__ == '__main__':
    
    cityList = readCities()
    nCity = len(cityList)  
    
    
    print("\n nCity = %3d \n" % (nCity))
    input("Press Enter to continue....")
    
    
    plotRoute(cityList)
    
    
    
    bestRoute = geneticAlgorithmPlot(population= cityList , popSize= 100 ,elliteSize=90 , mutationRate= 0.08, generations=50)
    
    
    
    plotRoute
    (bestRoute)  