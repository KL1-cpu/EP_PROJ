import json
import os
from typing import Optional

STORE_PATH = os.path.join(os.path.dirname(__file__), "..", "users.json")

def _load_store() -> dict:
    try:
        with open(STORE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception:
        return {}

def _save_store(data: dict):
    # ensure folder exists
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    with open(STORE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_user_info(user_id: int) -> Optional[dict]:
    data = _load_store()
    return data.get(str(user_id))

def set_user_info(user_id: int, last_name: str, first_name: str, phone: str, extra_data: dict = None):
    data = _load_store()
    user_data = {
        "last_name": last_name,
        "first_name": first_name,
        "phone": phone
    }
    if extra_data:
        user_data.update(extra_data)
    data[str(user_id)] = user_data
    _save_store(data)
