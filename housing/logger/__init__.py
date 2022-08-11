import logging
from datetime import datetime
import os

logDir = "housing_logs"
currentTime = f"{datetime.now().strftime('%b-%d-%Y__%H-%M-%S')}"
logFilename = f"{currentTime}.log"

os.makedirs(logDir, exist_ok=True)
filePath = os.path.join(logDir, logFilename)

logging.basicConfig(
    filename=filePath, filemode="w", level=logging.INFO,
    format='[%(asctime)s] %(name)s | %(levelname)s | %(module)s | %(message)s',
    datefmt="%b-%d-%Y_%H:%M:%S"
)

log = logging.getLogger()
