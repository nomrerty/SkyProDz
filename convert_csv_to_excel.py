import pandas as pd

# Путь к CSV
csv_path = "test_data/test_transactions.csv"
excel_path = "test_data/test_transactions.xlsx"  # Сохраню рядом

# Конвертация
df = pd.read_csv(csv_path, sep=";")
df.to_excel(excel_path, index=False, engine="openpyxl")

print(f"Файл {excel_path} успешно создан!")  #вот команда в терминал вставить и делает xlsx файл: python convert_csv_to_excel.py
