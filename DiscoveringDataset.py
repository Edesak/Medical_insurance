from builtins import set


class DiscoverDict:

    def __init__(self, dictionary: dict):
        """
        Simple class that will help with discovery of dataset.

        - Average age of subjects
        - Average age of subjects with specified number of children
        - Major region of subjects
        - Difference between cost smoker and non-smoker in average

        :param dictionary: Give dictionary to this object
        :type dictionary: Dictionary
        """
        self.dictionary = dictionary

    def average_age(self):
        """
        Will calculate average age of subjects.
        Dictionary must have keyword "age".

        :returns: average_age
        :rtype: float

        """
        total_age = 0
        num_of_people = len(self.dictionary["age"])
        for age in self.dictionary["age"]:
            total_age += int(age)
        avg_age = total_age / num_of_people
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




