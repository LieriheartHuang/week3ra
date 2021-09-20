def count(s: str):
    now = 0
    for i in s:
        if i == "(":
            now += 1
        elif i == ")":
            now -= 1
        if now < 0:
            return False
    return not now


if count(input("Enter string:\n")):
    print("Parentheses balanced")
else:
    print("Parentheses unbalanced")
