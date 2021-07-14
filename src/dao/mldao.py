from src.model.mlmodel import MLModel
import joblib


model = MLModel()
mldata = model.ml

class MLDao(object):
    def __init__(self):
        self.model = joblib.load('src/dao/model_dump.pkl')

    def predict(self, data):
        mldata = data
        observer = [[mldata['hr1'], mldata['hr2'], mldata['peak_locff'], mldata['peak_locr'], mldata['peak_locim'], mldata['stdre'], mldata['stdim']]]
        result = self.model.predict(observer)
        mldata['result'] = result
        return mldata