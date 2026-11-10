def show_menu():
    print("===== TEMPERATURE CONVERTER =====")

    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def celsius_to_fahrenheit(celsius):
    result = (celsius * 9/5) + 32
    return result

def fahrenheit_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return result

def celsius_to_kelvin(celsius):
    result = (celsius + 273.15)
    return result

def kelvin_to_celsius(kelvin):
    result = (kelvin - 273.15)
    return result

def fahrenheit_to_kelvin(fahrenheit):
    result = ((fahrenheit - 32) * 5/9) + 273.15
    return result

def kelvin_to_fahrenheit(kelvin):
    result = ((kelvin - 273.15) * 9/5) + 32
    return result

def get_conversion_choice():
    choice = int(input("Choose your conversion (1-7): "))
    return choice

def get_temperature():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            return temperature
        except ValueError:
            print("Invalid temperature! Please enter a number.")

def is_valid_temperature(temperature, choice):
    if choice == 1 or choice == 3:
        return temperature >= -273.15

    elif choice == 2 or choice == 5:
        return temperature >= -459.67

    elif choice == 4 or choice == 6:
        return temperature >= 0

while True:
    show_menu()
    try:
        choice = get_conversion_choice()
    except ValueError:
        print("Invalid input!. Please enter a number between 1 and 7.")
        continue
    if choice == 7:
        print("Thank you!")
        print("Goodbye!")
        break

    elif 1 <= choice <= 6:

        temperature = get_temperature()

        if not is_valid_temperature(temperature, choice):
            print("Temperature is below absolute zero. Please try again.")
            continue

        if choice == 1:
            print(f"Result: {celsius_to_fahrenheit(temperature):.2f} °F")

        elif choice == 2:
            print(f"Result: {fahrenheit_to_celsius(temperature):.2f} °C")

        elif choice == 3:
            print(f"Result: {celsius_to_kelvin(temperature):.2f} K")

        elif choice == 4:
            print(f"Result: {kelvin_to_celsius(temperature):.2f} °C")

        elif choice == 5:
            print(f"Result: {fahrenheit_to_kelvin(temperature):.2f} K")
        
        elif choice == 6:
            print(f"Result: {kelvin_to_fahrenheit(temperature):.2f} °F")

    else:
        print("Invalid choice! Please select between 1 and 7.")
    
    again = input("Do you want to convert another temperature? (yes/no): ").strip().lower()

    if again == "yes":
        continue

    elif again == "no":
        print("Thank you!")
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter yes or no.")
        continue
       





    

    