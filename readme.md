Here’s the corrected version of the `README.md` file with proper formatting:

### `README.md`

```md
# Web Scraper & Ad Poster for ikman.lk

This project provides a web scraper and automated ad poster for [ikman.lk](https://ikman.lk). Using Selenium and BeautifulSoup, it can scrape ads based on a query, store the results in a CSV file, and automatically post ads using the scraped data.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [Command-Line Arguments](#command-line-arguments)
- [Project Structure](#project-structure)
- [License](#license)

## Prerequisites

To run this project, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

Additionally, you need the following Python packages, which will be installed in the next step:

- `selenium`
- `webdriver-manager`
- `beautifulsoup4`

## Setup

1. Clone this repository to your local machine or download it as a ZIP file:
   
   ```bash
   git clone <repository-url>
   cd scraper_project
   ```

2. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the latest version of Firefox if it's not already installed, as this project uses Firefox through Selenium. The path to the Firefox executable can be updated in the code if needed.

## How to Run

### Scraping Ads

You can scrape ads from ikman.lk based on a query using the `-query` command-line argument. The results will be saved in a CSV file (`scraped_ads.csv`).

Example usage:

```bash
python src/main.py -query "phones"
```

### Posting an Ad

You can post an ad to ikman.lk using the `--post-ad` flag. The program will use the first row of the scraped ads in `scraped_ads.csv` to fill in the ad form.

Example usage:

```bash
python src/main.py --post-ad
```

### Combined Actions

You can first scrape ads with a query and then post an ad using the scraped data:

1. First, scrape the ads:

   ```bash
   python src/main.py -query "phones"
   ```

2. Then, post an ad:

   ```bash
   python src/main.py --post-ad
   ```

## Command-Line Arguments

| Argument         | Description                                                     | Example Usage                 |
|------------------|-----------------------------------------------------------------|-------------------------------|
| `--post-ad`      | Post an ad using the first row of the scraped CSV data           | `python src/main.py --post-ad` |
| `-query <term>`  | Scrape ads using the specified search query term                 | `python src/main.py -query "phones"` |

### Notes

- You can only use either `-query` or `--post-ad` in a single command, but you can run the commands consecutively to perform both actions.
- For testing purposes, you can modify the hardcoded values for brand, model, and other fields in the form-filling script.

## Project Structure

```
/scraper_project
│
├── /src
│   ├── /scraper
│   │   ├── __init__.py         # Scraper package initialization
│   │   ├── ads_scraper.py      # Scrapes ads from ikman.lk
│   │   ├── page_checker.py     # Checks for the presence of search results
│   ├── /forms
│   │   ├── form_filler.py      # Automatically fills and submits the ad form
│   └── main.py                 # Main script with command-line argument handling
│
├── /utils
│   ├── __init__.py             # Utility package initialization
│   ├── driver_setup.py         # Sets up the Selenium WebDriver
│   └── csv_writer.py           # (Optional) Handles CSV writing if extended
│
├── scraped_ads.csv             # CSV file where scraped ads are saved
└── requirements.txt            # Python dependencies for the project
```

