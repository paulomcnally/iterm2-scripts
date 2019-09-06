# coding: utf-8
import random
import iterm2
import socket

SERVICE = 'PostgreSQL'
IP = '127.0.0.1'
PORT = 5432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((IP, PORT))

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='PostgreSQL',
        detailed_description='Show PostgreSQL status',
        exemplar='PostgreSQL',
        update_cadence=5,
        identifier='engineering.paulomcnally.iterm-components.postgresql',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def postgresql_coroutine(knobs):
        if result == 0:
           status = '😀'
        else:
           status = '😴'
        
        return '%s %s' % (status, SERVICE)

    await component.async_register(connection, postgresql_coroutine)

iterm2.run_forever(main)
