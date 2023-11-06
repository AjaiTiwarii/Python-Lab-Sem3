from collections import Counter

def add_integers(lst):
    return sum(set([i for i in lst if type(i) == int]))

def check_consecutive(lst):
    indices = []
    for i in range(len(lst)-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            indices.append((i, i+1, i+2))
    return indices

def print_frequencies(lst):
    freq = Counter(lst)
    for key, value in freq.items():
        print(f"{key}: {value}")

def print_frequencies1(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        print(f"{key}: {value}")


def sort_elements(lst):
    return sorted(lst, key=lambda x: (len(str(x)), lst.count(x)))

def print_sublists(lst):
    int_list = [i for i in lst if type(i) == int]
    str_list = [i for i in lst if type(i) == str]
    float_list = [i for i in lst if type(i) == float]
    print(f"Integers: {int_list}")
    print(f"Strings: {str_list}")
    print(f"Floats: {float_list}")

lst = [1, 2, 2, 2, 'abc', 'def', 3.14, 2.71, 1, 1, 'ghi']
print(f"Sum of unique integers: {add_integers(lst)}")
print(f"Indices of consecutive elements: {check_consecutive(lst)}")
print("Frequencies:")
print_frequencies(lst)
print(f"Sorted list: {sort_elements(lst)}")
print("Sublists:")
print_sublists(lst)
