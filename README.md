# Web Scraping Outdoor Gear Prices

This project involves web scraping outdoor gear prices from the Fjellsport.no website. It aims to gather price information for various categories of climbing and outdoor gear and store the data in a CSV file for further analysis.

## Project Overview

The project consists of the following components:

- **Web Scraping**: Python script (`web_scraper.py`) that uses the requests library to send HTTP requests to the Fjellsport.no website and the BeautifulSoup library to parse the HTML response. It extracts the product names and prices for each category of gear and stores them in a CSV file.

- **Categories**: The script defines a list of categories, each with a name and a corresponding URL. These categories represent different types of outdoor gear, such as helmets, sunglasses, jackets, gloves, etc.

- **Data Cleaning**: The script includes a function to clean up the price values scraped from the website. It removes unwanted characters, such as non-breaking spaces and currency symbols, to ensure consistency in the data.

- **CSV Output**: The cleaned data is stored in a CSV file (`gear_prices.csv`). Each row in the CSV file represents a product and includes the following information: category, product name, and price.

## Getting Started

To run the web scraping script and gather the outdoor gear prices, follow these steps:

1. Install the required libraries: requests, BeautifulSoup, and csv. You can use pip to install them:

`pip install requests beautifulsoup4;`


2. Download the `web_scraper.py` script and save it to your local machine.

3. Open the `web_scraper.py` script in a text editor and review the list of categories. You can modify or add categories as per your requirements. Each category should include a name and a URL.

4. Run the script using the following command:
`python web_scraper.py`

The script will scrape the Fjellsport.no website for each category, extract the product names and prices, clean up the price values, and store the data in the `gear_prices.csv` file.

## Disclaimer

The information and code provided in this project are for educational and demonstration purposes only. By using this project, you acknowledge and agree that:

1. The scraping of websites may have legal implications, and it is your responsibility to ensure that you comply with all applicable laws and regulations.

2. The developer of this project shall not be held responsible for any misuse, legal issues, or damages arising from the use of this project.

Please consult with legal professionals or experts in your jurisdiction to understand the legal implications of web scraping and ensure your compliance with applicable laws and regulations.

By using this project, you agree to hold harmless and indemnify the developer from any and all claims, damages, losses, liabilities, costs, or expenses arising from your use or misuse of this project.

Please proceed with caution and use this project responsibly.
