import numpy as np
import tensorflow as tf
import time

from env import Gym
import rlmodel

import hparams as hp


model = rlmodel.RLModel()
model.load_weights(hp.checkpoint_dir)

env = Gym()

def maxs(x, y):
    if x> y:
        return 0
    else:
        return 1


print("episode start")
time.sleep(3)
env.press_key(1)

observation, done = env.start()
while not done:
    action = model(np.array([observation]))
    p = np.array(action)
    print("p=",p)
    actions.append(maxs(p[0][0],p[0][1]))
    action = env.transform(action, env.state)
    next_observation, reward, done, info = env.step(action)

    observation = next_observation
print("episode end")
