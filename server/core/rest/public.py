# API for public endpoints
# Note: think carefully before putting anything in here...
# ...anyone will have access to data exposed from these endpoints

import json
import logging
import zlib
from time import sleep, time

import peewee
import stripe
from dateutil.parser import parse
from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request

from core.auth.store import auth_store
from core.config import config

logger = logging.getLogger(__name__)
public_api = Blueprint("public_api", __name__)


# -------
# Write you endpoint to retrieve all available studies here.
# -------

@public_api.route("/studies", methods=["GET"])
def get_all_studies():
    studies = auth_store.get_studies()
    if studies:
        logger.info(f"Found {len(studies)} studies.")
    else:
        logger.info(f"Found no study.")
        return "Found no study", 

    return jsonify(studies), 200
