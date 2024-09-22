number=input("Enter a  number: ")
digits = len(number)
num2 = int(number)
resultNum = 0
for i in range(digits):
    resultNum += (num2%10)**digits #153%10 =3
    num2 = num2//10 #153//10 = 15
if resultNum == int(number):
    print("Armstrong number ", number)
else:
    print("Not an Armstrong number ", number)