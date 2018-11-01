import logbook

logbook.Logger('App')

def init_logger(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level, "stdout mode" if not filename else 'file mode: ' + filename)
    logger = logbook.Logger('Startup')
    logger.notice(msg)

