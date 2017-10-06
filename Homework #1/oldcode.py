from random import randint
# from future import print

l = []
eta = 0.01
with open("zdata.txt", "r") as f:
    for line in f:
        s = line[:-1].split("\t")
        l.append((int(s[0]), int(s[1])))

w0 = randint(1, 101)
w1 = randint(1, 101)
yErr = []
for i in range(1500):
    for j in range(len(l)):
        people = l[j][0]
        calories = l[j][1]
        y = calories
        yCap = (w0 * 1) + (w1 * people)
        yE = y - yCap
        yErr.append(yE)
    print(sum(yErr) / len(l))

    for k in range(len(l)):
        w0 = w0 + eta * yErr[k] * 1
        w1 = w1 + eta * yErr[k] * l[k][0]
    yErr=[]

print(w0, w1)
