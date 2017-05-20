from wordcloud import WordCloud

tags_from_0_to_10 = open('tags_from_0_to_10', 'r')
tags_from_10_to_13 = open('tags_from_10_to_13', 'r')
tags_from_13_to_18 = open('tags_from_13_to_18', 'r')
tags_from_18_to_30 = open('tags_from_18_to_30', 'r')
tags_more_then_30 = open('tags_more_then_30', 'r')

files = [tags_from_0_to_10,
         tags_from_10_to_13,
         tags_from_13_to_18,
         tags_from_18_to_30,
         tags_more_then_30]


def create_word_cloud(words, count,  file_name):
    word_cloud = WordCloud(width = 1000, height = 500,  max_words=count, collocations=False).generate(words)
    word_cloud.to_file(file_name)


all_tags = ''

for file in files:
        tags = file.read()
        if len(tags) > 0:
            all_tags += tags
            create_word_cloud(tags, 20, file.name + '.png')
        file.close()

create_word_cloud(all_tags, 100, 'all_tags.png')
