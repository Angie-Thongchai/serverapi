from google.auth.transport import requests
from google.oauth2 import id_token

class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """validate metod Queries the google OATH2 api to fetch the user info"""

        try: 
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request()
            )

            if 'accounts.google.com' in idinfo['iss']:
                return idinfo
        
        except:
            return 'the token is ether invalid or has expired'