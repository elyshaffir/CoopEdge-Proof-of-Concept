import sys

from sawtooth_sdk.processor.core import TransactionProcessor

from coop_edge.processor.transaction_handler import CoopEdgeTransactionHandler


def main():
    print(
        f'CoopEdge transaction processor started.\nThe following parameters were given:\n{sys.argv}')
    # In docker, the url would be the validator's container name with
    # port 4004
    processor = TransactionProcessor(url=sys.argv[3])

    handler = CoopEdgeTransactionHandler()

    processor.add_handler(handler)

    processor.start()
