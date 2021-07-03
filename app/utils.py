import hashlib
import json
import jwt

from datetime import datetime, timezone

from app.settings import JWT_SECRET

def get_now() -> datetime:
    return datetime.now()

def get_now_timestamp() -> float:
    return datetime.now(timezone.utc).timestamp()

def get_uuid() -> str:
    timestamp = get_now_timestamp()
    md5 = hashlib.md5()
    md5.update(str(timestamp).encode())
    return md5.hexdigest()

def decode_jwt(jwt_value: str) -> dict:
    return jwt.decode(jwt_value, JWT_SECRET, algorithms=["HS512"])

def generate_jwt(payload: dict) -> str:
    claims = {
        "iat": int(get_now_timestamp()),
        "jti": get_uuid(),
        "payload": payload
    }
    return jwt.encode(claims, JWT_SECRET, algorithm="HS512")

def get_json_file_data(file_path: str, default: str) -> dict:
    try:        
        json_file = open(file_path, "r")
        data = json_file.read()
    except FileNotFoundError:
        data = default

    return json.loads(data)

def write_json_file(file_path: str, data: dict) -> None:
    json_file = open(file_path, "w")
    json_file.write(json.dumps(data))
    json_file.close()

def get_time_diff(start_time: str, end_time:str) -> str:
    start = datetime.strptime(start_time,'%H:%M:%S')
    end = datetime.strptime(end_time,'%H:%M:%S')
    total_time = (end - start)
    return str(total_time)