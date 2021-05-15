from os import read
import re
from typing import final
import nltk
from numpy.core.defchararray import count
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pylab as plt
nltk.download('stopwords')
nltk.download('punkt')


text = input('Enter the text for Analyzing : ')

'''
Cleaning the text : 
1. Lowercasing the string
2. Removing the punctuautions.
3. Removing Special chars.
'''

lower_case = text.lower()
rmv_punc = re.sub(r'[^\w\s]', '', lower_case)


'''
Tokenizing the words and removing the stop words.
Tokenization --> Converting the strings into list but element wise. EX : 'My name is John' --> ['My', 'name', 'is', 'John']
Stop words --> Words that doesn't add or make any meaning for the sentence. EX: 'My name is John' --> 'My name John'
'''

tokenized_word = word_tokenize(rmv_punc, 'english')

final_list = []

for item in tokenized_word:
    if item not in stopwords.words('english'):
        final_list.append(item)


emotion_list = []

with open('emotions.txt', 'r') as file:
    for emotion in file:
        emotion = emotion.replace("\n","").replace(","," ").replace("'","").strip()
        word, emotions = emotion.split(':')
        
        if word in final_list:
            emotion_list.append(emotions)
            

count_emotion = Counter(emotion_list)   # dict for the no. of emotions 
                
'''
This function is used for analysing the intensity of a sentence
'''

def emotion_analyzer(emotion_text):
    score = SentimentIntensityAnalyzer().polarity_scores(emotion_text)
    print(score)
    pos = score['pos']
    neg = score['neg']
    
    if pos > neg:
        print('Positive Sentiment')
    elif neg > pos:
        print('Negative statement')
    else:
        print('Neutral statment')


emotion_analyzer(rmv_punc)



plt.figure()
plt.bar(count_emotion.keys(), count_emotion.values())
plt.show()

print("The statement is a ", max(count_emotion.keys()), " statement")
