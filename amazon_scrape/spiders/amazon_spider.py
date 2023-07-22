import re
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    base_url = 'https://www.amazon.in'

    def start_requests(self):
        search_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1&page={}'
        num_pages = 20

        for page_number in range(1, num_pages + 1):
            url = search_url.format(page_number)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Extract product details from the search result page
        for product in response.css('div[data-component-type="s-search-result"]'):
            product_url = self.base_url + product.css('a.a-link-normal::attr(href)').get()

            product_name = product.css('span.a-size-medium::text').get()

            product_price = product.css('span.a-price-whole::text').get()
            product_price = int(product_price.replace(',', '')) if product_price else "Price not available"

            rating = product.css('span.a-icon-alt::text').get()
            rating = float(rating.split()[0]) if rating else "Rating not available"

            num_reviews = product.css('span.a-size-base.s-underline-text::text').get()
            num_reviews = int(num_reviews.replace(',', '')) if num_reviews else 0

            # Now, follow the product detail page link to get additional information
            yield scrapy.Request(
                url= product_url,
                callback=self.parse_product_detail,
                meta={
                    'Product URL': product_url,
                    'Product Name': product_name,
                    'Product Price': product_price,
                    'Rating': rating,
                    'Number of Reviews': num_reviews,
                }
            )

        # Follow pagination links to scrape more pages
        next_page = response.css('li.a-last a::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=self.base_url + next_page, callback=self.parse)

    def parse_product_detail(self, response):
        # Extract additional information from the product detail page
        product_url = response.meta['Product URL']
        product_name = response.meta['Product Name']
        product_price = response.meta['Product Price']
        rating = response.meta['Rating']
        num_reviews = response.meta['Number of Reviews']

        product_url = response.url
    
        # Extracting ASIN
        asin_matches = re.findall(r"(?:dp%2F|dp/)([A-Z0-9]+)", response.url)
        if asin_matches:
            asin = asin_matches[0]
        else:
            asin = 'ASIN not available'

        #Extracting meta description
        description = response.css('meta[name="description"]::attr(content)').get()

        # Extracting Product Description
        product_description = response.css('div[id="productDescription_feature_div"] div[id="productDescription"] p span::text').get()

        # Extracting Manufacturer
        manufacturer = response.css('a[id="bylineInfo"]::text').get()
        yield {
            'Product URL': product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': rating,
            'Number of Reviews': num_reviews,
            'Description': description,
            'ASIN': asin,
            'Product Description': product_description,
            'Manufacturer': manufacturer,
        }
