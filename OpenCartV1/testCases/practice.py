# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
#
# chrome_ops = webdriver.ChromeOptions()
# chrome_ops.add_argument("--disable-notifications")
# chrome_service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service =chrome_service,options=chrome_ops)
# print("Chrome Browser Started Successfully")
# # driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
# wait = WebDriverWait(driver,20,ignored_exceptions=[Exception],poll_frequency=2)
#
# Radiobtn = "input-newsletter-yes"
# radio_btn = wait.until(EC.element_to_be_clickable((By.XPATH,Radiobtn)))
# print(radio_btn.is_displayed())
# # radio_btn.clear()
# # radio_btn.click()
# # time.sleep(5)
#
#
#
# # print(Radiobtn.is_displayed())
# # print(Radiobtn.is_selected())

