import logging
import random
from faker import Faker
fake = Faker()

logging.basicConfig(filename="logs.txt",
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')
######## Normal paths
path_about = '/about'
path_services = '/services'
path_guides = '/guides'
path_news = '/contents/news'
path_events = '/contents/events'
path_social_media = '/contents/social-media'
path_contact = '/contact'
correct_paths = [path_about,path_services,path_guides,path_news,path_events,path_social_media,path_contact]
######## Suspicious paths
suspicious_01 = '/config/getuser?index=0'
suspicious_02 = '/robots.txt'
suspicious_03 = '/Telerik.Web.UI.WebResource.axd?type=rau'
suspicious_04 = '/core/.env'
suspicious_05 = '/core/app/.env'
suspicious_06 = '/doc/.env'
suspicious_07 = '/docker/.env'
suspicious_08 = '/docker/app/.env'
suspicious_09 = '/en/.env'
suspicious_10 = '/dotfiles/.env'
suspicious_11 = '/js/.env'
suspicious_12 = '/lib/.env'
suspicious_13 = '/libs/.env'
suspicious_14 = '/pub/.env'
suspicious_15 = '/site/.env'
suspicious_16 = '/sites/.env'
suspicious_17 = '/phpinfo.php'
suspicious_18 = '/phpinfo'
suspicious_19 = '/laravel/.env'
suspicious_20 = '/laravel/core/.env'
suspicious_21 = '/beta/.env'
suspicious_22 = '/config/.env'
suspicious_23 = '/kyc/.env'
suspicious_24 = '/admin/.env'
suspicious_25 = '/prod/.env'
suspicious_26 = '/api/.env'
suspicious_27 = '/.docker/.env'
suspicious_28 = '/.docker/laravel/app/.env'
suspicious_29 = '/.env.backup'
suspicious_30 = '/.env.local'
suspicious_paths = [
    suspicious_01,
    suspicious_02,
    suspicious_03,
    suspicious_04,
    suspicious_05,
    suspicious_06,
    suspicious_07,
    suspicious_08,
    suspicious_09,
    suspicious_10,
    suspicious_11,
    suspicious_12,
    suspicious_13,
    suspicious_14,
    suspicious_15,
    suspicious_16,
    suspicious_17,
    suspicious_18,
    suspicious_19,
    suspicious_20,
    suspicious_21,
    suspicious_22,
    suspicious_23,
    suspicious_24,
    suspicious_25,
    suspicious_26,
    suspicious_27,
    suspicious_28,
    suspicious_29,
    suspicious_30
    ]
counter_of_suspicious = 0
max_of_suspicious = random.randint(560,634)
for log in range(0,2000):
    ip_number = fake.ipv4()
    if (random.randint(0, 1) == 0):
        number_path = random.randint(0,6)
        logging.info(f'{ip_number} GET {correct_paths[number_path]} 200')
    else:
        if (counter_of_suspicious <= max_of_suspicious):
            number_path_suspicious = random.randint(0,29)
            logging.info(f'{ip_number} GET {suspicious_paths[number_path_suspicious]} 404')
            counter_of_suspicious = counter_of_suspicious + 1
        else:
            number_path = random.randint(0,6)
            logging.info(f'{ip_number} GET {correct_paths[number_path]} 200')
