# TASK 1: AI-Powered Code Completion
# File: task1_code_completion.py

# -----------------------------------------
# MANUAL VERSION: Sort a list of dictionaries by a key
# -----------------------------------------

def sort_dict_list(data, sort_key):
    return sorted(data, key=lambda x: x[sort_key])

# Example data
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]

# Run manual version
sorted_data = sort_dict_list(data, 'age')
print("Sorted manually by age:")
print(sorted_data)

# -----------------------------------------
# AI VERSION: Sort by key (AI-suggested)
# -----------------------------------------

def sort_by_key(dict_list, key):
    return sorted(dict_list, key=lambda d: d.get(key, 0))

# Run AI version
ai_sorted = sort_by_key(data, 'age')
print("Sorted using AI-suggested function:")
print(ai_sorted)
