from art import logo
print(logo)

def addition(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

add = addition
sub = subtract
multi = multiply
div = divide

operators = {
    "+":add,
    "-":sub,
    "*":multi,
    "/":div,
}
def calculator():
    cont = True
    first_num = float(input("What's the first number?: "))
    while cont:

        for key in operators:
            print(key)
        operation = input("Pick an operator: ")
        second_num = float(input("What's the second number?: "))
        result = float(operators[operation](first_num,second_num))
        print(f"Your calculation of {first_num} {operation} {second_num} = {result}\n")
        same_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if same_calc == 'y':
           first_num = result
        else:
           cont = False
           print("\n" * 20 + logo)
           calculator()
calculator()

