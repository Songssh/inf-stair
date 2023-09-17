import numpy as np
import tensorflow as tf
import time

from utils.env import Gym
from model import rlmodel
import hparams as hp

model = rlmodel.RLModel()
if hp.use_ckpt:
    print(f"loaded: {hp.checkpoint_dir}")
    model.load_weights(hp.checkpoint_dir)
optimizer = rlmodel.optimizer

env = Gym()

def maxs(x, y):
    if x> y:
        return 0
    else:
        return 1


for i in range(hp.max_episode):
    print(f"episode {i} start")
    time.sleep(3)
    env.press_key(1)
    observations = []
    actions = []
    rewards = []
    
    observation, done = env.start()
    #print(observation)
    while not done:
        action = model(np.array([observation]))
        p = np.array(action)
        print("p=",p)
        actions.append(maxs(p[0][0],p[0][1]))
        action = env.transform(action, env.state)
        next_observation, reward, done, info = env.step(action)

        observations.append(observation)
        #actions.append(action)
        rewards.append(reward)

        observation = next_observation

    actions[-1] = 0 if actions[-1] == 1 else 1
    
    print(f"episode {i} end")
    '''with open("test.txt", "w") as f:
        for i in range(len(actions)):
            text = f"{observations[i]}"
            f.writelines(text)
        f.write(f"{actions}")'''
    print(actions)
    if len(actions) == 0:
        continue
    
    for epoch in range(hp.epochs):
        with tf.GradientTape() as tape:
            logits = model(np.array(observations))
            probabilities = tf.nn.softmax(logits)

            responsible_outputs = tf.gather(probabilities, actions, batch_dims=1)
            
            loss_value = -tf.reduce_mean(tf.math.log(responsible_outputs))
            print(loss_value)


        grads = tape.gradient(loss_value, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

    #model.save_weights(hp.checkpoint_dir+ f"_{i}")
    model.save_weights(hp.checkpoint_dir)
    print("checkpoint was saved")

