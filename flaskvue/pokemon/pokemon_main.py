import sys
import os
import json
if  len(sys.argv) != 2:
    print("画像名をコマンドライン引数に加えてください")
    sys.exit()
    
if not os.path.isfile(sys.argv[1]):
    print("そのファイルは存在しません")
    sys.exit()

import keras
from keras.models import model_from_json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def check(result):
    f = open('Pokemon.json','r')
    json_dict = json.load(f)
    if result == 0:
        return json_dict['Pikachu']
    elif result == 1:
        return json_dict['Raichu']
    elif result == 2:
        return json_dict['Pichu']

def image(pic):
    img = Image.open(pic).convert('RGB') ## Gray->L, RGB->RGB
    img = img.resize((64, 64))
    x = np.array(img, dtype=np.float32)
    x = x / 255.
    #reshape(サンプル数,盾,横,チャンネル数)
    x = x.reshape(1,64,64,3)
    #print(x)
    return x

def predict():
    pic = sys.argv[1]
    #モデル読み込み
    model = model_from_json(open('model/pokemon_mlp_model.json').read())
    model.load_weights('model/pokemon_mlp_weights.h5')
    x = image(pic)
    #予測結果
    tmp = model.predict(x,batch_size=1,verbose=0)
    result = np.argmax(tmp, axis=1)
    print(result)
    txt = check(result)
    return txt

def main():
    x = predict()
    print(x)

if __name__ == "__main__":
    main()
