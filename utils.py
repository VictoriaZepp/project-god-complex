import random
import config

def random_num():                         
    if config.seed is not None:
        random.seed(config.seed)
    return random



