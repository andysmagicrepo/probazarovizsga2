# 3 Feladat: Guess the number automatizálása
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Guess the number app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html](https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel az app funkcionalitását tesztelését.
#
# * Egy tesztet kell írnod ami addig találgat a megadott intervallumon belül amíg ki nem találja a helyes számot.
# Nem jár plusz pont azért ha úgy automatizálsz, hogy minnél optimálisabban és gyosabban találja ki a helyes számot a program
#
# * Amikor megvan a helyes szám, ellenőrizd le, hogy a szükséges lépések száma mit az aplikáció kijelez egyezik-e a saját belső számlálóddal.
#
# * Teszteld le, hogy az applikáció helyesen kezeli az intervallumon kívüli találgatásokat. Az applikéció -19 vagy 255 értéknél nem szabad, hogy összeomoljon. Azt kell kiírnia, hogy alá vagy fölé találtál-e.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `guess_the_number.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html')
    time.sleep(2)

    # * Egy tesztet kell írnod ami addig találgat a megadott intervallumon belül amíg ki nem találja a helyes számot.
    # Nem jár plusz pont azért ha úgy automatizálsz, hogy minnél optimálisabban és gyosabban találja ki a helyes számot a program

    # * Amikor megvan a helyes szám, ellenőrizd le, hogy a szükséges lépések száma mit az aplikáció kijelez egyezik-e a saját belső számlálóddal.
    #
    # * Teszteld le, hogy az applikáció helyesen kezeli az intervallumon kívüli találgatásokat. Az applikéció -19 vagy 255 értéknél nem szabad, hogy összeomoljon. Azt kell kiírnia, hogy alá vagy fölé találtál-e.
    #
    # Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).

    # gombok
    #restart_button = driver.find_element_by_class_name('btn btn-warning btn-sm pull-right pull-down')
    restart_button = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/button')
    guess_button = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
    #guess_button = driver.find_element_by_class_name('btn btn-primary')

    # mezok
    # How_many_guests_in_your_group_dd = driver.find_element_by_xpath('//*[@class="errorTxt"]//select')
    guess_input = driver.find_element_by_xpath('/html/body/div/div[2]/input')
    #guess_input = driver.find_element_by_class_name(form-control ng-valid ng-touched ng-not-empty ng-dirty ng-valid-number')
    guess_number_out = driver.find_element_by_xpath('/html/body/div/div[3]/p')
    #guess_number_out = driver.find_element_by_class_name('text - info')
    guess_higher_out = driver.find_element_by_xpath('/html/body/div/p[4]')
    #guess_higher_out = driver.find_element_by_class_name('alert alert-warning')

    # TC1:

    for i in range(99):
        guess_number_out.sendkeys(i)
    time.sleep(5)

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
