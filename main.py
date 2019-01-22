import numpy as np

import syntheticChrissAlmgren as sca
from ddpg_agent import Agent
from workspace_utils import keep_awake
from collections import deque

# Create simulation environment
env = sca.MarketEnvironment()

# Initialize Feed-forward DNNs for Actor and Critic models. 
agent = Agent(state_size=env.observation_space_dimension(), action_size=env.action_space_dimension(), random_seed=0)

# Set the liquidation time
lqt = 60

# Set the number of trades
n_trades = 60

# Set trader's risk aversion
tr = 1e-6

# Set the number of episodes to run the simulation
episodes = 10000

shortfall_hist = np.array([])
shortfall_deque = deque(maxlen=100)


for episode in keep_awake(range(episodes)): 
    # Reset the enviroment
    cur_state = env.reset(seed = episode, liquid_time = lqt, num_trades = n_trades, lamb = tr)

    # set the environment to make transactions
    env.start_transactions()

    for i in range(n_trades + 1):
      
        # Predict the best action for the current state. 
        action = agent.act(cur_state, add_noise = True)
        
        # Action is performed and new state, reward, info are received. 
        new_state, reward, done, info = env.step(action)
        
        # current state, action, reward, new state are stored in the experience replay
        agent.step(cur_state, action, reward, new_state, done)
        
        # roll over new state
        cur_state = new_state

        if info.done:
            shortfall_hist = np.append(shortfall_hist, info.implementation_shortfall)
            shortfall_deque.append(info.implementation_shortfall)
            break
        
    if (episode + 1) % 100 == 0: # print average shortfall over last 100 episodes
        print('\rEpisode [{}/{}]\tAverage Shortfall: ${:,.2f}'.format(episode + 1, episodes, np.mean(shortfall_deque)))        

print('\nAverage Implementation Shortfall: ${:,.2f} \n'.format(np.mean(shortfall_hist)))