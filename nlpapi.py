
from flask import Flask
from flask import jsonify
from flask import request


import spacy
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

#TYPE	DESCRIPTION
#PERSON	People, including fictional.
#NORP	Nationalities or religious or political groups.
#FAC	Buildings, airports, highways, bridges, etc.
#ORG	Companies, agencies, institutions, etc.
#GPE	Countries, cities, states.
#LOC	Non-GPE locations, mountain ranges, bodies of water.
#PRODUCT	Objects, vehicles, foods, etc. (Not services.)
#EVENT	Named hurricanes, battles, wars, sports events, etc.
#WORK_OF_ART	Titles of books, songs, etc.
#LAW	Named documents made into laws.
#LANGUAGE	Any named language.
#DATE	Absolute or relative dates or periods.
#TIME	Times smaller than a day.
#PERCENT	Percentage, including ”%“.
#MONEY	Monetary values, including unit.
#QUANTITY	Measurements, as of weight or distance.
#ORDINAL	“first”, “second”, etc.
#CARDINAL	Numerals that do not fall under another type.
@app.route('/nlp/EntityRecognizer/<type>/<sentence>',methods=['GET'])
def knowsentiment(sentence,type):
    type = type.lower()
    doc = nlp(sentence)
    if(type == 'verbs'):
        verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        return jsonify({'Verbs':verbs})
    elif(type == 'nouns'):
        noun = [chunk.text for chunk in doc.noun_chunks]
        return jsonify({'Nouns':noun})
    elif(type == 'entities'):
        entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
        return jsonify({'entities': entities})
    elif(type == 'all'):
        verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        noun = [chunk.text for chunk in doc.noun_chunks]
        entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
        return jsonify({'entities': entities,'Verbs':verbs,'Nouns':noun})
    elif(type != 'All' or type != 'Entities' or type != 'Verbs' or type != 'Nouns'):
        return jsonify({'error':'type not available'})
    

if __name__ == '__main__':
 app.run()