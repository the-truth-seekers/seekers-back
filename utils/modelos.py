from joblib import load
from keras.models import load_model

modelo_predicao_rf = load('resources/models/random_forest_model_news.pkl')
modelo_predicao_rnn = load_model('resources/models/model_rnn.h5')

modelo_vect = load('resources/models/count_vectorizer_model_news.pkl')
modelo_pad_sequences = load('resources/models/padsequences.pkl')
modelo_tokenizer = load('resources/models/tokenizer.pkl')
