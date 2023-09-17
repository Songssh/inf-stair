import hparams as hp
import rlmodel

import numpy as np
import tensorflow as tf
import random


ob = [[random.random() for i in range(10)] for j in range(9)]
ac = [random.randint(0,1) for i in range(9)]
model = rlmodel.RLModel()
optimizer = tf.keras.optimizers.Adam()
weight_dir = 'ckpt/test/model'

print(ob)
def test(observations, actions):
    global model, optimizer
    for epoch in range(hp.epochs):
        with tf.GradientTape() as tape:
            # 모델 예측
            logits = model(np.array(observations))
            probabilities = tf.nn.softmax(logits)
            # 선택한 행동에 대한 로짓 선택
            responsible_outputs = tf.gather(probabilities, actions, batch_dims=1)
            # 손실 계산
            loss_value = -tf.reduce_mean(tf.math.log(responsible_outputs))
            print(loss_value)

        # 그래디언트 계산
        grads = tape.gradient(loss_value, model.trainable_variables)
        # 모델 업데이트
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
    model.save_weights(weight_dir)

test(ob, ac)
