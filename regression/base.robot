*** Settings ***
Library           SeleniumLibrary
Library           Process
Library           BuiltIn
Library           OperatingSystem

Library           regressionLibrary.py

*** Variables ***
${URL}            http://127.0.0.1:5000
${CHARACTER_ID_FILE}    character_id.txt

