*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  vv  ville123
    Output Should Contain  Username is too short

Register With Username That Contains Other Than Letters And Valid Password
    Input Credentials  ville3  ville123
    Output Should Contain  Username needs to consist of lowercase letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  ville  ville12
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  villeVILLE
    Output Should Contain  Password cannot consist of letters only

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
