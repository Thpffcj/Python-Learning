# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-02-10.

import gym
import universe  # register the universe environments
from universe import wrappers

env = gym.make('gym-core.PongDeterministic-v0')
env = wrappers.experimental.SafeActionSpace(env)
env.configure(remotes=1)

observation_n = env.reset()

while True:
    action_n = [env.action_space.sample() for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()