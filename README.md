# Actor_Critic-Method-for-Financial-Trading


## Implementation of the DDPG algorithm for Automatic Finance Trading

In this project, I implemented the DDPG algorithm to solve the optimization problem of large portfolio transactions. This is an example of how Deep Reinforcement Learning can be used to solve real-world problems by simulating the problem in the form of an environment. Just like the various Deep RL algorithms, for example, DQN, DDPG and Multi-Agent DDPG algorithms are used to solve tasks related to robotics, gaming or even Autonomous Car Driving, these algorithms can be used to solve many supervised learning problems by properly formulating the tasks into an environment. 

The 'environment' is basically a python class having methods and attributes related to the task. It generates 'States' for an Agent. The agent is a class that follows one of the above algorithms. The agent then generates 'Actions' and gets rewarded based on that action. The important thing is to define carefully the 'State', 'Action' and 'Reward' for the environment based on the problem.

In this repository, I will show how this can be done for a finance related problem. 

Please see the report.pdf file for full description.


