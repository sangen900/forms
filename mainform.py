import streamlit as st
from form1 import form_1
from form2 import form_2
from form3 import form_3
from form4 import form_4
from form5 import form_5
from form6 import form_6
from form7 import form_7
from form8 import form_8
from form9 import form_9
from form10 import form_10
from form11 import form_11
from form12 import form_12
from form13 import form_13
from form14 import form_14

def main_form():
    page_names1001 = ["form1", "form2", "form3", "form4", "form5", "form6", "form7", "form8", "form9", "form10", "form11", "form12", "form13", "form14"]
    user_selected_page = st.sidebar.radio("Please read the form carefully and fill the below form.", page_names1001)
    
    if user_selected_page == "form1":
        form_1()
    elif user_selected_page == "form2":
        form_2()
    elif user_selected_page == "form3":
        form_3()
    elif user_selected_page == "form4":
        form_4()
    elif user_selected_page == "form5":
        form_5()
    elif user_selected_page == "form6":
        form_6()
    elif user_selected_page == "form7":
        form_7()
    elif user_selected_page == "form8":
        form_8()
    elif user_selected_page == "form9":
        form_9()
    elif user_selected_page == "form10":
        form_10()
    elif user_selected_page == "form11":
        form_11()
    elif user_selected_page == "form12":
        form_12()
    elif user_selected_page == "form13":
        form_13()
    elif user_selected_page == "form14":
        form_14()
if __name__ == "__main__":
    main_form()
