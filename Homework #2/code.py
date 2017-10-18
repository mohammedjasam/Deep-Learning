import math
from random import randint

# Sigmoid Function
def sigmoid(x):
  return 1 / (1 + math.e**(-x))


# Variable declarations
X = []
examples = []
YCap = 0
error = []
eta = 0.05
delta = 0

# Collect examples from the data
with open("pizzacatdata.txt") as f:
    for line in f:
        examples.append( ([int(x) for x in line[:-4].split()], int(line[-3])) )


# Randomly assigned 5 weights
# w = []
# for i in range(5):
#     w.append(randint(-100,100))
# # w = [77, -45, -29, -41, -76]
# print("Initial Weights")
# print(w)
# print()

SSE = []
cSSE = []
# Run Experiment 5000 times
for ab in range(1000):
    w = []
    for i in range(5):
        w.append(randint(-100,100))
    iterations = 5000
    for i in range(iterations):
        YCap = 0
        SSE = []
        for e in examples:
            X = [1] + e[0]
            Y = e[1]

            for j in range(5):
                YCap += w[j]*X[j]
            YCap = sigmoid(YCap)
            p = YCap

            delta = Y - YCap
            SSE.append(delta**2)

            for index in range(len(w)):
                w[index] = w[index] + eta * delta * p * (1 - p) * X[index]
                # w[index] = w[index] + eta * delta * X[index]
    cSSE.append(sum(SSE))
    print(ab , sorted(cSSE)[0])

# print(sorted(cSSE))
# # Output Part
# print("CS-5001 : HW#2 : Logistic Regression.")
# print("Programmer : Mohammed Jasam")
# print("No cats were hurt gathering this data.\n")
# print("Learning Rate eta = "+str(eta))
# print("After " + str(iterations) + " iterations:")
# print("Sum of Squares Error = " + str(sum(SSE)))
# print("Weights:\nw0 = " + str(w[0]) + "\nw1 = " + str(w[1]) + "\nw2 = " + str(w[2]) + "\nw3 = " + str(w[3]) + "\nw4 = " + str(w[4]))
# print(w)
