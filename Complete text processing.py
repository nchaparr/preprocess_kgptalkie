#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


import numpy as np


# In[10]:


import spacy


# In[11]:


from spacy.lang.en.stop_words import STOP_WORDS as stopwords


# In[12]:


#'https://raw.githubusercontent.com/laxmimerit/twqitter-data/master/twitter4000.csv'


# In[13]:


df = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/twitter-data/master/twitter4000.csv', encoding='latin1')


# In[ ]:





# In[14]:


df


# In[15]:


df['sentiment'].value_counts()


# # Word counts

# In[16]:


len('this is text'.split())


# In[17]:


df['word_counts']=df['twitts'].apply(lambda x: len(str(x).split()))


# In[18]:


df.sample(5)


# In[19]:


df['word_counts'].max()


# In[20]:


df['word_counts'].min()


# In[21]:


df[df['word_counts']==1]


# # Character counts

# In[22]:


df['char_counts']=df['twitts'].apply(lambda x: len(x))


# In[23]:


len('this is') #space is counted


# In[24]:


#custome method


# In[25]:


def char_counts(x):
    s = x.split()
    x=''.join(s)
    return len(x)


# In[26]:


char_counts('this is')


# In[27]:


df['char_counts'] = df['twitts'].apply(lambda x: char_counts(str(x)))


# In[28]:


df.sample(5)


# # Average word length

# In[29]:


x='this is' #6/2=3
y='thankyou guys'#12/2=6


# In[30]:


df['avg_word_len']=df['char_counts']/df['word_counts']


# In[31]:


df.sample(5)


# # Stop Words Count

# In[32]:


stopwords


# In[33]:


print(stopwords)


# In[34]:


len(stopwords)


# In[35]:


x = 'this is the text data'


# In[36]:


x.split()


# In[37]:


[t for t in x.split() if t in stopwords]


# In[38]:


len([t for t in x.split() if t in stopwords])


# In[39]:


df['stop_words_len']= df['twitts'].apply(lambda x: len([t for t in x.split() if t in stopwords]))


# In[40]:


df.sample(5)


# # Count #HashTags and @Mentions

# In[41]:


x = 'this is #hashtag and this is @mentionx'


# In[42]:


x.split()


# In[43]:


[t for t in x.split() if t.startswith('#')]


# In[44]:


len([t for t in x.split() if t.startswith('#')])


# In[45]:


df['hashtag_count']=df['twitts'].apply(lambda x: len([t for t in x.split() if t.startswith('#')]))


# In[46]:


df.sample(5)


# In[47]:


df['mentione_count']=df['twitts'].apply(lambda x: len([t for t in x.split() if t.startswith('@')]))


# In[48]:


df.sample(8)


# # If numeric digits are present in twitts

# In[49]:


x= 'this is 1 and 2'


# In[50]:


x.split()


# In[51]:


x.split()[3].isdigit()


# In[52]:


df['tweetdigits'] = df['twitts'].apply(lambda x: len([t for t in x.split() if t.isdigit()]))


# In[53]:


df.sample(5)


# # Upper case words

# In[54]:


x='I AM HAPPY'
y='i am happy'


# In[55]:


[t for t in y.split() if t.isupper()]


# In[56]:


df['upper case'] = df['twitts'].apply(lambda x: len([t for t in y.split() if t.isupper()]))


# In[57]:


df.sample(15)


# In[58]:


df.iloc[3962]['twitts']


# # Lower case conversion

# In[59]:


x = 'this is Text'


# In[60]:


x.lower()


# In[61]:


x = str(45)
x.lower()


# In[ ]:





# In[62]:


x = 'Hell how are YOU Mister?'


# In[63]:


x.lower()


# In[64]:


df


# In[65]:


df['twitts'] = df['twitts'].apply(lambda x: str(x).lower())


# In[66]:


df.sample(15)


# # Contraction to expansion

# In[67]:


contractions = { 
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how does",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
" u ": " you ",
" ur ": " your ",
" n ": " and ",
"won't": "would not",
'dis': 'this',
'bak': 'back',
'brng': 'bring',
"wont":"will not",
"dis":"this",
"bak":"back"
}


# In[68]:


x = "i'm don't he'll"


# In[69]:


def cont_to_exp(x):
    if type(x) is str:
        for key in contractions:
            value=contractions[key]
            x=x.replace(key, value)
        return x
    else:
        return x
    


# In[70]:


cont_to_exp(x)


# In[71]:


get_ipython().run_cell_magic('timeit', '', "df['twitts'] = df['twitts'].apply(lambda x: cont_to_exp(x))")


# In[72]:


df.sample(5)


# # Count and remove emails

# In[73]:


df[df["twitts"].str.contains('gmail.com')]


# In[74]:


df.iloc[2448]['twitts']


# In[75]:


df.iloc[3713]['twitts']


# In[76]:


x = '@securerecs arghh me please markbradbury_16@hotmail.com'


# In[77]:


import re
re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+._-]+\b)', x)


# In[78]:


df['emails'] = df['twitts'].apply(lambda x: re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+._-]+\b)', x))


# In[79]:


df['emails_count'] = df['emails'].apply(lambda x: len(x))
df[df['emails_count']>0]


# In[80]:


re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+._-]+\b)',"",x)


# In[81]:


df['twitts'] = df["twitts"].apply(lambda x: re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+._-]+\b)',"", x))


# In[82]:


df[df['emails_count']>0]


# # Count URLs and remove

# In[83]:


x = 'thankks for watching. for more visit https://youtube.com/kgptalkie'


# In[84]:


import re
re.findall(r'(http|https|ftp|ssh)://([\w_]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?=%&/~+#-])?',x)


# In[85]:


df['url_flags'] = df['twitts'].apply(lambda x: len(re.findall(r'(http|https|ftp|ssh)://([\w_]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?=%&/~+#-])?',x)))


# In[86]:


df.sample(5)


# In[87]:


df[df['url_flags']>0].sample(5)


# In[91]:


re.sub(r'(http|https|ftp|ssh)://([\w_]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?=%&/~+#-])?',"", x)


# In[92]:


df['twitts'] = df['twitts'].apply(lambda x: re.sub(r'(http|https|ftp|ssh)://([\w_]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?=%&/~+#-])?',"", x))


# In[93]:


df.sample(5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




