# %%
import tensorflow as tf


# %%
def mnist_digit_data():
    (train_images, train_labels), (
        test_images,
        test_labels,
    ) = tf.keras.datasets.mnist.load_data()
    return train_images, train_labels, test_images, test_labels


# %%
def mnist_model():
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation="softmax"),
            tf.keras.layers.Dense(10),
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
