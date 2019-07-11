from auth import authenticate
from datetime import datetime

def gen_config(n):
    name = "Shower Thought #: {}".format(n)
    title = name
    description = name
    config = {
        'album': album,
        'name': name,
        'title': title
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

    
    my_config = gen_config(n)
    image_path = "shower_thought #: {}".format(n)
    image_path = image_path+".jpg"
    image = upload_image(client, my_config,image_path, album)

    print("Image was posted!")
    print("You can find the image here: {0}".format(image['link']))
