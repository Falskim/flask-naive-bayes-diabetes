import pickle

asset_directory = 'static'
model_filename = 'model.pickle'

load_path = asset_directory + '/' + model_filename
model = pickle.load(open(load_path, 'rb'))

def predict(data):
  parsed_data = [data[key] for key in data]
  print("Parsed data : ", parsed_data)

  prediction = int(model.predict([parsed_data])[0])
  print("Prediction : ", prediction)

  return {"class" : prediction}