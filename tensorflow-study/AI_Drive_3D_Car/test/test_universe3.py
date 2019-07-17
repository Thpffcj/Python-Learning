# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-02-10.

"""
测试 Gym 和 Universe 环境是否正确安装
"""

import random
import gym
import universe

env = gym.make('flashgames.NeonRace-v0')  # 创建 NeonRace 的环境
env.configure(remotes=1)  # 自动创建一个本地的 Docker 容器
observation_n = env.reset()  # 重置环境，并且返回初始的 Observation

# 左转和右转
goleft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),
        ('KeyEvent', 'ArrowRight', False)]
goright = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
         ('KeyEvent', 'ArrowRight', True)]

# 向前加速
boostforward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowRight', False),
       ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'n', True)]

sum_reward = 0
turn = 0
rewards = []
buffer_size = 100
action = boostforward

while True:
    turn -= 1
    if turn <= 0:
        action = boostforward
        turn = 0
    # 根据速度来选择 action
    action_n = [action for ob in observation_n]

    # 实行 action，返回细分的多个参数
    observation_n, reward_n, done_n, info = env.step(action_n)

    sum_reward += reward_n[0]

    rewards += [reward_n[0]]
    # 如果卡住了，尝试向某一个方向开一会
    if len(rewards) >= buffer_size:
        mean = sum(rewards) / len(rewards)

        if mean == 0:
            turn = 25
            if random.random() < 0.5:
                action = goleft
            else:
                action = goright

        rewards = []

    env.render()