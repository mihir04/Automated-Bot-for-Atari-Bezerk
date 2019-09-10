import argparse
import sys
import time
#import pdb
import gym
import math
from gym import wrappers, logger

class Agent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    # You should modify this function

    def act(self, observation, reward, done):
        while(True):
            player_rowsAndcolumns = []      #A list for player co-ordinates is created
            enemy_rowsAndcolumns = []       #A list for enemy co-ordinates is created
            wall_rowsAndcolumns = []        #A list for wall co-ordinates is created
            score_rowsAndcolumns = []       #A list for score co-ordinates is created
            background = []                 #A list for background co-ordinates is created
            player_left = 0
            player_right = 0
            player_head = 0
            player_foot = 0
            player_centroid = 0
            row = -1

            #The co-ordinates for player, enemy, wall, score, background is stored as tuples as (row, column) in their
            #respective lists.
            for r in observation:
                row += 1
                column = 0

                for c in r:
                    column += 1

                    if 240 in c:
                        player_rowsAndcolumns.append((row, column))

                    elif 84 in c:
                        wall_rowsAndcolumns.append((row, column))

                    elif 232 in c:
                        score_rowsAndcolumns.append((row, column))

                    elif 0 in c:
                        background.append((row, column))

                    else:
                        enemy_rowsAndcolumns.append((row, column))


            if len(player_rowsAndcolumns) > 0:
                x_rows = []
                y_columns =[]
                for x, y in player_rowsAndcolumns:
                    x_rows.append(x)
                    y_columns.append(y)

                player_left = min(y_columns)
                player_right = max(y_columns)
                player_head = min(x_rows)
                player_foot = max(x_rows)

                player_centroid = (((player_head+player_foot)/2),((player_left+player_right)/2))
            return self.think(enemy_rowsAndcolumns, wall_rowsAndcolumns, player_left, player_right, player_head, player_foot, player_rowsAndcolumns)


    def think(self, enemy_rowsAndcolumns, wall_rowsAndcolumns, player_left, player_right, player_head, player_foot, player_rowsAndcolumns):
        """
        Description: This function will return the actions to be performed by the agents depending on where the threat is
        been detected. To detect the threat this function calls threatscan function and then returns the actions accordingly.

        :param enemy_rowsAndcolumns:
        :param wall_rowsAndcolumns:
        :param player_left:
        :param player_right:
        :param player_head:
        :param player_foot:
        :param player_rowsAndcolumns:
        :return: actions to be performed from [0 - 17]
        """
        threat = self.threatscan(enemy_rowsAndcolumns, wall_rowsAndcolumns, player_rowsAndcolumns)
        if threat == "up":
            return 10
        elif threat == "down":
            return 13
        elif threat == "right":
            return 11
        elif threat == "left":
            return 12
        elif threat == "upright":
            return 14
        elif threat == "downright":
            return 16
        elif threat == "upleft":
            return 15
        elif threat == "downleft":
            return 17
        elif threat == "empty":
            return self.move(wall_rowsAndcolumns, player_head, player_foot, player_left, player_right)
        else:
            return 0


    def threatscan(self, enemy_rowsAndcolumns, wall_rowsAndcolumns, player_rowsandcolumns):
        """
        Description: This function detects the direction in which the enemy is present. If enemy is found it will also check
        if there is any wall in between the agent and the enemy. If there is a wall it does not shoot else it shoots.
        :param enemy_rowsAndcolumns:
        :param wall_rowsAndcolumns:
        :param player_rowsandcolumns:
        :return: Strings(Directions in which enemy is present)  Empty(To determine if all enemies are killed or not)
        """

        self.flag = True
        for (x, y) in player_rowsandcolumns:
            for (a, b) in enemy_rowsAndcolumns:
                if y < b:
                    if x >= (a + 4) and x <= (a + 9):
                        for i in range(player_rowsandcolumns[0][1] + 5, b):
                            if (a, i) in wall_rowsAndcolumns:
                                self.flag = False
                                break
                        if self.flag is not False:
                            return "right"
                        else:
                            return None
                elif x > a:
                    if y >= (b - 5) and y <= (b + 10):
                        for i in range(player_rowsandcolumns[0][0] + 5, a):
                            if (i, b) in wall_rowsAndcolumns:
                                self.flag = False
                                break
                        if self.flag is not False:
                            return "up"
                        else:
                            return None
                elif y > b:
                    if x >= (a + 4) and x <= (a + 9):
                        for i in range(player_rowsandcolumns[0][1], b, -1):
                            if (a, i) in wall_rowsAndcolumns:
                                self.flag = False
                                break
                        if self.flag is not False:
                            return "left"
                        else:
                            return None
                elif x < a:
                    if y >= (b - 5) and y <= (b + 10):
                        for i in range(player_rowsandcolumns[-1][0] + 5, a):
                            if (i, b) in wall_rowsAndcolumns:
                                self.flag = False
                                break
                        if self.flag is not False:
                            return "down"
                        else:
                            return None
                elif abs((y - b)/(x - a)) is 1:
                    if (x > a) and (y < b):
                        return "upright"
                elif abs((y - b)/(x - a)) is 1:
                    if (x < a) and (y < b):
                        return "downright"
                elif abs((y - b)/(x - a)) is 1:
                    if (x > a) and (y > b):
                        return "upleft"
                elif abs((y - b)/(x - a)) is 1:
                    if (x > a) and (y > b):
                        return "downleft"
                else:
                    return None

        if len(enemy_rowsAndcolumns) == 0:
            return "empty"


    def move(self, wall_rowsAndcolumns, player_head, player_foot, player_left, player_right):
        """
        Description: This function is called after all the enemies are killed. Once the enemy list is empty this function
        will help the agent to decide in which direction should it move in order to exit the current level and move to the
        next level.

        :param wall_rowsAndcolumns:
        :param player_head:
        :param player_foot:
        :param player_left:
        :param player_right:
        :return: Movements to be done to reach the exit
        """
        self.rightflag = True
        self.upflag = True
        wall_rows = []
        wall_columns = []
        for x,y in wall_rowsAndcolumns:
            wall_rows.append(x)
            wall_columns.append(y)

        min_wall_row = 0
        max_wall_row = 0
        for i in range(len(wall_rows)):
            min_wall_row = min(wall_rows)
            max_wall_row = max(wall_rows)

        min_wall_column = 0
        max_wall_column = 0
        for j in range(len(wall_columns)):
            min_wall_column = min(wall_columns)
            max_wall_column = max(wall_columns)

        if player_foot >= (min_wall_row + 30):
            return 2
        elif player_right <= (max_wall_column + min_wall_column)/2:
            return 3
        elif player_left >= (max_wall_column + min_wall_column)/2:
            return 4
        else:
            return 2












## YOU MAY NOT MODIFY ANYTHING BELOW THIS LINE OR USE
## ANOTHER MAIN PROGRAM
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('--env_id', nargs='?', default='Berzerk-v0', help='Select the environment to run')
    args = parser.parse_args()

    # You can set the level to logger.DEBUG or logger.WARN if you
    # want to change the amount of output.
    logger.set_level(logger.INFO)

    env = gym.make(args.env_id)

    # You provide the directory to write to (can be an existing
    # directory, including one with existing data -- all monitor files
    # will be namespaced). You can also dump to a tempdir if you'd
    # like: tempfile.mkdtemp().
    outdir = 'random-agent-results'


    env.seed(0)
    agent = Agent(env.action_space)

    episode_count = 100
    reward = 0
    done = False
    score = 0
    special_data = {}
    special_data['ale.lives'] = 3
    ob = env.reset()
    while not done:
        action = agent.act(ob, reward, done)
        ob, reward, done, x = env.step(action)
        score += reward
        env.render()
     
    # Close the env and write monitor result info to disk
    print ("Your score: %d" % score)
    env.close()
