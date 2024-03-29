from keras.preprocessing.image import ImageDataGenerator
import os
datagen = ImageDataGenerator(
        rotation_range=30,
        width_shift_range=0.1,
        height_shift_range=0.1,
        rescale=1./255,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        zca_epsilon=1e-6,
        brightness_range=(0.1,1.5),
        fill_mode='nearest')
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import array_to_img
from tensorflow.keras.utils import load_img
#directory=len(os.listdir("C:\\Users\\sures\\Downloads\\archive\\train\\che"))
#print(directory)
for j in range(503,674):
        n=str(j)
        img = load_img('C:\\Users\\sures\\Downloads\\archive\\train\\ha\\'+'he'+n+'.jpg')
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        i = 0
        for batch in datagen.flow(x, batch_size=1,
			  save_to_dir='C:\\Users\\sures\\Downloads\\archive\\train\\ha', save_prefix='aug', save_format='jpg'):
                i += 1
                if i > 10:
                        break
