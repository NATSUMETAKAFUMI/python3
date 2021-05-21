#!/usr/bin/env python3

x = int(input("整数を入力してください : "))
y = int(input("整数を入力してください : "))

print("足し算は{}です".format(x + y))
print("引き算は{}です".format(x - y))
print("掛け算は{}です".format(x * y))
print("割り算は{}です".format(x / y))
print("{}を四捨五入すると{}です".format(x / y, x // y))
print("{}/{}の余りは{}です".format(x, y, x % y))
print("{}を{}乗すると{}です".format(x, y, x ** y))
