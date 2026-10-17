'''
Page for emotion detector
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def load_index_page():
    '''
    Just returns the main page
    '''
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def get_emotion_detection():
    '''
    Returns the emotion detection for the value
    in the form
    '''
    return '', 505 #NEED TO Be IMPLEMENTED

if __name__ == '__main__':
    app.run(debug=True)