
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """Function trnalsates english top french
    """
    french = language_translator.translate(
        text = english_text,
        model_id= 'en-fr').get_result()
    return french.get("translations")[0].get("translation")


def frenchToEnglish(french_text):
    """Function trnalsates english top french
    """
    english = language_translator.translate(
        text = french_text,
        model_id= 'fr-en').get_result()
    return english.get("translations")[0].get("translation")