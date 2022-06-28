import sys
import numpy as np
from PIL import Image
import wikipedia    # to extract information
from wordcloud import WordCloud,STOPWORDS

# we will import STOPWORDS because to remove common words like "the, a, than, here, after"

a = str(input("Enter the anem of which you want to make word cloud : "))
title = wikipedia.search(a)[0]   # it will search the title from the wikipedia
page = wikipedia.page(title) # it will search the page related to given topic in wikipedia
text = page.content # to extract the content of that topic
print(text)

bg = np.array(Image).open("abcd.pg")   # download the background image because we need base on which our words will
unwanted_words = set(STOPWORDS)
wordclo = WordCloud(background_color = "black", max_words = 400, mask = bg, stopwords = unwanted_words)
wordclo.generate(text)
wordclo.to_file("sample.png")  # what name you want to save 


#it will take some time to generate we have to got