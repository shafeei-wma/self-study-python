#  VERY FAST - new method
# pip install -r requirements.txt
import pandas as pd
import re
import nltk
import numpy as np

from nltk.corpus import stopwords as stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) # keluarkan later
stop_words.add("im")
stop_words.add("ahh")
stop_words.add("Text")
stop_words.add("x")
# print(stopwords.words('english'))

df = pd.read_csv('sales_data4.csv', encoding='utf-8', low_memory = False, usecols=[0,1,2,4,5])

df = df.dropna().drop_duplicates(subset = "Text")
total_sin =  (df.to_numpy())

def myfunc(a): 
    # Removal url,username and symbols
    b = re.sub(r"http[s]?://[\S+]*|www.\S+", "", a, flags=re.IGNORECASE)    
    b = re.sub(r"@\S+|[\S+]*_[\S+]*", "", b)
    b = re.sub('[^a-zA-Z]+',' ', b )

    # Tokenization
    word_tokens = word_tokenize(b)

    # Stop Words
    filtered_sentence0 = [w for w in word_tokens if (not w.lower()  in stop_words)]
    filtered_sentence = []
    
    # Lemonize
    for w in filtered_sentence0:
        # if w == "Text":
        #     print("wait:: ",w)
        filtered_sentence.append(lemmatizer.lemmatize(w.lower(),'v'))
    
    # Detokenization Test
    # print('Filtered Text: ',filtered_sentence)
    b = TreebankWordDetokenizer().detokenize(filtered_sentence)
    # df.loc[index,'Text'] = ' '.join(filtered_sentence).strip()
    return b

# Update all data in column 4 only
result= np.vectorize(myfunc)(total_sin[:,[4]])
total_sin[:,[4]] = result

# Update sheet and generate new .csv
df = pd.DataFrame(total_sin, columns = ['No','Twitter_ID','Date','User','Text'])
filter = df["Text"].str.strip() != ""
df = df[filter]
df = df.reset_index(drop=True)
df.to_csv('out_pp_final.csv', index=False)

# more example of numpy vectorization*********************************************************************************************************
# create a numpy array
x = np.array([1, 2, 3, 4, 5])

# subtract 2 from each element and then multiply the result by 7
result = (x - 2) * 7

print(result)  # It outputs: array([-7,  0,  7, 14, 21])
