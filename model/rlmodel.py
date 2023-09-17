import numpy as np
import tensorflow as tf

optimizer = tf.keras.optimizers.Adam()

class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.dense1 = tf.keras.layers.Dense(units=64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(units=32, activation='relu')
        self.dense3 = tf.keras.layers.Dense(units=2, activation='softmax')

    def convert(self, inputs):
        input_data = np.array(inputs) / 255.0
        input_data = input_data.flatten()
        input_data = tf.constant(input_data, dtype=tf.float32)
        input_data = tf.expand_dims(input_data, axis=0)
        return input_data

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        return self.dense3(x)

class RLModel(tf.keras.Model):
    def __init__(self):
        super(RLModel, self).__init__()
        self.dense1 = tf.keras.layers.Dense(units=64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(units=128, activation='relu')
        self.dense3 = tf.keras.layers.Dense(units=128, activation='relu')
        self.dense4 = tf.keras.layers.Dense(units=64, activation='relu')
        self.dense5 = tf.keras.layers.Dense(units=32, activation='relu')
        self.output_layer = tf.keras.layers.Dense(units=2, activation='softmax')

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        x = self.dense3(x)
        x = self.dense4(x)
        x = self.dense5(x)
        return self.output_layer(x)
