import requests

BASE_URL = "http://api.exchangeratesapi.io/v1/latest"
API_KEY = "YOUR API KEY HERE"

def get_rates():
    payload = {"access_key": API_KEY}
    response = requests.get(url=BASE_URL, params=payload)

    if response.status_code == 200:
        data = response.json()
        return data.get("rates")
    else:
        raise Exception("Error retrieving exchange rates.")

def get_currency(currency, rates):
    currency = currency.upper()
    if currency in rates:
        return rates[currency]
    else:
        raise ValueError(f"{currency} is not a valid currency")

def convert_currency(amount, from_currency, to_currency):
    rates = get_rates()
    from_rate = get_currency(from_currency, rates)
    to_rate = get_currency(to_currency, rates)
    conversion = round((to_rate / from_rate) * amount, 2)
    return conversion

def main():
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency: ").upper()
    to_currency = input("Enter the target currency: ").upper()

    try:
        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount:.2f} ({from_currency}) is {result:.2f} ({to_currency})")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
