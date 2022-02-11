#!/usr/bin/env python3
"""
Hashword.
"""
from hashlib import sha512
from urllib.parse import urlparse
import string


ALPHABET = string.ascii_letters + string.digits + string.punctuation


def get_password(url: str, p: str) -> str:
    """
    Find the password for a website.

    Args:
        url: The URL of the website.
        p: The password for the passwords.
    """
    if not urlparse(url).scheme:
        raise ValueError("URL must have a scheme")

    u = urlparse(url).netloc

    h = sha512(usedforsecurity=True)
    h.update(bytes(p, "utf-8"))
    h.update(bytes(u, "utf-8"))

    password = [ALPHABET[byte % len(ALPHABET)] for byte in h.digest()]
    return "".join(password)


def main():
    print("Password:")
    password = input(">>> ")

    print("URL:")
    url = input(">>> ")

    pw = get_password(url, password)
    print(pw)


if __name__ == "__main__":
    main()
