import sys
from pathlib import Path

# Add the project root to the Python path
root_path = str(Path(__file__).resolve().parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)
    
from background_job_processer.base_task import BaseTask

# pip install redis requests
import requests

class EmailTask(BaseTask):
    """
    task to send email to customer after they have ordered.
    """

    task_name = "EmailTask"

    def run(self, order_id, email_address):
        # lets pretend httpbin.org is an email service provider
        email = "email:{0}/{1}".format(order_id, email_address)
        print(email)
        response = f'send email to {email_address} for order {order_id}'
        print("response:: ", response)


if __name__ == "__main__":
    order_id = "24dkq40"
    email_address = "example@example.org"
    email_task = EmailTask()
    email_task.delay(order_id, email_address)