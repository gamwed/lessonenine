# task 1
# if len(lst) == len(set(lst)):
#         return True
#     else:
#         return False
# task 2
# def count_unique_elements(lst):
#     unique_elements = set(lst)
#     return len(unique_elements)
# task 3
# def check_unique_values(dictionary):
#     values = list(dictionary.values())
#     unique_values = set(values)
#     return len(values) == len(unique_values)
# task 4


# task 5
def find_longest_common_word(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    common_words = words1.intersection(words2)
    if common_words:
        return max(common_words, key=len)
    else:
        return None
