import json
import logging
import re


SENSITIVE_KEYS = ["access_token", "refresh_token", "password"]


def clean_dict_keys(json_dict: dict | list):
    """
    cleans sensitive keys from json type object
    """
    if type(json_dict) == dict:
        for key in json_dict:
            if key in SENSITIVE_KEYS:
                json_dict[key] = "****"
            clean_dict_keys(json_dict[key])
    elif type(json_dict) == list:
        for val in json_dict:
            clean_dict_keys(val)


class SecurityLoggingFilter(logging.Filter):
    """
    logging filter to redact tokens, keys and passwords
    """

    def filter(self, record):
        msg = record.getMessage()
        try:
            data = json.load(msg)
            for key in SENSITIVE_KEYS:
                if key in data:
                    data[key] = "****"
            record.msg = json.dumps(data)
        except Exception:
            # if json parsing fails - then we blank out the plain text
            for key in SENSITIVE_KEYS:
                pattern = rf'({key}[:=])\S*'
                msg = re.sub(r'(token=|password:\s*)\S+', r'\1****', msg)
            record.msg = msg
            record.args = None
        return True
