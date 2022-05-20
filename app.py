import streamlit as st
from app_home import run_home
from app_eda import run_eda
def main() :
    st.title('자동차 가격 예측')
    menu= ['Home','EDA','ML']
    choice = st.sidebar.selectbox('메뉴 선택',menu)
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        pass























if __name__ == '__main__' :
    main()
