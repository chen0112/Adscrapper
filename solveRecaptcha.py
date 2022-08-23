import sys
import os
from twocaptcha import TwoCaptcha


def solverecaptcha(sitekey, url):

    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


    api_key = os.getenv('APIKEY_@CAPTCHA', '5bc5a1c6286d60475e0eeeb84b4c6967')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey = sitekey,
            url = url
        )

    except Exception as e:
        print(e)

    else:
        return result

