#part 1 - downloading the Text 
from mediawiki import MediaWiki
wikipedia = MediaWiki()
ShenZhen = wikipedia.page('ShenZhen')
print(ShenZhen.title)
print(ShenZhen.content)

Boston = wikipedia.page('Boston')


#part 2- Analyzing the Text
from nltk.sentiment.vader import SentimentIntensityAnalyzer
Sentence = ShenZhen.summarize(sentences=10)
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)
from thefuzz import fuzz
a = fuzz.ratio(ShenZhen.summarize(sentences=10),Boston.summarize(sentences=10))
print(a)
b = fuzz.partial_ratio(ShenZhen.summarize(sentences=10),Boston.summarize(sentences=10))
print (b)
c = fuzz.token_sort_ratio(ShenZhen.summarize(sentences=10),Boston.summarize(sentences=10))
print (c)

#part3
#1.Project Overview 
#I used data source from Wikipedia, and I used a sentiment analyzer and a string similarity analyzer to analyze the texts. Through using the sentiment analyzer, I was hoping to learn the sentiments about the summary section on Shenzhen's Wikipedia page. Through using TheFuzz function, I tried to see the textual similarities and differences between Shenzhen and Boston's wiki pages 

#2. 
#I obtained texts from Wikipedia and then I analyzed the texts with a sentiment analyzer to see the emotional components of the text, and I used theFuzz to compare the text with another similar text. 
#In terms of content, I picked Shenzhen's wiki page and compared it against Boston's page. I picked Shenzhen because my parents live there now, and it is my favorite city in China. I am comparing it against Boston because my college is in Boston. 

#3. 
#I found out that the first ten sentences in the summary section of Shenzhen's Wiki page is fairly neutral to positive. There is little extreme negative languages and a little bit more positive language. 
#I also learned that Shenzhen's summary page is more similar to Boston's summary page than I expected. They have the stanfard Levenshtein distance similarity ratio of 42, a partial ratio of 43, and a token sort ratio of 59. 

#4
#Reflecting on this project, I did a good job writing code that successfully runs. (I can not answer if the project is appropriately scoped because I have not learned what scope is.) I learned how to pull text from Wikipedia, which should be useful even though I am not sure when I will use it again in the future. I also learned how to compare textual differences between texts. Going forward, I can use this function to compare my writing assignments against what I am paraphrasing to make sure I am not just copying and pasting. 