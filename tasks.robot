*** Settings ***
Library     RPA.Robocorp.Vault
Library     ZendeskLibrary

*** Tasks ***
Create Zendesk Ticket
    Log To Console    Create Zendesk Creds
    ${zendesk}=    Get Secret    Zendesk
    ${client}=    Login Zendesk    ${zendesk}[email]    ${zendesk}[token]    ${zendesk}[subdomain]
    
    Log To Console    Creating a ticket in Zendesk
    ${result}=    Create Ticket
    ...    ${client}
    ...    Subject is something
    ...    Description is much more than that
    ...    tommi@robocorp.com
    ...    Tommi Holmgren

    Log To Console    ${result}
