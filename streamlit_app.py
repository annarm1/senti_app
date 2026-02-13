import streamlit as st
import numpy as np
import pandas as pd


# Show title and description.
st.title("Эмоциональный анализ текстов на русском языке")
st.write(
    "Мяу мяу что же будет здесь и как будет выглядеть не знаааааююююю"
    "Хай хай я просто тестирую платформу"
)



uploaded_file = st.file_uploader(
        "Загрузи документ (форматы .txt or .md)", type=("txt", "md", "pdf")
    )


in_text = st.text_input('Здесь можно напечатать текст')

st.button('Просто кнопочка')
st.write('Опять текст опять текст')
st.title("проверяю разные штуки поэтому АЛЯЛАЛЯЛАЛАФУАОТФОЦА")


number = st.text_input('Ляляля попробуй вбить цифры например 1 2 3 4 5 6')
if len(number.split()) > 5:
    st.write("Хаха как много цифр")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBAf-0MF3Kz2SMbmDxCzYiVQvRaadyBqL5Hw&s", caption="Ты молодец! Вот тебе котик")
elif len(number.split()) <= 5 and len(number.split()) != 0:
    st.write("Ну что так мало цифр????")

st.write('А это просто прикольный график ляляля')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)