import re

class Game:
    def __init__(self):
        self.scores_for_moves = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
        self.equal_moves = {"A": "X", "B": "Y", "C": "Z"}                    
        self.winning_moves = {"A": "Y", "B": "Z", "C": "X"}
        self.losing_moves = {"A": "Z", "B": "X", "C": "Y"}

    def part_one(self):
        score = 0
        with open('input.txt', 'r') as f:
            input = f.read().split("\n")
            for round in input:
                round_score = 0
                opponent, player = round[0], round[-1]
                round_score += self.scores_for_moves[player]
                if self.equal_moves[opponent] == player: #draw
                    round_score += 3
                elif (player == "X" and opponent == "C") or (player == "Y" and opponent == "A") or (player == "Z" and opponent == "B"):
                    round_score += 6 
                score += round_score
        return score
    
    def part_two(self):
        score = 0
        with open('input.txt', 'r') as f:
            input = f.read().split("\n")
            for round in input:
                round_score = 0
                opponent, outcome = round[0], round[-1]
                if outcome == "X": # lose
                    move = self.losing_moves[opponent]
                    round_score += self.scores_for_moves[move]
                elif outcome == "Y": # draw
                    round_score += self.scores_for_moves[opponent] + 3
                elif outcome == "Z":
                    move = self.winning_moves[opponent]
                    round_score += self.scores_for_moves[move] + 6  
                    
                score += round_score
        return score                

if __name__ == '__main__':
    print('Score in part one:', Game().part_one())
    print('Score in part two:', Game().part_two())