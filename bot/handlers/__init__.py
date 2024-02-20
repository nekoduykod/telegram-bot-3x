from aiogram import Router

# from .errors import error_routers

def get_handlers_router() -> Router:
    from .users import get_user_routers

    router = Router()

    user_routers = get_user_routers()

    router.include_router(user_routers)
    return router