class player:
  def play(self):
    print("the player is playing cricket")

class batsman(player):
  def play(self):
    print("the bowler is bowling")

class bowler(player):
  def play(self):
    print("the bowler is bowling")

batsman=batsman()
batsman=bowler()

batsman=play()
batsman=play()