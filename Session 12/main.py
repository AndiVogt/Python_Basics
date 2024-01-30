from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from localconfig import xpaths, identifier, links, german_months, envs
from utils import wait_and_click, select_date_from_calendar, show_open_windows, show_open_tabs

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")

driver_path = Path("C:/Users/A200017481/OneDrive - Deutsche Telekom AG/Dokumente/Hochschule/1. Semester/Prozeduales Programmieren (Python)/Code/Session 12/driver/chromedriver.exe")
service = Service(executable_path=driver_path)

driver = webdriver.Chrome(options=chrome_options, service=service)
wait = WebDriverWait(driver, 10)

try:
    driver.get(links["myportal_login"])
    
    navigationsliste = [
        xpaths["windows_login"],
        xpaths["arbeitsverhaeltnis"],
        xpaths["my_portal"],
        xpaths["gebaeude_verwaltung"],
        xpaths["desksharing"]
    ]
    
    wait_and_click(wait, navigationsliste)
    
    # Wait for the new window/tab to open
    wait.until(lambda driver: len(driver.window_handles) > 1)

    # Close the window with the title "Meine Services - MyPortal"
    for window_handle in driver.window_handles:
        driver.switch_to.window(window_handle)
        if driver.title == "Meine Services - MyPortal":
            print(f"Closing window: {driver.title}")
            driver.close()
            break

    # Switch to the remaining window
    for window_handle in driver.window_handles:
        driver.switch_to.window(window_handle)
        print(f"Switched to window: {driver.title}")

    print("Searching for Calendar Button on: ", driver.title, window_handle)
    
    kalender_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths["kalender_button"])))
    print("Kalender Button found")
    time.sleep(4)
    kalender_button.click()
    print("clicked")
    
    
    

    select_date_from_calendar(driver, german_months, 
                              14, identifier["calendar_title_id"], 
                              identifier["calendar_next_button_class"], identifier["calendar_prev_button_class"])
    print("Date Inserted successfully")
    
    
    # Input "06:00" in the start time field
    time_from_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpaths["time_from_xpath"])))
    time_from_field.clear()
    time_from_field.send_keys(envs["work_from"])

    # Input "20:00" in the end time field
    time_to_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpaths["time_to_xpath"])))
    time_to_field.clear()
    time_to_field.send_keys(envs["work_until"])
    
    
    
    
    
    
    
    
    # Open the dropdown
    # replace with before logic
    # Scroll the dropdown into view and click it
    dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "RcbBereich_Input")))
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)  # Wait for any dynamic overlays to disappear
    dropdown.click()

    # # Wait for the dropdown options to be visible and find the specific item
    # desired_option_text = "Leipzig, Kärrnerstraße 66  - Zentrum Core 1. OG"
    # option_xpath = f"//li[@class='rcbItem' and text()='{desired_option_text}']"
    # desired_option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    # print("Dropdownelement gefunden")
    # desired_option.click()
    
    # Wait for the dropdown options to be visible and click the first item
    first_option_xpath = "//ul[@id='RcbBereich_listbox']/li[2]"

    first_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, first_option_xpath))
    )
    first_option.click()
    
    
    # Belegungsplanbutton search to check if page has reloaded
    belegungsplan_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths["belegungsplan"])))
    print("Page reloaded.")
    
    
    
    # search_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths["search_button"])))
    # print("Search Button found")
    # time.sleep(4)
    # search_button.click()
    # print("Search Button pressed")
    
    # # wait for page reload
    # belegungsplan_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpaths["belegungsplan"])))
    
    
    rows = driver.find_elements(By.XPATH, "//tbody/tr")

    for row in rows:
        # Check if this row contains the place ID
        if envs["place_id"] in row.text:
            # Check if the status is 'frei'
            try:
                status = row.find_element(By.XPATH, ".//td[@class='bg-success']")
            except NoSuchElementException:
                raise Exception(f"Place ID {envs['place_id']} is not free or status cell not found.")

            if 'frei' in status.text.lower():
                # Find and click the 'Buchen' button in this row immediately
                time.sleep(4)
                buchen_button = row.find_element(By.XPATH, ".//a[contains(text(), 'Buchen')]")
                print("Place is free. Booking now.")
                buchen_button.click()

                # Wait for the page to reload after clicking 'Buchen'
                belegungsplan_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpaths["belegungsplan"])))
                print("Page reloaded.")
                break
            else:
                raise Exception(f"Place ID {envs['place_id']} is not free.")
    else:
        raise Exception(f"Place ID {envs['place_id']} not found in the table.")
    
    # Wait for the page to reload after clicking 'Buchen'
    # belegungsplan_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpaths["belegungsplan"])))
    

    time.sleep(4)
    print("wait 10 seconds")
    
    iframe_name = "ctl00_Content_RadWindowManager1706626450075"  # The name attribute of the iframe

    try:
        # Switch to the iframe
        print("try switching to frame")
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, iframe_name)))
        print("Switched to iframe.")

        # Now you can interact with elements inside the iframe
        # For example, find and interact with the input field

        # ... Your code for interacting with elements inside the iframe ...

        # Switch back to the main document when done
        driver.switch_to.default_content()
    except:
        print("not found")


   
    
    # time.sleep(4)
    # book_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths["book_button2"])))
    # print("Kalender Button found")
    # time.sleep(2)
    # book_button.click()
    # print("clicked")
    
    
    
    
    time.sleep(1000)
    
    
    

finally:
    driver.quit()
