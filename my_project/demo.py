import tensorflow as tf


# Model taken from https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.py


def run_mnist():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = tf.expand_dims(x_train / 255., 3).numpy()
    x_test = tf.expand_dims(x_test / 255., 3).numpy()
    y_train = tf.keras.backend.one_hot(y_train, 10).numpy()
    y_test = tf.keras.backend.one_hot(y_test, 10).numpy()

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32,
                                     kernel_size=(3, 3),
                                     activation='relu',
                                     input_shape=(28, 28, 1)))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(loss=tf.keras.losses.categorical_crossentropy,
                  optimizer=tf.keras.optimizers.Adadelta(),
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              batch_size=64,
              epochs=20,
              verbose=1,
              validation_data=(x_test, y_test))
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])


if __name__ == '__main__':
    run_mnist()
