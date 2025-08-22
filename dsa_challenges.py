#filter_and_sort_evens(numbers)
def filter_and_sort_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)
print(filter_and_sort_evens([3, 1, 4, 1, 5, 9, 2, 6]))

#count_character_frequency(text)
def count_character_frequency(text):
    text = text.lower()
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
result = count_character_frequency("RAKESH")
print(result)
