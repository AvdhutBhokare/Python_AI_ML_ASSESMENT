"""
Scenario 7: Image Augmentation Pipeline
Task: Use TensorFlow/Keras to create an image augmentation pipeline with random rotations (±20 degrees), 
horizontal flips, and zoom (0.2x).
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Create image augmentation pipeline
datagen = ImageDataGenerator(
    rotation_range=20,           # Random rotations ±20 degrees
    horizontal_flip=True,         # Random horizontal flips
    zoom_range=0.2               # Random zoom 0.2x
)

# Example input data - create a sample image
sample_image = np.random.rand(1, 224, 224, 3) * 255  # Single RGB image
sample_image = sample_image.astype('float32')

# Generate augmented images
augmented_images = []
iterator = datagen.flow(sample_image, batch_size=1)

for i in range(5):
    batch = iterator.next()
    augmented_images.append(batch[0])

# Output
print("Image Augmentation Pipeline Created")
print(f"Rotation Range: ±20 degrees")
print(f"Horizontal Flip: Enabled")
print(f"Zoom Range: 0.2x")
print(f"\nOriginal Image Shape: {sample_image.shape}")
print(f"Number of Augmented Images Generated: {len(augmented_images)}")
print(f"Augmented Image Shape: {augmented_images[0].shape}")
