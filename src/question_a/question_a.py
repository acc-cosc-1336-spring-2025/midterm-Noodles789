#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_day_of_week(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day - 1] if 1 <= day <= 7 else "Enter a number between 1 and 7."

while True:
    try:
        user_input = int(input("Enter a number (1-7) or 0 to exit: "))
        if user_input == 0:
            print("Goodbye!")
            break
        print(get_day_of_week(user_input))
    except ValueError:
        print("Please enter a valid number.")