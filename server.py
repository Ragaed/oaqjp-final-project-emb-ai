'''
Page for emotion detector
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def load_index_page():
    '''
    Just returns the main page
    '''
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion_detection():
    '''
    Returns the emotion detection for the value
    in the form
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_analysis = emotion_detector(text_to_analyse)

    if emotion_analysis['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return emotion_analysis

if __name__ == '__main__':
    app.run(debug=True)
    