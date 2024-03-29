import tensorflow as tf

from ..utils import prepare_image_as_input
import os
from pathlib import Path


# This dataset is quite large so we can limit element count to speed up development
def load_dataset(batch_size=5, image_size=(256, 256)):
    dataset_dir = os.path.join(Path(os.getcwd()).parent, 'landscapes_small')
    dataset_train = tf.keras.preprocessing.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset='training',
        seed=321,
        batch_size=batch_size,
        image_size=image_size
    )

    dataset_test = tf.keras.preprocessing.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset='validation',
        seed=321,
        batch_size=batch_size,
        image_size=image_size
    )

    dataset_train = dataset_train\
        .shuffle(1000)\
        .map(prepare_image_as_input)\
        .prefetch(tf.data.experimental.AUTOTUNE)

    dataset_test = dataset_test\
        .shuffle(1000) \
        .map(prepare_image_as_input) \
        .prefetch(tf.data.experimental.AUTOTUNE)

    return dataset_train, dataset_test
