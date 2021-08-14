import spacy
import en_core_web_sm
import fr_core_news_sm
import de_core_news_sm
import es_core_news_sm
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/ner', methods=('POST',))
def ner():
    """Named Entity Recognition for the text passed in request body

    Returns:
    ner_results: Flask wrapper of dictionary with labels and text
    
    """
    return_val   = []
    sel_language = request.json["language"]
    text_dict    = {}

    #load model with respect to the language selected
    if sel_language == "English":
        nlp = en_core_web_sm.load()
    if sel_language == "French":
        nlp = fr_core_news_sm.load()
    if sel_language == "German":
        nlp = de_core_news_sm.load()
    if sel_language == "Spanish":
        nlp = es_core_news_sm.load()

    document = nlp(str(request.json["text"]))

    #check if entities are found for the text and return empty list
    if not document.ents:
        return jsonify({"results":return_val})

    #store text in a dictionary with label as key
    for each_entry in document.ents:
        if each_entry.label_ not in text_dict.keys():
            text_dict[each_entry.label_] = [each_entry.text]
        else:
            text_dict[each_entry.label_].append(each_entry.text)

    #process text_dict and remove duplicate text
    for label in text_dict.keys():
        temp_dict = {"label":label,"text":list(set(text_dict[label]))}
        return_val.append(temp_dict)

    ner_results = jsonify({"results":return_val})
    
    return ner_results