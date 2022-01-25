import csv
from DiscoveringDataset import DiscoverDict
#Importing dataset to dictionary
fieldnames = []
insurance_dict = {}

with open("insurance.csv") as insurance_file:
    insurance_reader = csv.DictReader(insurance_file)
    fieldnames = next(insurance_reader)

    for field in fieldnames:
        insurance_dict[field] = []
    for row in insurance_reader:
        for field in fieldnames:
            insurance_dict[field].append(row[field])

#Createting object
dis_dict = DiscoverDict(insurance_dict)

print(f"Average age: {dis_dict.average_age():.2f} ")

num_of_people,avrg_age,num_of_children = dis_dict.average_age_children(0)
print(f"There are {num_of_people} subjects with {num_of_children} children. The average age of these subjects is {avrg_age:.2f}")

region_count= dis_dict.region_count()

for region in region_count:
    print(f"There are {region_count[region]} subjects in {region}")


