import streamlit as st
import pandas as pd 
import joblib
def run_ml():
    st.subheader('자동차 구매 가능 금액 예측')

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












