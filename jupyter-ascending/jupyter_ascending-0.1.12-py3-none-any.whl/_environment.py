import os

EXECUTE_HOST = os.getenv("JUPYTER_ASCENDING_EXECUTE_HOST", "localhost")
EXECUTE_PORT = os.getenv("JUPYTER_ASCENDING_EXECUTE_PORT", 12517)

EXECUTE_HOST_LOCATION = (EXECUTE_HOST, EXECUTE_PORT)
EXECUTE_HOST_URL = f"http://{EXECUTE_HOST_LOCATION[0]}:{EXECUTE_HOST_LOCATION[1]}"

LOG_LEVEL = os.getenv("JUPYTER_ASCENDING_LOG_LEVEL", "INFO")
SHOW_TO_STDOUT = os.getenv("JUPYTER_ASCENDING_SHOW_TO_STDOUT", False)
