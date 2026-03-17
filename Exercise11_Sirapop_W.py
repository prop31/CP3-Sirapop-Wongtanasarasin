height = int(input("Enter a height: "))

for row in range(height):
    for col in range(height - row -1):
        print(" ",end="")
    for col in range(row + 1):
        print("*", end=" ")
    print()
