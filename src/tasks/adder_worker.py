import sys
from pathlib import Path

# Add the project root to the Python path
root_path = str(Path(__file__).resolve().parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)
    

from adder_task import AdderTask

from background_job_processer.worker import Worker

if __name__ == "__main__":
    adder_task = AdderTask()

    # run workers
    worker = Worker(task=adder_task)
    worker.start()

