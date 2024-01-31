import os
import requests
import zipfile
import subprocess
from sys import platform
from packaging import version
import shutil

from localconfig import proxies, links


def update_chromedriver_if_needed(version_path):
    # Assuming get_chrome_version and other required functions are defined elsewhere

    # Get the current Chrome browser version
    browser_version = get_chrome_version()
    print(f"Chrome Browser Version: {browser_version}")

    # Read the current ChromeDriver version from file
    try:
        with open(version_path, "r") as file:
            driver_version = file.read().strip()
        print(f"Current ChromeDriver Version: {driver_version}")
    except FileNotFoundError:
        print(f"Version file not found at {version_path}. Assuming no driver installed.")
        driver_version = None

    # Update ChromeDriver if versions do not match
    if browser_version != driver_version:
        print("Updating ChromeDriver...")
        drivers_data = fetch_data(links["chromedriver_json"])

        compatible_driver = find_compatible_driver_version(browser_version, drivers_data)
        if compatible_driver:
            print("Found compatible driver version:", compatible_driver['version'])

            # Check if the compatible driver version is the same as the current driver version
            if compatible_driver['version'] == driver_version:
                print("ChromeDriver is already up to date with version:", driver_version)
            else:
                # Proceed with downloading and updating the ChromeDriver
                print("Downloading Chromedriver")
                download_chromedriver(compatible_driver['url'], str(version_path.parent))
                with open(version_path, "w") as file:
                    file.write(compatible_driver['version'])
                print("ChromeDriver updated successfully.")
        else:
            print("No compatible driver version found.")
    else:
        print("ChromeDriver is up to date.")








# Function to fetch data with proxy
def fetch_data(url):
    response = requests.get(url, proxies=proxies)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to find compatible ChromeDriver version
def find_compatible_driver_version(browser_version, drivers_data):
    browser_ver = version.parse(browser_version)
    matching_driver = None

    # Access the list of versions
    for driver in drivers_data['versions']:
        if 'chromedriver' in driver['downloads']:  # Ensure we are looking at ChromeDriver versions
            for download in driver['downloads']['chromedriver']:
                if download['platform'] == 'win64':  # Assuming you need the Windows 64-bit version
                    driver_ver = version.parse(driver['version'])
                    if driver_ver <= browser_ver and (matching_driver is None or driver_ver > version.parse(matching_driver['version'])):
                        matching_driver = {
                            'version': driver['version'],
                            'url': download['url']
                        }
    return matching_driver

# Function to get Chrome browser version
def get_chrome_version():
    if platform == "win32":
        return subprocess.check_output("reg query \"HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon\" /v version", shell=True).decode().split()[-1]
    elif platform == "darwin":
        process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
        return process.communicate()[0].decode().split()[-1].strip()
    elif platform in ["linux", "linux2"]:
        return subprocess.check_output(['google-chrome', '--version']).decode().split()[-1].strip()


# Function to download and replace ChromeDriver

def download_chromedriver(url, driver_path):
    response = requests.get(url, proxies=proxies, stream=True)
    zip_filename = "chromedriver.zip"

    with open(zip_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

    # Extract to a temporary directory
    temp_extract_dir = "temp_chromedriver"
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(temp_extract_dir)

    # Move contents from the extracted 'chromedriver-win64' folder to the desired directory
    extracted_dir_path = os.path.join(temp_extract_dir, "chromedriver-win64")
    for filename in os.listdir(extracted_dir_path):
        src_file = os.path.join(extracted_dir_path, filename)
        dest_file = os.path.join(driver_path, filename)

        # If the destination file exists, remove it
        if os.path.exists(dest_file):
            os.remove(dest_file)

        shutil.move(src_file, dest_file)

    # Clean up: Remove the temporary directory
    shutil.rmtree(temp_extract_dir)

    # Attempt to delete the ZIP file, handle any permission error
    try:
        os.remove(zip_filename)
    except PermissionError:
        print("Warning: Unable to delete 'chromedriver.zip' - it may be in use by another process.")
