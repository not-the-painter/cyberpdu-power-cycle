
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
CYCLES = 100

def select_outlets():
        outlet6 = driver.find_element(by=By.NAME, value="ActOut6")
        outlet6.click()
        outlet7 = driver.find_element(by=By.NAME, value="ActOut7")
        outlet7.click()
        outlet8 = driver.find_element(by=By.NAME, value="ActOut8")
        outlet8.click()
        sleep(3)


def cyberpdu():    

    driver.get("http://172.16.10.247") # replace this with the IP of your Cyber PDU

    sleep(1)

    # find username and password fields
    username = driver.find_element(by=By.ID, value="username")
    password = driver.find_element(by=By.ID, value="password")
    login = driver.find_element(by=By.ID, value="login_sub")

    # fill them in and log in
    username.clear()
    username.send_keys("cyber")
    password.clear()
    password.send_keys("cyber")
    login.click()

    # wait for summary.html to load
    sleep(5)

    # navigate to outlets.html
    # first find the PDU link
    pdu_link = driver.find_element(by=By.LINK_TEXT, value="PDU")
    pdu_link.click()
    sleep(2)

    # then find the 'Outlet Action' link
    outlet_action = driver.find_element(by=By.LINK_TEXT, value="Outlet Action")
    outlet_action.click()
    sleep(2)

    # and finally find the 'Outlets' link
    outlets_link = driver.find_element(by=By.LINK_TEXT, value="Control")
    outlets_link.click()
    sleep(2)

    #---------------------------------------------------------------------------------------------
    # POWER CYCLE LOOP

    i = 0
    while i < CYCLES:
        # turn the outlets off
        select_outlets()

        action_select = Select(driver.find_element(by=By.NAME, value="ActionSel"))
        action_select.select_by_visible_text("Turn Off")
        next_btn = driver.find_element(by=By.NAME, value="action")
        next_btn.click()
        sleep(3)
        apply_btn = driver.find_element(by=By.NAME, value="action")
        apply_btn.click()
        sleep(15)

        # turn the outlets back on
        select_outlets()
        
        action_select = Select(driver.find_element(by=By.NAME, value="ActionSel"))
        action_select.select_by_visible_text("Turn On")
        next_btn = driver.find_element(by=By.NAME, value="action")
        next_btn.click()
        sleep(3)
        apply_btn = driver.find_element(by=By.NAME, value="action")
        apply_btn.click()
        sleep(15)

        i += 1
        print(f"Completed power cycles: {i}")

    # END LOOP
    #----------------------------------------------------------------------------------------------

    #log out and close browser when done
    logout = driver.find_element(by=By.LINK_TEXT, value="Logout")
    logout.click()

    sleep(2)
    driver.quit()


cyberpdu()
