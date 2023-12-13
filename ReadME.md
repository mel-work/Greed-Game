# Greed Game Logic

## Objects
* 6 Dice
* Players
* Game
### Methods
* Roll

## Turns and Rounds
Each player takes a `turn` rolling the dice to see how many points they can get. Each turn will consist of various rounds within the turn. 

## Game Format
Once a new game is created, an embed will pop up asking people to click the button to join the game.
`Game starting...` Use Discord timestamp for `In 60 seconds`

The game will be in a single embed that updates each round and turn.

## Gameplay
While the highest score is < 10000,
    Loop through the players list,
        While player turn,
            Player begins turn with 6 dice
            They roll `n` dice
                Case 1: Hold and roll
                    Remove held dice,
                    Update Score,
                    Update dice to roll
                    continue loop
                Case 2: Hold and Stay
                    Remove held dice,
                    Update turn score
                    Update player score
                    break
                Bust
                    Remove all points gained this round
                    break


## Commands
* `/start_game` creates a new game instance
* `/how_to_play`

