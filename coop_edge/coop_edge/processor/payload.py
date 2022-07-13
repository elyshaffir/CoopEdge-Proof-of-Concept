from coop_edge.processor.task_record import TaskRecord


class CoopEdgeTransaction:
    def __init__(self, action, job_id, worker_id, publisher_id):
        self.action = action
        self.job_id = job_id
        self.worker_id = worker_id
        self.publisher_id = publisher_id

    def serialize(self):
        return ','.join([self.action, self.job_id, self.worker_id, self.publisher_id]).encode()

    def deserialize(payload):
        return CoopEdgeTransaction(*payload.decode().split(','))

    def generate_task_record(self):
        return TaskRecord(self.job_id, self.worker_id, self.publisher_id)
