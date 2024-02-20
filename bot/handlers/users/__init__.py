from aiogram import Router

from .echo import echo_router
from .help import help_router
from .start import start_router, exit_router
from .request_chatgpt import gpt_router
# from .admin import router_admin


def get_user_routers() -> Router:

    router = Router()
    router.include_router(start_router)
    router.include_router(help_router)
    router.include_router(exit_router)
    router.include_router(echo_router)
    router.include_router(gpt_router)
    
    return router