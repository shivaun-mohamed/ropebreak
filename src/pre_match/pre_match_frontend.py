import json

# load match data info
with open("data/match_data.json", "r") as file:
    match_data = json.load(file)

# Match display / formatting for user
def display_primary_match_type(get_primary_match_type):

    primary_match_types = ""

    for match_type in get_primary_match_type:
        if primary_match_types != "":
            primary_match_types += "\n" #add newline after each entry
        primary_match_types += match_type

    return primary_match_types


def display_secondary_match_type(get_secondary_match_type):

    secondary_match_types = ""

    for match_type in get_secondary_match_type:
        if secondary_match_types != "":
            secondary_match_types += "\n" #add newline after each entry
        secondary_match_types += match_type

    return secondary_match_types


# Match Type Getters
def get_primary_match_type(match_data):
    return match_data["primary_match_type"]

def get_secondary_match_type(match_data):
    return match_data["secondary_match_type"]




match_type = get_secondary_match_type(match_data)

print(display_secondary_match_type(match_type))