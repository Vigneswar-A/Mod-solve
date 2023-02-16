from collections import Counter


def get_mod(a, b):
    a, b = sorted((a, b), reverse=1)
    print(f"({b})X ≡ 1(mod {a})")
    temp = b
    rem = -1
    mapping = {}
    while rem != 0:
        q, rem = divmod(a, b)
        mapping[rem] = [a, b, q]
        if rem == 0:
            if b != 1:
                print("Multiplication Inverse Does not Exist!")
                return
            break
        print(f"{a} = {b}x{q} + {rem}")
        a, b = b, rem
    eq = Counter([1])
    print("-"*30)
    print("1", end="")
    while True:
        flag = True
        for num in set(eq):
            if eq[num] and num in mapping:
                a, b, q = mapping[num]
                eq[a] += eq[num]
                eq[b] -= q*eq[num]
                del eq[num]
                flag = False

        if flag:
            break
        print(convert(eq))
    print("-"*30)
    print(f"({eq[temp]})({b})(X) ≡ {eq[temp]}(mod {a})")
    print(f" => X ≡ {eq[temp]}(mod {a})")
    print(f" => X = {eq[temp]%a}")


def convert(counter):
    res = " = "
    for key, val in counter.items():
        if not val:
            continue
        res += (f"({key})({val}) + ")
    return res[:-2]


a = int(input("Enter value of a:"))
n = int(input("Enter value of n:"))

get_mod(a, n)

print("Done by Vigneswar A :)")
input()
