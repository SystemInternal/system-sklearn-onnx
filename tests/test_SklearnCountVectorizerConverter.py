"""
Tests scikit-learn's binarizer converter.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), 'test_utils'))

import unittest
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from scikitonx import convert_sklearn
from scikitonx.common.data_types import FloatTensorType, StringTensorType
from test_utils import dump_data_and_model

class TestSklearnCountVectorizer(unittest.TestCase):

    def test_model_count_vectorizer11(self):
        corpus = [
                'This is the first document.',
                'This document is the second document.',
                'And this is the third one.',
                'Is this the first document?',
                ]
        vect = CountVectorizer(ngram_range=(1, 1))
        vect.fit(corpus)
        pred = vect.transform(corpus)
        model_onnx = convert_sklearn(vect, 'scikit-learn count vectorizer', [('input', StringTensorType([1, 1]))])
        self.assertTrue(model_onnx is not None)
        # REVIEW: enable the test when the runtime implements the primitives.
        # dump_data_and_model(corpus, vect, model_onnx, basename="SklearnCountVectorizer")

    def test_model_count_vectorizer13(self):
        corpus = [
                'This is the first document.',
                'This document is the second document.',
                'And this is the third one.',
                'Is this the first document?',
                ]
        vect = CountVectorizer(ngram_range=(1, 3))
        vect.fit(corpus)
        pred = vect.transform(corpus)
        model_onnx = convert_sklearn(vect, 'scikit-learn count vectorizer', [('input', StringTensorType([1, 1]))])
        self.assertTrue(model_onnx is not None)
        # REVIEW: enable the test when the runtime implements the primitives.
        # dump_data_and_model(corpus, vect, model_onnx, basename="SklearnCountVectorizer")


if __name__ == "__main__":
    unittest.main()