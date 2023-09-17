import numpy as np
import time

from utils.env import Gym
from model import rlmodel

import hparams as hp


model = rlmodel.RLModel()
model.load_weights(hp.checkpoint_dir)

env = Gym()

print("episode start")
time.sleep(3)
env.press_key(1)

observation, done = env.start()
while not done:
    action = model(np.array([observation]))
    p = np.array(action)
    print("p=",p)
    action = env.transform(action, env.state)
    next_observation, reward, done, info = env.step(action)

    observation = next_observation
print("episode end")
