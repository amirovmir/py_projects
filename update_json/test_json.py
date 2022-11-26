# 1) Прочитать содержимое файла
# 2) Дописать третий вопрос в блок math
# 3) Записать в файл

import json
import numpy as np
import pandas as pd


def open_json():
    with open('quiz.json', 'r') as f:
        data = json.load(f)
        print(json.dumps(data, indent=4, sort_keys=True))


question = {"question": "7 + 8 = ?",
        "options": [
            "14",
            "78",
            "15",
            "16"
        ],
        "answer": "15"
}

def change_content():
    with open('quiz.json', 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df2 = pd.DataFrame()
    df2 = df['quiz']
    df3 = pd.DataFrame(df2['maths'])

    df3["q3"] = question
    df2["maths"] = df3
    df["quiz"] = df2

    df.to_json(r'.\quiz.json', indent=4)

if __name__ == '__main__':
    open_json()
    change_content()
