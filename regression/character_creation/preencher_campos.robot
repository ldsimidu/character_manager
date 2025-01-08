*** Settings ***

Resource        ../base.robot 

*** Test Cases ***
Preencher Todos Os Campos
    [Tags]    @creation1
    # Verificar se o arquivo existe, caso contrário, criar com o valor inicial 11
    ${FILE_EXISTS}=    Run Keyword And Return Status    File Should Exist    ${CHARACTER_ID_FILE}
    Run Keyword If    '${FILE_EXISTS}' == 'False'    Create File    ${CHARACTER_ID_FILE}    11

    # Ler o número atual do CHARACTER_ID, se o arquivo estiver vazio ou com valor inválido, usar 11
    ${CHARACTER_ID}=    Get File    ${CHARACTER_ID_FILE}
    Run Keyword If    '${CHARACTER_ID}' == ''    Set Variable    ${CHARACTER_ID}    11
    Run Keyword If    '${CHARACTER_ID}' != ''    Convert To Number    ${CHARACTER_ID}

    # Incrementar o número
    ${CHARACTER_ID}=    Evaluate    ${CHARACTER_ID}+1

    # Salvar o novo número no arquivo
    ${CHARACTER_ID_STR}=    Convert To String    ${CHARACTER_ID}
    Create File    ${CHARACTER_ID_FILE}    ${CHARACTER_ID_STR}

    ${CHARACTER_NAME}=    Set Variable    GUERREIRO ALEATORIO ${CHARACTER_ID}

    Start Process    python    app.py
    Sleep    5s
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Sleep    3s
    
    Click Element    xpath=//a[@href='/create_character']/button[@class='btn btn-success btn-lg']
    
    Sleep    3s

    # Preencher os campos do formulário
    Input Text    xpath=//input[@name="name"]                ${CHARACTER_NAME}
    Input Text    xpath=//input[@name="character_class"]     Guerreiro
    Input Text    xpath=//input[@name="level"]               1
    Input Text    xpath=//input[@name="strength"]            15
    Input Text    xpath=//input[@name="strength_modifier"]   2
    Input Text    xpath=//input[@name="dexterity"]           13
    Input Text    xpath=//input[@name="dexterity_modifier"]  1
    Input Text    xpath=//input[@name="constitution"]        14
    Input Text    xpath=//input[@name="constitution_modifier"]  2
    Input Text    xpath=//input[@name="intelligence"]        16
    Input Text    xpath=//input[@name="intelligence_modifier"]  3
    Input Text    xpath=//input[@name="wisdom"]              12
    Input Text    xpath=//input[@name="wisdom_modifier"]     1
    Input Text    xpath=//input[@name="charisma"]            10
    Input Text    xpath=//input[@name="charisma_modifier"]   0

    # Habilidades
    Input Text    xpath=//input[@name="acrobatics"]          1
    Input Text    xpath=//input[@name="animal_handling"]     -1
    Input Text    xpath=//input[@name="arcana"]              2
    Input Text    xpath=//input[@name="athletics"]           3
    Input Text    xpath=//input[@name="deception"]           1
    Input Text    xpath=//input[@name="history"]             -1
    Input Text    xpath=//input[@name="insight"]             2
    Input Text    xpath=//input[@name="intimidation"]        -1
    Input Text    xpath=//input[@name="investigation"]       3
    Input Text    xpath=//input[@name="medicine"]            -1
    Input Text    xpath=//input[@name="nature"]              2
    Input Text    xpath=//input[@name="perception"]          -1
    Input Text    xpath=//input[@name="performance"]         1
    Input Text    xpath=//input[@name="persuasion"]          -1
    Input Text    xpath=//input[@name="religion"]            2
    Input Text    xpath=//input[@name="sleight_of_hand"]     -1
    Input Text    xpath=//input[@name="stealth"]             3
    Input Text    xpath=//input[@name="survival"]            -1

    # Notas
    Input Text    xpath=//textarea[@name="notes"]            Algumas observações sobre o personagem.


    Sleep    100000000000s
    # Submeter o formulário
    Click Element    xpath=//button[@type='submit' and @class='btn btn-primary btn-lg']
    Sleep    2s
    Click Element    xpath=//a[text()='Voltar para o Índice']

    

    # Clique no link do personagem criado
    Click Link    xpath=//*[@id="character-list"]/div[${CHARACTER_ID}]/a
    
    Sleep    1000000s
    Terminate Process    app.py
