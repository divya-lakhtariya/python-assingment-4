# Write python program that user to enter only odd numbers, else will raise an exception.


def num(n):
    if n % 2 == 0:
        return f' ({n}) is even'
    else:
        return f'({n}) is odd'
while True:
    try:
        print(num(int(input('Enter an integer number: '))))
        break
    except ValueError:
        print("Bitch that ain't an integer!")
