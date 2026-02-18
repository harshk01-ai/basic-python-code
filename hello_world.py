print("hello world")

secret = 7
while True:
    num = int(input('guess a number: '))
    if num == secret:
        print('the secret number is',secret)
        break
    else:
        print("enter guess  number is worng ,try again")
