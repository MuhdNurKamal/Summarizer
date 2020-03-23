import logging
import sys
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from pprint import pprint as print
from gensim.summarization import summarize

text = ("".join([line for line in sys.stdin]))

print(summarize(text, ratio=0.01) )
