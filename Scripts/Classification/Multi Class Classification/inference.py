import joblib

# import pickle
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
#
# classes = np.load('classes.npy', allow_pickle=True)
# with open('tokenizer.pickle', 'rb') as handle:
#     tokenizer = pickle.load(handle)
#
# model = load_model('BI-GRU.h5')
#
# new_complaint = ['how is everything going for you']
# # seq = tokenizer.texts_to_sequences(new_complaint)
#
#
# n_most_common_words = 8000
# max_len = 40
#
#
# def tokenization(data, maxlength=100):
#     token = Tokenizer(num_words=n_most_common_words, lower=True, oov_token='oov')
#     token.fit_on_texts(data)
#
#     data_seq = token.texts_to_sequences(data)
#     data_pad = pad_sequences(data_seq, maxlen=maxlength, padding='post')
#
#     return token, data_pad
#
#
# token, seq = tokenization(new_complaint, maxlength=max_len)
# padded = pad_sequences(seq, maxlen=max_len)
# pred = model.predict(padded)
# res = np.argmax(model.predict(padded), axis=-1)
# print(classes[res[0]])
#