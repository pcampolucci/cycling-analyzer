"""
Plot all the fields in the record separately in one figure.
"""

import matplotlib.pyplot as plt
import numpy as np

class Plotter:

    def __init__(self, data, log=None):
        self.data = data
        self.log = log

    def plot_all(self):
        # set the plotting parameters
        n_subplots = len(self.data.columns)
        fig, axes = plt.subplots(n_subplots, 1, sharex=True, figsize=(10, 10))

        # plot each field with title
        for i, field in enumerate(self.data.columns):
            axes[i].set_title(field)
            axes[i].plot(self.data[field], label=field)
            axes[i].legend()

        # show the plot
        plt.show()

    def plot_heart_rate(self):
        """Plot the heart rate"""
        plt.plot(self.data['heart_rate'], label='Heart rate')
        plt.legend()
        plt.show()
