# from datetime import datetime as dt
# from enum import IntEnum

# from sqlalchemy import BigInteger, Column, DateTime, Enum, String

# from .base import Base


# class Role(IntEnum):
#     USER = 0
#     MODERATOR = 1
#     ADMINISTRATOR = 2


# class UserModel(Base):
#     """
#     Основная модель користувачів
#     """

#     __tablename__ = "users"
#     id = Column(BigInteger, nullable=False, primary_key=True)
#     role = Column(Enum(Role), default=Role.USER)
#     full_name = Column(String, nullable=False)
#     referral_id = Column(BigInteger)
#     update_date = Column(DateTime, default=dt.today(), onupdate=dt.today())
#     registration_date = Column(DateTime, default=dt.today())

#     def __str__(self) -> str:
#         """
#         Повертає ID користувача
#         :param self: UserModel
#         :return: str
#         """
#         return f"User ID: {self.id}"