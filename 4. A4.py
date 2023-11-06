def int_to_roman(num):
    roman_nums = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
    if num in roman_nums:
        return roman_nums[num]
    else:
        return "Number out of range"

# Test the function
print(int_to_roman(6))  # Output: VI


def longest_common_prefix_pair(words):
    # Start with an empty string for the longest common prefix
    longest_prefix = ""

    # Compare each pair of words
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            # Start with the whole first word as the prefix
            prefix = words[i]

            # Check if the second word starts with the prefix
            while words[j][:len(prefix)] != prefix and prefix:
                # If not, remove the last letter from the prefix
                prefix = prefix[:-1]

            # If this prefix is longer than the current longest, update it
            if len(prefix) > len(longest_prefix):
                longest_prefix = prefix

    # If no common prefix was found, return None
    return longest_prefix if longest_prefix else None

# Test the function
words = ["flight", "flower", "flow", "Ball"]
print(longest_common_prefix_pair(words))  # Output: "fl"


def merge_sort_and_count(list1, list2):
    # I. Merge two integer lists
    merged_list = list1 + list2
    print("Merged list:", merged_list)

    # II. Sort the list in descending order
    sorted_list = []
    while merged_list:
        max_val = merged_list[0]
        for i in range(1, len(merged_list)):
            if merged_list[i] > max_val:
                max_val = merged_list[i]
        sorted_list.append(max_val)
        merged_list.remove(max_val)
    print("Sorted list:", sorted_list)

    # III. Print each integer and their frequencies
    freq_dict = {}
    for num in sorted_list:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    print("Frequencies:", freq_dict)

# Test the function
list1 = [2, 4, 1]
list2 = [1, 6, 3]
merge_sort_and_count(list1, list2)


def is_palindrome(s):
    # Convert the string to lowercase to ignore case sensitivity
    s = s.lower()

    # Remove spaces from the string
    s = s.replace(" ", "")

    # Check if the string is the same as its reverse
    return s == s[::-1]

# Test the function
print(is_palindrome("Able was I ere I saw Elba"))  # Output: True



