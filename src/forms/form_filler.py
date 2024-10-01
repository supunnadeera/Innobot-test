# /src/forms/form_filler.py
from selenium.webdriver.common.by import By
import time

class FormFiller:
    def __init__(self, driver, ad_data):
        self.driver = driver
        self.ad_data = ad_data

    def fill_form(self):
        # Fill condition (assuming 'Used' for now)
        condition = self.driver.find_element(By.XPATH, "//input[@value='Used']")
        condition.click()

        # Fill brand, model, etc. (hardcoded since these are not in the CSV)
        brand_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Brand']")
        brand_field.send_keys("Samsung")  # Hardcoded

        model_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Model']")
        model_field.send_keys("Galaxy S21")  # Hardcoded

        # Fill description (from scraped data)
        description_field = self.driver.find_element(By.XPATH, "//textarea[@maxlength='4000']")
        description_field.send_keys(self.ad_data['Title'])  # Use title as description

        # Fill price (from scraped data)
        price_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Pick a good price']")
        price_field.send_keys(self.ad_data['Price'].replace('Rs', '').strip())  # Extract price

        # Upload photos (optional, can use an image path if available)
        # You could either upload a static image or handle it dynamically if provided
        photo_upload_button = self.driver.find_element(By.XPATH, "//input[@type='file']")
        photo_upload_button.send_keys("C:/path/to/sample_image.jpg")  # Hardcoded path to image

        # Contact details (hardcoded in this case)
        name_field = self.driver.find_element(By.XPATH, "//input[@name='name']")
        name_field.send_keys("John Doe")  # Hardcoded

        email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_field.send_keys("john.doe@example.com")  # Hardcoded

        phone_field = self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone_field.send_keys("0712345678")  # Hardcoded

    def submit_form(self):
        # Click the post button to submit the ad
        submit_button = self.driver.find_element(By.XPATH, "//button[text()='Post ad']")
        submit_button.click()

        # Optionally wait to ensure the form submission completes
        time.sleep(5)
