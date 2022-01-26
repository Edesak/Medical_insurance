from Dataset_prep import prepare
from DiscoveringDataset import DiscoverDict

insurance_dict = prepare(name_of_csv="insurance.csv")

# Createting object
dis_dict = DiscoverDict(insurance_dict)
length = dis_dict.num_of_subjects()
num_of_smokers, num_of_non_smokers, _, _, difference = dis_dict.difference_smoker_non_smoker()
region_count = dis_dict.region_count()
num_of_people, average_age_child, num_of_children = dis_dict.average_age_children(0)
average_bmi = dis_dict.average_bmi()
average_cost = dis_dict.average_cost()
average_age = dis_dict.average_age()

print(f"Average age of subjects is {average_age:.2f} ")
print(f"There are {num_of_people} subjects with {num_of_children} children. The average age of these subjects is {average_age_child:.2f}")
print(f"Average cost of insurace is {average_cost:.2f} USD.")
print(f"There are {num_of_smokers} smokers and {num_of_non_smokers} none smokers in dataset.")
print(f"Smoker pay in average: {difference:.2f} USD more/less than non-smoker.")
print(f"Average BMI in dataset is {average_bmi:.2f}")

for region in region_count:
    print(f"There are {region_count[region]} subjects in {region}")

dict_summary = {"Number of subjects": length, "Number of subjects per region": region_count,
                "Average BMI": dis_dict.average_bmi(),
                "Average age": average_age, "Average cost": average_cost,
                "Difference between smoker/non-smoker": difference}
