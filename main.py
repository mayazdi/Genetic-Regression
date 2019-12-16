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


def init():
    for i in range(0, genome):
        a = random.uniform(-50, 50)
        b = random.uniform(-50, 50)
        c = random.uniform(-50, 50)
        population.append(CoEf(a, b, c, 0))


def poly(x, a, b, c):
    return a * x ** 2 + b * x + c


def draw(coef):
    # for x in range(-100, 100, 1):
    # fig = plt.figure()
    # axes = fig.add_subplot(111)
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


def fitness(genome):
    diff = 0
    for i in range(0, 999):
        diff += abs(
            yCos[i] - poly(xCos[i], genome.a, genome.b, genome.c))
    genome.fitness = diff
    return


# Cut-Off half with low fitness
def selection():
    # shayad bayad reverse konam
    population.sort(key=fitness)
    size = int(len(population) / 2)
    for i in range(0, size):
        population.remove(population[0])


def findIndex():
    pass


def cross(num1, num2):
    index = random.randint(0, 31)
    child1 = float_to_bin(population[1])[0:index] + float_to_bin(population[1])[index:]
    child2 = float_to_bin(population[1])[0:index] + float_to_bin(population[1])[index:]
    while (not (-50 <= float(bin_to_float(child1)) <= 50)) or (not (-50 <= float(bin_to_float(child2)) <= 50)):
        index = random.randint(0, 31)
        child1 = float_to_bin(population[1])[0:index] + float_to_bin(population[1])[index:]
        child2 = float_to_bin(population[1])[0:index] + float_to_bin(population[1])[index:]
    li = [child1, child2]
    return li


def crossover():
    size = len(population)
    addition = []
    for i in range(0, size):
        index1 = findIndex()
        index2 = findIndex()
        A = cross(index1.a, index2.a)
        B = cross(index1.b, index2.b)
        C = cross(index1.c, index2.c)
        addition.append(CoEf(A[0], B[0], C[0]))
        addition.append(CoEf(A[1], B[1], C[1]))
    for i in range(0, len(addition)):
        population.append(addition[i])


def mutate():
    pass
    # for i in range(0, len(population)):
    #     probability = random.randint(0, 100000)
    #     if probability < 10:
    #         gen = population[i]


xCos = numpy.genfromtxt('x_train.csv', delimiter=',')
yCos = numpy.genfromtxt('y_train.csv', delimiter=',')
population = list()
generation = int(input("Number of Generation:"))
genome = int(input("Number of Genome:"))
print("----------------Initializing Genetic Algorithm----------------")
init()
for i in range(0, generation):
    draw(population[0])
    report(population[0])
    selection()
    crossover()
    mutate()
