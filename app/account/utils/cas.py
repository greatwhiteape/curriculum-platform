import logging

from typing import Dict

from django.conf import settings
from django.contrib.auth import get_user_model
from memoize import memoize
import requests

TIMEOUT_SECONDS = 10

logger = logging.getLogger(__name__)


@memoize()
def headers() -> Dict[str, str]:
    """ Headers for quering CAS API """
    try:
        return {"Authorization": f"Token {settings.CAS_API_TOKEN}"}
    except AttributeError as e:
        logger.error("Unable to get CAS token")
        raise e


session = requests.session()
session.headers.update(headers())
session.timeout = TIMEOUT_SECONDS


class Error404(Exception):
    pass


def user_data(username: str):
    """ Retrieve User data from CAS """
    url = f"https://cas.gmri.org/api/cas/v1/users/?username={username}"

    response = session.get(url)

    if response.status_code != 200:
        raise Error404
    return response.json()[0]


def update_user(username: str):
    """ Update a user's information """
    UserModel = get_user_model()

    user, _ = UserModel.objects.get_or_create(username=username)

    user_json = user_data(username)

    user.last_name = user_json["last_name"]
    user.first_name = user_json["first_name"]
    user.email = username
    user.save()


def cas_callback(tree):
    username = tree[0][0].text

    try:
        update_user(username)
    except Exception as e:
        logger.error(f"Error updating user {username}: {type(e)} - {e}")
