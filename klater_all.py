import requests
from bs4 import BeautifulSoup
import csv

categories = [
    {'name': 'HEAD', 'subcategories': [
        {'name': 'BUFF', 'url': 'https://www.fjellsport.no/sok?q=buff'},
    ]},
    {'name': 'UPPER BODY', 'subcategories': [
        {'name': 'HARDSHELL JACKET', 'url_male': 'https://www.fjellsport.no/sok?q=shelljakker&custom.Gender=Herre',
         'url_female': 'https://www.fjellsport.no/sok?q=shelljakker&custom.Gender=Dame'},
        {'name': 'SOFTSHELL JACKET', 'url_male': 'https://www.fjellsport.no/sok?q=softshell+jacket&custom.Gender=Herre',
         'url_female': 'https://www.fjellsport.no/sok?q=softshell+jacket&custom.Gender=Dame'},
        {'name': 'INSULATED LAYER', 'url_male': 'https://www.fjellsport.no/sok?q=insulated+layer+1+top&custom.Gender=Herre',
         'url_female': 'https://www.fjellsport.no/sok?q=insulated+layer+1+top&custom.Gender=Dame'},
        {'name': 'FLEECE/SWEATER', 'url_male': 'https://www.fjellsport.no/sok?q=fleece&custom.Gender=Herre',
         'url_female': 'https://www.fjellsport.no/sok?q=fleece&custom.Gender=Dame'},
        {'name': 'BASELAYER', 'url_male': 'https://www.fjellsport.no/sok?q=baselayer+tops&custom.Gender=Herre',
         'url_female': 'https://www.fjellsport.no/sok?q=baselayer+tops&custom.Gender=Dame'},
        {'name': 'GLOVES', 'url_male': 'https://www.fjellsport.no/sok?q=gloves&custom.Gender=Herre&custom.RecommendedUse=Tur+og+friluftsliv&custom.RecommendedUse=Hverdag+og+aktiv+livsstil',
         'url_female': 'https://www.fjellsport.no/sok?q=gloves&custom.Gender=Dame&custom.RecommendedUse=Tur+og+friluftsliv&custom.RecommendedUse=Hverdag+og+aktiv+livsstil'},
    ]},
    {'name': 'LOWER BODY', 'subcategories': [
        {'name': 'HARDSHELL PANTS', 'url_male': 'https://www.fjellsport.no/sok?q=shell+pants&custom.CategoryName=Skallbukser+herre',
         'url_female': 'https://www.fjellsport.no/sok?q=shell+pants&custom.CategoryName=Skallbukser+dame'},
        {'name': 'SOFTSHELL PANTS', 'url_male': 'https://www.fjellsport.no/sok?q=softshell+pants&custom.CategoryName=Turbukser+herre',
         'url_female': 'https://www.fjellsport.no/sok?q=softshell+pants&custom.CategoryName=Turbukser+dame'},
        {'name': 'BASELAYER', 'url_male': 'https://www.fjellsport.no/sok?q=baselayer+pants&custom.CategoryName=Longs+herre',
         'url_female': 'https://www.fjellsport.no/sok?q=baselayer+pants&custom.CategoryName=Longs+dame'},
        {'name': 'SOCKS', 'url_male': 'https://www.fjellsport.no/sok?q=socks&custom.CategoryName=Sokker+herre&custom.RecommendedUse=Tur+og+friluftsliv&custom.RecommendedUse=L%C3%B8p+og+trening&custom.RecommendedUse=Hverdag+og+aktiv+livsstil',
         'url_female': 'https://www.fjellsport.no/sok?q=socks&custom.CategoryName=Sokker+dame&custom.RecommendedUse=Tur+og+friluftsliv&custom.RecommendedUse=L%C3%B8p+og+trening&custom.RecommendedUse=Hverdag+og+aktiv+livsstil'},
        {'name': 'HIKING BOOTS', 'url_male': 'https://www.fjellsport.no/sok?q=hikingsko&custom.Gender=Herre',
         'url_female': 'https://www.fjellsport.no/sok?q=hikingsko&custom.Gender=Dame'},
    ]},
    {'name': 'TECHNICAL', 'subcategories': [
        {'name': 'BACKPACK', 'url': 'https://www.fjellsport.no/sok?q=hiking+backpack'},
        {'name': 'SLEEPING BAG', 'url': 'https://www.fjellsport.no/sok?q=sleeping+bag&custom.Gender=Unisex'},
        {'name': 'SLEEPING PAD', 'url': 'https://www.fjellsport.no/sok?q=sleeping+pad&custom.Gender=Unisex'},
        {'name': 'TENT', 'url': 'https://www.fjellsport.no/sok?q=tent&custom.CategoryName=Telt'},
        {'name': 'STOVE/BURNER', 'url': 'https://www.fjellsport.no/sok?q=stove'},
        {'name': 'HIKING POLES', 'url': 'https://www.fjellsport.no/sok?q=HIKING+POLES'},
        {'name': 'CAMERA', 'url': 'https://www.vpg.no/search?q=kamera&Filter=PrdGruppeLev3ID%C2%A41:PrdGruppeLev3ID%C2%A41_299'},
        {'name': 'GPS', 'url': 'https://www.fjellsport.no/sok?q=gps'},
    ]},
]

# Create a CSV file for the data
csv_file = open('hiking_camping_products.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Category', 'Sub-category', 'unisex', 'male', 'female'])

# Iterate over the categories
for category in categories:
    category_name = category['name']
    subcategories = category['subcategories']
    
    # Iterate over the subcategories
    for subcategory in subcategories:
        subcategory_name = subcategory['name']
        
        # Get the URLs for different genders
        url_male = subcategory.get('url_male', '')
        url_female = subcategory.get('url_female', '')
        
        # Scrape the data for male and female URLs
        response_male = requests.get(url_male)
        response_female = requests.get(url_female)
        
        # Parse the HTML content
        soup_male = BeautifulSoup(response_male.text, 'html.parser')
        soup_female = BeautifulSoup(response_female.text, 'html.parser')
        
        # Extract the product count for each gender
        count_male = soup_male.find('span', class_='count').text.strip()
        count_female = soup_female.find('span', class_='count').text.strip()
        
        # Write the data to the CSV file
        csv_writer.writerow([category_name, subcategory_name, url_male, url_female])
        
# Close the CSV file
csv_file.close()
