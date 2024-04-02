from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_body'], body=data['email_subject'], to=[data['to_email']]
        )
        email.send