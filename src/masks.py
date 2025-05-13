from typing import Union
import logging
from pathlib import Path

logger = logging.getLogger("MASKS_LOGGER")
logger.setLevel(logging.DEBUG)

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True, mode=0o777)

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


def get_mask_card_number(card_number: Union[int, str, float]) -> str:
    """Маскирует номер карты с обработкой всех случаев из тестов"""
    logger.debug(f"Начало обработки: {card_number}")
    try:
        card_str = str(card_number).strip().replace(" ", "")

        if not card_str or not card_str.isdigit():
            logger.error(f"Некорректный ввод: {card_number}")
            return "Некорректный номер карты, пожалуйста введите верный номер карты"

        if len(card_str) != 16:
            logger.error(f"Неверная длина: {len(card_str)}")
            return "Некорректный номер карты, пожалуйста введите верный номер карты"

        masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        logger.info(f"Успешно: {masked}")
        return masked

    except Exception as e:
        logger.critical(f"Ошибка обработки: {e}", exc_info=True)
        return "Некорректный номер карты, пожалуйста введите верный номер карты"


def get_mask_account(account: Union[int, str]) -> str:
    """Маскирует номер счета (последние 4 цифры)"""
    logger.debug(f"Начало обработки счёта: {account}")
    try:
        account_str = str(account).strip().replace(" ", "")

        if not account_str or not account_str.isdigit():
            logger.error(f"Некорректный ввод: {account}")
            return "Некорректный номер счета"

        if len(account_str) < 4:
            logger.error(f"Счёт слишком короткий: {len(account_str)}")
            return "Некорректный номер счета"

        masked = f"**{account_str[-4:]}"
        logger.info(f"Успешно: {masked}")
        return masked

    except Exception as e:
        logger.critical(f"Ошибка обработки счёта: {e}", exc_info=True)
        return "Ошибка обработки счёта"