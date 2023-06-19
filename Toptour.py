# Import necessary libraries
import csv
import requests
from bs4 import BeautifulSoup

# Define a function to clean the price
def clean_price(price):
    # Remove currency symbol and whitespace
    cleaned_price = price.replace('kr', '').strip()
    # Replace comma with dot for decimal point
    cleaned_price = cleaned_price.replace(',', '.')
    return cleaned_price

# Define the categories
categories = [
    {'name': 'HELMET', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/skihjelmer/Herrer'},
    {'name': 'GOGGLES', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/goggles'},
    {'name': 'SUNGLASSES', 'url': 'https://www.fjellsport.no/sok?q=sungalsses&cq=sunglasses'},
    {'name': 'HAT/BEANIE', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturluer'},
    {'name': 'SKI/SPLITBOARD BOOTS', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturstovler?custom.Gender=Dame&custom.Gender=Herre&custom.Gender=Unisex'},
    {'name': 'TECHNICAL', 'url': 'https://www.fjellsport.no/sok?q=technical'},
    {'name': 'SKIS/SPLITBOARD', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturski'},
    {'name': 'SKI BINDINGS', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturbindinger?sortBy=Rating'},
    {'name': 'SKINS', 'url': 'https://www.fjellsport.no/sok?q=skins'},
    {'name': 'SKI POLES', 'url': 'https://www.fjellsport.no/sok?q=poles&custom.CategoryName=Skistaver+fast+lengde'},
    {'name': 'CRAMPONS', 'url': 'https://www.fjellsport.no/sok?q=CRAMPONS'},
    {'name': 'HARNESS', 'url': 'https://www.fjellsport.no/turutstyr/klatreutstyr/klatreseler'},
    {'name': 'ROPE', 'url': 'https://www.fjellsport.no/turutstyr/klatreutstyr/tau'},
    {'name': 'BEACON', 'url': 'https://www.fjellsport.no/sok?q=beacon'},
    {'name': 'BACKPACK', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/topptursekker'},
    {'name': 'HEADLAMP', 'url': 'https://www.fjellsport.no/sok?q=headlamp'},
    {'name': 'HARDSHELL/RAIN JACKET (Male)', 'url': 'https://www.fjellsport.no/sok?q=skalljakker&custom.Gender=Herre&custom.RecommendedUse=Topptur+og+alpinisme&custom.RecommendedUse=Snowboard'},
    {'name': 'HARDSHELL/RAIN JACKET (Female)', 'url': 'https://www.fjellsport.no/sok?q=skalljakker&custom.Gender=Dame&custom.RecommendedUse=Topptur+og+alpinisme&custom.RecommendedUse=Snowboard'},
    {'name': 'INSULATED LAYER (Male)', 'url': 'https://www.fjellsport.no/sok?q=insulated+layer&custom.Gender=Herre'},
    {'name': 'INSULATED LAYER (Female)', 'url': 'https://www.fjellsport.no/sok?q=insulated+layer&custom.Gender=Dame'},
    {'name': 'FLEECE/SWEATER (Male)', 'url': 'https://www.fjellsport.no/sok?q=sweater&custom.Gender=Herre'},
    {'name': 'FLEECE/SWEATER (Female)', 'url': 'https://www.fjellsport.no/sok?q=sweater&custom.Gender=Dame'},
    {'name': 'GLOVES (Male)', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturhansker?custom.Gender=Herre'},
    {'name': 'GLOVES (Female)', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturhansker?custom.Gender=Dame'},
    {'name': 'HARDSHELL PANTS (Male)', 'url': 'https://www.fjellsport.no/sok?q=skallbukse&custom.Gender=Herre&custom.RecommendedUse=Topptur+og+alpinisme'},
    {'name': 'HARDSHELL PANTS (Female)', 'url': 'https://www.fjellsport.no/sok?q=skallbukse&custom.Gender=Dame&custom.RecommendedUse=Topptur+og+alpinisme'},
    {'name': 'SOFTSHELL PANTS (Male)', 'url': 'https://www.fjellsport.no/sok?q=softshell+pants&custom.Gender=Herre'},
    {'name': 'SOFTSHELL PANTS (Female)', 'url': 'https://www.fjellsport.no/sok?q=softshell+pants&custom.Gender=Dame'},
    {'name': 'SOCKS', 'url': 'https://www.fjellsport.no/sok?q=str%C3%B8mper&custom.Gender=Herre&custom.RecommendedUse=Frikj%C3%B8ring+og+alpint&custom.RecommendedUse=Snowboard&custom.RecommendedUse=Topptur+og+alpinisme'}
]

# Create a CSV file
csv_file = open('products.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Category', 'Gender', 'Brand', 'Description', 'Image URL', 'Price'])

# Scrape each category
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
        if is_male_category:
            csv_writer.writerow([category_name, 'Male', brand, description, image_url, price])
        elif is_female_category:
            csv_writer.writerow([category_name, 'Female', brand, description, image_url, price])
        else:
            csv_writer.writerow([category_name, 'Unisex', brand, description, image_url, price])

# Close the CSV file
csv_file.close()
