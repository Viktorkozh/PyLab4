# Напиcaл программу, которая предлагает пользователю решить пример 4 * 100 - 54.
# Потом выводит на экран правильный ответ и ответ пользователя.
print("What's 4 * 100 - 54?")
a = input()
print("Your answer is", a, "\nCorrect answer is", 4*100-54)
if int(a) == 4*100-54:
    print("You're correct.")
else:
    print("You're wrong.")