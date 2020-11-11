from app import app
import logging

if __name__ == "__main__":

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    app.run(debug=True)
