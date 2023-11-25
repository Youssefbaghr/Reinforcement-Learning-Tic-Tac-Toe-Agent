import numpy as np
import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

    def reset(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def is_winner(self, player):
        for combo in self.winning_combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_draw()

    def available_moves(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def print_board(self):
        print("-------------")
        for i in range(3):
            print("|", self.board[3*i], "|", self.board[3*i+1], "|", self.board[3*i+2], "|")
            print("-------------")

class QLearningAgent:
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=1.0):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.q_values = {}
        self.prev_state = None
        self.prev_action = None

    def get_q_value(self, state, action):
        if (state, action) not in self.q_values:
            self.q_values[(state, action)] = 0.0
        return self.q_values[(state, action)]

    def update_q_value(self, state, action, reward, next_state):
        max_next_q_value = max([self.get_q_value(next_state, next_action) for next_action in range(9)])
        new_q_value = (1 - self.alpha) * self.get_q_value(state, action) + \
                      self.alpha * (reward + self.gamma * max_next_q_value)
        self.q_values[(state, action)] = new_q_value

    def choose_action(self, state, available_moves):
        if random.random() < self.epsilon:
            return random.choice(available_moves)
        else:
            q_values = [self.get_q_value(state, action) for action in available_moves]
            max_q_value = max(q_values)
            best_actions = [action for action, q_value in zip(available_moves, q_values) if q_value == max_q_value]
            return random.choice(best_actions)

    def act(self, env):
        state = tuple(env.board)
        available_moves = env.available_moves()
        action = self.choose_action(state, available_moves)
        self.prev_state = state
        self.prev_action = action
        return action

    def learn(self, reward, next_env):
        next_state = tuple(next_env.board)
        self.update_q_value(self.prev_state, self.prev_action, reward, next_state)

def play_game(agent, env):
    env.reset()
    while not env.is_game_over():
        action = agent.act(env)
        current_state = tuple(env.board)
        env.make_move(action)
        reward = 0
        if env.is_winner('X'):
            reward = 1
        elif env.is_winner('O'):
            reward = -1
        elif env.is_draw():
            reward = 0.5
        agent.learn(reward, env)

def main():
    agent = QLearningAgent()
    env = TicTacToe()
    num_episodes = 10000

    for episode in range(num_episodes):
        play_game(agent, env)

    print("Training completed!")

    # Play against the trained agent
    while True:
        env.reset()
        env.print_board()
        while not env.is_game_over():
            if env.current_player == 'X':
                action = int(input("Enter your move (0-8): "))
                while action not in env.available_moves():
                    print("Invalid move! Try again.")
                    action = int(input("Enter your move (0-8): "))
            else:
                action = agent.act(env)
                print("AI's move:", action)
            env.make_move(action)
            env.print_board()

        if env.is_winner('X'):
            print("Congratulations! You win!")
        elif env.is_winner('O'):
            print("AI wins!")
        else:
            print("It's a draw!")
        
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
