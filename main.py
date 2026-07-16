import signal

from core.interface.Flask_interface import run_web_app


def signal_handler(sig, frame):
    """
    Handle sig int command
    :param sig: signal
    :param frame: function to execute in case of signal
    :return: None
    """
    print('\n')
    print(f'"ProjectPad" utility ending work, bye')
    exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  # if program goes wrong
    run_web_app()
