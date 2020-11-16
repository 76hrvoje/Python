
with open("homework.csv", "r") as csvfile:
    csvfile = csvfile.read()
    csvfinal=csvfile.splitlines()

    for row in csvfinal:
        byrow = row.split(",")
        print(byrow)
        print (byrow[0],"is",byrow[1],"years old and",byrow[2])

