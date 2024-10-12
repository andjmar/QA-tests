from selenium.webdriver.common.by import By

class GreenKart:
    def __init__(self, driver):
        self.driver = driver

    input = (By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']")
    btn = (By.XPATH,"(//button[@type='button'][normalize-space()='ADD TO CART'])")
    cart= (By.XPATH,"//img[@alt='Cart']")
    checkout = (By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']")
    promocode= (By.CSS_SELECTOR,"input.promoCode")
    promobtn= (By.CSS_SELECTOR,".promoBtn")
    ordbtn= (By.XPATH,"//button[normalize-space()='Place Order']")
    country= (By.XPATH,"//div[@class='wrapperTwo']//div//select")
    checkbox= (By.XPATH,"//input[@type='checkbox']")
    purchasebtn= (By.XPATH,"//button[normalize-space()='Proceed']")
    promocodeText = (By.XPATH,"//span[@class='promoInfo']")


    def getPromocodeText(self):
        return self.driver.find_element(*GreenKart.promocodeText)

    def getInput(self):
        return self.driver.find_element(*GreenKart.input)

    def getBtn(self):
        return self.driver.find_elements(*GreenKart.btn)

    def getCart(self):
        return self.driver.find_element(*GreenKart.cart)

    def getCheckout(self):
        return self.driver.find_element(*GreenKart.checkout)

    def getPromocode(self):
        return self.driver.find_element(*GreenKart.promocode)

    def getPromobtn(self):
        return self.driver.find_element(*GreenKart.promobtn)

    def getOrdbtn(self):
        return self.driver.find_element(*GreenKart.ordbtn)

    def getCountry(self):
        return self.driver.find_element(*GreenKart.country)

    def getCheckbox(self):
        return self.driver.find_element(*GreenKart.checkbox)

    def getPurchasebtn(self):
        return self.driver.find_element(*GreenKart.purchasebtn)

