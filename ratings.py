"""Restaurant rating lister."""
from typing import List, Dict, Tuple
import sys
import enum


SCORES_PATH = "scores.txt"
VALID_RATINGS = (0, 1, 2, 3, 4, 5)


class States(enum.Enum):
    # These are the different 'states' the program can be in.
    INSTANTIATE_DICT = 1
    WHAT_NEXT = 2
    ADD_NEW_RESTAURANT = 3
    DISPLAY_DICT = 4
    QUIT = 5


VALID_STATE_CHOISES = {
    1: States.ADD_NEW_RESTAURANT,
    2: States.DISPLAY_DICT,
    3: States.QUIT,
}
VALID_STATE_NUMBERS = {
    States.ADD_NEW_RESTAURANT: 1,
    States.DISPLAY_DICT: 2,
    States.QUIT: 3,
}


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


def validate_number(n: str, valid_ans: Tuple[int]) -> bool:
    """Check if the rating is valid."""

    n = n.rstrip()
    try:
        n = int(n)
    except ValueError:
        return False

    return n in valid_ans


def user_adds_restaurant_score(d: Dict[str, int]) -> None:
    """This function is called to allow users to input new restaurant names and scores to
    a dict.

    Nothing is returned, the dict (d) is modified"""

    restaurant = input("What is the name of the restaurant you would like to rate? ")
    rating = ""

    while validate_number(rating, VALID_RATINGS) == False:
        rating = input(
            f"""What rating would you like to give {restaurant}?
        Please provide a rating between 1 and 5, 5 being the highest rating. """
        )

    d[restaurant] = rating
    return


def print_options() -> None:
    """Prints the options to the user regarding what to do next."""
    print(
        f"""
Please choose one of the following options:
    - Add new restaurant rating ({VALID_STATE_NUMBERS[States.ADD_NEW_RESTAURANT]})
    - Print current ratings ({VALID_STATE_NUMBERS[States.DISPLAY_DICT]})
    - Quit program ({VALID_STATE_NUMBERS[States.QUIT]})
    """
    )


def get_state():
    """Asks the user what to do next."""

    # Initiate state with arbitrary invalid state
    state_n = ""
    while validate_number(state_n, list(VALID_STATE_CHOISES.keys())) == False:
        state_n = input("Please indicate the number of the desired option: ")
        print("")

    return VALID_STATE_CHOISES[int(state_n)]


print(
    f"State {States.ADD_NEW_RESTAURANT}: {States.ADD_NEW_RESTAURANT.value}, {type(States.ADD_NEW_RESTAURANT.value)}"
)
# Initialize the variable 'state'
state = States.INSTANTIATE_DICT
print("\nWelcome to the restaurant rating program!")

while True:

    if state == States.INSTANTIATE_DICT:
        # Initialize ratings dict from a file

        names_and_ratings = parse_ratings_dict(file_path())
        state = States.WHAT_NEXT

    elif state == States.WHAT_NEXT:
        # Print options of what to do next. Get the users answer.

        print_options()
        state = get_state()

    elif state == States.ADD_NEW_RESTAURANT:
        # Ask for a new restaurant name and rating.

        user_adds_restaurant_score(names_and_ratings)
        state = States.WHAT_NEXT

    elif state == States.DISPLAY_DICT:
        # Display all current ratings, sorted in alphabetical order.

        print_restaurant_ratings(names_and_ratings)
        state = States.WHAT_NEXT

    elif state == States.QUIT:
        # Print exit message and quit program.
        print("Goodbye!")
        exit()
