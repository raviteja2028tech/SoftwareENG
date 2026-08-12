from se_01 import ravi

def test_prediction_for_12():
    prediction = ravi.predict([[12]])
    assert prediction[0] == 24
