import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_argument("--disable-web-security")
#chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works # ChromeDriverManager().install()
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(15)
browser.create_options()
browser.maximize_window()
start_time = time.time()
browser.get('https://www.adidas.com/us/ultraboost-4.0-dna-shoes/FY9120.html')

# browser.find_elements_by_css_selector("img[alt=\
# close button]")\
# .click()

browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div[2]/div[2]/section/div[1]/div[2]/button[14]").click()

actions = ActionChains(browser)

add_to_cart = browser.find_element_by_xpath("//button[@title='Add To Bag']")

actions.move_to_element(add_to_cart).perform()
add_to_cart.click()

browser.find_element_by_xpath("//a[@href='/us/delivery']").click()

browser.find_element_by_id("shippingAddress-firstName").send_keys('First')
browser.find_element_by_id("shippingAddress-lastName").send_keys('Last')
browser.find_element_by_id("inline-search-input").send_keys('Address')

browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/div[2]/div/div[3]/div[2]/div/div[3]/a/span").click()

browser.find_element_by_id("shippingAddress-address1").send_keys('Address')
# browser.find_element_by_id("shippingAddress-address2").send_keys('Apt 151')
browser.find_element_by_id("shippingAddress-city").send_keys('City')
browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/form/div/div/div[6]/span/div[1]/div[1]/button").click()
browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/form/div/div/div[6]/span/div[1]/div[1]/div/ul/li[24]/button").click()
browser.find_element_by_id("shippingAddress-zipcode").send_keys('Zip')


browser.find_element_by_id("shippingAddress-emailAddress").send_keys('email')
browser.find_element_by_id("shippingAddress-phoneNumber").send_keys('phone')

browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/div[4]/div/div/label/input").click()

browser.find_element_by_id("billingAddress-firstName").send_keys('First')
browser.find_element_by_id("billingAddress-lastName").send_keys('Last')

# browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/div[2]/div/div[3]/div[2]/div/div[3]/a/span").click()

browser.find_element_by_id("billingAddress-address1").send_keys('Address')
# browser.find_element_by_id("shippingAddress-address2").send_keys('Apt 151')
browser.find_element_by_id("billingAddress-city").send_keys('City')
browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/form[2]/div/div/div[7]/span/div[1]/div[1]/button").click()
browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/form[2]/div/div/div[7]/span/div[1]/div[1]/div/ul/li[50]/button").click()

# browser.find_element_by_xpath("//html").click()
# browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/form/div/div/div[6]/span/div[1]/div[1]/button").click()

browser.find_element_by_id("billingAddress-zipcode").send_keys('Zip')
browser.find_element_by_id("billingAddress-phoneNumber").send_keys('Phone')


browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/div[6]/button").click()

#Normal PAYMENT INFO STUFF (When Paying From Adidas.com)
# browser.switch_to.frame(browser.find_element_by_xpath("//iframe[@name='card.number']"))
# browser.find_element_by_xpath("/html/body/form/input[1]").send_keys('number')
# browser.switch_to.default_content()
# browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/main/div[2]/div[1]/div[2]/div/div/div/form/div[4]/div/input").send_keys('exp')
# browser.switch_to.frame(browser.find_element_by_xpath("//iframe[@name='card.cvv']"))
# browser.find_element_by_xpath("/html/body/form/input").send_keys('cvv')
# browser.switch_to.default_content()

browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/div[2]/div[2]/div[1]/div[1]/label/span").click()

browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div/div/div[2]/div/main/button").click()

# time.sleep(15)

#PAYPAL STUFF (When Navigating From Adidas.com)

browser.find_element_by_xpath("//*[@id='acceptAllButton']").click()

browser.find_element_by_xpath("//*[@id='email']").send_keys('email')

browser.find_element_by_xpath("//*[@id='btnNext']").click()

browser.find_element_by_xpath("//*[@id='password']").send_keys('password')

browser.find_element_by_xpath("//*[@id='btnLogin']").click()

browser.find_element_by_xpath("//*[@id='payment-submit-btn']").click()



# browser.find_element_by_xpath("//a[@href='https://www.nike.com/us/en/cart']").click()
# time.sleep(1)

# try:
#     browser.find_element_by_class_name("css-runnyg").click()
# except NoSuchElementException:
#     print('not there')
#     pass

# browser.find_element_by_xpath("//button[@data-automation='guest-checkout-button']").click()

# browser.find_element_by_xpath("//input[@type='email']").send_keys('email@gmail.com')

# password = browser.find_element_by_xpath("//input[@type='password']").send_keys('')

# browser.find_element_by_xpath("//input[@type='button']").click()

# browser.find_element_by_xpath("//input[@value='MEMBER CHECKOUT']").click()

# try:
#     browser.find_element_by_xpath("//button[@class='ncss-brand pt2-sm pr5-sm pb2-sm pl5-sm ncss-btn-black error-code-btn u-uppercase u-full-width pb3-sm pt3-sm pt2-lg pb2-lg']").click()
# except NoSuchElementException:
#     pass

# browser.find_element_by_xpath("//button[@class='js-next-step continuePaymentBtn mod-ncss-btn ncss-btn-accent ncss-brand mod-button-width pt3-sm prl5-sm pb3-sm pt2-lg pb2-lg u-md-ib u-uppercase u-rounded fs14-sm']").click()
# browser.find_element_by_class_name("js-next-step").click()


# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# browser.switch_to.frame(browser.find_element_by_xpath("//iframe[@class='credit-card-iframe-cvv mt1 u-full-width']"))
# browser.switch_to.frame(browser.find_element_by_class_name("credit-card-iframe"))
# browser.find_element_by_id("cvNumber").send_keys('777')
# browser.switch_to.default_content()

# browser.find_element_by_xpath("//button[@data-qa='save-button']").click()

# browser.find_element_by_xpath("//button[text()='Submit Order']]").click()
# time.sleep(1)

print("--- %s seconds ---" % (time.time() - start_time))
# size_selector = browser.find_element_by_xpath("//label[@for='ProductDetails_radio_size_120']").click()
# time.sleep(1)
# browser.find_element_by_class_name("ProductDetails-form__action").click()
# time.sleep(5)

# browser.quit()

# $x("//img[@alt=\"Nike Kyrie 7 - Men's\"]")


"""
<input id="7a301d3b-6c80-45e0-8afd-7a97e5913916" type="email" placeholder="Email address" value="" name="emailAddress" data-componentname="emailAddress" autocomplete="email" autocorrect="off" autocapitalize="off" spellcheck="false">
<input id="eaa32ddc-50b9-4a4c-b192-ea06b514efeb" type="password" placeholder="Password" value="" name="password" data-componentname="password" autocomplete="current-password" autocorrect="off" autocapitalize="off" spellcheck="false">
<input id="6f5e0cd7-0ae7-4973-8746-29ec5b96c8f3" type="button" value="SIGN IN">
<iframe sandbox="allow-scripts allow-same-origin" title="creditCardIframeForm" src="https://paymentcc.nike.com/services/cvv?id=b587165e-ab4d-4e95-a1d0-ceae3fa94359&amp;c=&amp;lf=" frameborder="0" scrolling="no" class="credit-card-iframe mt1 u-full-width fs-block"></iframe>
<input type="tel" id="cvNumber" tabindex="1" data-shortname="cvv" class="cc-input ncss-input pt2-sm pr4-sm pb2-sm pl4-sm u-align-center" "cvv"="" autocomplete="off" autocorrect="off" value="" maxlength="4">
<button type="button" class="ncss-btn-primary-dark selectable" data-qa="save-button">Save &amp; Continue</button>
<button type="button" class="ncss-btn-primary-dark selectable" data-qa="save-button">Submit Order</button>
"""