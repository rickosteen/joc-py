def count_vowels(words):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for word in words:
        for char in word:
            if char in vowels:
                count += 1
    return count

print(count_vowels(['hi', 'hello', 'OOF!']))

#print(count)
                           