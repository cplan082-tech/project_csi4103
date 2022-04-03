import csv
import math

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

def angles_to_xy(rows):

    inner_arm = 10 # in cm, from prototype
    outer_arm = 11 # in cm, from prototype

    header = ['X', 'Y']
    data = [] # empty array to store X,Y coordinates

    for elements in rows:

        shoulder_motor_angle = float(elements[0])
        elbow_motor_angle = float(elements[1])

        """Return the x/y co-ordinates represented by a pair of servo angles."""

        elbow_motor_angle = math.radians(elbow_motor_angle)
        shoulder_motor_angle = math.radians(shoulder_motor_angle)

        """Using cosine law, we can find relations to get the x and y coordinates"""
        hypotenuse = math.sqrt(inner_arm ** 2 + outer_arm ** 2 - 2 * inner_arm * outer_arm * math.cos(math.pi - elbow_motor_angle))
        base_angle = math.acos((hypotenuse ** 2 + inner_arm ** 2 - outer_arm ** 2) / (2 * hypotenuse * inner_arm))
        inner_angle = base_angle + shoulder_motor_angle

        x = math.sin(inner_angle) * hypotenuse
        y = math.cos(inner_angle) * hypotenuse
        data.append([x,y])

    filename = 'xycoordinates.csv' # create new file to store CSV - IT WILL OVERWRITE EXISTING FILES OF THE SAME NAME
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(data)
    return

def main(filename):
    rows = read_csv_file(filename) #change name to actual file name
    angles_to_xy(rows)
    return

if __name__ == "__main__":
	main()
