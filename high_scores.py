class High_Scores:

    MAX_NUM_HIGHSCORES = 5

    high_scores = []

    def __init__(self):
        self.read_highscores()


    def add_highscore(self, new_score):
        # Add right away if the max number of high scores was not exceeded
        if len(self.high_scores) < self.MAX_NUM_HIGHSCORES:
            self.high_scores.append(new_score)
        else:
            # Sort: smallest first
            self.high_scores.sort()
            for score in self.high_scores:
                if new_score > score:
                    self.high_scores.remove(score)
                    self.high_scores.append(new_score)
                    return True
        return False


    def get_highscores(self):
        # Sort: largest first
        self.high_scores.sort(reverse=True)
        return self.high_scores


    def write_highscores(self):
        file = open("highscores.txt", "w")
        for score in self.high_scores:
            line = str(score) + "\n"
            file.write(line)
        file.close()


    def read_highscores(self):
        file = open("highscores.txt", "r")
        for score in file:
            if score is not None:
                self.add_highscore(int(score))
