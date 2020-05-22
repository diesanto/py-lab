secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input())
condition = False

while condition == False:
    if user_number == secret_number:
        condition = True
    else:
        print("Ha ha! You're stuck in my loop!\nSo, what is the secret number?")
        user_number = int(input())

print("Well done, muggle! You are free now.")
