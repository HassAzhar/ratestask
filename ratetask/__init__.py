from flask import Flask # type: ignore

app = Flask(__name__)

import ratetask.controllers.appController # pylint: disable=wrong-import-position
app.run(port=8000, debug=True)
    