# This program asks the user for a number and then prints the square of that number

def main():
    number = float(input("Enter a number: "))
    print(f"The square of {number} is {squared(number)}")
    
def squared(n):
    return n * n

main()