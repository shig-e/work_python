import logging
import logging.handlers
import logging.config

# ハンドラ
ch = logging.StreamHandler()
trh = logging.handlers.TimedRotatingFileHandler(filename="logs/app.log",
                                                encoding="utf-8",
                                                when="midnight",
                                                backupCount=3)
# ベースのlogging設定
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s (line:%(lineno)d) | %(message)s",
                    handlers=[ch, trh])
