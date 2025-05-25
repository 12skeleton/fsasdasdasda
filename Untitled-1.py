class less14(Exception):
    pass
name = int(input("name:"))
try:
    age = int(input("age:"))
    if age < 14:
        raise less14("you less than 14")
except ValueError:
    print("this is not value")
print("age is correct")

production = int(input("production name:"))
kolichestvo = int(input("kolichestvo:"))
adress = int(input("adress:"))