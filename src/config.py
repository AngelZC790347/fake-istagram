flask_config = dict(
    SECRET_KEY='dev',
    DEBUG=False,
    PONNY={
        "provider": "sqlite",
        "filename": "fake-instagram.sqlite",
        "create_db": True
    }
)
