import argparse
import sys
import time
# import pdb
import gym
import math
import random
import numpy
from gym import wrappers, logger

class Agent(object):
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space
        self.shootList = []
        self.moveList = []
        self.diagonalShoot = []
        self.diagonalMove = []

    # You should modify this function
    def act(self, observation, reward, done):
        """
        :param observation:
        :param reward:
        :param done:
        :return: actions to be performed
        """

        # A number is randomly choosen from numbers 1, 2, 3, 4 with the probability of 0.6, 0.4, 0.0, 0.0 respectively
        x = numpy.random.choice([1, 2, 3, 4], p=[0.6, 0.4, 0.0, 0.0])

        if x == 1:  #If the random chosen number is 1

            #A number from 10, 11, 12 ,13 with probabilities to be chosen as 0.3, 0.3, 0.2, 0.2 will be returned randomly. These
            #are the numbers which will fire up, right, left or down
            return numpy.random.choice([10, 11, 12, 13], p=[0.3, 0.3, 0.2, 0.2])

        elif x == 2:#If the random chosen number is 2

            # A number from 2, 3, 4 ,5 with probabilities to be chosen as 0.3, 0.3, 0.2, 0.2 will be returned randomly. These
            # are the numbers which will move the agent in up, right, left or down directions
            return numpy.random.choice([2, 3, 4, 5], p=[0.3, 0.3, 0.2, 0.2])

        elif x == 3: #If the random chosen number is 3

            # A number from 14, 15, 16, 17 with probabilities to be chosen as 0.3, 0.3, 0.2, 0.2 will be returned randomly. These
            # are the numbers which will fire upright, upleft, downright or downleft directions.
            return numpy.random.choice([14, 15, 16, 17], p=[0.3, 0.3, 0.2, 0.2])
        else:

            # A number from 2, 3, 4 ,5 with probabilities to be chosen as 0.3, 0.3, 0.2, 0.2 will be returned randomly. These
            # are the numbers which will move the agent in upright, upleft, downright or downleft directions
            return numpy.random.choice([6, 7, 8, 9], p=[0.3, 0.3, 0.2, 0.2])



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
    print("Your score: %d" % score)
    env.close()
