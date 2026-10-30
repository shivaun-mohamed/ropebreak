## Frontend:

Signature:
get_primary_match_type: MatchData -> List[String]

Purpose:
Returns primary_match_types list from the given match data

Examples:
- given match data whose primary_match_types field contains the full list, the getter returns that same list

Template:
- Get full list of primary match types from match_data from MatchData input
- Return full list

Signature:
get_secondary_match_type: MatchData -> List[String]

Purpose:
Returns secondary_match_types list from the given match data

Examples:
- given match data whose secondary_match_types field contains the full list, the getter returns that same list

Template:
- Get full list of secondary match types from MatchData input
- Return full list

<!-- Signature:
display_match_type: get_primary_match_type, get_secondary_match_type -> string

Purpose:
Show the different types of wrestling matches available to the user

Examples:
- display_match_type([singles, normal]) -> "Singles", "Normal"
- display_match_type([tagteam, tornado]) -> "Tag team", "Tornado"
- display_match_type([triplethreat, hellinacell]) -> "Triple Threat", "Hell in a Cell"

Template:
- Call getter get_primary_match_types
- Display get_primary_match_types output to user -->

