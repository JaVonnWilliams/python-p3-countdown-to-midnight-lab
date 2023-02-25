from time import sleep

def countdown(num):
    while num:
        print(f"{num} SECOND(S)!")
        num -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(num):

    while num:
        print(f'{num} SECOND(S)!')
        num -= 1
        sleep(1)
    print('HAPPY NEW YEAR!')