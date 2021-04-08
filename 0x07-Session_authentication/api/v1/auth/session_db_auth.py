#!/usr/bin/env python3
""" Session DataBase Authentication Module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ Session DataBase Authentication Class
    """

    def create_session(self, user_id=None):
        """ creates and stores new instance
            of UserSession and returns the Session ID
        """
        if not user_id:
            return
        session_id = super().create_session(user_id)
        if not session_id:
            return
        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ returns the User ID by requesting UserSession
            in the database based on session_id
        """
        if not session_id:
            return
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return
        try:
            sessions = UserSession.search({'session_id': session_id})
            if not sessions:
                return

            if sessions[0].created_at + \
               timedelta(seconds=self.session_duration) < datetime.utcnow():
                return None

            return sessions[0].user_id
        except Exception:
            return

    def destroy_session(self, request=None):
        """ destroys the UserSession based on the Session ID
            from the request cookie
        """
        if not request:
            return
        session_id = self.session_cookie(request)
        if not session_id:
            return
        try:
            users = UserSession.search({'session_id': session_id})
            if not users:
                return
            for user in users:
                user.remove()
        except Exception:
            return
