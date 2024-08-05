FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .

# Установите ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && \
    pip install --no-cache-dir -r requirements.txt

COPY src/env.py src/env.py
COPY src/streamlit_app.py src/streamlit_app.py
COPY src/utils.py src/utils.py

EXPOSE 7861

CMD [ "streamlit", "run", "src/streamlit_app.py" ]


# FROM python:3.11-slim
# WORKDIR /app

# COPY requirements.txt .

# # Установите ffmpeg
# RUN apt-get update && apt-get install -y ffmpeg && \
#     pip install --no-cache-dir -r requirements.txt

# COPY src/env.py src/env.py
# COPY src/gradio_app.py src/gradio_app.py
# COPY src/main.py src/main.py
# COPY src/utils.py src/utils.py

# EXPOSE 7861

# CMD [ "python", "src/main.py" ]