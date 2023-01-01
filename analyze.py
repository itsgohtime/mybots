import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
matplotlib.pyplot.plot(backLegSensorValues, label = "back", linewidth = 3)
matplotlib.pyplot.plot(frontLegSensorValues, label = 'front', linewidth = 0.75)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
