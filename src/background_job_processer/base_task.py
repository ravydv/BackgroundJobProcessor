import abc
from .broker import Broker
import uuid
import json

class BaseTask(abc.ABC):
    task_name = None

    def __init__(self) -> None:
        if not self.task_name:
            raise ValueError("task name should be set")
        self.broker = Broker()
    
    @abc.abstractclassmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError("BaseTask run method must be implemented")
    
    def delay(self, *args, **kwargs):
        try:
            task_id = str(uuid.uuid4())
            _task = {"task_id": task_id, "args": args, "kwargs": kwargs}
            serialized_task = json.dumps(_task)
            self.broker.enqueue(queue_name=self.task_name, item=serialized_task)
            print("task: {0} succesfully queued".format(task_id))

        except Exception:
            raise Exception("Unable to publish task to broker.")
