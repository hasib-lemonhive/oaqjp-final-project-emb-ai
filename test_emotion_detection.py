import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        test_statements = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for statement, expected_emotion in test_statements:
            with self.subTest(statement=statement):
                response = emotion_detector(statement)
                self.assertEqual(response['dominant_emotion'], expected_emotion)


if __name__ == '__main__':
    unittest.main()