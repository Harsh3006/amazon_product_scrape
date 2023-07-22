# Web Scraping Assignment

## Part 1 - Scraping Product Listing Pages

In this assignment, it is required to scrape all products from the Amazon website based on the search query "bags." The main objective is to extract essential product information from the search results.

### Website URL:
https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1

### Task Description:
Scrape at least 20 pages of product listing pages and extract the following information for each product:

- Product URL
- Product Name
- Product Price
- Rating
- Number of Reviews

## Part 2 - Scraping Product Details Pages

After obtaining the Product URLs from Part 1, the next step is to visit each individual product page and gather more information about the products.

### Additional Items to Scrape:
For each product URL obtained in Part 1, we need to visit the corresponding detail page and extract the following additional information:

- Description
- ASIN (Amazon Standard Identification Number)
- Product Description
- Manufacturer

### Total URLs to Visit:
We need to scrape at least 200 product URLs to collect the required information.

## Data Export:
The final scraped data will be exported in CSV (Comma-Separated Values) format. The CSV file will contain all the scraped information for further analysis and processing.

### Usage:
To run the scraper, execute the Python script provided in the repository. The script uses Scrapy, a powerful web scraping framework, to efficiently collect data from web pages.

### Requirements:
Make sure to have Python and the required libraries Scrapy, Selenium installed.
```
pip install scrapy selenium
```

### Execution:
Run the following command in the terminal or command prompt to start the web scraping process:

```
scrapy crawl amazon_spider -o amazon_products_data.csv
```
Added an `output_file.csv` for reference.

## Disclaimer:
Please ensure that you abide by Amazon's terms of service and robots.txt while performing web scraping. Respect the website's policies and do not overload their servers with excessive requests.
