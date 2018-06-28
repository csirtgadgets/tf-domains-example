import os

BATCH_SIZE = os.getenv('BATCH_SIZE', 8)
MAX_STRING_LEN = 255
MODEL = os.getenv('MODEL', 'model.h5')
WEIGHTS = os.getenv('WEIGHTS', 'weights.h5')