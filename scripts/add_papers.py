#!/usr/local/bin/python3

import json
from datetime import datetime


def check_dateformat(inp):
    try:
        parsed = datetime.strptime(inp, "%d/%m/%Y")
        return datetime.strftime(parsed, "%d/%m/%Y")
    except Exception as e:
        print(e)
        print("Please enter date in the format DD/MM/YYYY")
        return None


def main():

    with open('paper-list.json', 'r') as jsonfile:
        data = json.load(jsonfile)

    papername = input("Enter name of the paper\n")
    paperlink = input("Enter link to the paper\n")
    reviewlink = input("Review link? Enter 'n' if not\n")
    authorlist = input("Enter the list of authors\n")
    conference = input("Enter the name of the conference\n")

    dateadded = None
    while dateadded is None:
        dateadded = input("Enter the date added\n")
        dateadded = check_dateformat(dateadded)

    keywords = input("Keywords associated\n")

    newpaper = []
    newpaper.append(dateadded)
    newpaper.append(authorlist)
    newpaper.append("<a href=\""+paperlink+"\">"+papername+"</a>")
    newpaper.append(conference)
    newpaper.append(keywords)
    newpaper.append(reviewlink)

    data["data"] = [newpaper] + data["data"]

    for i in range(len(data["data"])):
        for j in range(len(data["data"][i])):
            data["data"][i][j] = data["data"][i][j].strip()

    with open('paper-list.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)

if __name__ == "__main__":
    main()
