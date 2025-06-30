import tensorflow as tf
from pathlib import Path
from cnnProject.entity.config_entity import TrainingConfig

class Training:
    def __init__(self,config:TrainingConfig):
        self.config=config
    
    def get_base_model(self):
        self.model=tf.keras.models.load_model(self.config.updated_base_model)
    
    #Imagine you're training a robot to identify fruit:
        #🥭 Train DataGenerator: You show it mangos in different lighting, angles, partially covered — so it learns to generalize.
        #✅ Validation DataGenerator: You show it clean, clear images of mangos — to check how well it learned.

    def train_valid_generator(self):
        datagenerator_kwargs=dict(rescale=1./255,validation_split=0.20)

        dataflow_kwargs=dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

        self.valid_generator=valid_datagenerator.flow_from_directory(directory=self.config.training_data,
                                                                     subset="validation",
                                                                     shuffle=False,
                                                                     **dataflow_kwargs)
        if self.config.params_is_augmentation:
            train_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator=valid_datagenerator

        self.train_generator=train_datagenerator.flow_from_directory(directory=self.config.training_data,
                                                                     subset="training",
                                                                     shuffle=True,
                                                                     **dataflow_kwargs)
        
    @staticmethod
    def save_model(path:Path,model:tf.keras.Model):
        model.save(path)

    def train(self):
        self.steps_per_epoch=self.train_generator.samples//self.train_generator.batch_size
        self.validation_steps=self.valid_generator.samples//self.valid_generator.batch_size

        self.model.fit(self.train_generator,
                       epochs=self.config.params_epochs,
                       steps_per_epoch=self.steps_per_epoch,
                       validation_steps=self.validation_steps,
                       validation_data=self.valid_generator)
        self.save_model(path=self.config.trianed_model_path,model=self.model)

# 🔧 1. Configuration Setup
# 🔹TrainingConfig dataclass holds all training-related parameters like:
# 		->Paths to models and data
# 		->Training hyperparameters (epochs, batch size, image size)
# 		->Whether to apply data augmentation
# 🔹ConfigurationManager class:
# 		->Reads config.yaml and params.yaml
# 		->Creates necessary directories
# 		->Combines config and params to return a TrainingConfig object

# 🧠 2. Training Class (Core Logic)
# 🔹 __init__: Takes TrainingConfig and stores it
# 🔹 get_base_model(): Loads a pre-trained model from the saved path (updated_base_model)
# 🔹 train_valid_generator(): 
# 		->Creates training and validation image generators:
# 			Uses ImageDataGenerator with rescale=1./255 and validation_split=0.2
# 		->Validation generator:
# 			No augmentation
# 			Used for evaluating model performance
# 		->Training generator:
# 			Uses augmentation (flip, rotate, zoom, etc.) if enabled
# 			Helps improve model generalization
# 🔹 train():Calculates:
# 		->steps_per_epoch = total training samples // batch size
# 		->validation_steps = total validation samples // batch size
# 		->Trains the model using .fit()
# 		->Saves the trained model to the specified path using save_model()
# 🔹 save_model(path, model): Static method to save the trained model to disk