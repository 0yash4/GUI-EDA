import logging
import os

# Create log folder if it doesn't exist
LOG_FOLDER = "Logs"
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

LOG_FILE = os.path.join(LOG_FOLDER, "Logging_info.log")


logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


if __name__=="__main__":
    logging.warning("Half-way through logging")
    logging.info("This is Info")