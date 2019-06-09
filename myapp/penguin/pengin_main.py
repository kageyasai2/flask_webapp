import keras
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.models import model_from_json
from PIL import Image
import os
import json
import numpy as np

def check(result):
    f = open('/myapp/penguin/Penguin.json','r')
    json_dict = json.load(f)
    return json_dict[str(result)]

def image(pic):
    img = Image.open(pic).convert('RGB') ## Gray->L, RGB->RGB
    img = img.resize((64, 64))
    x = np.array(img, dtype=np.float32)
    x = x / 255.
    #reshape(サンプル数,盾,横,チャンネル数)
    x = x.reshape(1,64,64,3)
    return x

def main():
    pic = "/myapp/penguin/predict_test/makaroni.jpg"

    #モデル読み込み
    print(os.getcwd())
    model = model_from_json(open('/myapp/penguin/model/pengin_mlp_model.json').read())
    model.load_weights('/myapp/penguin/model/pengin_mlp_weights.h5')
    x = image(pic)
    #予測結果
    tmp = model.predict(x,batch_size=1,verbose=1)
    result = np.argmax(tmp, axis=1)
    txt = check(result[0])
    return txt