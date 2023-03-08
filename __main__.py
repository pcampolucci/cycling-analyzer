"""
Main module for the workout analyzer.
"""

import logging
import matplotlib
from read_fit import Reader
from plot_all import Plotter

# setup logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Get the logger for the current module
logger = logging.getLogger(__name__)


# Define a custom filter class that ignores messages from matplotlib
class MatplotlibFilter(logging.Filter):
    def filter(self, record):
        return not record.name.startswith(matplotlib.__name__)


# Add the filter to the logger
logger.addFilter(MatplotlibFilter())

file = "sample_2"
reader = Reader(file, logger)
data = reader.get_data()

plotter = Plotter(data, logger)
plotter.plot_heart_rate()

# print reader
print(reader)
