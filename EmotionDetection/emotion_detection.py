'''

Module responsible for getting emotion

from text with the help of IBM libraries

'''

import requests
import json

def emotion_detector(text_to_analyse):

    '''

    This function return an dictionary 

    containing the label and score from

    from BERT API analysis

    '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers = header)

    formatted_output = json.loads(response.text)

    emotions = formatted_output['emotionPredictions'][0]['emotion']

    emotions['dominant_emotion'] = get_dominant_emotion(emotions)

    return emotions

def get_dominant_emotion(emotions):
    '''
    Gets the most dominant emotion
    from dictionary
    '''

    hightest_score = 0
    dominant_emotion = ''

    for emotion in emotions.keys():
        current_score = emotions[emotion]
        if (current_score > hightest_score):
            hightest_score = current_score
            dominant_emotion = emotion

    return dominant_emotion;