

from auth import authenticate
from datetime import datetime
import os
import random

from os import path

import pandas as pd
from meme_gen import make_meme, get_upper, get_lower

def find_file_path(my_str):

    cwd = os.getcwd()

    # r=root, d=directories, f = files
    my_file = ""
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(my_str):
                my_file = os.path.join(root, file)

    return my_file

def gen_config(n):
    name = "Shower Thought #: {}".format(n)
    title = name
    description = name
    config = {
        'album': album,
        'name': name,
        'title': title,
        'description': description
    }

    return config

def upload_image(client,config,image_path, album):
    """
    Uploads and image to imgur
    """

    print('Uploading image...')
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image

if __name__ == "__main__":
    client = authenticate()

    album =None

    cwd = os.getcwd()

    # r=root, d=directories, f = files
    my_file = find_file_path('combined_csv.csv')


    df = pd.read_csv(my_file, sep='\n')
    n_rows = df.shape[0]

    n = random.randint(0,(n_rows-1))
    my_config = gen_config(n)
    meme_string =  df.iloc[n][0]

    image_path = "shower_thought_{}".format(n)
    image_path = image_path+".jpg"

    image_file = path.join(cwd, image_path)
    print()
    shower_file = path.join(cwd,'shower.jpg')

    make_meme(meme_string,shower_file, image_path)
    image = upload_image(client, my_config,image_path, album)

    print("Image was posted!")
    print("You can find the image here: {0}".format(image['link']))
