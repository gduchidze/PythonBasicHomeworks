#1
def rec(times, x="Hello"):
    if times > 0:
        print(x)
        rec(times - 1, x)

rec(5)

#3
def calc(*numbers):
    if len(numbers) < 3:
        print("Please provide at least three numbers ")
        return None

    x = 1
    for number in numbers:
        x *= number

    print("Result:", x)
    return x


result = calc(2, 3, 4, 5)

#2
def order(name, quantity=1):
    print(f"Order: {quantity} {name}(s)")

order("Pizza")
order("Burger", 2)
