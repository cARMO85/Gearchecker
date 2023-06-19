import requests
from bs4 import BeautifulSoup
import csv

# Function to clean up price values
def clean_price(price):
    # Remove unwanted characters
    price = price.replace('\xa0', '').replace(',-', '')
    return price

# Define the list of categories and their corresponding URLs
categories = [
    {'name': 'HELMET', 'url': 'https://www.fjellsport.no/sok?q=climbing+helmet&custom.Gender=Unisex'},
    {'name': 'SUNGLASSES', 'url': 'https://www.fjellsport.no/sok?q=sunglasses&custom.Gender=Unisex'},
    {'name': 'HAT/BEANIE', 'url': 'https://www.fjellsport.no/sok?q=beanie'},
    {'name': 'HARDSHELL JACKET', 'url': 'https://www.fjellsport.no/aktiviteter/klatring/klatrebekledning/klatrejakker?custom.Gender=Dame'},
    {'name': 'SOFTSHELL JACKET', 'url': 'https://www.fjellsport.no/aktiviteter/klatring/klatrebekledning/klatrejakker?custom.Gender=Herre'},
    {'name': 'INSULATED LAYER', 'url': 'https://www.fjellsport.no/sok?q=insulated+layer&custom.Gender=Dame'},
    {'name': 'FLEECE/SWEATER', 'url': 'https://www.fjellsport.no/sok?q=climbing++fleece&custom.Gender=Dame'},
    {'name': 'BASELAYER', 'url': 'https://www.fjellsport.no/sok?q=baselayer+tops&custom.Gender=Dame'},
    {'name': 'GLOVES', 'url': 'https://www.fjellsport.no/sok?q=climbing++gloves&custom.Gender=Unisex'},
    {'name': 'SOFTSHELL PANTS', 'url': 'https://www.fjellsport.no/aktiviteter/klatring/klatrebekledning/klatrebukser?custom.Gender=Dame'},
    {'name': 'BASELAYER', 'url': 'https://www.fjellsport.no/sok?q=baselayer+pants&custom.Gender=Dame'},
    {'name': 'CLIMBING SHOES (Female)', 'url': 'https://www.fjellsport.no/aktiviteter/klatring/klatresko?custom.Gender=Dame'},
    {'name': 'CLIMBING SHOES (Male)', 'url': 'https://www.fjellsport.no/aktiviteter/klatring/klatresko?custom.Gender=Herre'},
    {'name': 'ROPE', 'url': 'https://www.fjellsport.no/turutstyr/klatreutstyr/tau'},
    {'name': 'HARNESS', 'url': 'https://www.fjellsport.no/turutstyr/klatreutstyr/klatreseler?custom.Gender=Unisex'},
    {'name': 'BELAY DEVICE', 'url': 'https://www.fjellsport.no/sok?q=belays'},
    {'name': 'QUICKDRAWS', 'url': 'https://www.fjellsport.no/sok?q=quickdraws'},
    {'name': 'LOCKING CARABINERS', 'url': 'https://www.fjellsport.no/sok?q=locking+carabiners'},
    {'name': 'CRASH PAD', 'url': 'https://www.fjellsport.no/sok?q=crash+pads'},
    {'name': 'CHALK BAG', 'url': 'https://www.fjellsport.no/aktiviteter/klatring/tilbehor+klatring/kalkposer?custom.Gender=Unisex'},
    {'name': 'CLIMBING HOLD', 'url': 'https://www.fjellsport.no/sok?q=climbing+holds'},
    {'name': 'CAMALOTS', 'url': 'https://www.fjellsport.no/sok?q=camalots'},
    {'name': 'NUTS', 'url': 'https://www.fjellsport.no/sok?q=nuts'},
    {'name': 'CAMS/FRIENDS', 'url': 'https://www.fjellsport.no/sok?q=cams'},
    {'name': 'SLINGS', 'url': 'https://www.fjellsport.no/sok?q=slings'},
    {'name': 'BACKPACK', 'url': 'https://www.fjellsport.no/aktiviteter/klatring/klatresekker'},
    {'name': 'CARABINERS', 'url': 'https://www.fjellsport.no/sok?q=carabiner'}
]

# Create a CSV file for the data
csv_file = open('rock_climbing_products_ver1.0.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['Category', 'Gender', 'Brand', 'Model', 'Image', 'Price'])

# Iterate over the categories
for category in categories:
    category_name = category['name']
    url = category['url']

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all product items
    products = soup.find_all('div', class_='fp h5 a5 a6 dl')

    # Check if the category is specific to a gender
    is_male_category = 'Herre' in url
    is_female_category = 'Dame' in url

    # Iterate over the products
    for product in products:
        # Extract the brand, model, and description
        brand = product.find('div', class_='an bi d3 di dj hp').text.strip()
        description = product.find('div', class_='an d3 di dj fm').text.strip()

        # Extract the image URL
        image_url = product.find('img')['src']

        # Extract the price
        price_element = product.find('span', class_='q as av')
        if price_element:
            price = clean_price(price_element.text.strip())
        else:
            # Check for discounted price
            price_element = product.find('span', class_='fz as av')
            price = clean_price(price_element.text.strip()) if price_element else 'N/A'

        # Write the data to CSV
        if category_name.startswith('CLIMBING SHOES'):
            if is_male_category:
                writer.writerow([category_name + ' (Male)', 'Male', brand, description, image_url, price])
            elif is_female_category:
                writer.writerow([category_name + ' (Female)', 'Female', brand, description, image_url, price])
        else:
            if is_male_category:
                writer.writerow([category_name, 'Male', brand, description, image_url, price])
            elif is_female_category:
                writer.writerow([category_name, 'Female', brand, description, image_url, price])
            else:
                writer.writerow([category_name, 'Unisex', brand, description, image_url, price])

# Close the CSV file
csv_file.close()
