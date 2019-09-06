# coding: utf-8
import random
import iterm2
import socket

SERVICE = 'MongoDB'
IP = '127.0.0.1'
PORT = 27017

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((IP, PORT))

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='MongoDB',
        detailed_description='Show MongoDB status',
        exemplar='MongoDB',
        update_cadence=5,
        identifier='engineering.paulomcnally.iterm-components.mongodb',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def mongo_db_coroutine(knobs):
        if result == 0:
           status = '😀'
        else:
           status = '😴'
        
        return '%s %s' % (status, SERVICE)

    await component.async_register(connection, mongo_db_coroutine)

iterm2.run_forever(main)
