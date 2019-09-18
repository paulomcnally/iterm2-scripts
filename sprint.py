# coding: utf-8
import random
import iterm2
from datetime import date

SPRINT_END_DATE = date(2019,9,30)
SPRINT_NUMBER = 37


days = (SPRINT_END_DATE-date.today()).days

def message(argument):
    return '%s días restantes' % argument

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Sprint',
        detailed_description='show Sprint days',
        exemplar='Sprint',
        update_cadence=5,
        identifier='engineering.paulomcnally.iterm-components.sprint',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def sprint_coroutine(knobs):
        return '🗓️ Sprint %d: %s' % (SPRINT_NUMBER, message(days))

    await component.async_register(connection, sprint_coroutine)

iterm2.run_forever(main)
