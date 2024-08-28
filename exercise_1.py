word = input("Введите слово: ")

inverted_word = word[::-1]

if word == inverted_word:
    print("yes")
else:
    print("no")
