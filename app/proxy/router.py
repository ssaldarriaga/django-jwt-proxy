from datetime import datetime
from fastapi import APIRouter, Request, Depends, Body, Response

from app.utils import get_json_file_data, get_time_diff
from app.settings import REPORT_STRUCTURE, REPORT_FILE

routes = APIRouter()

@routes.get("/status")
async def post(request: Request, response: Response):
    data = get_json_file_data(REPORT_FILE, REPORT_STRUCTURE)
    end_time = datetime.now().time().strftime('%H:%M:%S')
    time_frome_start = get_time_diff(data["start_time"], end_time)
    return {"time_frome_start": time_frome_start, "total_requests": data["total_requests"], "details": data["details"]}