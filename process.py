import tensorflow as tf
import tensorflow_hub as hub
import textract as tx
import glob
import numpy as np
import pandas as pd
import os
import loadfile as lf


def load_model():
    model = tf.saved_model.load('./universal-sentence-encoder-nli-stsb-mean-tokens/')
    # model = 
    return model

def cosine(u,v):
  return np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))

def get_similarity_list(text):
    query = lf.load_job_txt(text)
    files1 = glob.glob("./Data/res txt/*",recursive=True)
    # from transformers import AutoTokenizer, AutoModelForMaskedLM
    # tokenizer = AutoTokenizer.from_pretrained("johngiorgi/declutr-small")
    # model = AutoModelForMaskedLM.from_pretrained("johngiorgi/declutr-small")
    model = load_model()
    org_list=[]
    file_name=[]
    for single_file in files1:
        with open(single_file,'r') as f1:
            sentences_list=[f1.read()]
            sentence_embed=model(sentences_list)
            query_vec = model([query])[0]
            for sent in sentences_list:
                sim=cosine(query_vec,model([sent])[0])
                org_list.append(sim)
                file_name.append(single_file)

    mapped=zip(file_name,org_list)
    mapped=list(mapped)
    res=sorted(mapped,key=lambda x:x[1], reverse=True)
    return res

def get_table(res):
    scores = []
    for i in res:
        temp = i[0].split('/')
        text = temp[-1:]
        text = text[0].split('.')[0]
        text = text.split('\\')[1]
        scores.append([text,i[1]])
    scores = pd.DataFrame(scores,columns=['Name', 'Score'])
    return scores


