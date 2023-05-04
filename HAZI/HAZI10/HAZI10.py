# %%
import tensorflow as tf


# %%
def mnist_digit_data():
    (train_images, train_labels), (
        test_images,
        test_labels,
    ) = tf.keras.datasets.mnist.load_data()
    train_images = train_images.reshape(60000, 784)
    test_images = test_images.reshape(10000, 784)
    train_images = train_images.astype("float32")
    test_images = test_images.astype("float32")
    train_images /= 255
    test_images /= 255
    return train_images, train_labels, test_images, test_labels


# %%
def mnist_model():
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(784,)),
            tf.keras.layers.Dense(512),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    return model


# %%
def model_compile(model):
    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        metrics=["accuracy"],
    )
    return model


# %%
def model_fit(model, epochs, train_images, train_labels):
    model.fit(train_images, train_labels, epochs=epochs)
    return model


# %%
def model_evaluate(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    return test_loss, test_acc
