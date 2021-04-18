import numpy as np


# Tried to generate a random number generator as per the following requirements from math.stackexchange:
# https://math.stackexchange.com/q/4106115/439353
#
# What algorithms exist, if any, for (pseudo-) random dice rolls such that some aggregate properties
# across many rolls are obeyed, for example,
#
# I want to get to roll a 3-sided die (faces 'A', 'B', 'C') such that, if rolled 100 times:
#
# 1. the expected numbers of 'A', 'B', 'C' are 90, 8, 2 respectively;
# 2. the number of 'A' rolls will be between 89 and 91 with probability 67%
# or some other similar such specification. I am still looking for algorithms that can provide a random(-looking)
# single roll; but over many rolls I do not want the cumulative results to follow a binomial distribution but
# rather one like I've specified. What should I look into for such pseudo-random rolling algorithms? (Pseudo-code,
# or actual code in say R or Python or Mathematica, would also be very appreciated)
#
# EDIT: I know how to satisfy property (1), it's (2) I'm interested in


def normal(size=1, mean=0, sigma=1):
    if size == 1:
        return mean + sigma * np.random.randn()
    return mean + sigma * np.random.randn(size)


def ABCgenerator(size, mean, sigma, BCThreshold=0.5):
    Xn = normal(size, mean, sigma)
    Yn = 1 - Xn
    Sn = Yn
    for index in range(len(Sn)):
        Sn[index] = Sn[index - 1] + Sn[index]
    thresholds = np.array(range(size)) + np.random.rand(size)

    outList = []
    j = 0
    for i in range(size):
        if Sn[i] > thresholds[j]:
            if np.random.rand() < BCThreshold:
                outList.append("B")
            else:
                outList.append("C")
            j += 1
        else:
            outList.append("A")
    return outList


if __name__ == "__main__":
    np.random.seed(8)
    print(ABCgenerator(100, 0.9, 0.045, 0.8))
