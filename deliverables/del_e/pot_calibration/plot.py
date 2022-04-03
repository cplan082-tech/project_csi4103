import csv
import math
import numpy as np
import matplotlib.pyplot as plt

def read_csv_file(name):
    file = open(name)
    type(file)
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader) #First line of CSV is name of headers

    "Populates array with rows from CSV [[shoulder_angle_1,elbow_angle_2],...]"
    rows = []
    for row in csvreader:
        rows.append(row)

    file.close()
    return rows

def plot(rows):
    for row in rows:
        x = float(row[0])
        y = float(row[1])
        plt.scatter(x,y,s=1.5, color='black')
    plt.axis('off')
    fig = plt.gcf()
    fig.savefig('scanned_image.png',dpi=100)
    plt.show()
    return

def main():
    rows = read_csv_file('xycoordinates.csv') #change name to actual file name
    plot(rows)

if __name__ == "__main__":
	main()
