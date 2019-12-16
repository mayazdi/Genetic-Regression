# Code Available at https://github.com/mayazdi/Genetic-Regression
import random
import struct

import matplotlib.pyplot as plt
import numpy


def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')


def bin_to_float(binary):
    return struct.unpack('!f', struct.pack('!I', int(binary, 2)))[0]


class CoEf:
    fitness = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.fitness = fitness_calc(a, b, c)


def fitness_calc(a, b, c):
    diff = 0
    for i in range(0, 999):
        diff += abs(yCos[i] - poly(xCos[i], a, b, c))
    return diff


def poly(x, a, b, c):
    return (a * (x ** 2)) + (b * x) + c


def draw(coef):
    v = numpy.arange(-100, 100, 1)
    plt.plot(v, poly(v, coef.a, coef.b, coef.c))
    plt.show()


def report(individual):
    print("Best found yet:", end="\n a:")
    print(individual.a, end="\t b:")
    print(individual.b, end="\t c:")
    print(individual.c, end="\n fitness:")
    print(individual.fitness)
    print("-----------------------------------------------")


# Initial Genomes
def init():
    for i in range(0, genome):
        a = random.uniform(-50, 50)
        b = random.uniform(-50, 50)
        c = random.uniform(-50, 50)
        population.append(CoEf(a, b, c))


# Cut-Off half with low fitness
def selection():
    population.sort(key=lambda x: x.fitness, reverse=True)
    size = int(len(population) / 2)
    for i in range(0, size):
        population.remove(population[0])


# Fetch random Index
def findIndex(size):
    rand_probability = random.randint(1, 100)
    if rand_probability <= 33:
        index = random.randint(0, int(size / 2))
    else:
        index = random.randint(int(size / 2), size - 1)
    return index


# Cross two A or B or C of CoEf[ind1] & CoEf[ind2]
def cross(num1, num2):
    index = random.randint(0, 31)
    child1 = float_to_bin(num1)[0:index] + float_to_bin(num2)[index:]
    child2 = float_to_bin(num2)[0:index] + float_to_bin(num1)[index:]
    while not ((-50 <= float(bin_to_float(child1)) <= 50) and (-50 <= float(bin_to_float(child2)) <= 50)):
        index = random.randint(0, 31)
        child1 = float_to_bin(num1)[0:index] + float_to_bin(num2)[index:]
        child2 = float_to_bin(num2)[0:index] + float_to_bin(num1)[index:]
    li = [bin_to_float(child1), bin_to_float(child2)]
    return li


def crossover():
    size = len(population)
    addition = []
    for i in range(0, size, 2):
        index1 = findIndex(size)
        index2 = findIndex(size)
        A = cross(population[index1].a, population[index2].a)
        B = cross(population[index1].b, population[index2].b)
        C = cross(population[index1].c, population[index2].c)
        addition.append(CoEf(A[0], B[0], C[0]))
        addition.append(CoEf(A[1], B[1], C[1]))
    for i in range(0, len(addition)):
        population.append(addition[i])


def switch(num):
    if num == 0:
        return 1
    else:
        return 0


# Mute A, B and C of CoEf's
def mute(num):
    # Float is 32 Bits, So we decide for the chosen bit next line!
    index = random.randint(0, 31)
    ind = num
    ind = float_to_bin(ind)
    ind = ind[0:index] + str(switch(ind[index])) + ind[index + 1:len(ind)]
    while not (-50 <= float(bin_to_float(ind)) <= 50):
        index = random.randint(0, 31)
        ind = num
        ind = float_to_bin(ind)
        ind = ind[0:index] + str(random.randint(0, 1)) + ind[index + 1:len(ind)]
    result = float(bin_to_float(ind))
    return result


def mutate():
    size = len(population)
    for i in range(0, size):
        probability = random.randint(0, 100)
        if probability < 10:
            A = mute(population[i].a)
            B = mute(population[i].b)
            C = mute(population[i].c)
            population[i] = CoEf(A, B, C)


# Code Initiate here
xCos = numpy.genfromtxt('x_train.csv', delimiter=',')
yCos = numpy.genfromtxt('y_train.csv', delimiter=',')
population = list()
generation = int(input("Number of Generation:"))
genome = int(input("Number of Genome:"))
print("-------------------Initializing Genetic Algorithm-------------------")
init()
for i in range(0, generation):
    draw(population[0])
    report(population[0])
    selection()
    crossover()
    mutate()
