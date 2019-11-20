#!/usr/bin/python3
""" Write Script to vote for yourself 1024 times """


if "__name__" == "__main__":
    import requests
    from bs4 import BeautifulSoup

    for i in range(1024):
        response = requests.post("http://158.69.76.135/level0.php", data={"id":845, "holdthedoor":"Submit"})
