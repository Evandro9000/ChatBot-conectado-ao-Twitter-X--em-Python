# Chatbot com Busca no Twitter e Respostas Baseadas em Corpus Local

Este projeto é um chatbot que integra duas funcionalidades principais:
1. Busca de tweets recentes no Twitter usando a API v2.
2. Respostas baseadas em um corpus local utilizando o modelo TF-IDF para medir similaridade textual.

## Funcionalidades

### 1. Busca no Twitter
- Permite buscar tweets recentes baseados em uma palavra-chave ou frase fornecida pelo usuário.
- Integração com a API v2 do Twitter usando autenticação via `bearer_token`.
- Implementa controle de erros, incluindo limites de requisição e mensagens amigáveis ao usuário.

### 2. Respostas Baseadas em Corpus Local
- Utiliza a biblioteca `newspaper3k` para processar um artigo online como corpus.
- Segmenta o corpus em frases e aplica limpeza textual (remoção de stopwords e pontuação).
- Responde às perguntas do usuário calculando a similaridade entre a entrada e as frases do corpus usando TF-IDF.

## Tecnologias e Bibliotecas
- **Python**: Linguagem principal.
- **Google Colab**: Onde o bot foi desenvolvido.
- **Tweepy**: Integração com a API do Twitter.
- **NLTK**: Tokenização e remoção de stopwords.
- **newspaper3k**: Extração de texto de artigos online.
- **Scikit-learn**: Cálculo de TF-IDF e similaridade de cosseno.

## Requisitos
Antes de rodar o projeto, instale as bibliotecas necessárias:

```Python
pip install tweepy
pip install nltk
pip install newspaper3k
pip install "lxml[html_clean]"
```

Certifique-se de que o NLTK tenha os pacotes necessários baixados:
```Bash
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
```

## Configuração
1. **Configurar Credenciais do Twitter**:
   - Substitua `SEU_BEARER_TOKEN` no código pelo seu token de acesso do Twitter.

2. **Definir Corpus Local**:
   - O corpus é extraído automaticamente de um link de artigo definido no código. Você pode alterar o link para um artigo de sua escolha.

## Como Usar
1. Execute o script principal `chatbot_twitter_tfidf.py`(desenvolvido em Google Colab).
2. Digite uma pergunta ou solicitação no terminal:
   - Para buscar no Twitter, inclua "Twitter" ou "X" na frase. Exemplo: `Pesquise sobre IA no Twitter`.
   - Para buscar no corpus local, digite uma pergunta curta. Exemplo: `O que é Manhunt 2?`.
3. Para encerrar, digite `sair`.

## Estrutura do Projeto
```
├── chatbot_twitter_tfidf.py   # Código principal do chatbot
├── Requerimentos.txt           # Lista de dependências
├── README.md                  # Documentação do projeto
```