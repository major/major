#!/usr/bin/env python
# Add a user to a list of Fedora packages.
import sys

import requests

TOKEN = "PAGURE_TOKEN_GOES_HERE"

def main():
    packages = [package.strip(",") for package in sys.argv[1:]]

    for package in packages:
        print(f" - adding ACL to {package} ...")

        url = f"https://src.fedoraproject.org/api/0/rpms/{package}/git/modifyacls"
        data = {
            "user_type": "user",
            "name": "USERNAME",
            "acl": "commit",
        }
        headers = {
            "Authorization": f"token {TOKEN}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()

    return 0


if __name__ == "__main__":
    exit(main())
