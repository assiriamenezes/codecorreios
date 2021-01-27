
Feature: Buscar cep

Scenario Outline: Buscar CEP da bemol

    Given que entrei no site dos "Correios"
    When digitar "<cep>" na barra de busca
    Then clicar em "buscar" na barra de busca

Examples:
    |    cep   | 
    | 69005-040|

Scenario Outline: Buscar por palavra
    Given vou entrar no site "Correios"
    When eu digitar "<Palavra>" na barra de busca
    Then e clicar em "buscar" na barra de busca

Examples:
    |   Palavra    |
    | Lojas Bemol  |