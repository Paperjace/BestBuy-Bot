from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import info
from selenium_driver import SeleniumDriver

from plyer import notification

import time

def notify() :
    notification.notify (
        title="!!!!!!!!",
        message="MANUAL INPUT REQUIRED",
        app_name="RTX BOT",
        timeout=10
    )


selenium_object = SeleniumDriver()
selenium_object.login(info.email, info.password)

driver = selenium_object.driver
driver.get(info.RTXLINK1)

isComplete = False

# notify()
# input("Press Enter to continue...")

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        # add to cart
        atcBtn.click()

        time.sleep(3)

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.com/cart")

        # Find and click the delivery button instead of Pickup
        deliveryBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id^="fulfillment-shipping"]'))
        )

        deliveryBtn.click()
        time.sleep(3)
        
        dropdownElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'select[id^="quantity-"]'))
        )
        dropdown = Select(dropdownElement)
        
        if dropdown.first_selected_option.text != '1':
            dropdown.select_by_visible_text('1')
            # Wait for page reload when changing quantity
            time.sleep(3)
        
        print("Successfully added to cart - beginning check out")

        checkoutBtn = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))
        )
        checkoutBtn.click()
        # continuePaymentInfo = WebDriverWait(driver, 10).until(
        #      EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[3]/div[1]/section/div[2]/section/div/div/button"))
        # )
        # continuePaymentInfo.click()
        # print("Successfully added to cart - beginning check out")

        # fill in card cvv
        cvvField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cvv"))
        )
        cvvField.send_keys(info.cvv)
        
        print("Attempting to place order")

        # place order
        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/main/div[3]/div[1]/div[6]/div/div/div/div/div[2]/button"))
        )
        # placeOrderBtn.click()
        print("Is place order button found?")
        print(placeOrderBtn.is_displayed())

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".thank-you-enhancement__info"))
        )

        isComplete = True
    except Exception as e:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(info.RTXLINK1)
        print(f"Error - {e}")
        notify()
        input("Press Enter to continue...")
        continue

print("Order successfully placed")



