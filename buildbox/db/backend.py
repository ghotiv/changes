from sqlalchemy.orm import sessionmaker


class Backend(object):
    def __init__(self, engine=None):
        from buildbox.app import application

        if engine is None:
            engine = application.settings['sqla_engine']

        self.engine = engine
        self.create_session = sessionmaker(bind=engine)

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def get_session(self):
        return SessionContextManager(self)


# TODO(cramer): this is likely blocking the Tornado ioloop
class SessionContextManager(object):
    def __init__(self, backend):
        self.backend = backend

    def __enter__(self):
        self.session = self.backend.create_session(expire_on_commit=False)
        return self.session

    def __exit__(self, *exc_info):
        self.session.commit()
        self.session.expunge_all()
        self.session.close()
