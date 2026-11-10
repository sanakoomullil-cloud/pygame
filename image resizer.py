import numpy as np
import random


img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)


sizes = [(random.randint(10, 200), random.randint(10, 200)) for _ in range(3)]

for i, (w, h) in enumerate(sizes, start=1):
    rows = np.linspace(0, 99, num=h).astype(int)
    cols = np.linspace(0, 99, num=w).astype(int)
    
    resized = img[rows[:, None], cols, :]
    print(f"Resized {i}: {w}x{h} -> New Matrix Shape: {resized.shape}")
