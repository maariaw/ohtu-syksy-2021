*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test Teardown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Form
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  kk
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Form
    Registering Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Form
    Registering Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Form
    Registering Should Fail With Message  Password confirmation did not match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Form
    Registering Should Succeed
    Click Element  link:Continue to main page
    Click Button  Logout
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kk
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Form
    Registering Should Fail With Message  Username is too short
    Click Element  link:Login
    Set Username  kk
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Form
    Click Button  Register

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
