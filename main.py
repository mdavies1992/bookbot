with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def wordcount(file_string):
    words = file_string.split()
    return len(words)

def charactersort(dict):
    list_of_dicts = [{"char": k, "count": v} for k, v in dict.items()]
    sorted_list = sorted(list_of_dicts, key=lambda x: x['count'], reverse=True)
    return sorted_list

def charactercount(file_string):
    result = {}
    sanitized_string = file_string.lower()
    for char in sanitized_string:
        if char.isalpha():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

def report(file_string):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There were {wordcount(file_string)} words found in this document.\n")
    results = charactercount(file_string)
    sorted_results = charactersort(results)
    for item in sorted_results:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End of Report ---")

report(file_contents)
