# Project Name: Reinforcement Learning Tic-Tac-Toe Agent

## Description:
This project implements a Tic-Tac-Toe game using reinforcement learning (Q-learning) to train an AI agent to play against a human player. The AI learns through interactions with the environment and gradually improves its gameplay strategy.

## Components:
- **TicTacToe Class**: Manages the game environment, tracks the game state, and checks for wins, draws, available moves, etc.
- **QLearningAgent Class**: Implements the Q-learning algorithm for the AI agent. Manages Q-values, chooses actions based on exploration-exploitation strategy, and updates Q-values based on rewards received.
- **play_game Function**: Runs a single game between the AI agent and the environment, facilitating learning and updating Q-values accordingly.
- **Main Function (main)**: Orchestrates the training process for the AI agent by running multiple episodes of the game. After training, it allows a user to play against the trained AI.

## Files Included:
- `tictactoe.py`: Contains the main code implementing the game logic, Q-learning agent, and gameplay functionalities.
- `README.md`: Provides an overview, instructions, and details about the project.

## Usage:
### Training the AI:
1. Run the `main()` function in `tictactoe.py` to initiate the training process for the AI agent.
2. Adjust the `num_episodes` variable to control the number of training episodes.

### Playing against the AI:
1. After training, the user can play against the trained AI by following the prompts displayed in the console.
2. Run the `main()` function and interact with the command-line interface to make moves against the AI.

## Requirements:
- Python 3.x
- NumPy library

## Setup Instructions:
1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed.
3. Create a virtual environment: `python3 -m venv venv_name`
4. Activate the virtual environment:
   - For Windows: `venv_name\Scripts\activate`
   - For macOS and Linux: `source venv_name/bin/activate`
5. Install the required dependencies (numpy): `pip install numpy`
6. Run `python tictactoe.py` to start the program.

## Additional Notes:
- Feel free to explore and modify the code as needed. Contributions, suggestions, and improvements are welcome. 
- If you encounter any issues or have questions, please create an issue in the repository.

## Author:
Youssef Baghrous

## License:
This project is licensed under the MIT License.
