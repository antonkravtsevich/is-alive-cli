import atexit
import json
import os
import pathlib
import sys
import time
import uuid

import requests

HOST_URL = 'https://is-alive-21218.herokuapp.com/'
UUID = None
STATUS = 'online'


def is_backend_accessible():
    try:
        requests.get(HOST_URL+'/healthcheck', timeout=5)
        return True
    except Exception:
        return False


def proper_shutdown():
    """
    Used to shut down connection properly
    """
    if STATUS == 'online':
        print('Отправляем твой обновленный статус на сервер. НЕ ОТКЛЮЧАЙ пожалуйста, это важно...')
        requests.post(HOST_URL+'/connections/{}/disable'.format(UUID))
        print('Готово!')


def main():
    config_file = pathlib.Path.home() / '.is_alive_cli_config.json'
    if config_file.is_file():
        with config_file.open() as f:
            config = json.load(f)
        UUID = config['uuid']
    else:
        UUID = str(uuid.uuid1())
        config = {
            "uuid": UUID
        }
        with config_file.open('w') as f:
            json.dump(config, f)

    atexit.register(proper_shutdown)

    print('Проверяем, доступен ли сервис...')
    if is_backend_accessible():
        print('Доступ есть, начинаем работу')
    else:
        print('Сервис недоступен. Проверь соединение и попробуй подключиться позже')
        STATUS='offline'
        sys.exit(1)

    print('----------------------------------------------')

    print('Твоя персональная ссылка: ')
    print('{}/connections/{}'.format(HOST_URL, UUID))
    print('Можешь поделиться ей с кем угодно!')

    payload = {
        'uuid': UUID
    }

    while True:
        try:
            requests.post(HOST_URL+'/check', json=payload, timeout=5)
            if STATUS == 'offline':
                STATUS = 'online'
                print('Соединение вернулось, снова в деле')
        except Exception:
            if STATUS == 'online':
                STATUS = 'offline'
                print('Похоже, сервис больше недоступен. Возможно, проблемы с соединением. Можешь отключиться либо подождать какое-то время - скрипт автоматически переподключится по возможности.')
        finally:
            time.sleep(60)


if __name__ == '__main__':
    main()
