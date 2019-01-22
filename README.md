# Actor_Critic-Method-for-Financial-Trading


## Implementation of the DDPG algorithm for Automatic Finance Trading

In this project, I implemented the DDPG algorithm to solve the optimization problem of large portfolio transactions. This is an example of how Deep Reinforcement Learning can be used to solve real-world problems by simulating the problem in the form of an environment. Just like the various Deep RL algorithms, for example, DQN, DDPG and Multi-Agent DDPG algorithms are used to solve tasks related to robotics, gaming or even Autonomous Car Driving, these algorithms can be used to solve many supervised learning problems by properly formulating the tasks into an environment. 

The 'environment' is basically a python class having methods and attributes releted to the task. It generates 'States' for an Agent. The agent is a class that follows one of the above algorithms. The agent then generates 'Actions' and gets rewarded based on that action. The important thing is to define carefully the 'State', 'Action' and 'Reward' for the environment based on the problem.

In this repository, I will show how this can be done for a finance related problem. 

## Simulation Environment
The simulation environment generates random stock prices based on the Geometric Brownian Motion. The task is to determine the optimal number of shares to sell at a particular time in order to minimize expected shortfall for the trader. 

In order to solve this problem through reinforcement learning, we need to restate the optimal liquidation problem in terms of States, Actions, and Rewards. 

### State

In order to get an optimal trading weights, our state vector must tell us how many shares are remaining to be sold and how much time is remaining to sell them. By showing the number of trades remaining, we will know about the time remaining to sell the remaining shares. We also need to know what the stock price trend was in the recent past to determine current strategy. Hence we will also include log returns of past five trades. The state vector looks as follows - 

```[r<sub>(t-5)</sub>,r<sub>(t-4)</sub>,r<sub>(t-3)</sub>,r<sub>(t-2)</sub>,r<sub>(t-1)</sub>,r<sub>t</sub>, M<sub>t</sub>, I<sub>t</sub> ]``` where 

- r(t-i) = normalized log return at time t-i.
- Mt = number of trades remaining at time t, normalized by total number of trades.
- It = number of shares remaining to sell at time t, normalized by total number of shares.

Please note that more stock related parameters can be added to the state like leading or lagging financial indicators.

## Action










I used the Almgren and Chriss model to 
In order to train our DDPG algorithm we will use a very simple simulated trading environment. This environment simulates stock prices that follow a discrete arithmetic random walk and that the permanent and temporary market impact functions are linear functions of the rate of trading, just like in the Almgren and Chriss model. This simple trading environment serves as a starting point to create more complex trading environments. You are encouraged to extend this simple trading environment by adding more complexity to simulte real world trading dynamics, such as book orders, network latencies, trading fees, etc...

The simulated enviroment is contained in the syntheticChrissAlmgren.py module. You are encouraged to take a look it and modify its parameters as you wish. Let's take a look at the default parameters of our simulation environment. We have set the intial stock price to be  𝑆0=50 , and the total number of shares to sell to one million. This gives an initial portfolio value of  $50  Million dollars. We have also set the trader's risk aversion to  𝜆=10−6 .

The stock price will have 12% annual volatility, a bid-ask spread of 1/8 and an average daily trading volume of 5 million shares. Assuming there are 250 trading days in a year, this gives a daily volatility in stock price of  0.12/250⎯⎯⎯⎯⎯⎯√≈0.8% . We will use a liquiditation time of  𝑇=60  days and we will set the number of trades  𝑁=60 . This means that  𝜏=𝑇𝑁=1  which means we will be making one trade per day.

For the temporary cost function we will set the fixed cost of selling to be 1/2 of the bid-ask spread,  𝜖=1/16 . we will set  𝜂  such that for each one percent of the daily volume we trade, we incur a price impact equal to the bid-ask spread. For example, trading at a rate of  5%  of the daily trading volume incurs a one-time cost on each trade of 5/8. Under this assumption we have  𝜂=(1/8)/(0.01×5×106)=2.5×10−6 .

For the permanent costs, a common rule of thumb is that price effects become significant when we sell  10%  of the daily volume. If we suppose that significant means that the price depression is one bid-ask spread, and that the effect is linear for smaller and larger trading rates, then we have  𝛾=(1/8)/(0.1×5×106)=2.5×10−7 .

The tables below summarize the default parameters of the simulation environment

