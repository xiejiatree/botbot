# verify_deployment.py
import sys
import os
import logging

# Configure logging
logging.basicConfig(
    filename='/home/LogFiles/deployment_verify.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def verify_environment():
    logging.info("Starting deployment verification")
    
    # Log system information
    logging.info(f"Current Working Directory: {os.getcwd()}")
    logging.info(f"Python Executable: {sys.executable}")
    logging.info(f"Python Version: {sys.version}")
    
    # Log Python path
    logging.info("Python Path:")
    for path in sys.path:
        logging.info(path)
    
    # Log installed packages
    try:
        import pkg_resources
        logging.info("Installed Packages:")
        for package in pkg_resources.working_set:
            logging.info(f"{package.key} == {package.version}")
    except Exception as e:
        logging.error(f"Error listing packages: {str(e)}")
    
    # Attempt to import critical packages
    packages_to_verify = ['discord', 'discord.py', 'aiohttp']
    
    for package in packages_to_verify:
        try:
            imported = __import__(package)
            logging.info(f"Successfully imported {package}")
            logging.info(f"Version: {imported.__version__}")
        except Exception as e:
            logging.error(f"Failed to import {package}: {str(e)}")

if __name__ == "__main__":
    verify_environment()