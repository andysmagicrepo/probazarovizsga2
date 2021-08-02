# 4 Feladat: charterbooker automatizálása
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a charterbooker app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html](https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a charterbooker app tesztelését.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
# * Teszteld le a többoldalas formanyomtatvány működését.
# * Ellenőrizd a helyes kitöltésre adott választ: "Your message was sent successfully. Thanks!
# We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
# * Készíts tesztesetet az e-mail cím validációjára.
#
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `charterbooker.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
def test_set(email):
    # page 1
    # Legördülő menü kezelése
    How_many_guests_in_your_group_dd.click()
    How_many_guests_in_your_group_dd.send_keys(Keys.ARROW_DOWN)
    How_many_guests_in_your_group_dd.send_keys(Keys.ENTER)
    time.sleep(5)
    next_button_p1.click()

    # page 2
    Which_date_and_time_are_dd.send_keys('2021.08.02 16:02')
    Which_time_of_day_dd.click()
    Which_time_of_day_dd.send_keys(Keys.ARROW_DOWN)
    Which_time_of_day_dd.send_keys(Keys.ENTER)
    How_many_hours_would_you_like_to_charter_for_dd.click()
    How_many_hours_would_you_like_to_charter_for_dd.send_keys(Keys.ARROW_DOWN)
    How_many_hours_would_you_like_to_charter_for_dd.send_keys(Keys.ENTER)
    time.sleep(5)
    next_button_p2.click()
    # page 3
    What_is_your_first_and_last_name_dd.send_keys('Harry Potter')
    Which_email_address_should_we_send_dd.send_keys(email)
    time.sleep(5)
    request_button_p3.click()
    time.sleep(5)


try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')
    time.sleep(2)

    # gombok
    #next_button = driver.find_element_by_class_name('next-btn next-btn1')
    next_button_p1 = driver.find_element_by_xpath('//button[@class ="next-btn next-btn1"]')
    next_button_p2 = driver.find_element_by_xpath('//button[@class ="next-btn next-btn2"]')
    request_button_p3 = driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/ul/li[4]/button')

    # mezok  (/html/body/form/div[1]/div[1]/ul/li[1]/select)
    #How_many_guests_in_your_group_dd = driver.find_element_by_xpath('//*[@class="errorTxt"]//select')
    How_many_guests_in_your_group_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[1]/ul/li[1]/select')
    Which_date_and_time_are_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/ul/li[1]/input')
    Which_time_of_day_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/ul/li[2]/select')
    How_many_hours_would_you_like_to_charter_for_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/ul/li[3]/select')
    What_is_your_first_and_last_name_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/ul/li[1]/input')
    Which_email_address_should_we_send_dd = driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/ul/li[2]/input')

    #TC1:
    test_set('abc@abc.com')
    assert driver.find_element_by_xpath('/html/body/form/h2').text == "Your message was sent successfully." \
                                                                      " Thanks! We'll be in touch as soon as we can," \
                                                                      " which is usually like lightning (Unless we're sailing or eating tacos!)."
    time.sleep(5)
    #TC2:
    test_set('abc@abc')
    # Készíts tesztesetet az e - mail cím validációjára.
    assert driver.find_element_by_xpath('/html/body/form/h2').text == "Your message was sent successfully." \
                                                                      " Thanks! We'll be in touch as soon as we can," \
                                                                      " which is usually like lightning (Unless we're sailing or eating tacos!)."

    # Az email validáció hibás, mert simán megengedi a továbblépést hiányzó domain-ű emeil cimmel
finally:
    driver.close()
