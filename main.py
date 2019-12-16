import random
import struct

import matplotlib.pyplot as plt
import numpy


def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')


def bin_to_float(binary):
    return struct.unpack('!f', struct.pack('!I', int(binary, 2)))[0]


class CoEf:
    def __init__(self, a, b, c, f):
        self.a = a
        self.b = b
        self.c = c
        self.fitness = f


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


def report():
    print("Best found yet:", end="\n a:")
    print(population[0].a, end="\t b:")
    print(population[0].b, end="\t c:")
    print(population[0].c, end="\n fitness:")
    print(population[0].fitness)
    print("-----------------------------------------------")


def fitness(genome):
    diff = 0
    for i in range(0, 999):
        diff += abs(
            yCos[i] - poly(xCos[i], genome.a, genome.b, genome.c))
    return diff


# Cut-Off half with low fitness
def selection():
    # shayad bayad reverse konam
    population.sort(key=fitness)
    size = int(len(population) / 2)
    for i in range(0, size):
        population.remove(population[0])


def crossover():

    pass


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
    selection()
    crossover()
    mutate()
