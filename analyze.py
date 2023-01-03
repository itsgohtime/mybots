import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetangles_bl = numpy.load("data/targetangles_bl.npy")
matplotlib.pyplot.plot(targetangles_bl)
targetangles_fl = numpy.load("data/targetangles_fl.npy")
matplotlib.pyplot.plot(targetangles_fl)
#matplotlib.pyplot.plot(backLegSensorValues, label = "back", linewidth = 3)
#matplotlib.pyplot.plot(frontLegSensorValues, label = 'front', linewidth = 0.75)
#matplotlib.pyplot.legend()
matplotlib.pyplot.show()
