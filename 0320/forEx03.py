num = int(input("Enter a number: "))

fact = 1

print(f"{num}! = ", end="")
for i in range(1, num + 1):
    fact *= i
    print(i, end=" * ")

print(f"= {fact}")