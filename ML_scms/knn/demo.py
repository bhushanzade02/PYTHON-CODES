# import numpy as np

# # 6 rows, 2 columns
# random_matrix = np.random.rand(6, 2)
# print(random_matrix)



import numpy as np
import pandas as pd

# Data
df = pd.DataFrame({
    'x1': [0.6, 0.1],
    'x2': [0.2, 0.3]
})

# Centroid
c1, c2 = 0.5, 0.65

# Euclidean distance to centroid
df['distance'] = np.sqrt((df['x1'] - c1)**2 + (df['x2'] - c2)**2)

print(df)
