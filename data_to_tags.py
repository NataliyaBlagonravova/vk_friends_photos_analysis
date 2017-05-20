import requests
import time

microsoft_key = '...'

vk_data = open('vk_data', 'r')

tags_from_0_to_10 = open('tags_from_0_to_10', 'a')
tags_from_10_to_13 = open('tags_from_10_to_13', 'a')
tags_from_13_to_18 = open('tags_from_13_to_18', 'a')
tags_from_18_to_30 = open('tags_from_18_to_30', 'a')
tags_more_then_30 = open('tags_more_then_30', 'a')


def output_file(age):
    if age < 10:
        return tags_from_0_to_10
    if age < 13:
        return tags_from_10_to_13
    if age < 18:
        return tags_from_13_to_18
    if age < 30:
        return tags_from_18_to_30
    return tags_more_then_30


def photo_tags(photo_url):
    url = '...'

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = microsoft_key

    json = {'url': photo_url}
    params = {'visualFeatures': 'Tags'}
    data = None

    response = requests.request('post', url, json=json, data=data, headers=headers, params=params)

    tags = ''

    if response.json().get('tags'):
        response_tags = response.json()['tags']
        for tag in response_tags:
            tags = tags + str(tag['name']) + ' '

    return tags


friends_count = int(vk_data.readline())

for i in range(friends_count):
    print('Friend:', i, '/', friends_count)
    age = int(vk_data.readline())
    file = output_file(age)
    photo_count = int(vk_data.readline())

    for j in range(photo_count):
        photo_url = vk_data.readline().rstrip('\n')
        print('Photo: ', j, '/', photo_count)
        tags = photo_tags(photo_url)
        file.write(tags)
        time.sleep(0.001)

vk_data.close()
tags_from_0_to_10.close()
tags_from_10_to_13.close()
tags_from_13_to_18.close()
tags_from_18_to_30.close()
tags_more_then_30.close()
