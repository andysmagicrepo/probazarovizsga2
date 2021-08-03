# 2 Feladat: Film register applikáció funkcióinak automatizálása
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a sales Film register app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html](https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html) oldalról.
#
# Feladatod, hogy automatizáld az alkalmazás két funkciójának a tesztelését
# * Teszteld le, hogy betöltés után megjelennek filmek az alkalmazásban, méghozzá 24 db.
# * Teszteld le, hogy fel lehet-e venni az alábbi adatokkal egy új filmet:
#     * Film title: Black widow
#     * Release year: 2021
#     * Chronological year of events: 2020
#     * Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
#     * Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
#     * Film summary: https://www.imdb.com/title/tt3480822/
#
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `film_register.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html')
    time.sleep(5)

    # buttons
    register_button = driver.find_element_by_class_name("mostra-container-cadastro")
    save_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]')
    # fields
    movie_titles = driver.find_elements_by_xpath('//h2')
    Film_Title = driver.find_element_by_id("nomeFilme")
    #nem hasznaltak
    Release_Year = driver.find_element_by_id("anoLancamentoFilme")
    Chronological_year_of_events = driver.find_element_by_id("anoCronologiaFilme")
    Trailer_url = driver.find_element_by_id("linkTrailerFilme")
    Image_url = driver.find_element_by_id("linkImagemFilme")
    Film_Summary_url = driver.find_element_by_id("linkImdbFilme")

    # Képek számolása
    assert (len(movie_titles) == 24)

            # Új film bevitele
            # Film title: Black widow
            # Release year: 2021
            # Chronological year of events: 2020
            # Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
            # Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
            # Film summary: https://www.imdb.com/title/tt3480822/

    register_button.click()
    time.sleep(5)
    Film_Title.send_keys("Black widow")
    Release_Year.send_keys("2021")
    Chronological_year_of_events.send_keys("2020")
    Trailer_url.send_keys("https://www.youtube.com/watch?v=Fp9pNPdNwjI")
    Image_url.send_keys("https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg")
    Film_Summary_url.send_keys("https://www.imdb.com/title/tt3480822/")
    time.sleep(5)
    save_button.click()
    time.sleep(5)
    assert (len(movie_titles) == 25)

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()
