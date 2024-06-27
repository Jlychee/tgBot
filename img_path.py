import os
import random

dict = {'Angry.jpg': 'Злой', 'Clown.jpg': 'Просто клоун', 'Crying.jpg': 'Плакса', 'Cute.jpg': 'Милаш',
        'Happy.jpg': 'Счатсливчик', 'Happy_frogling.jpg': 'Лягушонок', 'Horny.jpg': 'Хорни',
        'in_prostration.jpg': 'В прострации',
        'inflated.jpg': 'Надутый', 'Irritated.jpg': 'Раздраженный', 'Rage.jpg': 'В ярости',
        'Uncomprehending.jpg': 'Непонимающий'}


def get_img():
    img_list = os.listdir(r'Mood')
    img_name = random.choice(img_list)
    return img_name, dict[img_name]
