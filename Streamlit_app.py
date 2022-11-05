import streamlit as st

st.write('Hello world!')
st.title('Edileny Cardoso!')
st.selectbox('Selecione uma opção:',['opção 1','opção 2','teste3'])

st.sidebar.title('MENU')

st.sidebar.write('Hello world!')
st.sidebar.title('Edileny Cardoso!')
st.sidebar.selectbox('Selecione uma opção:',['opção 4','opção 5','teste6'])

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')




import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)