## pip install requests
import requests
url="https://restcountries.com/v3.1/all"
r1=requests.get(url)
r1
print(r1.json())



# question 1,2,3,4
#fetch all json data,diaplay the name of cuntries,currencies,and currency symbols

import requests

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_country_info(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})
        
        if currencies:
            print(f"Country: {name}")
            print("Currencies:")
            
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                
                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")
            
            print("\n")

# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_country_info(countries_data)
else:
    print("Failed to fetch data.")


# question 5-create a method to display the name of countries which have the DOLLAR as its curency.

import requests

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_countries_with_dollar_currency(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})
        
        # Check if the currency is "Dollar"
        if any(currency_code.lower() == 'usd' for currency_code in currencies):
            print(f"Country: {name}")
            print("Currencies:")
            
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                
                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")
            
            print("\n")

# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_countries_with_dollar_currency(countries_data)
else:
    print("Failed to fetch data.")




# question-6-Display the countries which have EURO as its curency

import requests

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_countries_with_euro_currency(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})
        
        # Check if the currency is "Euro"
        if any(currency_code.lower() == 'eur' for currency_code in currencies):
            print(f"Country: {name}")
            print("Currencies:")
            
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                
                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")
            
            print("\n")

# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_countries_with_euro_currency(countries_data)
else:
    print("Failed to fetch data.")
#####################################################

import requests
r1=requests.get("https://api.openbrewerydb.org/breweries")
d=r1.json()
d

#question 1-list the names of all breweries present in the states of Alaska,Marine,new yark

import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()
        json_data = response.json()
        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def list_brewery_names_by_states(url, states):
    for state in states:
        print(f"Breweries in {state}:")
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            for brewery in breweries_data:
                brewery_name = brewery.get('name', 'N/A')
                print(f"  - {brewery_name}")
        else:
            print("Failed to fetch data.")

        print("\n")

# Example usage
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
list_brewery_names_by_states(url, states_of_interest)

##question---2-what is the count of breweries in each of the state mentioned above

import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()
        json_data = response.json()
        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def count_breweries_by_states(url, states):
    for state in states:
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            brewery_count = len(breweries_data)
            print(f"Number of breweries in {state}: {brewery_count}")
        else:
            print(f"Failed to fetch data for {state}.")
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
count_breweries_by_states(url, states_of_interest)


#Question-3-count the number of types  of breweries present in individual citiesof the state 

import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def count_brewery_types_by_cities(url, state):
    breweries_data = fetch_breweries_by_state(url, state)

    if breweries_data:
        cities_data = {}
        
        for brewery in breweries_data:
            city = brewery.get('city', 'N/A')
            brewery_type = brewery.get('brewery_type', 'N/A')

            if city not in cities_data:
                cities_data[city] = set()

            cities_data[city].add(brewery_type)

        for city, brewery_types in cities_data.items():
            print(f"City: {city}")
            print(f"Number of Brewery Types: {len(brewery_types)}")
            print(f"Brewery Types: {', '.join(brewery_types)}")
            print("\n")
    else:
        print(f"Failed to fetch data for {state}.")

# Example usage
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']

for state in states_of_interest:
    count_brewery_types_by_cities(url, state)



#Question-4-Count and list the number breweries in each of the states mentioned above


import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def count_and_list_breweries_with_websites(url, states):
    for state in states:
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            breweries_with_websites = [brewery for brewery in breweries_data if 'website_url' in brewery]

            print(f"Number of breweries with websites in {state}: {len(breweries_with_websites)}")
            print(f"Breweries with websites in {state}:")

            for brewery in breweries_with_websites:
                name = brewery.get('name', 'N/A')
                website_url = brewery.get('website_url', 'N/A')

                print(f"  - {name}: {website_url}")

            print("\n")
        else:
            print(f"Failed to fetch data for {state}.")

# Example usage
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
count_and_list_breweries_with_websites(url, states_of_interest)



