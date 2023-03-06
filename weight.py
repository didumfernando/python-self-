heaviest = 29
lightest = 151
total = 0
student = int(input("Enter number of students: "))
for count in range(student):
    weight = int(input("Enter your weight(in kg): "))
    if not(30 < weight <150):
        weight = int(input("Re-enter your weight(in kg) in range 30kg-150kg: "))
    if weight > heaviest:
        heaviest = weight
    if weight < lightest:
        lightest = weight
    total = total + weight
    avg = float(total/student)

print("Heaviest weight is " + str(heaviest) + "kg")
print("Lightest weight is " + str(lightest) + "kg")
print("Average weight is {:.1f} kg".format(avg))
print("Total weight for all the students is " + str(total) + "kg")
