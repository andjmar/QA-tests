import time

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from repo.utilities.BaseClass import BaseClass
import time


scenarios('../features/examples.feature')

@given('I am on the home page')
def i_am_on_the_home_page(driver,homePage):
    url = 'https://rahulshettyacademy.com/angularpractice/'
    BaseClass.getLogger().info("Check if the URL is correct")
    driver.get(url)
    BaseClass.verifyUrlPresence(driver, url)
    assert driver.current_url == url, f"URL {driver.current_url} does not match {url}"
    assert driver.title == "ProtoCommerce", f"Title {driver.title} does not match ProtoCommerce"
    #end

@when('I enter the name, email and password')
def i_enter_the_name_email_and_password(driver, homePage):
    homePage.getName().send_keys("Andjela")
    homePage.getEmail().send_keys("andjelamarinkovic@gmail.com")
    homePage.getPassword().send_keys("pass1234")

@when('I click on the checkbox')
def i_click_on_the_checkbox(driver, homePage):
    homePage.getChbox().click()

@when('I select option Female and Student')
def i_select_female_and_student(driver, homePage):
    homePage.getGender().click()
    homePage.getFemale().click()
    homePage.getStudent().click()

@when('I enter the date')
def i_enter_the_date(driver, homePage):
    homePage.getDate().send_keys("01/01/2001")


@then('I click on the submit button and check the success message')
def i_click_on_the_submit(driver, homePage):
    homePage.getSubmit().click()
    BaseClass.verifyVisibilityOfElement(driver, homePage.success)
    assert homePage.getSuccess().is_displayed(), "Success message is not displayed"
    time.sleep(5)


@given('I am on the GreenKart page')
def i_am_on_the_greenkart_page(driver, greenKart):
    url = 'https://rahulshettyacademy.com/seleniumPractise/#/'
    BaseClass.getLogger().info("Check if the URL is correct")
    driver.get(url)
    BaseClass.verifyUrlPresence(driver, url)
    assert driver.current_url == url, f"URL {driver.current_url} does not match {url}"
    assert driver.title == "GreenKart - veg and fruits kart", f"Title {driver.title} does not match GreenKart"

@when('I search for the product')
def i_search_for_the_product(driver, greenKart):
    greenKart.getInput().send_keys("ber")
    time.sleep(1)

@when('I add the products to the cart')
def i_add_the(driver, greenKart):
    for product in greenKart.getBtn():
        product.click()
    greenKart.getCart().click()
    greenKart.getCheckout().click()

@when('I enter the promo code')
def i_enter_the(driver, greenKart):
    greenKart.getPromocode().send_keys("rahulshettyacademy")
    greenKart.getPromobtn().click()
    BaseClass.verifyVisibilityOfElement(driver, greenKart.promocodeText)
    assert greenKart.getPromocodeText().is_displayed(), "Promo code text is not displayed"
    greenKart.getOrdbtn().click()

@then('I select the country, check the checkbox and click on the purchase button')
def i_select_the_country(driver, greenKart):
    greenKart.getCountry().click()
    greenKart.getCountry().send_keys("Serbia")
    greenKart.getCheckbox().click()
    greenKart.getPurchasebtn().click()

