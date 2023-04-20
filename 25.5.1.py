import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

webdriver_path = "/D:/chromedriver"
selenium = webdriver.Chrome(executable_path=webdriver_path)

def test_petfriends():
    # Set implicitly wait to 10 seconds
    selenium.implicitly_wait(10)

    # Open PetFriends base page:
    selenium.get("https://petfriends.skillfactory.ru/")

    # click on the new user button
    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("FIXXIII@yandex.ru")

    # add password
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("Shalaur131313")

    # click submit button
    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    # Wait until the page with pets is loaded
    pets_page_loaded = WebDriverWait(selenium, 10).until(EC.url_to_be("https://petfriends.skillfactory.ru/all_pets"))

    if pets_page_loaded:
        # Wait until at least one pet card is visible
        pet_card_visible = WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='all_my_pets']/div[1]")))

        if pet_card_visible:
            # Wait until the pet's name is visible
            pet_name_visible = WebDriverWait(selenium, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='all_my_pets']/div[1]//h4")))

            # Wait until the pet's age is visible
            pet_age_visible = WebDriverWait(selenium, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='all_my_pets']/div[1]//p[1]")))

            # Wait until the pet's photo is visible
            pet_photo_visible = WebDriverWait(selenium, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='all_my_pets']/div[1]//img")))

            # Make the screenshot of browser window:
            selenium.save_screenshot('result_petfriends.png')
        else:
            raise Exception("No pet cards are visible")
    else:
        raise Exception("login error")

test_petfriends()
selenium.quit()
