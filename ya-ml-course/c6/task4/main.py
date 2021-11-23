import logging

import tensorflow as tf
import tensorflow_text as text  # noqa
from flask import Flask, request, escape


logging.basicConfig(level=logging.INFO, format='%(asctime)s\t%(levelname)s\t%(message)s')

logging.info('Loading TF model...')
classifier = tf.keras.models.load_model('review_classifier_model', compile=False)

logging.info('Starting server')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    message = ''
    if request.method == 'POST':
        text = request.form['text']
        result = tf.sigmoid(classifier(tf.constant([text])))

        message = 'Item is good'
        if result.numpy()[0] < 0.5:
            message = 'Item is bad'

    html = (
        '<!doctype html>'
        '<form method=post>'
        f'<textarea name=text required style="width: 400px; height: 200px">{escape(text)}</textarea>'
        '<br>'
        '<input type=submit>'
        '</form>'
        '<br>'
        f'<b>{message}</b>'
    )
    return html
