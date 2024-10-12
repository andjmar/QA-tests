from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME,"name")
    password = (By.ID,"exampleInputPassword1")
    email = (By.NAME,"email")
    chbox = (By.ID,"exampleCheck1")
    gender = (By.ID,"exampleFormControlSelect1")
    female = (By.XPATH,"//option[normalize-space()='Female']")
    male = (By.XPATH,"//option[normalize-space()='Male']")
    student = (By.XPATH,"//input[@id='inlineRadio1']")
    date = (By.XPATH,"//input[@name='bday']")
    submit = (By.CSS_SELECTOR,"input[type='submit']")
    success = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getChbox(self):
        return self.driver.find_element(*HomePage.chbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getFemale(self):
        return self.driver.find_element(*HomePage.female)

    def getMale(self):
        return self.driver.find_element(*HomePage.male)

    def getStudent(self):
        return self.driver.find_element(*HomePage.student)

    def getDate(self):
        return self.driver.find_element(*HomePage.date)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)




