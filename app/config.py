import os
from dotenv import load_dotenv

#讀取 .env 檔案裡面的隱藏設定
load_dotenv()

#設定環境狀態，預設是開發中 (development)
APP_ENV = os.getenv("APP_ENV", "development")

#設定 Agent的任務紀錄要存在哪一個檔案
AGENT_LOG_FILE = os.getenv("AGENT_LOG_FILE", "agent_log.json")