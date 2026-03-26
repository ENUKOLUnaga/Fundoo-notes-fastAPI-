import logging

# Create logger
logger = logging.getLogger("fundoo-app")

# Set level
logger.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler("logs/app.log")
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)