import sys
from pathlib import Path

# Add the project root to the Python path
root_path = str(Path(__file__).resolve().parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)

from  background_job_processer.base_task import BaseTask

class AdderTask(BaseTask):

    task_name = "AdderTask"

    def run(self, a, b):
        # lets pretend httpbin.org is an email service provider
        task_details = "a: {0} + b:{1}".format(a, b)
        print(task_details)
        response = a + b
        print("response:: ", response)


if __name__ == "__main__":
    a = 10
    b = 20
    email_task = AdderTask()
    email_task.delay(a, b)