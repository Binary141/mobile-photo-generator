import time
# import keras_cv
# from tensorflow import keras
# import matplotlib.pyplot as plt
# from PIL import Image
import uuid
import os
import torch
from diffusers import StableDiffusionPipeline

remoteImageURL = os.environ['remoteImageURL']
imageSaveLocation = os.environ['imageSaveLocation']
imageWidth = os.environ['imageWidth']
imageHeight = os.environ['imageHeight']
huggingFaceToken = os.environ['huggingFaceToken']
iterations = os.environ['iterations']

class theAlgo:
    def __init__(self, img_width=imageWidth, img_height=imageHeight):
        # keras.mixed_precision.set_global_policy("mixed_float16")
        # self.model = keras_cv.models.StableDiffusion(img_width, img_height)

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            revision="fp16",
            torch_dtype=torch.float16,
            use_auth_token=huggingFaceToken
        )
        self.pipe = self.pipe.to("cuda")

        self.pipe.enable_attention_slicing()


    def generate(self, prompt):
        if prompt is None:
            return 0

        start_time = time.time()

        # images = self.model.text_to_image(prompt, batch_size=1)

        name = "".join(prompt.split(" ")) + str(uuid.uuid4())
        img_location = "%s%s.png" % (imageSaveLocation, name)

        image = self.pipe(prompt, height=int(imageHeight), width=int(imageWidth), num_inference_steps=int(iterations)).images[0]
        image.save(img_location)


        # Image.fromarray(images[0]).save(img_location)

        new_img_location = "%s%s.png" % (remoteImageURL, name)

        total_time = time.time() - start_time
        print("total_time: ", total_time)

        return new_img_location
