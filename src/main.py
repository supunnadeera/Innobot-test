# /src/main.py
import argparse
from scraper.ads_scraper import AdScraper
from forms.form_filler import FormFiller
from utils.driver_setup import DriverSetup
from scraper.page_checker import PageChecker
import csv

def get_first_row_from_csv(csv_file):
    """Read the first row from the scraped CSV file."""
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return next(reader)  # Return the first row

def post_ad_from_csv():
    # Step 1: Set up the Selenium WebDriver
    driver_setup = DriverSetup(headless=False)  # Run in headful mode for better visualization
    driver = driver_setup.get_driver()

    # Step 2: Load the posting page URL
    driver.get('https://ikman.lk/en/post-ad')

    # Step 3: Extract the first row from the CSV file
    ad_data = get_first_row_from_csv("scraped_ads.csv")

    # Step 4: Fill the form with the data and hardcoded values
    form_filler = FormFiller(driver, ad_data)
    form_filler.fill_form()

    # Step 5: Submit the form
    form_filler.submit_form()

    # Optional: Wait and then close the driver
    driver.quit()

def scrape_ads(query):
    driver_setup = DriverSetup(headless=True)  # Initialize driver in headless mode
    driver = driver_setup.get_driver()

    page = 1
    while True:
        # URL of the page to scrape with query and page appended
        url = f'https://ikman.lk/en/ads/sri-lanka/electronics?sort=price&buy_now=0&urgent=0&page={page}&order=desc&query={query.replace(" ", "%20")}'
        driver.get(url)

        # Page checker class to check if there are results on the page
        page_checker = PageChecker(driver.page_source)
        if not page_checker.has_results():
            print(f"No results found on page {page}. Stopping.")
            break

        # Scrape ads
        ad_scraper = AdScraper(driver.page_source)
        ads = ad_scraper.extract_ads()

        if ads:
            # Save ads data to CSV (could reuse the CSVWriter from earlier)
            with open("scraped_ads.csv", mode="w", newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Location", "Seller Badge"])
                writer.writeheader()
                writer.writerows(ads)

        # Display scraped ads
        for ad in ads:
            print(f"Title: {ad['Title']}")
            print(f"Price: {ad['Price']}")
            print(f"Location: {ad['Location']}")
            print(f"Seller Badge: {ad['Seller Badge']}")
            print('-' * 50)

        # Move to the next page
        page += 1

    # Close the driver
    driver.quit()

if __name__ == '__main__':
    # Step 1: Parse command-line arguments
    parser = argparse.ArgumentParser(description="Scrape ads or post an ad on ikman.lk.")
    
    parser.add_argument('--post-ad', action='store_true', help='Post an ad using the scraped data')
    parser.add_argument('-query', type=str, help='Query for searching ads (e.g., -query "phones")')

    args = parser.parse_args()

    # Step 2: Handle post-ad flag
    if args.post_ad:
        print("Posting an ad...")
        post_ad_from_csv()

    # Step 3: Handle search query
    if args.query:
        print(f"Searching for ads with query: {args.query}")
        scrape_ads(args.query)
