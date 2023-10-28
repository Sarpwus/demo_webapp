import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn = st.experimental_connection('gsheets', type = GSheetsConnection)

def load_db():
    data = conn.read(worksheet ="Fruit", usecols=list(range(2)),ttl=2)
    df = pd.DataFrame(data[data["Fruit"].notnull()])

    return df


# title for the app
st.title("Demo Fruit Database")

# add a query form to display follow up notes for a given member
st.sidebar.header("Fruit entry form")
fruit_form = st.sidebar.form("fruit_form")
fruit_name = fruit_form.text_input("Fruit", "")
fruit_value = fruit_form.text_input("Value", "")
add_data = fruit_form.form_submit_button("Add data")


# show df
my_df = load_db()
st.write("Current overview of the Fruit Database")
st.dataframe(my_df)

if add_data:
    my_df = load_db()
    #my_df
    new_data = {"Fruit": fruit_name, "Value": int(fruit_value)}
    st.write(new_data)
    
    my_df = my_df.append(new_data, ignore_index = True)
    st.success("Worksheet has been updated 🤓")
    #df.to_csv("userdata.csv", index = False)
    st.write("Updated overview of the Fruit Database")
    st.dataframe(my_df)
    conn.update(worksheet="Fruit", data = my_df)

    
    

