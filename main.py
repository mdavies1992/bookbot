with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def wordcount(file_string):
    words = file_string.split()
    return len(words)

# def charactercount(file_string):
#     sanitized_string = file_string.lower()
#     result = {"a": 0, "b":0 , "c":0, "d":0, "e":0, "f":0,
#               "g":0, "h":0, "i":0, "j":0, "k":0, "l":0,
#                "m":0, "n":0 , "o":0, "p":0, "q":0, "r":0, "s":0,
#                 "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
#     for char in result:
#         num = sanitized_string.count(char)
#         result[char] = num
#     return result

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
    print(f"There were {wordcount(file_string)} words found in this document.")
    results = charactercount(file_string)
    for char in results:
        print(f"The '{char}' character was found {results[char]} times")
    print("--- End of Report ---")

report(file_contents)
