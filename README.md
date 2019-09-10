# Automated-Bot-for-Atari-Bezerk
A reflexive agent and a randomized agent that could play Atari Bezerk Game

The project was to create two different agents:
1) Reduced Random agent: Agent which could shoot anywhere and move anywhere
2) Agent 1: Agent which could take action based on the changes in its environment

Reduced Random Agent:
  1) Reduced randomness ensures that diagonal movement and diagonal shooting is prevented. 
  2) It generates random moves in up, down, left and right directions with 40%  movement probability and 60 % shooting probability.
  3) It was observed that increasing shooting probability ensured that more threats in the immediate vicinity were eliminated. 
  4) This enabled safer movement and subsequently boosted the score. 
  5) The reason behind eliminating diagonal shooting was the low chance of enemy elimination  through random diagonal shots. 
  6) Also, enemies located diagonally do not pose immediate threat to the agent. 
  
Reflexive Agent(Greedy Method): Reflexive agent analyses the environment frame by frame to determine factors such as  player position, wall
positions and enemy locations. 
Then, based on those conditions, it takes a pre programmed series of steps to maximize the probability of a higher score.
The steps were as follows:
  1) Scan all the pixels in the observation frame.  
  2) Create lists to keep track of player, enemies, walls, score, background and enemy.  
  3) Append appropriate tuples (row, column) into the lists based on pixel RGB values.  
  4) Scans for enemies in players row, column and diagonals.  
  5) Checks for presence of wall between player and threat.  
  6) Shoots in appropriate direction.  
  7) Checks enemy list and repeats steps 4 to 7 if the list is not empty.  
  8) When enemy list is empty, player computes relative position with respect to exit.  
  9) Player moves towards exit and completes the level. 
  
I also tried to implement another approach using Deep Q network. But it wasn't a successfull approach.
Approach used:
  Q-Learning: 
    Q(s, a) = r + γ max ₐ ’(Q(s’, a’))
    1) The equation above states that the viability of a given pair of state and action is given by  the reward for that action summed
    with the reward for the action in a future state.
    2) I decided to use a neural network to converge on the best available state as given by the equation above. 
    
    
  Structure of the neural network: 
    1. Conv2D - Convolutional layer to extract features  
    2. Conv2D - Convolutional layer to reduce  
    3. Dense layer - relu activation 
    4. Dense layer - relu activation  
    5. Dense layer - output - softmax activation 
    
  State representation: Each frame would be converted to grayscale and reduced in size for  effective learning. 
    3 states would then be stacked. Reason for stacking states is so the neural net can infer the following properties:
              1 state = positions of objects 
              2 states = direction of travel of objects 
              3 states = acceleration 
              
  Apart from this we maintain a set of state, action, reward and next state tuples in memory.  These are used for a feature called
  experience replay. Experience replay allows the neural  net to learn from and minimize loss by using states that have already been
  played.

Reasons for failure of reinforcement learning agent implementation: 
1)  Could not represent the states effectively onto the neural network because of high amount of information contained in each state.





    



