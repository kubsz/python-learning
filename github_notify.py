import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://github.com/lylapitajen/python-learning/commits/main'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

soup_str = str(soup)

commits = re.findall("<h2 class=\"f5 text-normal\">Commits on ([A-Za-z]+\s\d+,\s\d+)",soup_str )

with open(r"C:/Users/Lyla/Desktop\workspaces/python-learning/github-commit.txt", "w") as file:
    for date in commits:
        file.write(f"{date}\n")
    file.close()

# print(commits)
