from sawtooth_sdk.processor.core import TransactionProcessor

from coop_edge.processor.transaction_handler import CoopEdgeTransactionHandler


def main():
    print('CoopEdge transaction processor started.')
    # In docker, the url would be the validator's container name with
    # port 4004
    processor = TransactionProcessor(url='tcp://localhost:4004')

    handler = CoopEdgeTransactionHandler()

    processor.add_handler(handler)

    processor.start()


if __name__ == '__main__':
    main()
