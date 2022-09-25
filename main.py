import find
import urllib.request
import discord
from discord.ext import commands
import os
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import cv2 
import numpy as np
from matplotlib import pyplot as plt
category_index = label_map_util.create_category_index_from_labelmap('label_map.pbtxt')

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file('pipeline.config')
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore('ckpt-51').expect_partial()

@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections
    


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("when in doubt guess Milcery"))
    print('bot online')
    print(bot.user.name)

@bot.event
async def on_message(message):
    if message.author.id == 716390085896962058:
##        print(message.message.content())

        embeds = message.embeds # return list of embeds

        # for embed in embeds:
        #     print(embed.to_dict()) # it's content of embed in dict

        # Makes sure there is embed in message
        if len(embeds) > 0:
            embed = embeds[0]
            embed = embed.to_dict()
        else:
            return

        if embed is not None and embed.get("image") is not None and embed.get("description") is not None and embed.get("description")== 'Guess the pokémon and type `@Pokétwo#8236 catch <pokémon>` to catch it!':
            url = embed.get("image").get("url")

            print(url)

            # Adding information about user agent
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)

            # setting filename and image URL

            # calling urlretrieve function to get resource
            urllib.request.urlretrieve(url, "pokemon.jpg")

            IMAGE_PATH = 'pokemon.jpg'

            img = cv2.imread(IMAGE_PATH)
            image_np = np.array(img)

            input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
            detections = detect_fn(input_tensor)

            num_detections = int(detections.pop('num_detections'))
            detections = {key: value[0, :num_detections].numpy()
                        for key, value in detections.items()}
            detections['num_detections'] = num_detections

            # detection_classes should be ints.
            detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

            # print(detections.keys()) --> dict_keys(['detection_boxes', 'detection_scores', 'detection_classes', 'raw_detection_boxes', 'raw_detection_scores', 'detection_multiclass_scores', 'detection_anchor_indices', 'num_detections'])

            names = []

            for index, object in enumerate(detections['detection_classes']):
                if index > 2:
                    break
                names.append(category_index[object+1]['name'])

            await message.reply(names)

#     if message.author.id == 851869159121616960:

#         embeds = message.embeds # return list of embeds
# ##        for embed in embeds:
# ##            print(embed.to_dict()) # it's content of embed in dict

#         embed = embeds[0]
#         embed = embed.to_dict()
#         print(embed)
#         print(embed.get("title"))


with open("token.txt", "r") as file:
    token = file.read().splitlines()[0].strip()
bot.run(token)
