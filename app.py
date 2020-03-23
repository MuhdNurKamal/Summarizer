import logging
import sys
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from pprint import pprint
from gensim.summarization import summarize

text = ("".join([line for line in sys.stdin]))

pprint(summarize(text, ratio=0.1) )
