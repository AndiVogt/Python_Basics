import datetime
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_and_click(wait, xpath_list: list):
    for xpath in xpath_list:
        button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        
def select_date_from_calendar(driver, german_months, days_from_today=14, calendar_title_id="ctl00_Content_RdpDate_calendar_Title", next_button_class="rcFastNext", prev_button_class="rcFastPrev"):
    """
    Selects a date from a calendar on a web page.

    :param driver: Selenium WebDriver instance.
    :param days_from_today: Number of days from today for the target date.
    :param calendar_title_id: The ID of the calendar title element.
    :param next_button_class: The class name of the 'next' button on the calendar.
    :param prev_button_class: The class name of the 'previous' button on the calendar.
    :param german_months: A dictionary mapping German month names to their corresponding month number.
    """


    # Calculate the target date
    target_date = datetime.date.today() + datetime.timedelta(days=days_from_today)
    
    while True:
        # Get the current month and year from the calendar
        calendar_title = driver.find_element(By.ID, calendar_title_id).text
        month_year_match = re.search(r"(\w+) (\d{4})", calendar_title)
        month, year = month_year_match.groups()
        month = german_months[month]
        year = int(year)

        # Define navigation buttons
        next_btn = driver.find_element(By.CLASS_NAME, next_button_class)
        prev_btn = driver.find_element(By.CLASS_NAME, prev_button_class)

        # Determine if we need to navigate forward or backward in the calendar
        if (year, month) < (target_date.year, target_date.month):
            next_btn.click()
        elif (year, month) > (target_date.year, target_date.month):
            prev_btn.click()
        else:
            day_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{target_date.day}']")))
            day_element.click()
            break
        
        
        
        
    
    
def show_open_windows(driver):
    """
    Prints the titles of all open windows.

    :param driver: Selenium WebDriver instance.
    """
    original_window = driver.current_window_handle
    all_windows = driver.window_handles

    for window in all_windows:
        driver.switch_to.window(window)
        print(f"Window Handle: {window}, Page Title: '{driver.title}'")

    # Switch back to the original window
    driver.switch_to.window(original_window)
    
    
    
def show_open_tabs(driver):
    """
    Prints the titles of all open tabs/windows.

    :param driver: Selenium WebDriver instance.
    """
    original_tab = driver.current_window_handle
    all_tabs = driver.window_handles

    for tab in all_tabs:
        driver.switch_to.window(tab)
        print(f"Tab/Window Handle: {tab}, Page Title: '{driver.title}'")

    # Switch back to the original tab/window
    driver.switch_to.window(original_tab)