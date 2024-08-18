fnum = input("Enter the First value :")
operator = input("Enter the Operator + , - , / , % : ")
snum = input("Enter the Second value :")
fnum = int(fnum)
snum = int(snum)
if operator =='+':
    sum = fnum + snum
    print(sum)
elif operator =='-':
    sum = fnum - snum
    print(sum)
elif operator =='/':
    sum = fnum / snum
    print(sum)
elif operator =='%':
    sum = fnum % snum
    print(sum)
else:
    print("Invalid Operation!!!")