import json
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')

log_file_path = os.path.join(log_dir, "utils.log")

os.makedirs(log_dir, exist_ok=True)

file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Транзакции успешно загружены из файла: {filepath}")
                return data
            else:
                logger.warning(f"Файл {filepath} содержит данные не в формате списка. Возвращен пустой список.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {filepath}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {filepath}")
        return []
    except Exception as e:
        logger.exception(f"Произошла ошибка при загрузке транзакций: {e}")  # Логируем полную трассировку
        return []
