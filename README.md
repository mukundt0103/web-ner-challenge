# Web-based named entity recognition

This project is done using Vue.js as frontend and Flask as backend.

## Steps to run the project
1. Clone the repository using `git clone `.
2. Run `make install FRONTEND=vue-frontend BACKEND=flask-backend`.
3. Run the following to install few requirements.
```
cd web-ner-challenge/vue-frontend
npm install vue bootstrap bootstrap-vue
npm install axios --save
cd ..
python3 -m spacy download en_core_web_sm
python3 -m spacy download fr_core_news_sm
python3 -m spacy download de_core_news_sm
python3 -m spacy download es_core_news_sm
pip3 install spacy
```
4. Run `make start FRONTEND=vue-frontend BACKEND=flask-backend`.
