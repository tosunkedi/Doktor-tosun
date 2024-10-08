import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from tensorflow.keras.utils import plot_model
import matplotlib.pyplot as plt

file_path = 'ah_kalbim.csv'
data = pd.read_csv(file_path)

x = data[['yas', 'cinsiyet', 'gogus_agrı_tipi', 'dinlenme_kan_basıncı',
           'Kolesterol', 'Aclık_Kan_Sekeri', 'Elektrokardiyografik_Ölcümü',
           'Ulasılan_maks_kalp_hızı', 'egzersize_baglı_durumu',
           'depresyon_ST', 'egim', 'ca', 'talasemi']].values

y = data[['amac']].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=3)

model = models.Sequential([
    layers.Dense(13, activation='relu', input_shape=(x_train.shape[1],)),
    layers.Dense(13, activation='relu'),
    layers.Dense(13, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy')

history = model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test), epochs=600, verbose=1)

modelkaybi = pd.DataFrame(history.history)
modelkaybi.plot()


tahminler = model.predict(x)
tahmin_siniflar = (tahminler > 0.5).astype(int)

dogruluk = np.mean(tahmin_siniflar == y)
print(tahmin_siniflar)
print("Doğruluk Oranı:", dogruluk)
