# /src/main.py
from scraper.ads_scraper import AdScraper
from scraper.page_checker import PageChecker
from utils.driver_setup import DriverSetup
from utils.csv_writer import CSVWriter

def scrape_ads(query):
    driver_setup = DriverSetup(headless=True)  # Initialize driver in headless mode
    driver = driver_setup.get_driver()

    csv_writer = CSVWriter("scraped_ads.csv")  # Initialize the CSV writer
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
            # Save ads data to CSV
            csv_writer.write_data(ads)

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
    query = "phone"
    scrape_ads(query)
