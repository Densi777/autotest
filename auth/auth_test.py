from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import gui
import time
import datetime
import os

def auth_test():
    os.startfile(r'D:\Project\000Autotest000\Winium.Desktop.Driver.exe')
    wrong_logins_passwords = ['nkr', 'лкт',	r'!@#$%^&*()_+-=|<>":;/\№{}[]`~', '1234567890', 'krn', 'KRN', 'P@ssw0rd']
    today = datetime.datetime.today()
    driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={"app": r"D:\Project\stadium\src\Stadiums\bin\Debug\Stadiums.exe"})
    time.sleep(2)
    log = open(r'C:\Users\kursky.d\Documents\dev\test\auth\log.txt', 'w')

    #right_login       wrong_password
    for pswrd in wrong_logins_passwords:
        driver.find_element_by_class_name('WPF_PanelAutentification').click()
        driver.find_element_by_id('loginTextTB').send_keys('krn')
        driver.find_element_by_id('passwordBox').send_keys(pswrd)
        pyautogui.press('enter')
        time.sleep(1)
        if driver.find_element_by_id('userLogged').is_displayed():
            log.write('%s :: login: "krn", password: %s autentificated\n' % (today.strftime("%Y.%m.%d - %H:%M:%S"), pswrd))
            driver.find_element_by_class_name('WPF_PanelAutentification').click()
            driver.find_element_by_id('OKButton').click()
        elif driver.find_element_by_id('YesButton_HighWIdth').is_displayed():
            driver.find_element_by_id('OKButton').click()

    log.close()
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('ctrl', 'c')

test_btn = gui.window.auth_test_btn
test_btn.clicked(auth_test())
