import vk
from dateutil import parser, relativedelta
import datetime
import time

user_id = 36497241

access_token = '...'

def age(person):
    if 'bdate' in person:
        s = person['bdate']
        if s.count('.') > 1:
            d = parser.parse(person['bdate'])
            return relativedelta.relativedelta(datetime.date.today(), d.date()).years
        else:
            return 0
    else:
        return 0


def write_photo_urls_in_file(person, file):
    urls = []
    photos = api.photos.getAll(owner_id=person['user_id'], count=100)

    file.write(str(len(photos) - 1) + '\n')

    for i in range(1, len(photos)):
        urls.append(photos[i]['src_big'])
        file.write(photos[i]['src_big'] + '\n')


session = vk.Session(access_token=access_token)
api = vk.API(session)
friends = api.friends.get(user_id=user_id, fields='sex, bdate')

file = open('vk', 'w')

counter = 0
for person in friends:
    person_age = age(person)

    if person_age != 0:
        file.write(str(person_age) + '\n')
        write_photo_urls_in_file(person, file)
        counter += 1
        print(counter)
        time.sleep(3)

file.close()

