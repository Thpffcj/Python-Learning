# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-02-10.

import gym

env = gym.make('CartPole-v0')

for i_episode in range(100):
    observation = env.reset()
    for t in range(100):
        env.render() # 更新动画
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action) # 推进一步
        if done:
            env.reset()
            continue