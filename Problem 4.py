def show_menu():
    print("Measurement Converter")
    print("1. Millimeters to Centimeters")
    print("2. Feet to Meters")
    print("3. Inches to Centimeters")
    print("4. Kilometers to Miles")
    print("5. Pounds to Kilograms")
    print("6. Exit")

def convert_mm_to_cm(mm):
    return mm / 10

def convert_ft_to_m(ft):
    return ft * 0.3048

def convert_in_to_cm(inches):
    return inches * 2.54

def convert_km_to_miles(km):
    return km * 0.621371

def convert_lb_to_kg(lb):
    return lb * 0.453592

def main():
    while True:
        show_menu()
        choice = input("Choose a conversion (1-6): ")
        
        if choice == '1':
            mm = float(input("Enter millimeters: "))
            print(f"{mm} mm is {convert_mm_to_cm(mm)} cm")
        elif choice == '2':
            ft = float(input("Enter feet: "))
            print(f"{ft} ft is {convert_ft_to_m(ft)} m")
        elif choice == '3':
            inches = float(input("Enter inches: "))
            print(f"{inches} inches is {convert_in_to_cm(inches)} cm")
        elif choice == '4':
            km = float(input("Enter kilometers: "))
            print(f"{km} km is {convert_km_to_miles(km)} miles")
        elif choice == '5':
            lb = float(input("Enter pounds: "))
            print(f"{lb} lb is {convert_lb_to_kg(lb)} kg")
        elif choice == '6':
            print("Exiting the converter.")
            break
        else:
            print("Invalid choice, please choose a valid option.")

if __name__ == "__main__":
    main()
