import os
import sys
import logging

#defining the custom logging stream
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# asctime - ASCII time of running
# levelname - file name on which log returns after running it
# module - name of the module on which you are running your code
# message -  log message

logs_dir = "logs"   #directory name
os.makedirs(logs_dir, exist_ok=True)    #creating logs directory to store the log files

log_filepath = os.path.join(logs_dir, "running_logs.log")
#initializing the final log
logging.basicConfig(
    level=logging.INFO,
    format=logging_str, #initializing logging screen
    handlers=[
        logging.FileHandler(log_filepath),  #for creating log files
        logging.StreamHandler(sys.stdout)   #for printing in the console
    ]
)

logger = logging.getLogger("cnnClassifierLogger")