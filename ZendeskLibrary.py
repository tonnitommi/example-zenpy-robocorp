from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
from zenpy.lib.api_objects import User

class ZendeskLibrary:

    def __init__(self):
        return

    def auth_with_token(self, email, token, subdomain):
        creds = {
            "email" : email,
            "token" : token,
            "subdomain": subdomain
        }
        self.zenpy = Zenpy(**creds) 

    def create_ticket(self, subject, description, submitter_email, submitter_name):

        # 1 create/update the user
        user = User(email=submitter_email, name=submitter_name)

        try:
            result = self.zenpy.users.create_or_update(user)
        except Exception as e:
            print(f"User creation/update failed: {e}")
            return e

        # 2 create the ticket
        ticket = Ticket(
            subject=subject, 
            description=description,
            requester_id=result.id)

        try:
            self.zenpy.tickets.create(ticket)
        except Exception as e:
            print(f"Ticket creation failed: {e}")
            return e

        return None