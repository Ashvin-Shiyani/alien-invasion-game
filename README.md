Hello Welcome to my game,
This is a fully functional Space Invaders-style arcade game built from scratch in Python using the Pygame library. This was a personal project I completed while studying Computer Science at Acadia University
🚀 How to Run
Requirements
Python 3.11+ Pygame installed in your device
Here is an example how it would look like.
<img width="1496" height="1034" alt="image" src="https://github.com/user-attachments/assets/03058d74-371e-43a4-bde5-aa363158da7f" />
Install & Play
bash# Clone the repo
git clone https://github.com/Ashvin-Shiyani/alien-invasion-game.git
cd alien-invasion-game

# Install pygame
pip install pygame

# Run the game
python main.py is the main file and you will need all the files to run the game.
And please try to keep all the files in one folder for a smooth experience.

What I Learned & Skills I Explored
Object-Oriented Programming (OOP)

Built multiple classes: Ship, Alien, Bullet, Scoreboard, Button, GameStats
Used inheritance — Alien, Bullet, and Ship all inherit from pygame's Sprite class
Understood __init__, self, instance variables, and method calls across classes

Python Fundamentals

Nested for loops — used to generate the alien fleet grid
Float vs int — stored positions as floats for smooth movement
Variable scope — debugged classic loop variable shadowing bugs
Conditional logic — game state management with game_active flag

Pygame Library

Sprite groups — used pygame.sprite.Group to manage fleets and bullets
Collision detection — groupcollide() and spritecollideany() for hit detection
Event handling — keyboard and mouse input with pygame.event.get()
Rendering pipeline — learned the blit() pattern: what and where
Screen refresh loop — game loop with pygame.display.flip()
Image scaling — pygame.transform.scale() for resizing ship icons

Game Architecture

Separated concerns into modules: game_functions.py, Settings.py, game_stats.py, scoreboard.py
Understood game loop structure — event handling → update → render
Managed game state cleanly with a dedicated GameStats class
Built a dynamic settings system with speed scaling across levels

Debugging Skills

Traced and fixed a loop variable shadowing bug that caused aliens to stack in one column
Diagnosed pygame event starvation causing game freeze instead of exit
Fixed position sync issues between alien.x and alien.rect.x
Identified score reset order bugs affecting high score tracking

Git & Version Control

Initialized a local git repository

All the game settings, stats, function and images are available for your, please feel free to fork my repo, run the game change the settings, play around the game and please let me know if you find any bugs.
Thanks
Connected to a remote GitHub repo
Resolved merge conflicts and pushed code successfully
