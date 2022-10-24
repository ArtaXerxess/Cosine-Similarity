from pandas import DataFrame
from sklearn.metrics.pairwise import cosine_distances,cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings('ignore')

class engine:
    def __init__(self,sentence1=None,sentence2=None) -> None:
        self.sentence1=sentence1
        self.sentence2=sentence2
        self.corpus = [self.sentence1,self.sentence2]
        self.magic()
    def magic(self):
        self.terms = CountVectorizer(stop_words='english',ngram_range=(1,1))
        self.vector = self.terms.fit_transform(raw_documents=self.corpus)
        self.matrix = self.vector.todense()
        self.elements = self.terms.get_feature_names()
        row_head = ['sentence 1','sentence 2']
        self.df = DataFrame(self.matrix, columns=self.elements, index=row_head)
        self.cs = cosine_similarity(self.df,self.df)
        self.cd = cosine_distances(self.df,self.df)
    def output(self):
        self.results = f"""
sentence 1:
{self.sentence1}

sentence 2:
{self.sentence2}

DataFrame:
{self.df}

Cosine Similarity Matrix
{self.cs[0,0]}  {self.cs[0,1]}
{self.cs[1,0]}  {self.cs[1,1]}

Cosine Distance Matrix
{self.cd[0,0]}   {self.cd[0,1]}
{self.cd[1,0]}   {self.cd[1,1]}"""
        return self.results



# Testing
if __name__ == '__main__':
    # Hosea 6:6
    # New International Version [NIV]
    test1 = "For I desire mercy, not sacrifice, and acknowledgment of God rather than burnt offerings"
    # Living Bible [TLB]
    test2 = "I dont want your sacrifices I want your love; I dont want your offerings I want you to know me"
    obj = engine(sentence1=test1,sentence2=test2)
    print(obj.output())



__author__ = 'Harshvardhan Singh'