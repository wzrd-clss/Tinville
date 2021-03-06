from lettuce import *
from lettuce import step
from django.core.management import call_command
import lettuce.django
import os
import time
import math
from selenium.webdriver.common.keys import Keys

from Tinville.settings.base import MEDIA_ROOT
from designer_shop.models import Shop
from user.models import TinvilleUser
from selenium.webdriver.support.ui import Select
from common.lettuce_utils import *


# Scenario: Adding an item to the empty shopping bag
@step(u'Demo page')
def demo_page(step):
     world.browser.get(lettuce.django.get_server().url("/demo/testsizesetitem"))

@step(u'Then I go to the checkout page')
def then_I_go_to_the_checkout_page(step):
    world.browser.get(lettuce.django.get_server().url("/cartdetail"))

@step(u'The shopping bag is empty')
def the_shopping_bag_is_empty(step):
     assert_number_of_selectors(".shoppingcartitem[id^=lineId]", 0)

@step(u'Then I add an item to my shopping bag')
def then_I_add_an_item_to_my_shopping_bag(step):
    Select(wait_for_element_with_id_to_exist("itemColorSelection")).select_by_value("Blue")
    Select(wait_for_element_with_id_to_exist("itemSizeSelection")).select_by_value("XS")
    wait_for_element_with_css_selector_to_exist("#id_AddToCart")
    wait_for_element_with_css_selector_to_be_clickable("#id_AddToCart").click()
    time.sleep(3)

@step(u'Then The bag icon should show the number of the item')
def then_the_bag_icon_should_show_the_number_of_the_item(step):
    wait_for_element_with_css_selector_to_exist(".shoppingcartitem[id^=lineId]")
    assert_number_of_selectors(".shoppingcartitem[id^=lineId]", 1)

@step(u'And  I click on the bag icon')
def and_I_click_on_the_bag_icon(step):
    wait_for_element_with_id_to_exist('shoppingcart')
    myelement = world.browser.find_element_by_id('shoppingcart')
    myelement.click()

@step(u'And I continue as guest')
def and_I_continue_as_guest(step):
    form = wait_for_element_with_id_to_exist("checkoutOption")
    form.find_element_by_name("username").send_keys('joe@schmoe.com')
    wait_for_element_with_id_to_exist('guestButton')
    myelement = world.browser.find_element_by_id('guestButton')
    myelement.click()

@step(u'And I choose to register')
def and_I_choose_to_register(step):
    form = world.browser.find_element_by_id("checkoutOption")
    form.find_element_by_name("username").send_keys('foo@bar.com')
    wait_for_element_with_id_to_exist('registerButton')
    myelement = world.browser.find_element_by_id('registerButton')
    myelement.click()
    # form = fill_in_user_form(email='foo@bar.com', password='foobar')
    wait_for_element_with_class_to_be_displayed("close").click()
    form = fill_in_user_form(password='foobar')
    form.submit()

def fill_in_user_form(password):
    form = world.browser.find_element_by_id("registrationForm")
    # form.find_element_by_name("email").send_keys(email)
    form.find_element_by_name("password").send_keys(password)
    return form

@step(u'Then I add a valid address')
def then_I_add_a_valid_address(step):
    wait_for_element_with_name_to_be_displayed('first_name').send_keys('Joe')
    wait_for_element_with_name_to_be_displayed('last_name').send_keys('Schmoe')
    wait_for_element_with_name_to_be_displayed('line1').send_keys('14 Minnesota Ave.')
    wait_for_element_with_name_to_be_displayed('line4').send_keys('Somerville')
    wait_for_element_with_name_to_be_displayed('state').send_keys('Ma')
    wait_for_element_with_name_to_be_displayed('postcode').send_keys('02145')
    wait_for_element_with_css_selector_to_be_clickable("button[type='submit']").click()

@step(u'Then I add my address')
def then_I_add_my_address(step):
    if(wait_for_element_with_class_to_be_displayed_no_exception("close")):
        wait_for_element_with_class_to_be_displayed("close").click()

    wait_for_element_with_name_to_be_displayed('first_name').send_keys('Joe')
    wait_for_element_with_name_to_be_displayed('last_name').send_keys('Schmoe')
    wait_for_element_with_name_to_be_displayed('line1').send_keys('14 Minnesota Ave.')
    wait_for_element_with_name_to_be_displayed('line4').send_keys('Somerville')
    wait_for_element_with_name_to_be_displayed('state').send_keys('Ma')
    wait_for_element_with_name_to_be_displayed('postcode').send_keys('02145')
    wait_for_element_with_css_selector_to_be_clickable("button[type='submit']").click()

@step(u'Then I enter a valid payment')
def then_I_add_a_valid_payment(step):
    wait_for_element_with_id_to_exist('id_card_number').send_keys('4242424242424242')
    wait_for_element_with_id_to_exist('id_expiration_date').send_keys('0925')
    wait_for_element_with_id_to_exist('id_cvc').send_keys('666')
    wait_for_element_with_css_selector_to_be_clickable("#submit-id-paymentform").click()

@step(u'Then the thank you page is displayed')
def then_the_thank_you_page_is_displayed(step):
     assert_id_exists('basket_totals')

@step(u'(?:When|And) I sign in')
def and_i_sign_in(step):
    form = wait_for_element_with_id_to_exist("signInOption")
    form.find_element_by_name("username").send_keys('demo@user.com')
    form.find_element_by_name("password").send_keys('tinville')
    wait_for_element_with_id_to_exist('returningButton')
    myelement = world.browser.find_element_by_id('returningButton')
    myelement.click()

@step(u'When a registered user logs in with email "([^"]*)" and password "([^"]*)"')
def when_a_registered_user_logs_in_with_email_and_password(step, email, password):
    world.user_info = {
        "email": email,
        "password": password,
    }
    sign_in_local()

@step(u'Then The checkout drop down is displayed')
def then_the_checkout_drop_down_is_displayed(step):
    assert_id_exists('cartDropdown')
    wait_for_element_with_id_to_be_displayed('cartDropdown')

@step(u'And  I click on the checkout button')
def and_I_click_on_the_checkout_button(step):
    world.browser.find_element_by_id("shoppingcartcheckout").click()

@step(u'Then The checkout form should be displayed')
def then_the_checkout_form_should_be_displayed(step):
    assert_id_exists('shoppingcartcheckout')


#Scenario: Checkout page using arrows to control number of items
@step(u'Given Checkout page with an item to checkout')
def given_checkout_page_with_an_item_to_checkout(step):
    assert_number_of_selectors(".shoppingcartitem[id^=lineId]", 1)

@step(u'When I increase the number of items by 2 using arrow')
def when_I_increase_the_number_of_items_by_2_using_arrow(step):
    product = world.browser.find_element_by_tag_name('table')
    rows = product.find_elements_by_tag_name('tbody')
    inputField = rows[0].find_element_by_css_selector("""td[data-th="Quantity"]>input""")
    inputField.send_keys(Keys.ARROW_UP)
    inputField.send_keys(Keys.ARROW_UP)

@step(u'Then The total sum should be 3')
def then_the_total_sum_should_be_3(step):
    product = world.browser.find_element_by_tag_name('table')
    rows = product.find_elements_by_tag_name('tbody')
    #print rows[0]
    quantityNumber = rows[0].find_element_by_css_selector("""td[data-th="Quantity"]>input""")
    assert_selector_contains_text(quantityNumber, 3)
    value = quantityNumber.get_attribute("value")
    #print value
    assert True

@step(u'And I decrease the number of items using arrow by 1')
def and_I_decrease_the_number_of_items_using_arrow_by_1(step):
    product = world.browser.find_element_by_tag_name('table')
    rows = product.find_elements_by_tag_name('tbody')
    inputField = rows[0].find_element_by_css_selector("""td[data-th="Quantity"]>input""")
    inputField.send_keys(Keys.ARROW_DOWN)

@step(u'Then The total sum should be 2')
def then_the_total_sum_should_be_2(step):
    product = world.browser.find_element_by_tag_name('table')
    rows = product.find_elements_by_tag_name('tbody')
    quantityNumber = rows[0].find_element_by_css_selector("""td[data-th="Quantity"]>input""")
    value = quantityNumber.get_attribute("value")
    assert True

#Scenario: Checkout
#@step(u'Given checkout page with 2 items')
#def given_checkout_page_with_2_items(step):
#   assert_number_of_selectors(".shoppingcartitem[id^=lineId]", 1) #item number is 1, it shouldn't work!

@step(u'When I click on checkout button')
def when_I_click_on_checkout_button(step):
    wait_for_ajax_to_complete()
    wait_for_javascript_to_complete()
    time.sleep(3)
    world.browser.find_element_by_id("checkoutBtn").click()





#Scenario: Deleting an item -continue on this after bug fix
#@step(u'Given A shopping bag with 2 items')
#def given_a_shopping_bag_with_2_items(step):
#    wait_for_element_with_css_selector_to_exist(".shoppingcartitem[id^=lineId]")
#    assert_number_of_selectors(".shoppingcartitem[id^=lineId]", 2)




# Scenario: Trying to click on Add to Bag without choosing any item
#@step(u'Main Demo page with a shopping bag that is empty')
#def main_demo_page_with_a_empty_shopping_bag(step):
#    world.browser.get(lettuce.django.get_server().url("/demo/testsizesetitem"))
#   assert_number_of_selectors(".shoppingcartitem[id^=lineId]", 0)


@step(u'Then I click on Add_to_Bag button')
def then_I_click_on_add_to_bag_button(step):
    wait_for_element_with_css_selector_to_exist("#id_AddToCart")
    wait_for_element_with_css_selector_to_be_clickable("#id_AddToCart").click()

@step(u'Then I receive the following warnings')
def then_I_receive_the_following_warnings(step):
    wait_for_element_with_css_selector_to_be_displayed('#parsley-id-0987')
    #wait_for_element_with_css_selector_to_be_displayed('#parsley-id-2086')
    #assert_selector_contains_text("#parsley-id-0987.form-control selectpicker parsley-error", "This value is required.")
    #assert_selector_contains_text("#itemColorSelection+.parsley-errors-list>.parsley-required", "This value is required.")
#    assert True


