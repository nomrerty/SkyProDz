from typing import Union
import logging
import os
from pathlib import Path

# Жёсткая настройка логгера (100% рабочий вариант)
logger = logging.getLogger("MASKS_LOGGER")
logger.setLevel(logging.DEBUG)

# Абсолютный путь для надёжности
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True, mode=0o777)  # Полные права

handler = logging.FileHandler(
    filename=log_dir / "masks.log",
    mode='a',
    encoding='utf-8'
)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))
logger.addHandler(handler)



def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Маскирует номер карты"""
    logger.debug(f"Начало обработки: {card_number[:4]}...")
    try:
        card_number = str(card_number).replace(" ", "")
        if len(card_number) != 16:
            logger.error(f"Неверная длина: {len(card_number)}")
            return "Некорректный номер карты"

        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Успешно: {masked}")
        return masked
    except Exception as e:
        logger.critical(f"Ошибка: {e}", exc_info=True)
        return "Ошибка обработки"


# ... (остальные функции)

if __name__ == "__main__":
    # Тестовые вызовы
    print(get_mask_card_number("1234567890123456"))  # Успешный случай
    print(get_mask_card_number("123"))  # Ошибка


# Тестовый вызов
if __name__ == "__main__":
    logger.info("Тест записи в лог")
    print(f"Проверьте файл: {log_dir / 'masks.log'}")
