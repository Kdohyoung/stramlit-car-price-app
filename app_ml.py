import streamlit as st
import pandas as pd 
import joblib
import numpy as np
import sklearn
def run_ml():
    st.subheader('자동차 구매 가능 금액 예측')

    print(sklearn.__version__)

    # 예측하기 위해서 필요한 파일들을 불러와야 한다.
    # 이 예에서는, 인공지는파일, X 스케일러 파일 , y 스케일러 파일   이 3개를 불러와야한다,
    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')

    # 성별, 나이 , 연봉 ,카드빚 , 자산 을 입력받도록 만드세요
    my_order =  ['남자','여자']
    gender = st.radio('성별을 선택하세요',my_order)
    if gender =='여자' :
        gender = 0
    else :
        gender = 1

    age = st.number_input('나이를 입력하세요',1,100)
    salary = st.number_input('연봉입력',0,)
    debt = st.number_input('카드빚 입력',0,)
    worth = st.number_input('자산 입력',0,)
    
    if st.button ('자동차 구매 금액 예측') : 

        # 1.  신규 고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([gender,age,salary,debt,worth])

        # 2. 학습할때 사용한 X 의 피쳐 스케일러를 이용해서 , 피쳐스케일링한다.
        # 먼저 , 데이터를 2차원으로 만들어준다.
        new_data = new_data.reshape(1,5)
        new_data=scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)

        # 4. 예측한 값을 원상 복구
        y_pred = scaler_y.inverse_transform(y_pred)
        y_pred = round(y_pred[0,0])
        st.write('이 사람의 구매 가능 금액은' + str(y_pred)+'달러입니다')






