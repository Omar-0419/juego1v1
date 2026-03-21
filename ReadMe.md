1. Project Description
This project is a Turn-Based Combat Simulator called "Terminal Souls". One player (the Hero) fights against one Monster (the Enemy). The goal is to defeat the enemy using attacks, magic, and items before your life (HP) reaches 0.

2.Proyect structure
For this proyect we used 2 two parts the code:
  -functions.py ---->	Contains all the game logic and rules.
  -main.py ----->	Controls the game loop and starts the battle.

3.Roles en responsabilities
  A.Developer lead ----> Omar Vizcaino -------> Created the game logic, damage system, and winner check.
  B.Scrum Master------> Kerlys bello-------> Organized the project tasks and technical documentation.

4.Technical Documentation
Module: 

  A.functions.py
     -generate_damage(min, max): Calculates a random number for attacks. It has a 10% chance for a Critical Hit (Double Damage).
     -turn_player(hp_h, hp_e, pots): Shows the menu (Attack, Heal, Special). It updates the life and potions.
     -is_game_active(hp_h, hp_e):  Checks if the Hero or the Enemy is dead (HP <= 0). It stops the game.
  B. Main.py
      -Game Loop: It uses a while loop with a variable called playing.

5. How to Run

-Clone the repository.
-Open your terminal.
-Run: python main.py

6.Challenger Dev.

  As a Dev, we have to confront many blockers, our team lost and chance new members, in order to this we consider a challenger :
  
    -Variable Order: When a function returns 3 values (hp_h, hp_e, pots), we must use the same order in the main file.
    -No Break Rule: We learned to control the while loop using a Boolean Flag (True/False). This makes the code cleaner.
    -Git Sync: Sometimes it was hard to upload the code from different computers, but we used the terminal to synchronize the repository.

7.Test cases

  you can provee some options
  
    -TC-01----> Critical Hit---->	Attack the Enemy.	Damage is doubled (2x). A message says "CRITICAL HIT!.
    -TC-02----> Healing	Use a Potion ----->Hero life increases by 20. Potions decrease by 1.
    -TC-03----> No Potions ----->	Use a Potion when potions = 0.	A message says "No stock". The player must choose another action.
    -TC-04---->Special Fail	Use Special Ability ---->If the random chance is < 50%, 0 damage is caused.	S
    -TC-05----> Hero Victory--Enemy HP reaches ----> 	The loop stops. A message says "You win!".	
    -TC-06----> Game Ove----Hero HP reaches 0.	 ---->The loop stops. A message says "You lose!".

 
8. Porpuse

We developed this project to practice:

-Python Logic: if/else, while loops, and functions.
-Random Systems: Using random.randint and probabilities.
-Teamwork: Using Git and Scrum to work together.



