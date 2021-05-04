"""Restaurant rating lister."""
from typing import List, Dict
import sys

SCORES_PATH = "scores.txt"
VALID_RATINGS = [0, 1, 2, 3, 4, 5]


def file_path() -> str:
    f"""Return the path to the desired .txt file.

    If a path is sent in through the CLI, use that one. Otherwise, use
    the one defined by {SCORES_PATH}."""

    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = SCORES_PATH
    return file_name


def parse_ratings_dict(file_name: str) -> Dict[str, int]:
    """Parse a txt file and store names and ratings in a dict.

    Each line in the file parsed by this this script must have the structure
    name:rating_xxx, where rating is a number between 0 and 5 and _xxx are
    trailing characters that are not interesting to us.
    """
    ratings = open(file_name)
    names_and_ratings = {}

    for line in ratings:
        name, rating = line.split(":")
        names_and_ratings[name] = int(rating[0])
        # The first value following the colon is the rating.
    return names_and_ratings


def print_restaurant_ratings(d: Dict[str, int]):
    """Print the names and ratings in alphabetical order."""

    # Create a list of the keys, sorted in alphabetical order
    sorted_names = sorted(d)

    # Loop through the sorted list and print out the restaurant name

    for name in sorted_names:
        print(f"{name} is rated at {d[name]}.")


def validate_rating(rating: str) -> bool:
    """Check if the rating is valid."""

    rating = rating.rstrip()
    try:
        rating = int(rating)
    except ValueError:
        return False

    if rating in VALID_RATINGS:
        return True
    else:
        return False


def user_adds_restaurant_score(d: Dict[str, int]) -> None:
    """This function is called to allow users to input new restaurant names and scores to
    a dict.

    Nothing is returned, the dict (d) is modified"""

    restaurant = input("What is the name of the restaurant you would like to rate? ")
    rating = ""

    while validate_rating(rating) == False:
        rating = input(
            f"""What rating would you like to give {restaurant}?
        Please provide a rating between 1 and 5, 5 being the highest rating. """
        )

    d[restaurant] = rating
    return


names_and_ratings = parse_ratings_dict(file_path())
user_adds_restaurant_score(names_and_ratings)
print_restaurant_ratings(names_and_ratings)
