class VotingMachine:
    def __init__(self):
        self.democrat_votes = 0
        self.republican_votes = 0

    def vote_democrat(self):
        self.democrat_votes += 1

    def vote_republican(self):
        self.republican_votes += 1

    def clear_votes(self):
        self.democrat_votes = 0
        self.republican_votes = 0

    def get_tallies(self):
        return {"Democrat": self.democrat_votes, "Republican": self.republican_votes}


