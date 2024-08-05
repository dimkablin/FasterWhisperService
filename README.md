# Faster Whisper Service
![img](
    https://img.shields.io/badge/12.0_|_12.1_|_12.2-black?style=flat&logo=nvidia&label=CUDA
) ![img](
    https://img.shields.io/badge/3.10_|_3.11_|_3.12-black?style=flat&logo=python&label=python
) 

![img](
https://img.shields.io/badge/Apache_2.0-orange?style=flat&label=license
)


# FasterWhisperService

FasterWhisperService — это веб-сервис на основе FastAPI, использующий библиотеку Faster Whisper для транскрибирования аудиофайлов. Сервис контейнеризован с использованием Docker для упрощения развертывания.

## Особенности

- Транскрибирование аудиофайлов в текст с использованием модели Whisper.
- Поддержка как GPU, так и CPU для транскрибирования.
- Предоставление временных меток на уровне слов по запросу.

## Требования

- Docker
- Python 3.9 (если запускать локально)

## Установка

### Использование Docker

1. **Клонируйте репозиторий**:
    ```sh
    git clone https://github.com/yourusername/FasterWhisperService.git
    cd FasterWhisperService
    ```

2. **Создайте файл `.env`** в корневом каталоге проекта со следующим содержимым:
    ```env
    WHISPER_MODEL=large-v3
    WEIGHTS_PATH=whisper/weights
    WHISPER_PORT=8000
    WHISPER_ADDRESS=0.0.0.0
    ```

3. **Соберите Docker-образ**:
    ```sh
    docker build -t faster-whisper-service .
    ```

4. **Запустите Docker-контейнер**:
    ```sh
    docker run --env-file .env -p 8000:8000 faster-whisper-service
    ```

### Запуск локально

1. **Клонируйте репозиторий**:
    ```sh
    git clone https://github.com/dimkablin/FasterWhisperService.git
    cd FasterWhisperService
    ```

2. **Создайте виртуальное окружение и активируйте его**:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Установите необходимые зависимости**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Создайте файл `.env`** в корневом каталоге проекта со следующим содержимым:
    ```env
    WHISPER_MODEL=large-v3
    WEIGHTS_PATH=whisper/weights
    WHISPER_PORT=8000
    WHISPER_ADDRESS=127.0.0.1
    ```

5. **Запустите приложение**:
    ```sh
    python3 -m whisper
    ```

## Использование API

### Эндпоинт

`POST /api/v1/speech2text`

### Запрос

- **Заголовки**:
    - `Content-Type: multipart/form-data`

- **Тело запроса**:
    - `audio`: Аудиофайл для транскрибирования.
    - `word_timestamps` (необязательно): Булевый флаг для включения временных меток слов в ответ.

### Ответ

- **Успех**: `200 OK`
    - `result`: Результат транскрибирования, либо в виде обычного текста, либо в виде списка сегментов с временными метками.
- **Ошибка**: `4xx` или `5xx`

## Пример

Использование `curl` для отправки запроса:

```sh
curl -X POST "http://localhost:8000/api/v1/speech2text" -F "audio=@path_to_audio_file" -F "word_timestamps=true"
```

## Структура проекта

```
FasterWhisperService/
├── whisper/
│   ├── data/
│   ├── Dockerfile
│   ├── env.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── speech2text.py
│   ├── requirements.txt
│   └── weights/
├── .env
└── README.md
```

## Лицензия

Этот проект лицензирован по лицензии MIT. Смотрите файл [LICENSE](LICENSE) для подробностей.

## Благодарности

- [FastAPI](https://fastapi.tiangolo.com/)
- [Faster Whisper](https://github.com/openai/whisper)


### Примечания:
- Замените `https://github.com/yourusername/FasterWhisperService.git` на фактический URL вашего репозитория.
- Убедитесь, что содержимое файла `.env` соответствует необходимым переменным окружения для вашего проекта.
- Убедитесь, что предоставляете соответствующую лицензию в файле `LICENSE`, если включаете этот раздел в `README.md`.
