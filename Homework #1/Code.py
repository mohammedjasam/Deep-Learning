from random import randint

# Extract all the data from the file to list examples
examples = []
with open("zdata.txt", "r") as f:
    for line in f:
        line = line[:-1].split("\t")
        examples.append((int(line[0]), int(line[1])))

# Randomly assigns weights to W0 and W1
weight = []
weight.append(randint(0, 20000))
weight.append(randint(0, 20000))

# Error list
error = [0, 0]
eta = 0.001

# Running 1500 iterations
X = [1, 0] # Xi values!
delta = 0
for x in range(1500):
    for k in range(len(examples)):
        X[1] = examples[k][0]
        Y = examples[k][1]
        YCap = (weight[0] * X[0]) + (weight[1] * X[1])
        delta = (Y - YCap)

        for i in range(2):
            error[i] = error[i] + delta * X[i]

    for i in range(2):
        error[i] = (1 / len(examples)) * error[i]
        weight[i] = weight[i] + eta * error[i]
    # print(delta)
    error = [0, 0]

SSE = delta * delta
print("CS-5001 : HW#1 : Regression with one variable.")
print("Programmer : Mohammed Jasam")
print("Learning Rate eta = 0.001")
print("After 1500 iterations:")
print("Sum of Squares Error = " + str(SSE))
print("Weights:\nw0 = "+str(weight[0])+"\nw1 = "+str(weight[1]))
