import psutil
import time
import logging
import configparser
import os
from logging.handlers import RotatingFileHandler

config_file = "config.ini"
log_file = "proc_killer.log"
max_log_size = 1 * 1024 * 1024
backup_count = 3


logger = logging.getLogger("ProcessKiller")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=backup_count)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


config = configparser.ConfigParser()

def is_enabled() -> bool:
    """Check if the script is enabled via the config file."""
    if os.path.exists(config_file):
        config.read(config_file)
        return config.getboolean('Settings', 'enabled')
    else:
        logger.error("Config file not found, defaulting to enabled.")
        return True

def get_program_name() -> str:
    """Return the program name from the config file."""
    if os.path.exists(config_file):
        config.read(config_file)
        return config.get('Settings', 'program_name')
    else:
        logger.error("Config file not found, defaulting to program.")
        return 'discord'

def get_program_processes() -> list:
    """Return a list of processes."""
    program_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            program_name = get_program_name()
            if program_name.lower() in proc.info['name'].lower():
                program_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return program_processes

def kill_program() -> None:
    """Kill all Program processes and log the events."""
    program_processes = get_program_processes()
    if program_processes:
        program_name: str = get_program_name()
        logger.info(f"{program_name.capitalize()} detected! Terminating {len(program_processes)} process(es).")
        for proc in program_processes:
            try:
                proc.kill()
                proc.wait()
                logger.info(f"Process {proc.pid} terminated.")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                logger.error(f"Failed to terminate process {proc.pid}: {str(e)}")


def monitor_program() -> None:
    """Monitor Program and terminate it when found, if enabled."""
    while True:
        if is_enabled():
            kill_program()
        time.sleep(1)


if __name__ == "__main__":
    monitor_program()
