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

Register With Too Short Username And Valid Password
    Set Username  kk
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registering Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Credentials
    Registering Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Credentials
    Registering Should Fail With Message  Password confirmation did not match

*** Keywords ***
Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
