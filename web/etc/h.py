CONFIG = {
    'mode': 'wsgl',
    'working_dir': 'home/box/web/hello.py',
    # 'python': '/usr/bin/python.py',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=16',
        '--timeout=60',
        'hello.app',
    ),
}

