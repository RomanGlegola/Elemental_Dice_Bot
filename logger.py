import json
import hashlib
import datetime

class Logger:
    """
    Logs dice rolls and provides functionalities to access and manage the logs.

    Attributes:
        LOG_FILE (str): Name of the file where logs are stored.
        logs (list): List containing the logs.
    """
    LOG_FILE = 'dice_rolls.json'
    
    def __init__(self):
        """
        Initializes a new instance of the Logger class and loads existing logs.
        """
        self.logs = self.load_logs()

    def load_logs(self):
        """Loads the logs from the LOG_FILE.

        Returns:
            list: A list of logs. If the file is not found or corrupted, an empty list is returned.
        """
        try:
            with open(self.LOG_FILE, 'r+') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    return []
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_logs(self):
        """
        Saves the current logs to the LOG_FILE.
        """
        with open(self.LOG_FILE, 'w') as f:
            json.dump(self.logs, f)
    
    def log_roll(self, roll_data):
        """
        Logs a new dice roll.

        Args:
            roll_data (dict): Data related to the dice roll.

        Returns:
            str: Hash of the logged roll.
        """
        current_time = datetime.datetime.now().isoformat()
        roll_hash = hashlib.md5(current_time.encode()).hexdigest()

        if len(self.logs) >= 500:
            self.logs.pop(0)

        self.logs.append({
            'hash': roll_hash,
            'time': current_time,
            'roll_data': roll_data
        })
        
        self.save_logs()
        return roll_hash
    
    def get_roll_by_hash(self, roll_hash):
        """
        Retrieves a dice roll log using its hash.

        Args:
            roll_hash (str): Hash of the roll to retrieve.

        Returns:
            dict: Data related to the dice roll. None if the roll is not found.
        """
        for log in self.logs:
            if log['hash'] == roll_hash:
                return log['roll_data']
        return None
