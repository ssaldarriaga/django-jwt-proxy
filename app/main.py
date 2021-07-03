from datetime import datetime
from fastapi import FastAPI, Request

from app.proxy import router as proxy_router
from app.settings import REPORT_STRUCTURE, REPORT_FILE
from app.users import router as user_router
from app.utils import get_json_file_data, write_json_file

app = FastAPI()
app.start_time = datetime.now().time().strftime('%H:%M:%S')

app.include_router(user_router.routes)
app.include_router(proxy_router.routes)

@app.middleware("http")
async def update_status_report(request: Request, call_next):
    data = get_json_file_data(REPORT_FILE, REPORT_STRUCTURE)
    data["start_time"] = app.start_time
    data["total_requests"] += 1
    value = data["details"].get(request.url.components.path, 0)
    data["details"][request.url.components.path] = value + 1    
    write_json_file(REPORT_FILE, data)
    
    response = await call_next(request)
    return response