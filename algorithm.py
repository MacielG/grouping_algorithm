# algorithm.py
def group_people(data, criteria=None):
    if criteria is None:
        criteria = {'gender': True}  # True for same, False for different

    groups = {}
    for index, person in data.iterrows():
        key = tuple(person[attr] for attr in criteria if criteria[attr])
        if key not in groups:
            groups[key] = []
        groups[key].append(person.to_dict())
    return groups
