
import basilica
import os
from dotenv import load_dotenv

load_dotenv() #parse .env files for variables

BASILICA_API_KEY = os.getenv('BASILICA_API_KEY')

with basilica.Connection('BASILICA_API_KEY') as c:
print(type(connection))


if __name__ == 'main':
    
    sentences = ['Hello World!', 'How are you?']
    embeddings = connection.embed_sentences(sentences)
    
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]
