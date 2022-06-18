from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket

def login_zendesk(email, token, subdomain):
    creds = {
        "email" : email,
        "token" : token,
        "subdomain": subdomain
    }
    return Zenpy(**creds)

def create_ticket(self, subject, description):

    ticket = Ticket(
        subject=subject, 
        description=description)

    try:
        self.tickets.create(ticket)
    except Exception as e:
        print(f"Ticket creation failed: {e}")

    return