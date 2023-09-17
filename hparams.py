# left
#   top: X:  132 Y:  554 RGB: (178, 128, 112)
#   bot: X:  200 Y:  589 RGB: ( 68,  51,  51)

# right
#   top: X:  281 Y:  552 RGB: (175, 173, 144)
#   bot: X:  348 Y:  589 RGB: ( 68,  51,  51)

# end
#   top: X:  391 Y:  759 RGB: (204,  34,  34)
#   bot: X:  416 Y:  782 RGB: (204,  34,  34)

stair_x = 142
stair_y = 555
stair_x_len = 190 - 142
stair_y_len = 583 - 555

end_x = 398
end_y = 775
end_rgb = (204,  34,  34)


# X:  363 Y:  377 RGB: (255, 170, 204)
# X:  250 Y:  650 RGB: (102,  17,   0)
#util_x = 
#util_y = 


keys = ['q', 'e']
num_sample = 15
pad = 10


use_ckpt = False
checkpoint_dir = 'ckpt/st/model'
epochs = 40

max_episode = 10000
