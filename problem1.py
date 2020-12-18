# Name: Quang Le
# Student ID: 1768324

if __name__ == "__main__":
    current_input = input("Enter the current date by month, day and year (separated by whitespace):")
    current = current_input.split()
    bday_input = input("Enter the birthday date by month, day and year (separated by whitespace):")
    bday = bday_input.split()
    print("Birthday Calculator")
    print("Current day ")
    print("Month: {} ".format(current[0]))
    print("Day: {} ".format(current[1]))
    print("Year: {} ".format(current[2]))
    print("Birthday ")
    print("Month: {} ".format(bday[0]))
    print("Day: {} ".format(bday[1]))
    print("Year: {} ".format(bday[2]))
    age = 0
    if current[0] >= bday[0] and current[1] >= bday[1]:
        if current[0] == bday[0] and current[1] == bday[1]:
            print("Happy Birthday!")
        age = int(current[2]) - int(bday[2])
    else:
        age = int(current[2]) - int(bday[2]) - 1

    print("You are {} years old.".format(age))
