*** Settings ***
Library     RPA.Robocorp.Vault
Library     ZendeskLibrary
Task Setup    Authorize Zendesk

*** Tasks ***
Create Zendesk Ticket
    Log To Console    Creating a ticket in Zendesk
    ${result}=    Create Ticket
    ...    Subject is something nr 2
    ...    Description is much more than that
    ...    tommi+demo1@robocorp.com
    ...    Tommi Demo

    Log To Console    ${result}

*** Keywords ***
Authorize Zendesk
    Log To Console    Create Zendesk Creds
    ${secrets}=    Get Secret    Zendesk
    Auth With Token    ${secrets}[email]    ${secrets}[token]    ${secrets}[subdomain]
