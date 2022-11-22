def calWinRate(champList):
    # champList는 챔피언명 10개가 담긴 리스트
    # 순서는 아군 탑~서폿 + 적군 탑~서폿
    import pickle
    import numpy as np
    import pandas as pd
    # 승률 예측 모델
    with open("pickles/model.pickle", "rb") as fr:
        model = pickle.load(fr)

    # 모델에 필요한 각 포지션별 챔피언에 대응되는 x값들
    with open("pickles/label_top2.pickle", "rb") as fr:
        label_top = pickle.load(fr)
    with open("pickles/label_jgl2.pickle", "rb") as fr:
        label_jgl = pickle.load(fr)
    with open("pickles/label_mid2.pickle", "rb") as fr:
        label_mid = pickle.load(fr)
    with open("pickles/label_bot2.pickle", "rb") as fr:
        label_bot = pickle.load(fr)
    with open("pickles/label_sup2.pickle", "rb") as fr:
        label_sup = pickle.load(fr)

    labels = [label_top, label_jgl, label_mid, label_bot, label_sup]  # for문 돌리기 위함
    x = np.array([])
    for i in range(10):
        x = np.append(x, labels[i % 5].loc[champList[i]])
    return model.predict_proba([x])[0][0]


def recommendChamp(champList, position):
    # champList: 내가 골라야 할 포지션은 None, 나머지는 결정된 상태
    # position: top/jgl/mid/bot/sup
    import pickle
    with open("pickles/" + position + "_major.pickle", "rb") as fr:  # 입력된 포지션에 따라 챔프리스트 다르게 불러옴
        major = pickle.load(fr)

    dictp = {'top': 0, 'jgl': 1, 'mid': 2, 'bot': 3, 'sup': 4}
    resList = []  # 모든 챔프에 대해 기대승률 계산한 결과 담아둘 리스트

    for champ in major:
        champList[dictp[position]] = champ  # champList에서 추천받을 포지션에 챔피언 대입
        resList.append((calWinRate(champList), champ))  # 계산 결과 리스트에 보관

    resList.sort(reverse=True)  # 승률로 정렬
    return resList[0:3]  # 최대 승률인 챔프리턴
