import json
import os

# Normally you should not import ANYTHING from Django directly into your settings,
# but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

secrets_file = os.path.join(os.path.dirname(__file__), 'secrets.json')
with open(secrets_file) as f:
    module_secrets = json.load(f)


def get_secret(setting, secrets=module_secrets):
    """
    Get the secret variable or return explicit exception
    """

    try:
        return secrets[setting]
    except Exception:
        error_msg = f'The secret variable {setting} is not set'
        print(error_msg)
        raise ImproperlyConfigured(error_msg)
