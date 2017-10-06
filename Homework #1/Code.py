import random

# Randomly assigns weights to W0 and W1
weight = []
weight.append(random.random())
weight.append(random.random())

# Error list
error = []

# Extract all the data from the file to list examples
examples = []
with open("zdata.txt", "r") as f:
    for line in f:
        line = line[:-1].split("\t")
        examples.append((int(line[0]), int(line[1])))

for i in range(len(examples)):
    error.append(0)

print(examples[-1][0])
# Running 1500 iterations
X = [1,0] # Xi values!
for i in range(1500):
    for k in range(len(examples)):
        X[1] = examples[k][0]
        Y = examples[k][1]
        YCap = (weight[0] * X[0]) + (weight[1] * X[1])
        error[k] = error[k] + (Y - YCap)*examples[-1][0]
    
