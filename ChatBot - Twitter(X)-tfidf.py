from newspaper import Article
import tweepy
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize

# Configurações do NLTK
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# Credenciais da API do Twitter (API v2)
bearer_token = "Seu BEARER TOKEN"
# Autenticação no Twitter para API v2
client = tweepy.Client(bearer_token=bearer_token)

# Corpus local (artigo de exemplo)
link = 'LINK DO SEU ARTIGO ONLINE'
article = Article(link, language='pt')
article.download()
article.parse()
corpus_text = article.text

# Segmentar o corpus em frases
corpus = sent_tokenize(corpus_text)

# Stopwords para português
stopwords_pt = stopwords.words('portuguese')

# Função para limpar texto
def clean_text(text):
    words = nltk.word_tokenize(text.lower())
    return ' '.join([word for word in words if word.isalpha() and word not in stopwords_pt])

# Resposta usando TF-IDF
def tfidf_response(user_input, corpus):
    corpus_cleaned = [clean_text(sentence) for sentence in corpus]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus_cleaned)

    user_input_cleaned = clean_text(user_input)
    tfidf_user = vectorizer.transform([user_input_cleaned])
    similarity = cosine_similarity(tfidf_user, tfidf)

    idx = similarity.argsort()[0, -1]
    score = similarity[0, idx]

    if score > 0.1:
        return corpus[idx]
    else:
        return "Desculpa, não consegui encontrar uma resposta no corpus local."

# Busca no Twitter usando API v2
# Busca no Twitter usando API v2


# Busca no Twitter com delay
def twitter_search(query, max_results=10):
    try:
        query_with_lang = f"{query} lang:pt"

        # Realiza a busca com a API v2
        response = client.search_recent_tweets(
            query=query_with_lang,
            max_results=max_results,
            tweet_fields=["author_id", "created_at", "text"]
        )

        if not response.data:
            return ["Nenhum tweet encontrado."]

        # Limita os resultados exibidos
        tweets = response.data[:3]
        return [f"Autor: {tweet.author_id}, Texto: {tweet.text}" for tweet in tweets]
    except tweepy.TooManyRequests as e:
        print("Limite de requisições excedido. Aguardando...")
        time.sleep(15)  # Aguarda 15 segundos antes de tentar novamente
        return ["Tente novamente mais tarde."]
    except tweepy.TweepyException as e:
        return [f"Erro ao buscar no Twitter: {e}"]
    except Exception as e:
        return [f"Erro inesperado: {e}"]


# Classificador de intenções
def classify_intent(user_input):
    user_input = user_input.lower()

    if "twitter" in user_input or "x" in user_input:
        return "twitter"
    elif len(user_input.split()) < 5:
        return "tfidf"
    else:
        return "unknown"

# Motor principal do chatbot
def chatbot(user_input):
    intent = classify_intent(user_input)

    if intent == "twitter":
        query = user_input.lower().replace("no twitter", "").replace("pesquise", "").strip()
        results = twitter_search(query)
        return "\n".join(results[:3]) if results else "Desculpa, não encontrei nada no Twitter."

    elif intent == "tfidf":
        return tfidf_response(user_input, corpus)

    else:
        return "Desculpa, não entendi sua solicitação."

# Interação com o usuário
print("Bem-vindo ao chatbot! Pergunte algo ou digite 'sair' para encerrar.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Chatbot: Até mais!")
        break
    else:
        response = chatbot(user_input)
        print(f"Chatbot: {response}")
