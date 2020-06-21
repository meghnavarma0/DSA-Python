# Given a sorted string and a key. Find the character next to the given key in the string.

def nextCharacter(s, key):
    result = "#"
    low, high, mid = 0, len(s) - 1, None
    while low <= high:
        mid = low + (high - low) // 2
        if s[mid] <= key:
            low = mid + 1
        else:
            result = s[mid]
            high = mid - 1

    return result

s = "abcdefghijklmnopqrstuvwxyz"
print(nextCharacter(s, "a"))
print(nextCharacter(s, "b"))
print(nextCharacter(s, "c"))
print(nextCharacter(s, "d"))
print(nextCharacter(s, "e"))
print(nextCharacter(s, "f"))
print(nextCharacter(s, "k"))
print(nextCharacter(s, "l"))
print(nextCharacter(s, "m"))
print(nextCharacter(s, "n"))
print(nextCharacter(s, "o"))
print(nextCharacter(s, "p"))
print(nextCharacter(s, "q"))
print(nextCharacter(s, "z"))

