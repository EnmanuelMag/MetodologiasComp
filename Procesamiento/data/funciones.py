from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from google.cloud import translate_v3 as translate
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#Coloco aqui esta linea para que no se ejecute cada vez que se llama a la funcion
stop_words = set(stopwords.words('spanish'))

def limpiarStopWords(comentario):

    comentario = comentario.replace("\n", "")
    oraciones = word_tokenize(comentario)
    comentFiltrado = [w for w in oraciones if not w in stop_words]
    return " ".join(comentFiltrado)

def separarPalabras(comentFiltrado):

    return " ".join(re.findall("[A-Z][^A-Z]*", comentFiltrado))

def llenarDiccionario(profesor, codigoMat, termino, anio, comentsLimpios, dicc):

    if profesor not in dicc.keys():
        dicc[profesor] = {codigoMat: {anio: {termino: comentsLimpios}}}
    else:
        if codigoMat not in dicc[profesor].keys():
            dicc[profesor][codigoMat] = {anio: {termino: comentsLimpios}}
        else:
            if anio not in dicc[profesor][codigoMat].keys():
                dicc[profesor][codigoMat][anio] = {termino: comentsLimpios}
            else:
                if termino not in dicc[profesor][codigoMat][anio].keys():
                    dicc[profesor][codigoMat][anio][termino] = comentsLimpios
                else:
                    dicc[profesor][codigoMat][anio][termino].extend(comentsLimpios)

    return dicc

def detectasSentimientos(comentario):

    authenticator = IAMAuthenticator('HGQfgUKC9Fqzjd1ByZlA2SUeovZaAz0G-veawWHILSLj')

    tone_analyzer = ToneAnalyzerV3(version='2017-09-21',authenticator=authenticator)
    tone_analyzer.set_service_url("https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21")
    tone_analysis = tone_analyzer.tone({'text': comentario},content_type='application/json').get_result()

    result = json.dumps(tone_analysis, indent=2)
    print(result)
    return result



def sample_translate_text(text):

    authenticator = IAMAuthenticator('wmFyRWgaNLIIlZ6DHVkC41j6ZvUWdZrO3mWsBgggSgs5')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)

    language_translator.set_service_url('https://gateway.watsonplatform.net/language-translator/api/v3/translate?version=2018-05-01')
    translation = language_translator.translate(
        text=text,model_id='en-es').get_result()

    print(json.dumps(translation, indent=2, ensure_ascii=False))


