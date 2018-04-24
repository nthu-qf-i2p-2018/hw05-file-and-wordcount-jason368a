
# coding: utf-8

# In[33]:


lines = open("i_have_a_dream.txt")
all_words = []
import string
string.punctuation

for line in lines:
    line = line.strip()
    words = line.split()
       
    for word in words:
            word = word.strip(string.punctuation)
            all_words.append(word)

from collections import Counter
word_Counter = Counter(all_words)
word_Counter.most_common()


# In[37]:


import csv
csv_file = open('word_count.csv', 'w')

with open('word_Counter.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['word', 'count'])
    # writer.writerows(word_Counter.most_common())
    for word, count in word_Counter.most_common():
        writer.writerow([word, count])


# In[24]:


import json


# In[29]:


json.dump(word_Counter.most_common(), open('word_count.json', 'w'))


# In[31]:


import pickle


# In[34]:


pickle.dump(word_Counter, open('word_count.json', 'wb'))

