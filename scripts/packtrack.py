#!/usr/bin/env python
# Gets a list of packages for a specific Fedora user account.
import json
import requests

FAS_USERNAME = "mhayden"

def get_package_page(page=1):
    """Get a page of packages from Pagure."""
    # print(f"Getting page {page}")
    payload = {
        "namespace": "rpms",
        "owner": FAS_USERNAME,
        "per_page": 100,
        "page": page,
        "fork": "false"
    }
    resp = requests.get("https://src.fedoraproject.org/api/0/projects", data=payload)
    return [x['fullname'].split('/')[1] for x in resp.json()['projects']]


def get_packages():
    """Get all packages for a user."""
    counter = 1
    projects = []
    while True:
        projects_page = get_package_page(counter)

        if not projects_page:
            break

        projects += projects_page
        counter += 1

    return projects


if __name__ == "__main__":
    print("\n".join(get_packages()))
