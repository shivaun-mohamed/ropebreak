# How to Design Data (HTDD)

## 1. Data Definition

A Wrestler is a compound data structure made up of the following fields:

| Field | Type |
| ----- | ---- |
| name  | String |
| height | Float |
| weight | Float |
| wrestler-type | List of strings (well-balanced, brawler, grappler, mat-technician, high-flyer, rule-breaker). Wrestler type will determine moveset. |
| moveset | List of signature-move records. Each record contains the move name and classification, plus a list of target body parts when applicable; the final move is the finisher. |
| static-stats | Dictionary of String : Float (keys: strength, speed, durability, counter, charisma, submission, aerial ability) |
| dynamic-stats | Dictionary (health, stamina, morale, momentum, injury status, injury target count; see breakdowns below) |

### Field interpretation:

| Height | Weight |
|  ----- |  ----- |
| Metres (m) | Pounds (lb) |

- Static stat scale: 0-10 in 0.25 increments

| Dynamic Stats | Description |
|  ------------ | ----------- |
| Health        | High health: health bar filled >=70%, Medium Health: health bar filled 40%<= and <70%, Low Health: health bar filled <40% |
| Stamina       | High Stamina: stamina bar filled >=70%, Medium Stamina: stamina bar filled 40%<= and <70%, Low Stamina: stamina bar filled <40% |

### wrestler-type breakdown: 

- Note: Strengths and weaknesses functionality not implemented in v0

| Wrestler-Type | Description | Strengths | Weaknesses | Stat Allocation |
| :--- | :--- | :--- | :--- | :--- |
| well-balanced | Does not rely on a single dominant fighting technique. | Versatile, adapts well to different opponents | Vulnerable to all opponents. Because of no specialization, there will be times when they play to opponents strengths | Balanced across all stats (**1.0**) |
| brawler | Brawlers are optimized for aggressive, standing pressure. They love to strike. | Brawlers are effective against rule-breakers, high-flyers, and well-balanced wrestlers. | Brawlers struggle against mat technicians, grapplers, rule-breakers, and well-balanced wrestlers. | Strength (**1.25**), Speed (**1.25**), Durability (**1.75**),  Counter (**0.75**), Charisma (**1.0**), Submission (**0.5**), Aerial Ability (**0.5**).|
| grappler | Grapplers use strength to inflict heavy slams, holds, suplexes, throws, etc. | Grapplers are effective against brawlers, rule-breakers, and well-balanced wrestlers. | Grapplers struggle against mat technicians, high-flyers, rule-breakers, and well-balanced wrestlers. | Strength (**1.75**), Speed (**0.5**), Durability (**1.5**),  Counter (**1.75**), Charisma (**0.75**), Submission (**0.5**), Aerial Ability (**0.25**). |
| mat-technician | Mat technicians specialize in technical wrestling: using submission holds, counters, targeting body parts and understanding in-ring psychology. | Mat technicians are effective against brawlers, grapplers, well-balanced wrestlers, and rule-breakers. | Mat technicians struggle against high-flyers, rule-breakers, and well-balanced wrestlers | Strength (**1.0**), Speed (**0.75**), Durability (**1.0**),  Counter (**1.5**), Charisma (**0.75**), Submission (**1.75**), Aerial Ability (**0.25**). |
| high-flyer | High flyers are agile and move fast, prioritizing turnbuckle moves. | High-flyers are effective against grapplers, mat-technicians, rule-breakers, and well-balanced wrestlers. | High-flyers struggle against brawlers, rule-breakers, and well-balanced wrestlers. | Strength (**0.75**), Speed (**1.75**), Durability (**0.5**),  Counter (**0.75**), Charisma (**1.0**), Submission (**0.5**), Aerial Ability (**1.75**). |
| rule-breaker | Rule-breakers will do anything to win. Even if that means not playing by the rules. | Rule-breakers are effective against all types. | Rule-breakers struggle against all types. | Strength (**1.0**), Speed (**1.0**), Durability (**1.0**),  Counter (**1.0**), Charisma (**1.0**), Submission (**1.0**), Aerial Ability (**1.0**). |

### moveset breakdown:

#### Overview

Each wrestler type has 15 generic move assignments.

- A wrestler has access to the generic moves assigned to every wrestler type they have.
- Each generic move entry stores the move name together with its classification, plus a list of target body parts when applicable.
- Each wrestler's moveset contains their signature moves, with the finisher listed last. Each signature-move entry stores the move name together with its classification, plus a list of target body parts when applicable.
- A move may target more than one body part. Target body parts are recorded separately from classification.
- Generic moves are available regardless of momentum. Signature moves, including the finisher, are available only when the wrestler's momentum is true.
- Three successful moves in a row unlock signature moves by setting momentum to true. Any opponent action interrupts the streak before the unlock and resets its count.
- Using a signature move does not reset momentum. Momentum remains true until the wrestler has used all of their signature moves or the opponent counters one of their moves.
- Each time momentum is unlocked, all of the wrestler's signature moves are available for that cycle. If momentum ends early because of a counter, the next unlock starts a fresh cycle with all signature moves available again.
- In v0, move classifications are used only to guide commentary. They do not otherwise affect move selection or match simulation.

#### Classification Key

| Category | Definition |
|---|---|
| Striking | A punch, kick, elbow, knee, clothesline, or similar impact attack. |
| Grappling | A throw, slam, takedown, or manipulation of the opponent. |
| Submission | A maintained hold used for submission attempts or wear-down effects. |
| Pinning | A maneuver primarily intended to trap the opponent in a pin. |
| Weapon attack | An attack using an external object. |

Additional descriptors:
- Standing: performed against a standing opponent.
- Running: performed with a running approach.
- Grounded opponent: performed against an opponent on the mat.
- Rear: performed from behind the opponent.
- Corner: performed in or from a corner.
- Aerial: performed by jumping or diving from an elevated position.
- Illegal: a move that violates the match's rules.
- Weapon-assisted: a move incorporating a weapon or external object.

Each move has one or more categories from this list. Commentary uses the categories to identify the kind of move. Write each classification as a category followed by zero or more descriptors in parentheses. Join multiple categories with `+`. Use only the descriptors listed above; omit a descriptor when none applies.

Examples:
- Diving elbow drop: `Striking (Aerial)`.
- Northern lights suplex with bridge: `Grappling + Pinning`.
- DDT onto a chair: `Grappling (Weapon-assisted)`.

#### 1. Well-Balanced

| Move | Classification | Target Body Parts |
|---|---|---|
| Straight punch | Striking (Standing) | Head |
| Toe kick | Striking (Standing) | Torso |
| Backhand chop | Striking (Standing) | Torso |
| Clothesline | Striking (Standing, Running) | Head |
| Dropkick | Striking (Standing) | Torso |
| Elbow drop | Striking (Grounded opponent) | Torso |
| Scoop slam | Grappling (Standing) | Torso |
| Snap suplex | Grappling (Standing) | Torso |
| Snapmare | Grappling (Standing) | Head |
| Arm drag | Grappling (Standing) | Arms |
| Neckbreaker | Grappling (Standing) | Head |
| DDT | Grappling (Standing) | Head |
| Sleeper hold | Submission (Rear) | Head |
| Diving crossbody | Grappling (Aerial) | Torso |
| Diving elbow drop | Striking (Aerial) | Torso |

#### 2. Brawler

| Move | Classification | Target Body Parts |
|---|---|---|
| Straight punch | Striking (Standing) | Head |
| Full-swing punch | Striking (Standing) | Head |
| Backhand chop | Striking (Standing) | Torso |
| Forearm smash | Striking (Standing) | Head |
| Elbow smash | Striking (Standing) | Head |
| Toe kick | Striking (Standing) | Torso |
| Clothesline | Striking (Standing) | Head |
| Running clothesline | Striking (Running) | Head |
| Shoulder block | Striking (Running) | Torso |
| Corner shoulder thrusts | Striking (Corner) | Torso |
| Stomp | Striking (Grounded opponent) | Torso |
| Ground punches | Striking (Grounded opponent) | Head |
| Scoop slam | Grappling (Standing) | Torso |
| Sidewalk slam | Grappling (Standing) | Torso |
| Bulldog | Grappling (Standing, Running) | Head |

#### 3. Grappler

| Move | Classification | Target Body Parts |
|---|---|---|
| Scoop slam | Grappling (Standing) | Torso |
| High-angle scoop slam | Grappling (Standing) | Torso |
| Vertical suplex | Grappling (Standing) | Torso |
| Stalling suplex | Grappling (Standing) | Torso |
| Belly-to-back suplex | Grappling (Rear) | Torso |
| German suplex | Grappling (Rear) | Torso |
| Belly-to-belly suplex | Grappling (Standing) | Torso |
| Powerslam | Grappling (Standing, Running) | Torso |
| Sidewalk slam | Grappling (Standing) | Torso |
| Pendulum backbreaker | Grappling (Standing) | Torso |
| Rib breaker | Grappling (Standing) | Torso |
| Spinebuster | Grappling (Standing) | Torso |
| Powerbomb | Grappling (Standing) | Torso |
| Fallaway slam | Grappling (Standing) | Torso |
| Superplex | Grappling (Corner) | Torso |

#### 4. Mat-Technician

| Move | Classification | Target Body Parts |
|---|---|---|
| Arm drag | Grappling (Standing) | Arms |
| Snapmare | Grappling (Standing) | Head |
| Dragon screw | Grappling (Standing) | Legs |
| Shin breaker | Grappling (Standing) | Legs |
| Arm wrench with elbow stomp | Grappling + Striking | Arms |
| Russian leg sweep | Grappling (Standing) | Legs, Torso |
| Northern lights suplex with bridge | Grappling + Pinning | Torso |
| Small package | Pinning | None |
| Backslide | Pinning (Rear) | None |
| Armbar | Submission | Arms |
| Reverse chinlock | Submission (Grounded opponent) | Head |
| Sleeper hold | Submission (Rear) | Head |
| Abdominal stretch | Submission (Standing) | Torso |
| Surfboard stretch | Submission (Grounded opponent) | Arms, Torso |
| Single-leg Boston crab | Submission (Grounded opponent) | Legs |

#### 5. High-Flyer

| Move | Classification | Target Body Parts |
|---|---|---|
| Dropkick | Striking (Standing) | Torso |
| Spinning heel kick | Striking (Standing) | Head |
| Running head-scissors takedown | Grappling (Running) | Head |
| Hurricanrana | Grappling (Standing) | Head |
| Monkey flip | Grappling (Standing, Corner) | Torso |
| Tornado DDT | Grappling (Aerial, Corner) | Head |
| Missile dropkick | Striking (Aerial) | Torso |
| Diving crossbody | Grappling (Aerial) | Torso |
| Diving double axe handle | Striking (Aerial) | Head |
| Diving elbow drop | Striking (Aerial) | Torso |
| Diving body splash | Striking (Aerial) | Torso |
| Moonsault | Striking (Aerial) | Torso |
| Shooting star press | Striking (Aerial) | Torso |
| Somersault plancha | Striking (Aerial) | Torso |
| Asai moonsault | Striking (Aerial) | Torso |

#### 6. Rule-Breaker

| Move | Classification | Target Body Parts |
|---|---|---|
| Straight punch | Striking (Standing) | Head |
| Toe kick | Striking (Standing) | Torso |
| Clothesline | Striking (Standing, Running) | Head |
| Neckbreaker | Grappling (Standing) | Head |
| DDT | Grappling (Standing) | Head |
| Schoolboy roll-up | Pinning | None |
| Low blow | Striking (Illegal) | Torso |
| Eye rake | Striking (Illegal) | Head |
| Eye poke | Striking (Illegal) | Head |
| Hair-pull slam | Grappling (Illegal) | Head |
| Grounded groin strike | Striking (Illegal, Grounded opponent) | Torso |
| Rope-assisted choke | Submission (Illegal) | Head |
| Chair strike | Weapon attack | Head, Torso |
| Stick strike | Weapon attack | Head, Torso |
| DDT onto a chair | Grappling (Weapon-assisted) | Head |

### static-stats description:

| Field | Description |
| ----- | ---- |
| Strength | Wrestler's power when attacking other wrestlers. |
| Speed | Wrestler's reaction speed, agility, change of direction, and how fast they move when performing moves, counters, etc. |
| Durability | Wrestler's longevity in the match and how easily their body breaks down, how many hits they can take. Affects dynamic stat (stamina, injury status). |
| Counter | Wrestler's ability to reverse or stop moves by the opponent. | 
| Charisma | Wrestler's ability to draw a reaction from the crowd, can impact their dynamic stats (morale, momentum). |
| Submission | Wrestler's ability to commit and break out of submission holds. | 
| Aerial Ability | Wrestler's ability to commit effective moves in the air. |


### dynamic-stats breakdown:

| Field | Type |
| ----- | ---- |
| Health | Float |
| Stamina | Float |
| Morale | String: confident, nervous, normal, furious, demoralized - see breakdown below |
| Momentum | Boolean |
| injury status | Dictionary of String: String - see breakdown below |
| injury target count | Dictionary of String: Integer - cumulative targeted-move count for each body part |

### match-state breakdown:

| Field | Type | Description |
| ----- | ---- | ----------- |
| consecutive move count | Integer per wrestler | Counts successful moves in a row toward unlocking signature moves. Starts at 0, resets when interrupted before unlock, and reaching 3 sets momentum to true. Resets to 0 when the momentum cycle ends. |
| signature moves used | List of Strings per wrestler | Names of signature moves used during the current momentum cycle. Starts empty when momentum unlocks and resets when the cycle ends. |

### morale-effects breakdown:

This is a separate lookup, not a field on wrestler

| Morale | Effect |
| ----- | ---- |
| Normal | Damage *= 1.0, Mistake *= 1.0 |
| Confident | Damage *= 1.5, Mistake *= 1.25 |
| Nervous | Damage *= 0.75, Mistake *= 1.75 |
| Furious | Damage *= 1.75, Mistake *= 1.75 |
| Demoralized | Damage *= 0.5, Mistake *= 1.75 |

### injury-status breakdown:

- All four body parts start out as healthy when wrestler is created
- Injury status has no effect on simulation (match results) in v0
- Commentary in v0 will make note of injuries
- Track the cumulative number of moves that target each body part throughout the match; non-targeting moves do not change the count.
- A regular move adds 1 to the count for each body part it targets. A signature move adds 5 to the count for each body part it targets.
- Derive injury status from the cumulative count: 0-2 is Healthy, 3-5 is Minor, 6-9 is Intermediate, and 10 or more is Major.
- A targeted move identifies its target body part or parts separately from its classification. Classifications guide commentary only.

| Body Part (Key) | Injury status (Value) |
| ----- | ---- |
| Head | Healthy, Minor, Intermediate, Major  |
| Arms | Healthy, Minor, Intermediate, Major |
| Legs | Healthy, Minor, Intermediate, Major |
| Torso | Healthy, Minor, Intermediate, Major |


## Wrestler Examples

These examples show values for the Wrestler data definition. Heights are in metres, weights are in pounds, and static-stat ratings are on the 0-10 scale. Health and stamina use a 0-100 scale. Every body part is present in the starting injury status. The final move listed in each moveset is that wrestler's finisher.

#### Eddie Guerrero
```json
{
  "name": "Eddie Guerrero",
  "height": 1.73,
  "weight": 225.0,
  "wrestler-type": ["mat-technician", "rule-breaker"],
  "moveset": [
    {"name": "Gory Special", "classification": "Grappling + Submission", "target body parts": ["Torso"]},
    {"name": "Lasso from El Paso", "classification": "Submission", "target body parts": ["Legs"]},
    {"name": "Frog Splash", "classification": "Striking (Aerial)", "target body parts": ["Torso"]}
  ],
  "static-stats": {
    "strength": 7.75,
    "speed": 8.0,
    "durability": 6.75,
    "counter": 9.25,
    "charisma": 10.0,
    "submission": 9.0,
    "aerial ability": 9.0
  },
  "dynamic-stats": {
    "health": 100.0,
    "stamina": 100.0,
    "morale": "normal",
    "momentum": false,
    "injury status": {
      "Head": "Healthy",
      "Arms": "Healthy",
      "Legs": "Healthy",
      "Torso": "Healthy"
    },
    "injury target count": {
      "Head": 0,
      "Arms": 0,
      "Legs": 0,
      "Torso": 0
    }
  }
}
```
#### Bret 'The Hitman' Hart
```json
{
  "name": "Bret 'The Hitman' Hart",
  "height": 1.83,
  "weight": 235.0,
  "wrestler-type": ["mat-technician", "well-balanced"],
  "moveset": [
    {"name": "Inverted Atomic Drop", "classification": "Grappling", "target body parts": ["Legs"]},
    {"name": "Pendulum Backbreaker", "classification": "Grappling", "target body parts": ["Torso"]},
    {"name": "The Sharpshooter", "classification": "Submission (Grounded opponent)", "target body parts": ["Legs"]}
  ],
  "static-stats": {
    "strength": 7.75,
    "speed": 7.5,
    "durability": 9.25,
    "counter": 10.0,
    "charisma": 8.0,
    "submission": 10.0,
    "aerial ability": 6.0
  },
  "dynamic-stats": {
    "health": 100.0,
    "stamina": 100.0,
    "morale": "normal",
    "momentum": false,
    "injury status": {
      "Head": "Healthy",
      "Arms": "Healthy",
      "Legs": "Healthy",
      "Torso": "Healthy"
    },
    "injury target count": {
      "Head": 0,
      "Arms": 0,
      "Legs": 0,
      "Torso": 0
    }
  }
}
```
#### Batista
```json
{
  "name": "Batista",
  "height": 1.98,
  "weight": 290.0,
  "wrestler-type": ["grappler", "brawler"],
  "moveset": [
    {"name": "Spinebuster", "classification": "Grappling", "target body parts": ["Torso"]},
    {"name": "The Spear", "classification": "Striking (Running)", "target body parts": ["Torso"]},
    {"name": "Batista Bomb", "classification": "Grappling", "target body parts": ["Torso"]}
  ],
  "static-stats": {
    "strength": 9.75,
    "speed": 7.0,
    "durability": 7.0,
    "counter": 7.25,
    "charisma": 8.0,
    "submission": 5.5,
    "aerial ability": 3.5
  },
  "dynamic-stats": {
    "health": 100.0,
    "stamina": 100.0,
    "morale": "normal",
    "momentum": false,
    "injury status": {
      "Head": "Healthy",
      "Arms": "Healthy",
      "Legs": "Healthy",
      "Torso": "Healthy"
    },
    "injury target count": {
      "Head": 0,
      "Arms": 0,
      "Legs": 0,
      "Torso": 0
    }
  }
}
```

## Planned Features:

- Type advantage as a tiebreaker / edge-case for close statistical matchups (not yet implemented)
- Strengths and weaknesses will have an effect on gameplay / simulation in a later version
- Dynamic stat archetype (heel, tweener, babyface) will have an effect on crowd reaction and temporary stat boosts (not yet implemented)
- Injury status will have an effect on gameplay / simulation in a later version
- Support optional wrestler nicknames for commentary in later version

