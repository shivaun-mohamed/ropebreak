# Pre-Match State


## Frontend:

### Responsibilities:
- Show available match types for user to choose from (in v0, just singles)
- Display prompts that guide user through match type and wrestler selection, including confirmation prompts:
    - Choose a Match Type (Primary)
    - Choose a Match Type (Secondary)
    - Confirm Match Selection
    - Back prompt after each selection
    - Choose Wrestler
    - Confirm wrestlers
- Show roster of wrestlers, with their names and IDs
- Get user's wrestler choice by name or roster number and provide feedback for invalid choices
- Display a selected wrestler's information, such as height, weight, type, and stats
- Display final selections before match
- Validity check to make sure same wrestler is not chosen for both sides (once a wrestler is selected by user, they can not be selected again)



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
- Given ["Normal"], return "Normal"
- Given ["Normal", "Submission", "TLC"], return "Normal\nSubmission\nTLC"

Template:
- Go through each match type in input list
- Combine their names into one string, with each name on a new line
- Return the string