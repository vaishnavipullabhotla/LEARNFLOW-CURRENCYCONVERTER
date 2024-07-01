import requests

# Function to get real-time exchange rates
def get_erate(oc, cc):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{oc}"
    response = requests.get(api_url)
    data = response.json()
    return data['rates'][cc]

# Function to perform the conversion
def convert(a, oc, cc):
    erate = get_erate(oc, cc)
    return a * erate

# Main function to handle user input and output
def main():
    print("Currency Converter")
    a = float(input("Enter the currency: "))
    oc = input("ORIGINAL CURRENCY (INR, USD, EUR, GBP): ").upper()
    cc = input("CONVERTED CURRENCY (INR, USD, EUR, GBP): ").upper()

    try:
        converted_currency = convert(a, oc, cc)
        print(f"{a} {oc} = {converted_currency:.2f} {cc}")
    except KeyError:
        print("Invalid currency code. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
