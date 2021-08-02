# 5 Feladat: Periodusos rendszer
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Periodusos rendszer app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html](https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html) oldalról.
#
# Feladatod, hogy leteszteld, hogy az alábbi sorrendben jelennek-e meg az elemek a weblapon:
#
# (az alábbi tartalmat írd ki kézzel egy data.txt nevű fileba és onnan olvassa fel a kódod a tesztadatot)
# ```
# 1, Hydrogen
# 2, Helium
# 3, Lithium
# 4, Beryllium
# 5, Boron
# 6, Carbon
# 7, Nitrogen
# 8, Oxygen
# 9, Fluorine
# 10, Neon
# 11, Sodium
# 12, Magnesium
# 13, Aluminium
# 14, Silicon
# 15, Phosphorus
# 16, Sulfur
# 17, Chlorine
# 18, Argon
# 19, Potassium
# 20, Calcium
# 21, Scandium
# 22, Titanium
# 23, Vanadium
# 24, Chromium
# 25, Manganese
# 26, Iron
# 27, Cobalt
# 28, Nickel
# 29, Copper
# 30, Zinc
# 31, Gallium
# 32, Germanium
# 33, Arsenic
# 34, Selenium
# 35, Bromine
# 36, Krypton
# 37, Rubidium
# 38, Strontium
# 39, Yttrium
# 40, Zirconium
# 41, Niobium
# 42, Molybdenum
# 43, Technetium
# 44, Ruthenium
# 45, Rhodium
# 46, Palladium
# 47, Silver
# 48, Cadmium
# 49, Indium
# 50, Tin
# 51, Antimony
# 52, Tellurium
# 53, Iodine
# 54, Xenon
# 55, Caesium
# 56, Barium
# 57-71, Lanthanide
# 72, Hafnium
# 73, Tantalum
# 74, Tungsten
# 75, Rhenium
# 76, Osmium
# 77, Iridium
# 78, Platinum
# 79, Gold
# 80, Mercury
# 81, Thallium
# 82, Lead
# 83, Bismuth
# 84, Polonium
# 85, Astatine
# 86, Radon
# 87, Francium
# 88, Radium
# 89-103, Actinide
# 104, Rutherfodum
# 105, Dubnium
# 106, Seaborgium
# 107, Bohrium
# 108, Hassium
# 109, Meitnerium
# 110, Damstadium
# 111, Roentgenium
# 112, Ununbium
# 113, Ununtrium
# 114, Ununquadium
# 115, Ununpentium
# 115, Ununhexium
# 115, Ununseptum
# 115, Ununoctium
# ```
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
# # ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `periodic_table.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

with open("data.txt", 'r', encoding="utf-8") as periodic_data:
    with open("res.csv", 'w', encoding="utf-8") as res:
        words = periodic_data().replace("\n", " ").replace(" ", "").split(",")
        for word in words[::2]:
            res.write(f"{words.index(word)}, {word.lower()}\n")

#
# Feladatod, hogy leteszteld, hogy az alábbi sorrendben jelennek-e meg az elemek a weblapon:

try:
    # Oldal betöltése
    # driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html')
    # time.sleep(2)
    # i = 1
    # for i in range(91):
    #     #elemek = driver.find_elements_by_xpath('/li[@class ="type-"]').text
    #     elemek = driver.find_elements_by_xpath('/li[@class ="type-"a]')
    # .type - 1
    # time.sleep(2)



    #driver.find_element_by_partial_link_text()

    # gombok
    #next_button = driver.find_element_by_class_name('next-btn next-btn1')
    #next_button_p1 = driver.find_element_by_('//button[@class ="next-btn next-btn1"]')
    # next_button_p2 = driver.find_element_by_xpath('//button[@class ="next-btn next-btn2"]')
    # request_button_p3 = driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/ul/li[4]/button')

    # mezok  (/html/body/form/div[1]/div[1]/ul/li[1]/select)
    #How_many_guests_in_your_group_dd = driver.find_element_by_xpath('//*[@class="errorTxt"]//select')
    # How_many_guests_in_your_group_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[1]/ul/li[1]/select')
    # Which_date_and_time_are_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/ul/li[1]/input')
    # Which_time_of_day_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/ul/li[2]/select')
    # How_many_hours_would_you_like_to_charter_for_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/ul/li[3]/select')
    # What_is_your_first_and_last_name_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/ul/li[1]/input')
    # Which_email_address_should_we_send_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/ul/li[2]/input')

    #TC1:
    # test_set('abc@abc.com')
    # assert driver.find_element_by_xpath('/html/body/form/h2').text == "Your message was sent successfully." \
    #                                                                   " Thanks! We'll be in touch as soon as we can," \
    #                                                                   " which is usually like lightning (Unless we're sailing or eating tacos!)."
    # time.sleep(5)
    # #TC2:
    # test_set('abc@abc')
    # # Készíts tesztesetet az e - mail cím validációjára.
    # assert driver.find_element_by_xpath('/html/body/form/h2').text == "Your message was sent successfully." \
    #                                                                   " Thanks! We'll be in touch as soon as we can," \
    #                                                                   " which is usually like lightning (Unless we're sailing or eating tacos!)."

    # Az email validáció hibás, mert simán megengedi a továbblépést hiányzó domain-ű emeil cimmel
finally:
    driver.close()
