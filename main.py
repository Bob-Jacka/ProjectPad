import signal

from common_py_lib.logger.CommonLogger import CommonLogger

from core.entities.Entity_manager import Entity_manager


def signal_handler(sig, frame):
    """
    Handle sig int command
    :param sig: signal
    :param frame: function to execute in case of signal
    :return: None
    """
    print('\n')
    entity_manager.real_save()
    print(f'"ProjectPad" utility ending work, bye')
    exit(0)


logger = CommonLogger()
entity_manager = Entity_manager(logger)

if __name__ == '__main__':
    from core.interface.Flask_interface import run_web_app

    print('ProjectPad utility start working')
    signal.signal(signal.SIGINT, signal_handler)  # if program goes wrong
    run_web_app(entity_manager)
