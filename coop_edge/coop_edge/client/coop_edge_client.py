import urllib.request
from urllib.error import HTTPError

from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader, Transaction
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader, Batch, BatchList


from hashlib import sha512

from coop_edge.interface.metadata import FAMILY_NAME, FAMILY_VERSION
from coop_edge.interface.actions import RECORD_ACTION

from coop_edge.processor.payload import CoopEdgeTransaction


def generate_transaction(signer):
    print(f'Generating a transaction signed by {signer}')
    payload_bytes = CoopEdgeTransaction(
        RECORD_ACTION, '1', 'test_worker', 'test_publisher').serialize()

    print('WARNING! NOT USING inputs OR outputs! this might affect performance.')
    header_bytes = TransactionHeader(
        family_name=FAMILY_NAME,
        family_version=FAMILY_VERSION,
        signer_public_key=signer.get_public_key().as_hex(),
        batcher_public_key=signer.get_public_key().as_hex(),
        dependencies=[],
        payload_sha512=sha512(payload_bytes).hexdigest()
    ).SerializeToString()

    signature = signer.sign(header_bytes)

    return Transaction(header=header_bytes,
                       header_signature=signature, payload=payload_bytes)


def generate_batch(signer, transaction):
    print(f'Generating a batch signed by {signer}')
    batch_header_bytes = BatchHeader(
        signer_public_key=signer.get_public_key().as_hex(),
        transaction_ids=[transaction.header_signature],
    ).SerializeToString()

    signature = signer.sign(batch_header_bytes)
    return Batch(
        header=batch_header_bytes,
        header_signature=signature,
        transactions=[transaction]
    )


def send_batch_list(batch_list_bytes):
    print('Sending a batch list')
    try:
        request = urllib.request.Request(
            'http://localhost:8008/batches',
            batch_list_bytes,
            method='POST',
            headers={'Content-Type': 'application/octet-stream'})
        response = urllib.request.urlopen(request)

    except HTTPError as e:
        response = e.file
    print(
        f'Finished sending the batch list. The response was:{response.read().decode()}')


def main():
    print('Client started')
    context = create_context('secp256k1')
    private_key = context.new_random_private_key()
    signer = CryptoFactory(context).new_signer(private_key)

    transaction = generate_transaction(signer)
    batch = generate_batch(signer, transaction)
    send_batch_list(BatchList(batches=[batch]).SerializeToString())
