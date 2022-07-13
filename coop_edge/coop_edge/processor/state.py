import hashlib

from coop_edge.interface.metadata import ADDRESS_PREFIX


def make_address(job_id):
    return ADDRESS_PREFIX + hashlib.sha512(job_id.encode('utf-8')).hexdigest()[-64:]


class CoopEdgeState:
    def __init__(self, context):
        self.context = context

    def record(self, task_record):
        address = make_address(task_record.job_id)
        self.context.set_state({address: task_record.serialize()})
