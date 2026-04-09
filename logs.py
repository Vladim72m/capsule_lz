import os
import pandas as pd
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        file_path = "logs.csv"
        now = datetime.now()

        # авто‑id
        if os.path.exists(file_path):
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

        new_row.to_csv(
            file_path,
            mode='a',
            header=not os.path.exists(file_path),
            index=False
        )

        print(f"Данные успешно записаны в {file_path}")
        return result

    return wrapper


