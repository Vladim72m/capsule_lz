import os
import pandas as pd
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)      # Выполняем исходную функцию и сохраняем её результат

        file_path = "logs.csv"
        now = datetime.now()    # текущее время

        if os.path.exists(file_path):     # Определяем ID новой записи:
            current_id = pd.read_csv(file_path).shape[0]
        else:
            current_id = 0

        new_row = pd.DataFrame([{
            "logs": current_id,
            "pc_username": os.getlogin(),
            "function_name": func.__name__,
            "Date in date.month.year": now.strftime("%d-%m-%Y"),
            "Time": now.strftime("%H:%M:%S")
        }])

        new_row.to_csv(     # Добавляем строку в CSV:
            file_path,
            mode='a',
            header=not os.path.exists(file_path),
            index=False
        )

        print(f"Данные успешно записаны в {file_path}")
        return result

    return wrapper


