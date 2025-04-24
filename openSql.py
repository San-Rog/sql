import streamlit as st
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from streamlit.runtime.secrets import secrets_singleton

secrets_singleton._secrets = {'conections.mysql': 
                             {
                              'type': 'sql', 
                              'dialect': 'mysql', 
                              'username': 'root', 
                              'password': '', 
                              'host': 'localhost', 
                              'port': '3306', 
                              'database': 'devmedia2'
                              }
                              }
st.write(st.secrets)
bdSql = 'devmedia2'
table = 'tabelaz'

#abertura do arquivo
conn = st.connection(name='', **st.secrets['conections.mysql'], ttl=600)

#pesquisa de todos os registros
allData = conn.query(f"SELECT * from {table}")
st.dataframe(allData)

#
allSchema = conn.query(f"SHOW COLUMNS FROM {table}")
attributes = allSchema.columns #atributos de cada campo tabela selecionada
fields = allSchema.iloc[:, 0] #campos da tabela selecionada
st.write(attributes)
st.write(fields)
for row in allData.itertuples():
    for f, field in enumerate(fields):
        n = f + 1
        try:
            match n:
                case 1:
                    icon = ':white_check_mark:'
                case 2:
                    icon = ':hash:'
                case 3:
                    icon = ':admission_tickets:'
                case 4:
                    icon = ':art:'
                case 5:
                    icon = ':boom:'                
                case _:
                    icon = ':mask:'            
            st.write(f"{icon}{field}: {row[n]}")
        except:
            pass
    st.divider()
           
