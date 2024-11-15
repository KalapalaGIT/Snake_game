# 🐍 Snake Game

This is a classic Snake game built using Python and the Turtle graphics library. The game features a simple yet interactive UI where players control a snake to eat food and grow in size. The objective is to achieve the highest score without colliding with the walls or the snake's own body. The game saves your highest score in a `highscore.txt` file for future sessions.

## 🌟 Features

- **Classic Gameplay**: Enjoy the traditional snake game experience with smooth controls.
- **High Score Tracking**: The game saves your high score to `highscore.txt` and displays it during each session.
- **Modular Codebase**: Organized into multiple Python files for better readability and maintainability.

## 🗂️ Project Structure

```
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── highscore.txt
└── README.md
```

- **main.py**: The main file to run the game.
- **snake.py**: Handles the snake's movement and collision logic.
- **food.py**: Manages the creation and placement of food items.
- **scoreboard.py**: Displays and updates the current and high scores.
- **highscore.txt**: Stores the highest score achieved in the game.

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.6 or higher installed on your machine.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Install the Turtle graphics library**:
   - The Turtle library is usually included with Python's standard installation. However, if needed, you can install it using:
     ```bash
     pip install PythonTurtle
     ```

3. **Run the game**:
   ```bash
   python main.py
   ```

### Controls

- **Arrow Keys**: Use the Up, Down, Left, and Right arrow keys to control the snake's movement.

## 📈 High Score

Your highest score is automatically saved in the `highscore.txt` file. Each time you beat your previous high score, it gets updated, so you can keep challenging yourself to improve.

## 🔮 Future Plans
- **AI Integration**: Implement an AI agent to play the game autonomously. The AI could use various techniques, such as:
  - **Reinforcement Learning**: Training an agent to learn optimal strategies by maximizing the score.
  - **Search Algorithms**: Using pathfinding algorithms like A* or BFS to navigate the snake and avoid collisions.
  - **Genetic Algorithms**: Evolving a population of strategies to find the best-performing AI.
