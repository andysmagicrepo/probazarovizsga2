# 1 Feladat: Hogwards express jegyautomata
#
# A Marvel új web alapú rajongó oldalt készít az X-man képregény adaptációkból.
#
#
# Itt találod a webes applikáció prototípusát:
# [https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html](https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html)
#
# Készíts egy Python python applikációt (akár csak egy darab python fileban) ami selenium-ot használ.
#
# Teszteld le, hogy a különböző szűrőfeltételek alapján megfelelő karaktereket mutatja az oldal.
#
# Tehát mondjuk `iceman` pontosan az `original` és a `factor` csapatban van benne és a `hellfire` illetve a `force` csapatokban nincs benne.
#
# (Figyelem: ne engedd, hogy az oldal dinamikus működése elvonja a figyelmed a célról! A karaktereket csoporthoz tartozását nem feltétlenül a felület változásával tudod ellenőrizni.)
#
# Al alkalmazás helyesen mutatja a felületen a csoporthoz tartozást. Nincs külön tesztadat leírás ehhez a feladathoz, tehát a látottak alapáj kell a tesztadatot összeállítanod.
#
#
# Az ellenőrzésekhez __NEM kell__ teszt keretrendszert használnod (mint pl a pytest). Egyszerűen használj elágazásokat
# __NEM kell__ OOP-t használnod. Viszont tartalmazzon vizsgálatot a megodásod. Lehetőleg használj az `assert` összehasonlításokat.
### A megoldás beadása
#
# * a megoldásokat a `testproject` mappába tedd, `mutants.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

thisdict = {
    "cyclops": 4+2+1,
    "emma-frost": 8,
    "iceman": 2+1,
    "jean-grey": 2+1,
    "magneto": 8,
    "beast": 4+1,
    "nightcrawler": 2,
    "professor-x": 1,
    "psylocke": 8+2,
    "quicksilver": 4,
    "rictor": 4+2,
    "storm": 8+2,
    "sunspot": 8+2,
    "tithe": 8,
    "wolverine": 2
}

print(thisdict)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html')
    time.sleep(2)

    # gombok
    #next_button = driver.find_element_by_class_name('next-btn next-btn1')
    # original_x_men_btn = driver.find_element_by_id('original')
    # x_force_btn = driver.find_element_by_id('force')
    # x_factor_btn = driver.find_element_by_id('factor')
    # hellfire_club_btn = driver.find_element_by_id('hellfire')

    # TC0 Teszteld le, hogy a különböző szűrőfeltételek alapján megfelelő karaktereket mutatja az oldal.
    #
    # Tehát mondjuk `iceman` pontosan az `original` és a `factor` csapatban van benne és a `hellfire` illetve a `force` csapatokban nincs benne.
    #
    # (Figyelem: ne engedd, hogy az oldal dinamikus működése elvonja a figyelmed a célról! A karaktereket csoporthoz tartozását nem feltétlenül a felület változásával tudod ellenőrizni.)
    #
    # Al alkalmazás helyesen mutatja a felületen a csoporthoz tartozást. Nincs külön tesztadat leírás ehhez a feladathoz, tehát a látottak alapáj kell a tesztadatot összeállítanod.

    #TC2:
    # test_set('abc@abc')
    # # Készíts tesztesetet az e - mail cím validációjára.
    # assert driver.find_element_by_xpath('/html/body/form/h2').text == "Your message was sent successfully." \
    #                                                                   " Thanks! We'll be in touch as soon as we can," \
    #                                                                   " which is usually like lightning (Unless we're sailing or eating tacos!)."

    # Az email validáció hibás, mert simán megengedi a továbblépést hiányzó domain-ű emeil cimmel
finally:
    driver.close()

