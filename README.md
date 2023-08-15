# Elemental_Dice_Bot

## Description
Elemental_Dice_Bot is a Python program that operates on the Matrix platform. It allows for the handling of dice rolling commands.

## Requirements
To run the program, you must have Python version 3.7 or newer installed. Additionally, the program requires several external libraries, which will be automatically installed upon first launch.

## Usage
1. Ensure that you have Python version 3.7 or newer installed.
2. Download and unzip the program files on your computer.
3. Run the bot_execute.bat script. This script will install the required libraries and start the program.
4. Follow the instructions displayed on the screen.

## Credentials
To authenticate the bot on the Matrix platform, you need to provide your credentials in the `credentials.txt` file. Please fill in the necessary information in the appropriate fields in the file.

## Supported Commands
1. `/ping`: Used to check if the bot is active.
2. `/credits`: Displays information about the copyright and license of the program.
3. `/roll`: Used to roll dice. The syntax is `/roll NdM+B roll_type`, where `N` is the number of dice to roll, `M` is the number of sides on the dice, and `B` is a bonus to add to the total. The `roll_type` parameter specifies the type of roll:
   - `normal`: Standard roll (default). Example: `/roll 1d10+5`
   - `e`: Exploding roll, where dice that roll the maximum value are rolled again and added to the total. Example: `/roll 2d6+3e`
   - `i`: Imploding roll, where dice that roll the minimum value are rolled again and subtracted from the total. Example: `/roll 3d8+2i`
   - `dh`: Drop highest result. Example: `/roll 4d6+1dh`
   - `dl`: Drop lowest result. Example: `/roll 4d6+1dl`
   - `kh`: Keep highest result. Example: `/roll 4d6+1kh`
   - `kl`: Keep lowest result. Example: `/roll 4d6+1kl`
4. `/reroll`: Used to reroll a previous roll. The syntax is `/reroll hash`, where `hash` is the unique identifier of the roll you want to reroll. This command will use the same dice and modifiers as the original roll.

## License
Elemental_Dice_Bot is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License (GPL) version 3, as published by the Free Software Foundation. The program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; even without the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. More details can be found in the LICENSE.md file.

## Author
The program was created by Roman Glegola in 2023.
