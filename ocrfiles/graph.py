import matplotlib.pyplot as plt
import csv

x = []
y = []

with open ("data.csv", "r") as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
        x.append(row[0])
        y.append(row[0])

plt.plot(x, y, label='Sample')

plt.xlabel("x axis")
plt.ylabel("y axis")

plt.title("One line graph")

plt.legend()

plt.show()