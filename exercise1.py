#Age calculation
name = input("Name: ")
year_of_birth = input("Year of birth: ")
year = input("Current year: ")

try:
    year_of_birth = int(year_of_birth)
    year = int(year)
    age = year - year_of_birth

    if age < 0:
        print("That can't be right, you aren't born yet.")
    else:
        print(f"Hello {name}, you are {age} years old!")
except ValueError:
    print("You should write integer numbers!")
