# Alien Invasion Game Project
I created this Python project to improve my Python skills and expand my understanding of Git and GitHub. This project also served as an opportunity to practice coding across multiple devices while collaborating with Git.

## Inspiration and Learning Resources
This project was inspired by and guided by the following resources:

- [Clear Code YouTube Channel](https://www.youtube.com/@ClearCode "Clear Code")
- *Python Crash Course* (2nd Edition) by Eric Matthes

## Game Overview
Alien Invasion is a 2D arcade-style game built using Python and Pygame. The player controls a spaceship and must shoot down incoming alien squadrons while avoiding collisions. The game increases in difficulty as the player progresses, with aliens becoming faster and more challenging.

<img src="https://github.com/user-attachments/assets/fa1c9e2f-6aab-4feb-a46a-aabe85859968" alt="Sample Image" width="1000">
<img src="https://github.com/user-attachments/assets/c9d68968-ac25-4bb6-8650-0967f4e89a95" alt="Sample Image" width="400">
<img src="https://github.com/user-attachments/assets/c4fb7d54-06a9-442c-8a8b-3099a5e39fe9" alt="Sample Image" width="400">



## Features
- Player-controlled spaceship with movement in four directions
- Shooting mechanics using bullets
- Alien squadrons that move and descend toward the player
- Score tracking and level progression
- Play button to start the game
- Game over condition when aliens reach the bottom or collide with the spaceship

## Installation and Setup
### Prerequisites
Ensure you have Python installed on your system. You also need to install Pygame:
```sh
pip install pygame
```

### Running the Game
1. Clone the repository:
```sh
git clone https://github.com/Othmaneelmo/AlienInvasion.py.git
```
2. Navigate to the project directory:
```sh
cd AlienInvasion
```
3. Run the game:
```sh
python AlienInvasion.py
```

## Controls
- **Arrow Keys (←, →, ↑, ↓) or WASD**: Move the spaceship
- **Spacebar**: Fire bullets
- **Backspace**: Quit the game
- **Mouse Click on Play Button**: Start a new game

## Project Structure
```sh
├── alien_invasion.py   # Main game file
├── settings.py         # Game settings and configurations
├── ship.py            # Player spaceship class
├── bullet.py          # Bullet mechanics
├── alien.py           # Alien behavior and movement
├── game_stats.py      # Game state tracking
├── button.py          # Play button functionality
├── scoreboard.py      # Score display system
└── README.md          # Project documentation
```

## Future Improvements
- Add sound effects and background music
- Introduce power-ups and new enemy types
- Implement a high-score saving system
- Add animations for explosions and ship movement

## Contributions
Feel free to fork the repository and contribute by submitting pull requests. Any suggestions or feedback are welcome!

## License
This project is for educational purposes and is open for modification and learning.

---
Enjoy playing Alien Invasion! 🚀👾

