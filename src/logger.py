import logging
import os
from datetime import datetime


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)  # create folder if not exists

log_file = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, log_file)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

