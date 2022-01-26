import csv


def prepare(name_of_csv: str):
    """
    Simple function to prepare CSV.

    :param name_of_csv: Name of CSV that you want to prepare,
    :return: Dictionary separated by fields.
    :rtype: dict
    """
    fieldnames = []
    insurance_dict = {}
    with open(name_of_csv) as insurance_file:
        insurance_reader = csv.DictReader(insurance_file)
        fieldnames = next(insurance_reader)
        for field in fieldnames:
            insurance_dict[field] = []
        for row in insurance_reader:
            for field in fieldnames:
                insurance_dict[field].append(row[field])
    return insurance_dict
