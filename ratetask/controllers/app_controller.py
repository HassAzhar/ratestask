from ratetask import app
from flask import request
import ratetask.utils.validators.app_service_validators as app_service_validators
from ratetask.utils.formatters.error_formatter import error_formatter
from http import HTTPStatus
from voluptuous import Error as ValidationError
import ratetask.services.app_service as AppService

@app.route("/rates")
def average_rate():
    try:
        app_service_validators.rates_validator(request.args.to_dict())
        return AppService.agregate_rates(request.args['date_from'], request.args['date_to'], request.args['origin'], request.args['destination'])
    except ValidationError as error_message:
        return error_formatter(error_message.__str__(), HTTPStatus.BAD_REQUEST)

    