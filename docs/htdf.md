# Pre-Match State


## Frontend:

### Responsibilities:
- Show available match types for user to choose from (in v0, just singles)
- Display prompts that guide user through match type and wrestler selection, including confirmation prompts:
    - Choose a Match Type (Primary)
    - Choose a Match Type (Secondary)
    - Instructions text
    - Choose Wrestler
    - Confirm wrestlers and match confirmation
- Show roster of wrestlers, with their names and IDs
- Get user's wrestler choice by name or roster number and provide feedback for invalid choices
- Display a selected wrestler's information, such as height, weight, type, and stats
- Display final selections before match
- Validity check to make sure same wrestler is not chosen for both sides (once a wrestler is selected by user, they can not be selected again)



#### Show available match types for user to choose from
Signature:
get_primary_match_type: MatchData -> List[String]

Purpose:
Returns primary_match_type list from the given match data

Examples:
- given match data whose primary_match_type field contains the full list, the getter returns that same list

Template:
- Get full list of primary match type from match_data from MatchData input
- Return full list


    
Signature:
get_secondary_match_type: MatchData -> List[String]

Purpose:
Returns secondary_match_type list from the given match data

Examples:
- given match data whose secondary_match_type field contains the full list, the getter returns that same list

Template:
- Get full list of secondary match types from MatchData input
- Return full list



Signature:
display_primary_match_type: List[String] -> String

Purpose:
Create and return one display string containing the primary match types, with each type on its own line

Examples:
- Given ["Singles"], return "Singles"
- Given ["Singles", "Tag Team"], return "Singles\nTag Team"

Template:
- Go through each match type in input list
- Combine their names into one string, with each name on a new line
- Return the string



Signature:
display_secondary_match_type: List[String] -> String

Purpose:
Create and return one display string containing the secondary match types, with each type on its own line

Examples:
- Given ["Normal Match"], return "Normal Match"
- Given ["Normal Match", "Submission", "TLC"], return "Normal Match\nSubmission\nTLC"

Template:
- Go through each match type in input list
- Combine their names into one string, with each name on a new line
- Return the string


#### Display prompts, guiding user through match type and wrestler selection

Signature:
prompt_primary_match_selection: List[String] -> String

Purpose:
Ask the user which primary match type they want to choose from the available primary match types, and return their valid choice

Examples:
- Given ["Singles"], when the user enters or selects Singles, return "Singles"
- Given the available list ["Singles"], when user enters an invalid choice and then Singles, show an error, ask again, and return "Singles"

Template:
- Use available primary match types to check user's choice
- Prompt user to enter choice
- Read user's response
- If it matches an available option, return it
- Otherwise, show an error and prompt again

Signature:
prompt_secondary_match_selection: List[String] -> String

Purpose:
Ask user which secondary match type they want to choose from the available secondary match types, return their valid choice

Examples:
- Given ["Normal Match"], when user enters or selects Normal Match, return "Normal Match"
- Given the available list ["Normal Match"], when user enters an invalid choice and then Normal Match, show an error, ask again, and return "Normal Match"

Template:
- Use available secondary match types to check user's choice
- Prompt user to enter choice
- Read user's response
- If it matches an available option, return it
- Otherwise, show an error and prompt again

Signature:
prompt_wrestler_selection: (List[Wrestler], List[Integer]) -> Wrestler

Purpose:
Prompt user to choose one wrestler by name or ID, reject invalid or already selected choices, return chosen wrestler

Examples:
- Given roster containing Andre the Giant (ID 1) and Bret 'The Hitman' Hart (ID 2), with no one selected yet, if user enters 1, return Andre's wrestler record
- Given that Andre the Giant (ID 1) is already selected, if user enters 1 again, explain that he's already selected and ask again. If the user then enters 2, return Bret 'The Hitman' Hart's wrestler record

Template:
- Prompt user to enter wrestler name or ID from available roster
- Read the choice
- Check whether it matches wrestler in roster
- If that wrestler's ID or name is already selected, explain and prompt again
- If that wreslter's ID or name is unavailable, explain and prompt again
- Return selected wrestler's record

#### Count the number of wrestlers the user can choose based on primary match type

Signature:
get_wrestler_count: String -> Integer

Purpose:
Return number of wrestler slots required for given primary match type

Examples:
- Given "Singles", return 2

Template:
- Examine selected primary match type
- If "Singles", return 2
- Add a case for each other primary match type when it becomes supported


#### Display wrestling roster's names and IDs

Signature:
display_wrestler_identifications: (List[Wrestler]) -> String

Purpose:
Create and return the complete list of wrestler IDs and wrestler names in the roster in one line per wrestler

Examples:
- Given roster containing Andre the Giant (ID 1) and Bret 'The Hitman' Hart (ID 2), the function returns "1. Andre the Giant\n2. Bret 'The Hitman' Hart"

Template:
- Read the list of wrestlers
- Go through each wrestler
- Get their respective names
- Get their respective IDs
- Format each entry 
- Combine entry with newlines
- Return the string of entries

#### Confirmation of upcoming match

Signature:
pre_match_summary: (String, String, List[String]) -> String

Purpose:
Create and return a pre-match summary of the selected primary and secondary match type and selected wrestlers for the user

Examples:
- Given "Singles", "Normal Match", "Bret 'the Hitman' Hart", "Andre the Giant", return "Singles\nNormal Match\nBret 'the Hitman' Hart\nAndre the Giant"

Template:
- Read the selected primary match type
- Read the selected secondary match type
- Read the selected wrestlers' names in the list
- Combine into a string with each selected match type and each selected wrestlers on their own new line
- Return this combined string


Signature:
pre_match_confirmation: String -> Boolean

Purpose:
Show the pre-match summary, ask the user whether to proceed, and return True for yes or False for no

Examples:
- Given the completed pre-match summary and the user answers "Yes", return True
- Given the completed pre-match summary and the user answers "No", return False
- Given the completed pre-match summary and the user enters an invalid response followed by "Yes", show an error, ask again, and return True

Template:
- Display the pre-match summary
- Ask whether the user wants to proceed
- Read the user's response
- If the response is yes, return True
- If the response is no, return False
- Otherwise, show an error and ask again


#### Display selected wrestler's details

display_wrestler_info: Wrestler -> String

Purpose:
Format and return the selected wrestler’s name, height, weight, wrestler type, and static stats, with each piece of information on a new line.

Examples:
- Given Bret Hart's wrestler record / data, return "Name: Bret 'The Hitman' Hart\nHeight: 1.83m\nWeight: 235.0lbs\nWrestler Type: Mat Technician, Well Balanced\nStatic Stats:\n- Strength: 7.75\n- Speed: 7.5\n- Durability: 9.25\n- Counter: 10.0\n- Charisma: 8.0\n- Submission: 10.0\n- Aerial Ability: 6.0"

Template:
- Read wrestler's name, height, weight, wrestler type, static stats
- Format each field as a readable line
- Combine the lines, with each on a new line
- Return the combined string


#### General Instructions

Signature:
pre_match_display_instructions: () -> String:

Purpose:
Return instructions that explain how to navigate the pre-match interface and make selections

Examples:
- Given no input, return "Choose a match type, then select two different wrestlers from the roster. Review your selections and confirm to continue."

Template:
- Create the instruction string
- Return the string