import pickle

def prediction(age):
    model = pickle.load(open('model.pkl','rb'))
    SBP = model.predict([[age]])
    return SBP