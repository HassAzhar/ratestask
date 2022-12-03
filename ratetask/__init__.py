from flask import Flask # type: ignore
import ratetask.db

app = Flask(__name__)

import ratetask.controllers.app_controller # pylint: disable=wrong-import-position
app.run(port=8000, debug=True)
    