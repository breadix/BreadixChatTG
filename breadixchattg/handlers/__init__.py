from aiogram import Router

from . import start

main_router = Router()

main_router.include_routers(
    start.router
)
