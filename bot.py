import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram, os

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "bot",
        bot_token=os.environ.get("6252471050:AAFlBX-EkOPRf7re1WHZnMlNyYjkOg6c8yo"),
        api_id=int(os.environ.get("5806640")),
        api_hash=os.environ.get("127f130ad3745dbcd31aa39aa0eabcb8"),
        plugins=plugins
    )
    app.run()
