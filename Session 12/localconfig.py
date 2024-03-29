"""
Umgebungsvariablen, xpaths, links
"""

xpaths = {
    "windows_login": "//scale-button[@id='kerberos']",
    "arbeitsverhaeltnis": "//button[@id='employment-200017482']",
    "my_portal": "//a[@title='MyPortal']",
    "gebaeude_verwaltung": "//button[@id='__button6-__vbox0-4']",
    "desksharing": "//div[@id='__xmlview2--mpServiceTileV2-__xmlview2--id_categories_scroll_container-1']",
    "kalender_button": "//a[@id='ctl00_Content_RdpDate_popupButton']",
    "belegungsplan": "//a[@id='Belegungsplan']",
    "search_button": "//button[@id='BtnSearch']",
    "time_from_xpath": "//input[@id='ctl00_Content_RdpTimeFrom_dateInput']",
    "time_to_xpath": "//input[@id='ctl00_Content_RdpTimeTo_dateInput']",
    "book_button": "//input[@id='ctl00_Content_BtnSave']",
    "book_button2": "//input[@value='Speichern']",
    "booking_iframe": "//iframe",
    "place_id_bookable": ".//td[@class='bg-success']",
    "buchungsplatz": "//ul[@id='RcbBereich_listbox']/li[2]",
    "book_selected_button": ".//a[contains(text(), 'Buchen')]",

}

identifier = {
    "calendar_title_id": "ctl00_Content_RdpDate_calendar_Title",
    "calendar_next_button_class": "rcFastNext",
    "calendar_prev_button_class": "rcFastPrev",
    
    
}

links = {
    "myportal_login": "https://myportal-websso.corp.telekom.de/login/?target=https://myportal-websso.corp.telekom.de:443/websso_linkpage/websso_linkpage.jsp",
    "chromedriver_json": "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json",
}



german_months = {"Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6,
                 "Juli": 7, "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12}


envs = {
    "place_id": "E43-003",
    "work_from": "06:00",
    "work_until": "20:00",
    "delta": 14,                        # wie weit im vorraus buchen ?
}

proxies = {
    "http": "http://sia-lb.telekom.de:8080/",
    "https": "http://sia-lb.telekom.de:8080/",
}