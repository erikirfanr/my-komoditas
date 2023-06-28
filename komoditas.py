import pandas as pd

komoditas = {
    'elevasi' : [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900],
    'tipe_lahan' : [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    'komoditas' : [1, 1, 1, 2, 3, 2, 1, 3, 4, 4, 4, 5, 5, 5]
}

komoditas_df = pd.DataFrame(komoditas)

import numpy as np

x_train = np.array(komoditas_df[['elevasi', 'tipe_lahan']])
y_train = np.array(komoditas_df['komoditas'])

print(x_train)
print(y_train)

X_transpossed = np.transpose(x_train)
print(X_transpossed)

x_binarized = X_transpossed.flatten()
print(x_binarized)

x_train = X_transpossed.transpose()
print(x_train)

from sklearn.neighbors import KNeighborsRegressor

K = 3
model = KNeighborsRegressor(n_neighbors=K)
model.fit(x_train, y_train)

x_new = np.array([[1500, 2]])
y_pred = model.predict(x_new)

print(y_pred)

import pickle

with open('komoditas.pkl','wb') as file:
    pickle.dump(model,file)
