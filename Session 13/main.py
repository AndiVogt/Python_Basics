from pathlib import Path
import time
import logging

#selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#local imports
from localconfig import xpaths, identifier, links, envs
from driver_utils import fetch_data, find_compatible_driver_version, get_chrome_version, download_chromedriver, update_chromedriver_if_needed



# init
script_dir = Path(__file__).parent
version_path = script_dir / "driver" / "version.txt"
driver_path = script_dir / "driver" / "chromedriver.exe"


update_chromedriver_if_needed(version_path)


chrome_options = Options()




service = Service(executable_path=driver_path)

driver = webdriver.Chrome(options=chrome_options, service=service)
wait = WebDriverWait(driver, 20)

try:
    # Seite aufrufen
    driver.get(links["myportal_login"])
    
    # Login-Button drücken
    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths["windows_login"])))
    button.click()
    

    
    time.sleep(1000)
    
    

except Exception as e:
    logging.error('Error at %s', 'division', exc_info=e)
    
finally:
    driver.quit()
