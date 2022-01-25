from builtins import set


class DiscoverDict:

    def __init__(self, dictionary: dict):
        """
        Simple class that will help with discovery of dataset.

        - Average age of subjects
        - Average age of subjects with specified number of children
        - Major region of subjects
        - Average cost total
        - Difference between cost smoker and non-smoker in average
        - Average BMI

        :param dictionary: Give dictionary to this object
        :type dictionary: Dictionary
        """
        self.dictionary = dictionary
        self.length = len(dictionary["age"])
        print("Number of loaded subjects: {}".format(len(dictionary["age"])))

        for sex_index in range(len(self.dictionary["sex"])):
            if self.dictionary["sex"][sex_index] == "female":
                self.dictionary["sex"][sex_index] = 1
            else:
                self.dictionary["sex"][sex_index] = 0

        for smoker_index in range(len(self.dictionary["smoker"])):

            if self.dictionary["smoker"][smoker_index] == "yes":
                self.dictionary["smoker"][smoker_index] = 1
            else:
                self.dictionary["smoker"][smoker_index] = 0

    def num_of_subjects(self):
        """

        :return: number of subjects
        :rtype: int
        """
        return len(self.dictionary["age"])

    def average_age(self):
        """
        Will calculate average age of subjects.
        Dictionary must have keyword "age".

        :returns: average_age
        :rtype: float

        """
        total_age = 0
        for age in self.dictionary["age"]:
            total_age += int(age)
        avg_age = total_age / self.length
        return avg_age

    def average_age_children(self, num_of_children: int):
        """
        Will calculate average age of subjects with specified number of children.

        Dictionary must have keyword "age".

        Dictionary must have keyword "children".

        :param num_of_children: Choose how many children should subject have
        :type: int


        :return: (number_of_people, average_age, number_of_children)

        :rtype: tuple
        """
        total_age = 0
        num_of_people = 0
        for children,age in zip(self.dictionary["children"],self.dictionary["age"]):
            if int(children) == num_of_children:
                total_age += int(age)
                num_of_people += 1
        if num_of_people != 0:
            avg_age = total_age / num_of_people
        else:
            avg_age = 0

        return num_of_people, avg_age, num_of_children

    def region_count(self):
        """
        Returns number of subjects per region.

        :return: counts_per_region
        :rtype: dict
        """
        regions = set(self.dictionary["region"])
        regions_count = {x:0 for x in regions}

        for region in self.dictionary["region"]:
            regions_count[region] +=1
        return regions_count

    def average_cost(self):
        """
        Calculate average cost of insurace.

        :return: average_cost
        :rtype: float
        """
        total_cost = 0
        for cost in self.dictionary["charges"]:
            total_cost += float(cost)
        average_cost = total_cost/self.length
        return average_cost

    def difference_smoker_non_smoker(self):
        """
        Calculate difference between cost of insurace smoker and non_smoker.

        Taking formula of:

        difference = smoker - non_smoker

        :return: (num_of_smokers,num_of_non_smokers,average_smoker,average_non_smoker,difference_in_cost)
        :rtype: tuple
        """
        total_cost_smoker = 0
        total_cost_non_smoker = 0

        num_of_smokers = 0
        num_of_non_smokers = 0
        for smoker,cost in zip(self.dictionary["smoker"],self.dictionary["charges"]):
            if smoker == 0:
                total_cost_non_smoker += float(cost)
                num_of_non_smokers +=1
            else:
                total_cost_smoker += float(cost)
                num_of_smokers +=1


        average_non_smoker = total_cost_non_smoker/num_of_non_smokers
        average_smoker = total_cost_smoker/num_of_smokers
        difference_in_cost = average_smoker - average_non_smoker

        return num_of_smokers,num_of_non_smokers,average_smoker,average_non_smoker,difference_in_cost

    def average_bmi(self):
        """
        Calculate average BMI in dataset.

        :return: average_bmi
        :rtype: float
        """
        total_bmi = 0

        for bmi in self.dictionary["bmi"]:
            total_bmi += float(bmi)
        average_bmi = total_bmi/self.length

        return average_bmi






