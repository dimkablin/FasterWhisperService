import os
import logging
from faster_whisper import WhisperModel
from whisper.env import MODEL, WEIGHTS_PATH


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Инициализация модели
try:
    whisper_model = WhisperModel(MODEL, download_root=WEIGHTS_PATH, device='cuda')
    logger.info(f'Whisper {whisper_model.model} на GPU...')
except Exception as cuda_error:
    logger.warning(f'Ошибка инициализации CUDA: {cuda_error}\nИнициализация модели на CPU')
    whisper_model = WhisperModel(MODEL, download_root=WEIGHTS_PATH, device='cpu')


# Убедитесь, что директория для данных существует
os.makedirs("whisper/data", exist_ok=True)
