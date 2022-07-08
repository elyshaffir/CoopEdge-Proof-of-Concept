# general-purpose processor class
# ------------------------------------------------------------------------------

import sys
import os
import argparse
import pkg_resources
import traceback

from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.log import init_console_logging
from sawtooth_sdk.processor.log import log_configuration
from sawtooth_sdk.processor.config import get_log_config
from sawtooth_sdk.processor.config import get_log_dir
from sawtooth_sdk.processor.config import get_config_dir
from sawtooth_job.processor.handler import JobTransactionHandler


DISTRIBUTION_NAME = 'sawtooth-job'


def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-C', '--connect',
        default='tcp://localhost:4004',
        help='Endpoint for the validator connection')

    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help='Increase output sent to stderr')

    return parser.parse_args(args)


def main(args=None):
    print('Main')
    if args is None:
        print('No args')
        args = sys.argv[1:]
    opts = parse_args(args)
    processor = None
    try:
        print("Creating processor")
        processor = TransactionProcessor(url=opts.connect)
        print("Creating transaction handler")
        handler = JobTransactionHandler()
        print("Adding handler")
        processor.add_handler(handler)
        print("Starting processor")
        processor.start()
        if False:
            log_config = get_log_config(filename="intkey_log_config.toml")

            # If no toml, try loading yaml
            if log_config is None:
                log_config = get_log_config(filename="intkey_log_config.yaml")

            if log_config is not None:
                log_configuration(log_config=log_config)
            else:
                log_dir = get_log_dir()
                # use the transaction processor zmq identity for filename
                log_configuration(
                    log_dir=log_dir,
                    name="job-" + str(processor.zmq_id)[2:-1])

            init_console_logging(verbose_level=opts.verbose)

            # The prefix should eventually be looked up from the
            # validator's namespace registry.
            handler = JobTransactionHandler()

            processor.add_handler(handler)

            processor.start()
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        pass
    except Exception:  # pylint: disable=broad-except
        print("Exception!")
        print(traceback.format_exc())
    finally:
        print('stopping the processor')
        if processor is not None:
            print('There was a processor')
            processor.stop()


if __name__ == '__main__':
    main()
