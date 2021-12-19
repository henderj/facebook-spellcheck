from typing import NewType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from tkinter import Tk, getdouble

driver_loc = "./drivers/chromedriver.exe"
spellboy_url = "https://www.spellboy.com/check_spelling/"
text_box_name = "text"
first_check_button_xpath = '/html/body/section/form/fieldset/button'
copy_text_button_xpath = '//*[@id="copy-button"]'
lang_button_xpath = '/html/body/section/form/fieldset/div'
es_button_xpath = '/html/body/section/form/fieldset/div/ul/li[9]'

JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.value += txt;
  elm.dispatchEvent(new Event('change'));
  """

def get_driver():
    driver = webdriver.Chrome(driver_loc)
    driver.get(spellboy_url)
    return driver

def change_lang(driver):
    driver.find_element(By.XPATH, lang_button_xpath).click()
    driver.find_element(By.XPATH, es_button_xpath).click()

def _paste_text(driver, text):    
    text_box = driver.find_element(By.NAME, text_box_name)
    driver.execute_script(JS_ADD_TEXT_TO_INPUT, text_box, text)
    text_box.send_keys('.')
    text_box.send_keys(Keys.BACKSPACE)
    ActionChains(driver)\
        .key_down(Keys.CONTROL)\
            .send_keys(Keys.ENTER)\
                .key_up(Keys.CONTROL).perform()

def _get_textbox_text(driver):    
    copy_text_button = driver.find_element(By.XPATH,copy_text_button_xpath)
    copy_text_button.click()
    new_text = Tk().clipboard_get()
    return new_text

def put_text_into_spellboy(text:str) -> None:
    driver = get_driver()
    change_lang(driver)
    _paste_text(driver, text)
    cont = input("press any key to continue")
    new_text = _get_textbox_text(driver)
    print(new_text)
    return new_text

def test_selenium() -> None:
    driver = get_driver()
    change_lang(driver)
    _paste_text(driver, "hola aqui estoy probando esto ")
    cont = input("press any key to continue")
    new_text = _get_textbox_text(driver)
    print(new_text)
    driver.close()

if __name__ == "__main__":
    test_selenium()