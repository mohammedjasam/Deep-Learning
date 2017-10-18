from random import randint
# import matplotlib.pyplot as plt

# Variable declarations
examples = []
initialX, initialY, weight = [], [], []
error = [0, 0]
delta = 0
eta = 0.001
X = [1, 0]

# Extract all the data from the file to list examples
with open("zdata.txt", "r") as f:
    for line in f:
        line = line[:-1].split("\t")
        examples.append((int(line[0]), int(line[1])))
        initialX.append(int(line[0]))
        initialY.append(int(line[1]))

weight.append(randint(0, 20000))
weight.append(randint(0, 20000))

SSE = []
# Running 1500 iterations
for x in range(1500):
    finalY = []
    SSE = []
    for k in range(len(examples)):
        X[1] = examples[k][0]
        Y = examples[k][1]
        YCap = (weight[0] * X[0]) + (weight[1] * X[1])
        delta = (Y - YCap)
        finalY.append(YCap)
        SSE.append(delta * delta)
        for i in range(2):
            error[i] = error[i] + delta * X[i]

    for i in range(2):
        error[i] = (1 / len(examples)) * error[i]
        weight[i] = weight[i] + eta * error[i]
    error = [0, 0]

# Output Part
print("CS-5001 : HW#1 : Regression with one variable.")
print("Programmer : Mohammed Jasam\n\n")
print("Learning Rate eta = 0.001")
print("After 1500 iterations:")
print("Sum of Squares Error = " + str(sum(SSE)))
print("Weights:\nw0 = " + str(weight[0]) + "\nw1 = " + str(weight[1]))

# Plotting Observed and Predicted Values
# plt.plot(initialX, initialY, 'ro')
# plt.plot(initialX, finalY, 'b')
# plt.legend(['Observed Y', 'Predicted Y'], loc='upper left')
# plt.show()
