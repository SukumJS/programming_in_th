word = input()
replaced = ["apa", "epe", "ipi", "opo", "upu",]
vowel = "aeiou"
for i in range(len(replaced)):
    if replaced[i] in word:
        word = word.replace(replaced[i], vowel[i])
print(word)
