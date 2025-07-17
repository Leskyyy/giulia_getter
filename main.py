import datetime
import os

def main():
    # Create logs directory if not exists
    os.makedirs('logs', exist_ok=True)
    
    # Create/append to log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Script executed at: {timestamp}\n"
    
    with open('logs/execution_log.txt', 'a') as f:
        f.write(log_entry)
    
    print("Success! Timestamp logged.")

if __name__ == "__main__":
    main()