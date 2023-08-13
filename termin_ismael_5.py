str = "The quick brown fox jumps over the lazy dog"

print(str)
print(len(str)) 
print(str.upper())
print(str.lower())
print(str.title())
print(str[::-1])
print(str.title()[::-1])
print(str.count('a'))
print(str.lower().count('the'))
print(str.replace('the', 'a'))


dictionary = {}

for i in str:
    if i in dictionary:
        continue
    elif i ==" ":
        continue
    else:
        dictionary[i]=str.count(i)

print(dictionary)


people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for people, sex, age in zip(people, sex, age):
    print(f"{people} the {sex} is {age} years old") 