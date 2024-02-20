from .echo import echo_router
from .help import help_router
from .start import start_router, exit_router
# from .admin import router_admin
from .issues_handler import issue_router
from .request_chatgpt import gpt_router
from .photo_url_handler import photoURL_router
from .donate_ua_army import donate_router

user_routers = (start_router, help_router, exit_router, echo_router, issue_router, gpt_router, photoURL_router, donate_router)