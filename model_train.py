import parameters as pr

# define model
def create_keras_model():
    model = pr.keras.Sequential([
        pr.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        pr.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])
    return model
