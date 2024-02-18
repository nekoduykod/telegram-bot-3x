# from datetime import datetime, timedelta

# from sqlalchemy import select, update
# from sqlalchemy.orm import sessionmaker

# from bot.db import Role, UserModel


# class Database:
#     def __init__(self, session: sessionmaker):
#         """
#         Метод ініціалізації
#         :param session: Пул з'єднання з БД
#         :return: bool
#         """
#         self.session = session

#     async def is_exists(self, user_id: int) -> bool:
#         """
#         Чи існує користувач
#         :param user_id: Телеграм id користувача
#         :return: bool
#         """
#         async with self.session() as session:
#             async with session.begin():
#                 return (
#                     await session.execute(
#                         select(UserModel).where(UserModel.id == user_id)
#                     )
#                 ).first()

#     async def add(self, user_id: int, full_name: str) -> None:
#         """
#         Додати нового користувача
#         :param user_id: Телеграм id користувача
#         :param full_name: Повне ім'я користувача
#         :return: None
#         """
#         async with self.session() as session:
#             async with session.begin():
#                 user = UserModel(id=user_id, full_name=full_name)
#                 session.add(user)

#     async def get(self, user_id: int) -> UserModel:
#         """
#         Отримати данні користувачів
#         :param user_id: Телеграм id користувача
#         :return: UserModel
#         """
#         async with self.session() as session:
#             async with session.begin():
#                 return (
#                     (
#                         await session.execute(
#                             select(UserModel).where(UserModel.id == user_id)
#                         )
#                     )
#                     .scalars()
#                     .first()
#                 )

#     async def get_by_role(self, role: Role):
#         """
#         Отримати користувачів відповідно до ролі
#         :param role: Роль користувача
#         :return: UserModel
#         """
#         async with self.session() as session:
#             async with session.begin():
#                 return (
#                     await session.execute(
#                         select(UserModel).where(UserModel.role == role)
#                     )
#                 ).scalars()

#     async def update(self, user_id: int, **kwargs) -> None:
#         """
#         Оновлює данні користувача
#         :param user_id: Телеграм id користувача
#         :param kwargs: Параметри, які тре оновити
#         :return: None
#         """
#         async with self.session() as session:
#             async with session.begin():
#                 await session.execute(
#                     update(UserModel).where(UserModel.id == user_id).values(kwargs)
#                 )

#     async def get_users_in_week(self) -> list[datetime]:
#         """
#         Отримати дані реєстрації нових користувачів за неділю
#         :return: list[datetime]
#         """
#         async with self.session() as session:
#             async with session.begin():
#                 week = datetime.today() - timedelta(days=7)
#                 return list((await session.execute(select(UserModel.registration_date)
#                                                    .where(UserModel.registration_date >= week))).scalars())