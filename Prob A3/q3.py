import matplotlib.pyplot as plt

piValue = 3.14
eValue = 2.7182

def squareRoot(number):
    return number ** 0.5

def exponential(power):
    return eValue ** power

def normalPdf(xValue, meanValue, stdDev):
    firstPart = 1 / (stdDev * squareRoot(2 * piValue))
    secondPart = -((xValue - meanValue) ** 2) / (2 * stdDev ** 2)
    return firstPart * exponential(secondPart)

def generateValues(start, end, step):
    values = []
    current = start
    while current <= end:
        values.append(current)
        current += step
    return values

xAxis = generateValues(-6, 6, 0.1)

pdfOne = []
for x in xAxis:
    pdfOne.append(normalPdf(x, 2, 0.5))

pdfTwo = []
for x in xAxis:
    pdfTwo.append(normalPdf(x, 2, 2))

pdfThree = []
for x in xAxis:
    pdfThree.append(normalPdf(x, 0, 1))

plt.figure()
plt.plot(xAxis, pdfOne)
plt.title("Gaussian Distribution N(2, 1/2)")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.show()

plt.figure()
plt.plot(xAxis, pdfTwo)
plt.title("Gaussian Distribution N(2, 2)")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.show()

plt.figure()
plt.plot(xAxis, pdfThree)
plt.title("Gaussian Distribution N(0, 1)")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.show()