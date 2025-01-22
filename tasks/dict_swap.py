# Swap items in dictionary 7kyu

# In this kata, you will take the keys and values of a dict and swap them around.
# You will be given a dictionary, and then you will want to return a dictionary with the old values as the keys, and list the old 
# keys as values under their original keys.

# For example, given the dictionary: {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'},
# you should return: {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}

# Notes:
# The dictionary given will only contain strings
# The dictionary given will not be empty
# You do not have to sort the items in the lists

def switch_dict(dic):
    new_dict = {}
    for key, value in dic.items():
        new_dict.setdefault(value, []).append(key)
    
    return new_dict

    # for key, value in dic.items():    
    #     if value not in new_dict:
    #         new_dict[value] = [key]         
    #     else:
    #         new_dict[value].append(key)

    # return new_dict

print(switch_dict({'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}))  
# {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}