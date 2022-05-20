import streamlit as st
import pandas as pd 
import seaborn as sb 

def run_eda() :
    st.subheader('데이터 분석')
    car_df = pd.read_csv('data/Car_Purchasing_Data.csv',encoding='ISO-8859-1')
    # 라디오버튼을 통해서 , 데이터 프레임과 , 통계치를 선택해서  보여줄수있도록 한다.

    radio_menu = ['데이터프레임','통계치']
    selected  = st.radio('선택하세요',radio_menu)

    if selected  == radio_menu[0] :
        st.dataframe(car_df)
    elif selected == radio_menu[1] :
        st.dataframe(car_df.describe())

    # 컬럼명을 보여주고, 컬럼을 선택하면
    # 해당 컬럼의 최대값 데이터와 , 최소값 데이터를 보여준다.

    col_list = car_df.columns[4 : ]
    selected_col = st.selectbox('최대 최소 원하는 컬럼 선택',col_list)

    df_max =car_df.loc[car_df[selected_col]==car_df[selected_col].max(), ]
    df_min =car_df.loc[car_df[selected_col]==car_df[selected_col].min(), ]

    st.text('{} 컬럼의 최대값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_max)
    st.text('{} 컬럼의 최소값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_min)

    # 유저가 선택한 컬럼들만, pairplot 그리고, 그아래 상관 계수를 보여준다.
    selected_list = st.multiselect('컬럼들 선택',col_list)
    if len(selected_list) != 0 :
        fig1 = sb.pairplot(data=car_df[selected_list])
        st.pyplot(fig1)
    