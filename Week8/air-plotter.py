'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''

import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime

with open('/workspaces/Test-Repo/Week8/leeds-air-quality.csv', mode='r')as file:
    reader = csv.reader(file)
    next(reader)
    counter = 0
    data = []
    dates = []
    for lines in reader:
        data.append((float(lines[1]) + float(lines[2]) + float(lines[3]) + float(lines[4])) / 4)
        dates.append(datetime.datetime.strptime(lines[0], "%d/%m/%Y"))
        counter += 1
        if counter == 605:
            break

xpoints = np.array(dates)
ypoints = np.array(data)
plt.title("Aram Ajib")
plt.xlabel("Date")
plt.ylabel("Average Pollution")    
plt.plot(xpoints, ypoints)
plt.show()
