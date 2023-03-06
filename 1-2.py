def is_even():
    num = input("Enter an integer: ")
    if int(num) % 2 == 0:
        return True
    else:
        return False

print(is_even())