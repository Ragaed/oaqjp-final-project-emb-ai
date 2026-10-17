'''
This module is intended to test 
EmotionDetection package
'''

from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    '''
    Class to test Emotion Detection
    '''

    def test_emotion_detector(self):
        '''
        Test the dominant emotion of 
        emotion detector
        '''
        self.assertEqual('joy', emotion_detector('I am glad this happened')['dominant_emotion'])
        self.assertEqual('anger', emotion_detector('I am really mad about this')['dominant_emotion'])
        self.assertEqual('disgust', emotion_detector('I feel disgusted just hearing about this')['dominant_emotion'])
        self.assertEqual('sadness', emotion_detector('I am so sad about this')['dominant_emotion'])
        self.assertEqual('fear', emotion_detector('I am really afraid that this will happen')['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()