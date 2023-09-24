from joblib import load

modelo_predicao = load('resources/models/random_forest_model_news.pkl')
modelo_vect = load('resources/models/count_vectorizer_model_news.pkl')
