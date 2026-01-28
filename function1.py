# this program prompts the user 
# for their name and greets them

def hello(to):
    print("Hello," , to)

#output greeting
name = input ("what's your name? ")
hello(name)

# Output without passing 
# the expected argument
hello()

def hello(to='John Doe'):
    print("Hello," , to)

main()