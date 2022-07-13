import json


class TaskRecord:
    def __init__(self, job_id, worker_id, publisher_id):
        self.job_id = job_id
        self.worker_id = worker_id
        self.publisher_id = publisher_id

    def serialize(self):
        return json.dumps({'job_id': self.job_id, 'worker_id': self.worker_id, 'publisher_id': self.publisher_id})
