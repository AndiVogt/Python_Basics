"""
Umgebungsvariablen, xpaths, links
"""

xpaths = {
    "beispiel_button": "//button[@id='beispiel_id']",
    "windows_login": "//scale-button[@id='kerberos']",
    "arbeitsverhaeltnis": "//button[@id='employment-200017482']",
    "my_portal": "//a[@title='MyPortal']",
    "zeit_verwaltung": "//button[@id='__button6-__vbox0-1']",
    "meine_abwesenheiten": "//div[@id='__xmlview2--mpServiceTileV2-__xmlview2--id_categories_scroll_container-0--hover']",
    "abwesenheit_anlegen": "//button[@title='Abwesenheitsantrag anlegen']",
    "iframe_xpath": "//iframe[@name='Meine Abwesenheiten']",


}

identifier = {
   
}

links = {
    "myportal_login": "https://myportal-websso.corp.telekom.de/login/?target=https://myportal-websso.corp.telekom.de:443/websso_linkpage/websso_linkpage.jsp",
    "chromedriver_json": "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json",
}


envs = {
    "place_id": "E43-003",
    "work_from": "06:00",
    "work_until": "20:00",
    "delta": 14,                    
}

proxies = {
    "http": "http://sia-lb.telekom.de:8080/",
    "https": "http://sia-lb.telekom.de:8080/",
}