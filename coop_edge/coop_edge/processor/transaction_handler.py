from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction

from coop_edge.processor.payload import CoopEdgeTransaction
from coop_edge.processor.state import CoopEdgeState
from coop_edge.interface.metadata import FAMILY_NAME, FAMILY_VERSION, ADDRESS_PREFIX


class CoopEdgeTransactionHandler(TransactionHandler):

    @property
    def family_name(self):
        return FAMILY_NAME

    @property
    def family_versions(self):
        return [FAMILY_VERSION]

    @property
    def namespaces(self):
        return [ADDRESS_PREFIX]

    def apply(self, transaction, context):
        print(
            f'apply was callled on a transaction with the payload:\n{transaction.payload}')
        coop_edge_transaction = CoopEdgeTransaction.deserialize(
            transaction.payload)
        coop_edge_state = CoopEdgeState(context)

        if coop_edge_transaction.action == 'record':  # Record a job on the blockchain
            coop_edge_state.record(
                coop_edge_transaction.generate_task_record())
        else:
            print('Invalid transaction! WARNING! not raising InvalidTransaction.')
            # raise InvalidTransaction(
            #     'Unhandled action: {}'.format(coop_edge_transaction.action))

        print(
            f'A new task was recorded. Signed by {transaction.header.signer_public_key}')
