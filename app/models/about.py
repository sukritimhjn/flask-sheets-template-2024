from pprint import pprint

from app.db import BaseModel

class About(BaseModel):

    SHEET_NAME = "about"

    COLUMNS = ["name", "email", "message"]

    SEEDS = []


if __name__ == "__main__":

    abouts = About.all()
    print("FOUND", len(abouts), "ABOUTS")
    for about in abouts:
        pprint(dict(about))
