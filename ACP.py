num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 1
    temp //= 10

    if num == sum:
        print(num,"is an Armstorng number")
    else:
        print(num,"is not an Armstrong number")