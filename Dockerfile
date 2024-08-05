FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

WORKDIR /app

COPY requirements.txt .

RUN apt-get update -y && apt-get install -y python3 python3-pip libcudnn8 libcudnn8-dev -y && \
ln -s /usr/bin/python3 /usr/bin/python && \    
pip install --no-cache-dir -r requirements.txt 

COPY . .

EXPOSE 8000

CMD ["python", "-m", "whisper"]
