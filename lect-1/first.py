print("hello world")


print("hello machine")


a = 10
print(a)
print(a*2)


a = 5
b = 10
c = 15
d = 20
e = 25
print(a+b+c+d+e)


a = input()
b = input()
print(a+b)


a = int(input())
b = int(input())
c = int(input())
print(a+b+c)


a = int(input())
b = int(input())
c = int(input())
print(a+b+c)



a = 1
b = 2
sum = a+b+w
print(sum)


a = 1
b = 2
print(a,b)
c = a
a = b
b = c
print(a,b)



a = 2
b = 3
print(a,b)
a = a+b
b = a-b
a = a-b
print(a,b)



a = 1
while(a<50):
    if(a%2!=0):
        #  print("odd")
         print("odd",a)
    else:
      # print("even")
      print("even",a)
    a = a+1



a = 1
if a%2 == 0:
  print("Even")
else:
  print("Odd")


a = 0
if a>0:
  print("Positive")
elif a<0:
  print("Negative")
else:
  print("Zero")



# else if = elif
a = str(input())
if a == "sun":
  print("Sunday")
elif a == "mon":
  print("Monday")
elif a == "tue":
  print("Tuesday")
elif a == "wed":
  print("Wednesday")
elif a == "thu":
  print("Thursday")
elif a == "fri":
  print("Friday")
elif a =="sat":
  print("Saturday")
else:
  print("Not a Day")



# for loop
# range has 3 elements
for i in range(start,end,step):
  print(i)



# while loop
i = 1
while i<10:
  print(i)
  i += 1


# Operator (/ and //)

# gives answer in decimal
print(5/2)

# gives answer in integers
print(5//2)



# Check Palindrome
a = "stats"
n = len(a)
# print(n)
i = 0
j = n-1
while i<j:
  if a[i] != a[j]:
    print("Not a Palindrome")
    break;
  i += 1
  j -= 1
if(i==j):
  print("Palindrome")