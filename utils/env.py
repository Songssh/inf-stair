import numpy as np
from time import sleep
import keyboard
import random
from mss import mss

import hparams as hp



def get_pixel_rgb(x, y):
    with mss() as sct:
        screenshot = sct.grab({'top': y, 'left': x, 'width': 1, 'height': 1})
        ar = np.array(screenshot)[0][0][:3]
        t = [ar[2], ar[1], ar[0]]
        return t  # RGB values

class Stair:
    @staticmethod
    def pixels(x:int, y:int, num:int= hp.num_sample) -> list:
        vals = []
        for _ in range(num):
            new_x = x + random.randint(hp.pad, hp.stair_x_len-hp.pad)
            new_y = y + random.randint(hp.pad, hp.stair_y_len-hp.pad)
            #pixel = pgi.pixel(new_x, new_y) # tuple : (204, 255, 34)
            pixel = get_pixel_rgb(new_x, new_y)
            #vals.append((pixel[0] + pixel[0]+ pixel[0])/3)
            vals.append(pixel[0]/255.0)
            vals.append(pixel[1]/255.0)
            vals.append(pixel[2]/255.0)

        """for _ in range(num):
            new_x = 281 + random.randint(hp.pad, hp.stair_x_len)
            new_y = 552 + random.randint(hp.pad, hp.stair_y_len)
            pixel = pgi.pixel(new_x, new_y) # tuple : (204, 255, 34)
            vals.append((pixel[0] + pixel[0]+ pixel[0])/3)"""
        return vals
    
    @staticmethod
    def press_key(key:int, encode=hp.keys):
        #return pgi.press(encode[key])
        #return keyboard.press_and_release(encode[key])
        return keyboard.send(encode[key])

    @staticmethod
    def transform(key:int, state:bool)->int:
        key = np.array(key)
        if key[0][0] <= key[0][1]:
            if state:
                return 1
            else:
                return 0
        else:
            if state:
                return 0
            else:
                return 1

    @staticmethod
    def is_end():
        def check(pixel):
            #if (pixel[0] == hp.end_rgb[0] and\
            #    pixel[1] == hp.end_rgb[1] and\
            #    pixel[2] == hp.end_rgb[2]):
            if (pixel[0] == hp.end_rgb[0] and pixel[1] == hp.end_rgb[1]):
                return False
            return True
            
        #pix = pgi.pixel(hp.end_x, hp.end_y)
        pix = get_pixel_rgb(hp.end_x, hp.end_y)
        if check(pix):
            return True
        return False
        

class Gym(Stair):
    def __init__(self):
        self.observation = self.reset()

    def reset(self):
        observation = []
        self.score = 0
        self.state = True
        return observation

    def start(self):
        self.score = 0
        self.state = True
        sleep(3)
        self.press_key(1)
        sleep(0.5)
        observation = self.pixels(hp.stair_x, hp.stair_y)
        return observation, False

    def step(self, action):
        key = action
        self.press_key(key)
        sleep(0.05)
        if key == 0:
            self.state = not self.state

        done = self.is_end()
        if not done:
            self.observation = self.pixels(hp.stair_x, hp.stair_y)
            self.score += 1
            info = f"cur score: {self.score}"
        else:
            info = f"end score: {self.score}"

        return self.observation, self.score, done, info


def test():
    pass

if __name__ == "__main__":
    test()










