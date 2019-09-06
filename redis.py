# coding: utf-8
import random
import iterm2
import socket

SERVICE = 'Redis'
IP = '127.0.0.1'
PORT = 6379

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((IP, PORT))

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Redis',
        detailed_description='Show Redis status',
        exemplar='Redis',
        update_cadence=5,
        identifier='engineering.paulomcnally.iterm-components.redis',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def redis_coroutine(knobs):
        if result == 0:
           status = '😀'
        else:
           status = '😴'
        
        return '%s %s' % (status, SERVICE)

    await component.async_register(connection, redis_coroutine)

iterm2.run_forever(main)
