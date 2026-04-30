import streamlit as st
import time

# Додати заголовок у додаток
st.title('Приклад Progress Bar')

# Створити progress bar
progress = st.progress(0)

# Імітація довготривалого процесу
for i in range(100):
    # Оновлення progress bar кожну секунду
    time.sleep(0.1)  # Пауза на 0.1 секунди
    progress.progress(i + 1)  # Оновити progress bar

# Вивести повідомлення про завершення процесу
st.success('Обробка завершена!')
