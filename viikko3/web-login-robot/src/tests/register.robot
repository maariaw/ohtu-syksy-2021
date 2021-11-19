*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  Reset Application
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registering Should Succeed

*** Keywords ***
Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registering Should Succeed
    Welcome Page Should Be Open
