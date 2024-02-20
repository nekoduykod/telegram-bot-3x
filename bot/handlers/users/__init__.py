from aiogram import Router

from .echo import echo_router
from .help import help_router
from .start import start_router, exit_router
# from .admin import router_admin
from .issues_handler import issue_router
from .request_chatgpt import gpt_router
from .photo_url_handler import photoURL_router
from .donate_ua_army import donate_router


def get_user_routers() -> Router:

    router = Router()
    # user_routers = (gpt_router, photoURL_router, donate_router, ...)
    # router.include_router(user_routers)
    router.include_router(start_router)
    router.include_router(help_router)
    router.include_router(exit_router)
    router.include_router(echo_router)
    router.include_router(issue_router)
    router.include_router(gpt_router)
    router.include_router(photoURL_router)
    router.include_router(donate_router)
    
    return router