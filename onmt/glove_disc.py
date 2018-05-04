#coding=utf8

import sys
import math
import torch
import gensim
import numpy as np
from scipy.spatial.distance import cosine

from glove import Glove
from glove import Corpus

class GloVe_Discriminator(object):
	def __init__(self):
		self.dict_path = "./data/dialogue.vocab.pt"
		self.no_components = 100
		self.learning_rate = 0.05
		# Corpus model
		self.vocab = dict(torch.load(self.dict_path, "text")) 
		self.corpus_model = Corpus(dictionary=self.vocab['tgt'].stoi)
		# Model
		self.glove = Glove(no_components=self.no_components, learning_rate=self.learning_rate)

	def load_model(self, model_path):
		print('Loading pre-trained GloVe model...')
		self.glove = Glove.load(model_path)
		print('Loading finished')

	def get_emb(self, ids):
		emb = self.glove.word_vectors[ids.data.cpu().numpy()]
		paragraph_emb = np.mean(emb, axis=0)
		return paragraph_emb

	def run(self, src, tgt):
		src = src.view(src.size()[0], -1)
		tgt = tgt.view(tgt.size()[0], -1)
		src_emb = self.get_emb(src)
		tgt_emb = self.get_emb(tgt)
		return [1 - cosine(src_emb[i], tgt_emb[i]) for i in range(0, src_emb.shape[0])]
