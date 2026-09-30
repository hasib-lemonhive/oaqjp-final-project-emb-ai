from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Receives the text from the HTML interface, runs emotion detection on it,
    and returns the formatted system response. If the input is blank, an
    error message is returned instead.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Error handling for blank entries
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)