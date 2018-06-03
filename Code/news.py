import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from datetime import datetime
import time
import urllib2
from bs4 import BeautifulSoup

feed_xml1=""
no_of_docs=0

time1 = time.time()


class frequency_summarizer:
    def __init__(self, minCut=0.2, maxCut=0.8):
        self._min_cut = minCut
        self._max_cut = maxCut
        self._stopwords = set(stopwords.words('english') + list(punctuation))
    """words with higher frequency than maxcut and lower frequency than mincut are eliminated """
    def _computefrequencies(self, word_sent):

        freq = defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1

        m = float(max(freq.values()))
        for w in freq.keys():
            freq[w] = freq[w] / m
            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                del freq[w]
        return freq
    """calculate frequency for each word """
    def summarize(self, text, n):

        sents = sent_tokenize(text)
        assert n <= len(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._computefrequencies(word_sent)
        ranking = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking, n)
        return [sents[j] for j in sents_idx]
    """ Print first n sentences which represent summary """

    def _rank(self, ranking, n):
        return nlargest(n, ranking, key=ranking.get)

def get_only_text(url):
    """
  print title and text of article in URL
 """
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page)
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text

def caller(urlString, num):

    #feed_xml1 = raw_input("Enter URL for summary")
    #no_of_docs = input("How many articles to be summarized?")
    feed_xml1 = urlString;
    no_of_docs = num;
    #print "Process started:", datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    feed_xml = urllib2.urlopen(feed_xml1).read()
    feed = BeautifulSoup(feed_xml.decode('utf8'),"html.parser")
    to_summarize = map(lambda p: p.text, feed.find_all('guid'))

    fs = frequency_summarizer()
    for article_url in to_summarize[:no_of_docs]:
        title, text = get_only_text(article_url)
        #print '----------------------------------'
        #print title
        for s in fs.summarize(text, 2):
            print ""
    time2 = time.time()
    total_time=(time2 - time1)
    ind_time=(total_time / no_of_docs)
    #print "Process ended: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #print "Total time required for ", no_of_docs, " articles to be summarized: ", round(total_time,3) , "seconds"
    return title+"\n"+s
    


