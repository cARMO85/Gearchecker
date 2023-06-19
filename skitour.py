import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.fjellsport.no/aktiviteter/topptur/goggles'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Create a CSV file to store the scraped data
csv_file = open('goggles.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['Company Name', 'Description', 'Price', 'Image URL'])

# Find each goggle item on the page
goggles = soup.find_all('div', class_='fp h5 a5 a6 dl')

# Extract information for each goggle
for goggle in goggles:
    company_name = goggle.find('div', class_='an bi d3 di dj hp').text.strip()
    description = goggle.find('div', class_='an d3 di dj fm').text.strip()
    price_element = goggle.find('span', class_='q as av')
    price = price_element.text.strip() if price_element else 'N/A'
    image_url = goggle.find('img')['src']

    # Write the data to the CSV file
    writer.writerow([company_name, description, price, image_url])

# Close the CSV file
csv_file.close()
  





#Softshell Jackets

# URL for softshell jackets
jackets_url = 'https://www.fjellsport.no/sok?q=softshell+jakke'

# Send a GET request to the jackets URL
jackets_response = requests.get(jackets_url)

# Create a BeautifulSoup object for the HTML content
jackets_soup = BeautifulSoup(jackets_response.content, 'html.parser')

# Create a CSV file for the data
csv_file = open('softshell_jackets.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['Company Name', 'Description', 'Price', 'Image URL'])

# Find each jacket item on the page
jackets = jackets_soup.find_all('div', class_='fp h5 a5 a6 dl')

# Extract information for each jacket
for jacket in jackets:
    company_name = jacket.find('div', class_='an bi d3 di dj hp').text.strip()
    description = jacket.find('div', class_='an d3 di dj fm').text.strip()
    price_element = jacket.find('span', class_='q as av')
    price = price_element.text.strip() if price_element else 'N/A'
    image_url = jacket.find('img')['src']

    # Write the data to the CSV file
    writer.writerow([company_name, description, price, image_url])

# Close the CSV file
csv_file.close()



# Hardshell Jackets

# Function to clean up price values
def clean_price(price):
    # Remove unwanted characters
    price = price.replace('\xa0', '').replace(',-', '')
    return price

# URLs for jackets
hardshell_jackets_url = 'https://www.fjellsport.no/sok?q=hardshell+rainjacket'
rain_jackets_url = 'https://www.fjellsport.no/sok?q=rainjacket'

# Send a GET request to the hardshell jackets URL
hardshell_jackets_response = requests.get(hardshell_jackets_url)

# Create a BeautifulSoup object for the hardshell jackets HTML content
hardshell_jackets_soup = BeautifulSoup(hardshell_jackets_response.content, 'html.parser')

# Send a GET request to the rain jackets URL
rain_jackets_response = requests.get(rain_jackets_url)

# Create a BeautifulSoup object for the rain jackets HTML content
rain_jackets_soup = BeautifulSoup(rain_jackets_response.content, 'html.parser')

# Create a CSV file for the data
csv_file = open('jackets.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['Category', 'Company Name', 'Description', 'Price', 'Image URL'])

# Find each jacket item on the hardshell jackets page
hardshell_jackets = hardshell_jackets_soup.find_all('div', class_='fp h5 a5 a6 dl')

# Extract information for each hardshell jacket
for jacket in hardshell_jackets:
    company_name = jacket.find('div', class_='an bi d3 di dj hp').text.strip()
    description = jacket.find('div', class_='an d3 di dj fm').text.strip()
    price_element = jacket.find('span', class_='q as av')
    price = price_element.text.strip() if price_element else 'N/A'
    image_url = jacket.find('img')['src']
    writer.writerow(['Hardshell/Rain Jacket', company_name, description, price, image_url])

# Find each jacket item on the rain jackets page
rain_jackets = rain_jackets_soup.find_all('div', class_='fp h5 a5 a6 dl')

# Extract information for each rain jacket
for jacket in rain_jackets:
    company_name = jacket.find('div', class_='an bi d3 di dj hp').text.strip()
    description = jacket.find('div', class_='an d3 di dj fm').text.strip()
    price_element = jacket.find('span', class_='q as av')
    price = price_element.text.strip() if price_element else 'N/A'
    image_url = jacket.find('img')['src']
    writer.writerow(['Rain Jacket', company_name, description, price, image_url])

# Close the CSV file
csv_file.close()

#Products_csv

# Function to clean up price values
def clean_price(price):
    # Remove unwanted characters
    price = price.replace('\xa0', '').replace(',-', '')
    return price

# URL for each category
categories = [
    {'name': 'HARDSHELL/RAIN JACKET', 'url': 'https://www.fjellsport.no/sok?q=hardshell+rainjacket'},
    {'name': 'INSULATED LAYER', 'url': 'https://www.fjellsport.no/sok?q=insulated+layer'},
    {'name': 'FLEECE/SWEATER', 'url': 'https://www.fjellsport.no/sok?q=fleece+AND+sweater'},
    {'name': 'BASELAYER', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturundertoy'},
    {'name': 'GLOVES', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturhansker'}
]

# Create a CSV file for the data
csv_file = open('products.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['Category', 'Company Name', 'Description', 'Price', 'Image URL'])

# Scrape each category
for category in categories:
    category_name = category['name']
    category_url = category['url']

    # Send a GET request to the category URL
    category_response = requests.get(category_url)

    # Create a BeautifulSoup object for the HTML content
    category_soup = BeautifulSoup(category_response.content, 'html.parser')

    # Find each product item on the page
    products = category_soup.find_all('div', class_='fp h5 a5 a6 dl')

    # Extract information for each product
    for product in products:
        company_name = product.find('div', class_='an bi d3 di dj hp').text.strip()
        description = product.find('div', class_='an d3 di dj fm').text.strip()
        price_element = product.find('span', class_='q as av')
        price = clean_price(price_element.text.strip()) if price_element else 'N/A'
        image_url = product.find('img')['src']

        # Write the data to the CSV file
        writer.writerow([category_name, company_name, description, price, image_url])

# Close the CSV file
csv_file.close()


# Head_section

# Function to clean up price values
def clean_price(price):
    # Remove unwanted characters
    price = price.replace('\xa0', '').replace(',-', '')
    return price

# URL for each category
categories = [
    {'name': 'HELMET', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/skihjelmer'},
    {'name': 'GOGGLES', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/goggles'},
    {'name': 'SUNGLASSES', 'url': 'https://www.fjellsport.no/sok?q=sunglasses'},
    {'name': 'HAT/BEANIE', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturluer'}
]

# Create a CSV file for the data
csv_file = open('head_section.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['Category', 'Company Name', 'Description', 'Price', 'Image URL'])

# Scrape each category
for category in categories:
    category_name = category['name']
    category_url = category['url']

    # Send a GET request to the category URL
    category_response = requests.get(category_url)

    # Create a BeautifulSoup object for the HTML content
    category_soup = BeautifulSoup(category_response.content, 'html.parser')

    # Find each product item on the page
    products = category_soup.find_all('div', class_='fp h5 a5 a6 dl')

    # Extract information for each product
    for product in products:
        company_name = product.find('div', class_='an bi d3 di dj hp').text.strip()
        description = product.find('div', class_='an d3 di dj fm').text.strip()
        price_element = product.find('span', class_='q as av')
        price = clean_price(price_element.text.strip()) if price_element else 'N/A'
        image_url = product.find('img')['src']

        # Write the data to the CSV file
        writer.writerow([category_name, company_name, description, price, image_url])

# Close the CSV file
csv_file.close()


# Products_1 csv
# Function to clean up price values
def clean_price(price):
    # Remove unwanted characters
    price = price.replace('\xa0', '').replace(',-', '')
    return price

# Define the list of categories and their corresponding URLs
categories = [
    {'name': 'HARDSHELL PANTS', 'url': 'https://www.fjellsport.no/sok?q=hardshell+pants'},
    {'name': 'SOFTSHELL PANTS', 'url': 'https://www.fjellsport.no/sok?q=softshell+pants&custom.CategoryName=Skibukser+herre&custom.CategoryName=Skibukser+dame'},
    {'name': 'BASELAYER', 'url': 'https://www.fjellsport.no/sok?q=baselayer+pants'},
    {'name': 'SOCKS', 'url': 'https://www.fjellsport.no/sok?q=str%C3%B8mper&custom.RecommendedUse=Frikj%C3%B8ring+og+alpint&custom.RecommendedUse=Snowboard&custom.RecommendedUse=Topptur+og+alpinisme'},
    {'name': 'SKI/SPLITBOARD BOOTS', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturstovler'},
    {'name': 'SKIS/SPLITBOARD', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturski'},
    {'name': 'SKI BINDINGS', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/toppturbindinger?sortBy=Rating'},
    {'name': 'SKINS', 'url': 'https://www.fjellsport.no/sok?q=skins'},
    {'name': 'SKI POLES', 'url': 'https://www.fjellsport.no/sok?q=poles&custom.CategoryName=Skistaver+fast+lengde'},
    {'name': 'CRAMPONS', 'url': 'https://www.fjellsport.no/sok?q=CRAMPONS'},
    {'name': 'HARNESS', 'url': 'https://www.fjellsport.no/turutstyr/klatreutstyr/klatreseler'},
    {'name': 'ROPE', 'url': 'https://www.fjellsport.no/turutstyr/klatreutstyr/tau'},
    {'name': 'BEACON', 'url': 'https://www.fjellsport.no/sok?q=beacon'},
    {'name': 'BACKPACK', 'url': 'https://www.fjellsport.no/aktiviteter/topptur/topptursekker'},
    {'name': 'HEADLAMP', 'url': 'https://www.fjellsport.no/sok?q=headlamp'}
]

# Create a CSV file for the data
csv_file = open('products_1.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['Category', 'Brand', 'Model', 'Image', 'Price'])

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

    # Iterate over the products
    for product in products:
        # Extract the brand, model, and description
        brand = product.find('div', class_='an bi d3 di dj hp').text.strip()
        description = product.find('div', class_='an d3 di dj fm').text.strip()

        # Extract the image URL
        image_url = product.find('img')['src']

        # Extract the price
        price_element = product.find('span', class_='q as av')
        price = clean_price(price_element.text.strip()) if price_element else 'N/A'

        # Write the data to CSV
        writer.writerow([category_name, brand, description, image_url, price])

# Close the CSV file
csv_file.close()

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
    {'name': 'HARDSHELL/RAIN JACKET', 'url_male': 'https://www.fjellsport.no/sok?q=skalljakker&custom.Gender=Herre&custom.RecommendedUse=Topptur+og+alpinisme&custom.RecommendedUse=Snowboard', 'url_female': 'https://www.fjellsport.no/sok?q=skalljakker&custom.Gender=Dame&custom.RecommendedUse=Topptur+og+alpinisme&custom.RecommendedUse=Snowboard'},
    {'name': 'INSULATED LAYER', 'url_male': 'https://www.fjellsport.no/sok?q=insulated+layer&custom.Gender=Herre', 'url_female': 'https://www.fjellsport.no/sok?q=insulated+layer&custom.Gender=Dame'},
    {'name': 'FLEECE/SWEATER', 'url_male': 'https://www.fjellsport.no/sok?q=sweater&custom.Gender=Herre', 'url_female': 'https://www.fjellsport.no/sok?q=sweater&custom.Gender=Dame'},
    {'name': 'GLOVES', 'url_male': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturhansker?custom.Gender=Herre', 'url_female': 'https://www.fjellsport.no/aktiviteter/topptur/toppturklaer/toppturhansker?custom.Gender=Dame'},
    {'name': 'HARDSHELL PANTS', 'url_male': 'https://www.fjellsport.no/sok?q=skallbukse&custom.Gender=Herre&custom.RecommendedUse=Topptur+og+alpinisme', 'url_female': 'https://www.fjellsport.no/sok?q=skallbukse&custom.Gender=Dame&custom.RecommendedUse=Topptur+og+alpinisme'},
    {'name': 'SOFTSHELL PANTS', 'url_male': 'https://www.fjellsport.no/sok?q=softshell+pants&custom.Gender=Herre', 'url_female': 'https://www.fjellsport.no/sok?q=softshell+pants&custom.Gender=Dame'},
    {'name': 'SOCKS', 'url_male': 'https://www.fjellsport.no/sok?q=str%C3%B8mper&custom.Gender=Herre&custom.RecommendedUse=Frikj%C3%B8ring+og+alpint&custom.RecommendedUse=Snowboard&custom.RecommendedUse=Topptur+og+alpinisme', 'url_female': 'https://www.fjellsport.no/sok?q=str%C3%B8mper&custom.Gender=Herre&custom.RecommendedUse=Frikj%C3%B8ring+og+alpint&custom.RecommendedUse=Snowboard&custom.RecommendedUse=Topptur+og+alpinisme'},
]

# Create a CSV file for the data
csv_file = open('products.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

# Write the header row
writer.writerow(['Category', 'Gender', 'Brand', 'Model', 'Image', 'Price'])

# Iterate over the categories
for category in categories:
    category_name = category['name']
    url_male = category['url_male']
    url_female = category['url_female']

    # Make a request to the male URL
    response = requests.get(url_male)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the product items
    product_items = soup.find_all('div', {'class': 'product-list-item'})

    # Iterate over the product items
    for product_item in product_items:
        # Extract the product details
        brand = product_item.find('span', {'class': 'brand'}).text.strip()
        model = product_item.find('span', {'class': 'name'}).text.strip()
        image = product_item.find('img')['src']
        price = clean_price(product_item.find('span', {'class': 'price'}).text.strip())
        gender = 'Men'  # Set the gender as male
        
        # Write the data to the CSV file
        writer.writerow([category_name, gender, brand, model, image, price])

    # Make a request to the female URL
    response = requests.get(url_female)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the product items
    product_items = soup.find_all('div', {'class': 'product-list-item'})

    # Iterate over the product items
    for product_item in product_items:
        # Extract the product details
        brand = product_item.find('span', {'class': 'brand'}).text.strip()
        model = product_item.find('span', {'class': 'name'}).text.strip()
        image = product_item.find('img')['src']
        price = clean_price(product_item.find('span', {'class': 'price'}).text.strip())
        gender = 'Women'  # Set the gender as female
        
        # Write the data to the CSV file
        writer.writerow([category_name, gender, brand, model, image, price])

# Close the CSV file
csv_file.close()

