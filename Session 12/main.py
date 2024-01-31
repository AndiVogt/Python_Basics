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
from driver_utils import fetch_data, find_compatible_driver_version, get_chrome_version, download_chromedriver, update_chromedriver_if_needed



# init
script_dir = Path(__file__).parent
version_path = script_dir / "driver" / "version.txt"
driver_path = script_dir / "driver" / "chromedriver.exe"


update_chromedriver_if_needed(version_path)


chrome_options = Options()




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
                              envs["delta"], identifier["calendar_title_id"], 
                              identifier["calendar_next_button_class"], identifier["calendar_prev_button_class"])
    print("Date Inserted successfully")
    
    # time injection
    time_from_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpaths["time_from_xpath"])))
    time_from_field.clear()
    time_from_field.send_keys(envs["work_from"])

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

    

    first_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpaths["buchungsplatz"]))
    )
    first_option.click()
    
    
    # Belegungsplanbutton search to check if page has reloaded
    belegungsplan_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths["belegungsplan"])))
    print("Page reloaded.")
    time.sleep(4)
    
    rows = driver.find_elements(By.XPATH, "//tbody/tr")

    for row in rows:
        # Check if this row contains the place ID
        if envs["place_id"] in row.text:
            # Check if the status is 'frei'
            try:
                status = row.find_element(By.XPATH, xpaths["place_id_bookable"])
            except:
                raise Exception(f"Place ID {envs['place_id']} is not free or status cell not found.")

            if 'frei' in status.text.lower():
                # Find and click the 'Buchen' button in this row immediately
                time.sleep(4)
                buchen_button = row.find_element(By.XPATH, xpaths["book_selected_button"])
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
    

    time.sleep(4)
    print("wait 10 seconds")
    
    iframes = driver.find_elements(By.XPATH, xpaths["booking_iframe"])

    # Check if there is at least one iframe
    if iframes:
        # Switch to the first iframe
        driver.switch_to.frame(iframes[0])

        kalender_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths["book_button"])))
        print("Speichern Knopf gefunden")
        time.sleep(4)
        kalender_button.click()
        print("Dein Platz wurde gebucht")
        

        
        driver.switch_to.default_content()
    else:
        print("No iframes found on the page.")    
        
    # Wait for the page to reload after clicking 'Buchen'
    belegungsplan_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpaths["belegungsplan"])))
    print("Page reloaded.")
    

finally:
    driver.quit()
