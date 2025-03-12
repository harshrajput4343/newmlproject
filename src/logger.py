import logging
import os
from datetime import datetime

# Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define logs directory (without file name)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # ✅ Creates only the folder, not the file

# Define full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ✅ Add test log messages
if __name__ == "__main__":
    logging.info("Logging system initialized successfully.")
    logging.warning("This is a test warning log.")
    logging.error("This is a test error log.")
    logging.critical("This is a test critical log.")