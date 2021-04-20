#!/usr/bin/env python3
""" Database for ORM """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base
from user import User


class DB:
    """ DB Class for Object Reational Mappin """

    def __init__(self):
        """ Constructor Method """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """create session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add a user instance to the session DB """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ returns the first row found in the users table
            as filtered by the method’s input arguments
        """
        if not kwargs:
            raise InvalidRequestError

        user_data = User.__table__.columns.keys()
        for i in kwargs.keys():
            if i not in user_data:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ update the user’s attributes as passed in the method’s arguments
            then commit changes to the database
        """
        user = self.find_user_by(id=user_id)

        user_data = User.__table__.columns.keys()
        for i in kwargs.keys():
            if i not in user_data:
                raise ValueError

        for i, j in kwargs.items():
            setattr(user, i, j)

        self._session.commit()
