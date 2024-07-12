Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import tensorflow as tf
... from tensorflow.keras import layers, models, preprocessing
... image_data_generator = preprocessing.image.ImageDataGenerator(rescale=1./255)
... 
... train_data_generator = image_data_generator.flow_from_directory(
...     '/content/drive/MyDrive/Colab Notebooks/dataset/train',
...     target_size=(64, 64),  # Resize images to 64x64 pixels
...     batch_size=32,
...     class_mode='categorical'
... )
... 
... validation_data_generator = image_data_generator.flow_from_directory(
...     '/content/drive/MyDrive/Colab Notebooks/dataset/test',
...     target_size=(64, 64),
...     batch_size=32,
...     class_mode='categorical'
... )
... model = models.Sequential([
...     layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
...     layers.MaxPooling2D((2, 2)),
...     layers.Conv2D(64, (3, 3), activation='relu'),
...     layers.MaxPooling2D((2, 2)),
...     layers.Conv2D(128, (3, 3), activation='relu'),
...     layers.MaxPooling2D((2, 2)),
...     layers.Flatten(),
...     layers.Dense(128, activation='relu'),
...     layers.Dense(33, activation='softmax')  
... ])
... 
... model.compile(optimizer='adam',
...               loss='categorical_crossentropy',
...               metrics=['accuracy'])
... model.fit(
...     train_data_generator,
...     steps_per_epoch=len(train_data_generator),
...     epochs=10,
    validation_data=validation_data_generator,
    validation_steps=len(validation_data_generator)
)
# Saving the model
model_json = classifier.to_json()
with open("model-bw.json", "w") as json_file:
    json_file.write(model_json)
