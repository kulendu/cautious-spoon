import re
from typing import final
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 


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

tokenized_word = rmv_punc.split()

final_list = []

for item in tokenized_word:
    if item not in stopwords.words('english'):
        final_list.append(item)

print(final_list)