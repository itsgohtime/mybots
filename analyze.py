import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/BackLegSensorValues.npy")
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()