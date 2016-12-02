DAY = 5

import re

def part1(data):
    return sum(is_valid(word) for word in data.split())

def is_valid(word):
    return has_vowels(word) and has_duplicate(word) and does_not_contain(word)

def has_vowels(word):
    vowels = "aeiou"
    return sum(word.count(j) for j in vowels) >= 3

def has_duplicate(word):
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            return True
    return False

def does_not_contain(word):
    error = ["ab", "cd", "pq", "xy"]
    for temp in error:
        if temp in word:
            return False
    return True

def part2(data):
    return sum(bool(is_valid2(word)) for word in data.split())

def is_valid2(word):
    return re.search("(.{1})(.{1}).*\\1\\2", word) and re.search("(.{1}).{1}\\1", word)
