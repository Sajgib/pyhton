first_name = "Kevin"
last_name = "Janin"
full_name = first_name + " " + last_name

print("Hello " + full_name)

age = 21
age += 1
print("Your age is: "+str(age))

height = 169.5
print("Your height is: "+str(height) + " cm")
print(type(height))

monday_tempature = {"Morning": 10.2, "Noon": 23.2, "Night": 30.2}
print(monday_tempature["Morning"])

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[2]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print('My name is')
for i in range(5):
    print('Jimmy Five Times')

#adding a str
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' +str(i) + ')')