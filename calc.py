def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mul, "/": div}
prevSum = 0


def calculate(n1):
    choice_operation = input("+\n-\n*\n/\nEnter Your Operation : ")
    if choice_operation not in operations:
        print("Invalid Operations")
        return n1

    n2 = float(input("Enter Second Number : "))
    result = operations[choice_operation](n1, n2)
    print(f"The result is {result}")
    return result


n1 = float(input("Enter first number : "))
prevSum = calculate(n1)

while True:
    choice = input(
        "Do you want to continue with previous sum (s), enter new number (n) or exit (e) : "
    ).lower()
    if choice == "s":
        prevSum = calculate(prevSum)
    elif choice == "n":
        n1 = float(input("Enter First Number : "))
        prevSum = calculate(n1)
    elif choice == "e":
        print("Thank You For using Calculator :)")
        break
    else:
        print("Invalid Choice")
