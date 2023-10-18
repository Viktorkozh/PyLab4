# У пользователя запрашиваются четыре числа.
# Отдельно складываются первые два и отдельно вторые два.
# Первая сумма делится на вторую.
# На экран выводится результат так, чтобы ответ содержал две цифры после запятой.
print("Write four values:")
a = float(input())
b = float(input())
c = float(input())
d = float(input())

sum1 = a + b
sum2 = c + d
ans = sum1 / sum2

print("Answer is {:.2f}".format(ans))
