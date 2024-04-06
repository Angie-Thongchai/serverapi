from django.core.mail import EmailMessage
import threading

class EmailThead(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_body'], body=data['email_subject'], to=[data['to_email']]
        )
        EmailThead(email).start()