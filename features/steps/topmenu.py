# pylint: disable=function-redefined
# pylint: disable=no-name-in-module
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('que entrei no site dos "Correios"')
def step_impl(context):
    context.driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php?t")


@when('digitar "{cep}" na barra de busca')
def step_impl(context, cep):
    context.driver.find_element(By.XPATH, '//*[@id="endereco"]').send_keys('69005-040')
    sleep(2)

@then('clicar em "buscar" na barra de busca')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()
    sleep(5)

@given('vou entrar no site "Correios"')
def step_impl(context):
    context.driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php?t")
    sleep(5)

@when('eu digitar "{Palavra}" na barra de busca')
def step_impl(context,Palavra):
    context.driver.find_element(By.XPATH, '//*[@id="endereco"]').send_keys('Lojas Bemol')
    sleep(2)

@then('e clicar em "buscar" na barra de busca')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()
    sleep(5)