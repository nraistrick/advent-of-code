"""
Generates the required password for a door based on a given input
"""

import itertools
from common.common import get_md5_hash

DOOR_INPUT = "wtnhxymk"
PASSWORD_LENGTH = 8
HEXADECIMAL_BASE = 16


def calculate_password(door_id):
    """
    :type door_id: str
    :rtype: str
    """
    password = ""

    for i in itertools.count():
        value_to_hash = "%s%s" % (door_id, str(i))
        hash_value = get_md5_hash(value_to_hash)
        if not hash_value.startswith("00000"):
            # Not a hash value of interest
            continue

        password += hash_value[5]
        if len(password) == PASSWORD_LENGTH:
            break

    return password


def calculate_advanced_password(door_id):
    """
    Calculates the password for the more advanced algorithm

    :type door_id: str
    :rtype: str
    """
    password = ""
    password_store = [""] * PASSWORD_LENGTH

    for i in itertools.count():
        value_to_hash = "%s%s" % (door_id, str(i))
        hash_value = get_md5_hash(value_to_hash)

        if not hash_value.startswith("00000"):
            # Not a hash value of interest
            continue

        character_position = int(hash_value[5], HEXADECIMAL_BASE)
        if character_position >= PASSWORD_LENGTH:
            # Character position doesn't fit within password length limits
            continue

        if password_store[character_position] != "":
            # We've already stored a character at this position -
            # we only want the first one.
            continue

        password_store[character_position] = hash_value[6]
        password = "".join(password_store)
        if len(password) == PASSWORD_LENGTH:
            # We've successfully got all the password characters
            break

    return password


def main():
    print "The simple password is: %s" % calculate_password(DOOR_INPUT)
    print "The advanced password is %s" % calculate_advanced_password(DOOR_INPUT)


if __name__ == "__main__":
    main()
