s =input("enter the word:")
for ch in s:
    if ch.isalpha() and ch.lower() not in "aeiou":
        print(ch, end="")
