import pandas as pd
import numpy as np
np.random.seed(24)
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [1.32921, -1.07082, -1.6264, 0.961538, np.nan, -1.33694, 0.121668, 0.354493, 1.68658, -0.12982],
    'C': [np.nan, -1.43871, 0.219565, 0.104011, 1.05774, 0.562861, 1.2076, 1.03753, -1.32596, 0.631523],
    'D': [-0.31628, 0.564417, 0.678805, np.nan, 0.165562, 1.39285, -0.00204021, -0.385684, 1.42898, -0.586538],
    'E': [-0.99081, 0.295722, 1.88927, 0.850229, np.nan, -0.063328, 1.6278, 0.519818, -2.08935, np.nan]
}
df = pd.DataFrame(data)
def color_negative_red(val):
    color = 'red' if pd.isnull(val) else 'black'
    return 'color: %s' % color

styled_df = df.style.applymap(color_negative_red)
styled_df
