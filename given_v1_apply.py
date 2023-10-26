
#  SLOW - old method
import pandas as pd
import re
import nltk

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

# df = pd.read_csv('sales_data2.csv', encoding = "ISO-8859-1", low_memory = False , skiprows=range(1, 1000), nrows = 50000)
# df = pd.read_csv('sales_data2.csv', encoding = "utf-8", low_memory = False, usecols=[5], nrows = 100000)
df = pd.read_csv('sales_data4.csv', encoding = "utf-8", low_memory = False, usecols=[0,1,2,4,5])

# Rule Pre - Remove Same Tweet
df = df.dropna().drop_duplicates(subset = "Text")

def lapet(a):

    # Rule 1 - Remove Link URL
    origin = re.sub(r"http[s]?://[\S+]*|www.\S+", "", a, flags=re.IGNORECASE)
    # print('da remove url: ',origin)

    # Rule 2 - Remove @username, user_name
    origin = re.sub(r"@\S+|[\S+]*_[\S+]*", "", origin)

    # Rule 3 - Remove special character and multiple white space
    origin = re.sub('[^a-zA-Z]+',' ', origin )
    # print('da remove special char: ',origin)
    
    # Rule 4 - Tokenization
    word_tokens = word_tokenize(origin)

    # Rule 5 - Stop Words
    filtered_sentence_ori = [w for w in word_tokens if (not w.lower()  in stop_words)]
    
    # Rule 6 - Lemonize
    lemon_sentence = []
    for w in filtered_sentence_ori:
        lemon_sentence.append(lemmatizer.lemmatize(w.lower(),'v'))
    
    # Rule 7 - Detokenization 
    a = TreebankWordDetokenizer().detokenize(lemon_sentence)
    return a
    
df['Text'] = df.apply(lambda row : lapet(row[4]),axis=1)

# Fin Remove Blank After Cleaning
filter = df["Text"].str.strip() != ""
df = df[filter]
df = df.reset_index(drop=True)
# print(print(df.columns))

df.to_csv('out1.csv', index=True,header=True) 
print((df.columns))
print("end")


# ////////////////////////////////////////////////////////////////////////////////////////////////////// TESTING AREA
# def add(a, b, c):
#     return a + b + c
# data = {
#             'A':[1, 2, 3],
#             'B':[4, 5, 6],
#             'C':[7, 8, 9] }
     
# # Convert the dictionary into DataFrame
# df9 = pd.DataFrame(data)
# print("Original DataFrame:\n", df9)
    
# df9['add'] = df9.apply(lambda row : add(row['A'],row['B'], 5), axis = 1)
# print('\nAfter Applying Function: ')
# # printing the new dataframe
# print(df9)