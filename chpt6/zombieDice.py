# zombiedicebots
# zombies eat as many brains as possible without getting shot 3 times
# a cup of 13 dice, each with brains, footsteps, and shotgun
# each dice is colored
# Green dice have more brains
# red dice have more shotguns
# yellow dice have even split of brains / shotguns
# every die has 2 footstep sides

# Steps to play:
#1. Player selects 3 random dice and rolls (always roll THREE dice)
#2. Count brains and shotguns. Each brain is 1 point.
#   3 shotguns: turn ends, all acuumulated brain-points discarded
#   0-2 shotguns: the player can continue to roll to get more brains
#3. If they continue to roll dice,
#   they must use every die that came up as "footsteps"
#   they must roll 3 dice: if number of dice is > 3, they must draw extra dice
#   Able to  roll dice until all 13 dice have been rolled,
#   or 3 shotguns come up and the player loses all points accumulated that turn
#4. If someone reaches 13 brains, their turn ends and the other players finish.
#   The person with the most brains wins.
#   If there's a tie, the tied players play a tiebreaker round



import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        originalbot='''
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
                '''
        bot0 = '''#suicidal bot only wants 3 shotguns
        brains = 0
        shotgun = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']
            if shotgun < 3:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break'''
        #after the first roll, randomly decides if it will continue or stop
        bot1 = '''tails = 0
        heads = 0
        import random
        while diceRollResults is not None:
            coin = random.randint(0,1)
            if coin == 0:
                heads += 1
                print("Heads: " + str(heads))
                diceRollResults = zombiedice.roll() # roll again
            if coin == 1:
                tails += 1
                print("Tails: "+str(tails))
                break'''
        #stops rolling after it has rolled two brains
        bot2 = '''
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break'''
        #stops rolling after it has rolled two shotguns
        bot3 = '''
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break'''

        #initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
        shotgun = 0
        dicerollnumber = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            dicerollnumber += 1
            if shotgun < 2 & dicerollnumber < 4:
                diceRollResults = zombiedice.roll() # roll again
            else:
                print('Number of rolls: '+ str(dicerollnumber))
                break
        #stops rolling after it has rolled more shotguns than brains


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
