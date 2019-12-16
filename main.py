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
        self.fitness = fitness(a, b, c)


def init():
    for i in range(0, genome):
        a = random.uniform(-50, 50)
        b = random.uniform(-50, 50)
        c = random.uniform(-50, 50)
        population.append(CoEf(a, b, c))


def poly(x, a, b, c):
    return (a * (x ** 2)) + (b * x) + c


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


def fitness(a, b, c):
    diff = 0
    for i in range(0, 999):
        diff += abs(yCos[i] - poly(xCos[i], a, b, c))
    return diff


# Cut-Off half with low fitness
def selection():
    population.sort(key=lambda x: x.fitness, reverse=True)
    size = int(len(population) / 2)
    for i in range(0, size):
        population.remove(population[0])


def findIndex(size):
    rand_probability = random.randint(1, 100)
    if rand_probability <= 33:
        index = random.randint(0, int(size / 2))
    else:
        index = random.randint(int(size / 2), size - 1)
    return index


def cross(num1, num2):
    index = random.randint(0, 31)
    child1 = float_to_bin(num1)[0:index] + float_to_bin(num2)[index:len(float_to_bin(num1))]
    child2 = float_to_bin(num2)[0:index] + float_to_bin(num1)[index:len(float_to_bin(num1))]

    while (not (-50 <= float(bin_to_float(child1)) <= 50)) or (not (-50 <= float(bin_to_float(child2)) <= 50)):
        index = random.randint(0, 31)
        child1 = float_to_bin(num1)[0:index] + float_to_bin(num2)[index:len(float_to_bin(num1))]
        child2 = float_to_bin(num2)[0:index] + float_to_bin(num1)[index:len(float_to_bin(num1))]
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


def mutate():
    pass


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
