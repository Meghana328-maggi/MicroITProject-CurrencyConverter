def currency_converter():
    print("Currency Converter")
    print("1. USD to INR")
    print("2. INR to USD")
    print("3. USD to EUR")
    print("4. EUR to USD")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        usd = float(input("Enter amount in USD: "))
        inr = usd * 83.5  # assuming 1 USD = 83.5 INR
        print(f"{usd} USD = {inr} INR")
    elif choice == '2':
        inr = float(input("Enter amount in INR: "))
        usd = inr / 83.5
        print(f"{inr} INR = {usd} USD")
    elif choice == '3':
        usd = float(input("Enter amount in USD: "))
        eur = usd * 0.92  # assuming 1 USD = 0.92 EUR
        print(f"{usd} USD = {eur} EUR")
    elif choice == '4':
        eur = float(input("Enter amount in EUR: "))
        usd = eur / 0.92
        print(f"{eur} EUR = {usd} USD")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    currency_converter()