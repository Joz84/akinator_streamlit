import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Akinator")

st.image("https://fr.akinator.com/bundles/elokencesite/images/akitudes_670x1096/defi.png", width=200)


st.markdown("## Description")
 
st.markdown('Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos sunt quod porro nulla omnis nam non earum debitis consectetur ut recusandae, sed quaerat qui iste? Delectus non minima minus dolorum.')

st.markdown('<a src="https://docs.streamlit.io/library/api-reference">Doc</a>', unsafe_allow_html = True)

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

df['thirth column'] = df['first column'] * 2


x1 = st.slider('x?', 1, 11, 3)
y1 = st.slider('y?', 1, 11, 3)

def sum(x, y):
    return x + y
    
st.write(f"La somme de {x1} et de {y1} est {sum(x1, y1)}")


lines_number = st.slider('Lines number?', 1, 11, 3)

head_df = df.head(lines_number)

head_df

st.line_chart(df)