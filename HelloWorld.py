# This is a comment
print("Hello, World!")  # This prints text to the console
#-------------------------------------------------------------------------------------

x = 5           # Integer
y = 3.14        # Float
name = "Tester string"  # String
is_valid = True # Boolean
#-------------------------------------------------------------------------------------


projectThing = int(input("please enter a number between 1 and 15 "))
for row in range (projectThing):
    for col in range(2*projectThing):
        print('*' if row in(0,projectThing-1) or col in(0,(2*projectThing)-1) else ' ', end=' ')
    print()


    #-------------------------------------------------------------------------------------

n=int(input('Please enter a positive integer between 1 and 15: '))
for col in range(n):
    for row in range(n):
        print('*' if col in(0,(2*n)+1) or row in(0,n+1) else ' ', end=' ')
    print()