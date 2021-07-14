from flask_restx import Namespace, fields

class MLModel():
    ns = Namespace('ML', description = 'this is for machine learning model input')
    ml = ns.model('ML', {
        'hr1' : fields.Float(required=True, description='Value of HR1 Measurement'),
        'hr2' : fields.Float(required=True, description='Value of HR2 Measurement'),
        'peak_locff' : fields.Float(required=True, description='Value of peak location from Fourier Transform'),
        'peak_locr' : fields.Float(required=True, description='Value of peak location from Real part of Fourier Transform'),
        'peak_locim' : fields.Float(required=True, description='Value of peak location from Imaginary part of Fourier Transform'),
        'stdre' : fields.Float(required=True, description='Standar deviation from real part of Fourier Transform'),
        'stdim' : fields.Float(required=True, description='Standar deviation from imaginary part of Fourier Transform'),
        'result' : fields.Integer(required=False, description='Return of Observe new data From model')
    })