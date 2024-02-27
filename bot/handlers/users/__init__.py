from aiogram import Router

# from .echo import echo_router
# from .admin import admin_router
from .help import help_router
from .start import on
from .gpt_req import gpt_router


def get_user_routers() -> Router:

    router = Router()
    router.include_router(on)
    router.include_router(help_router)
    router.include_router(gpt_router)
    
    return router