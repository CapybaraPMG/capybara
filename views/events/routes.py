#!/usr/bin/python3

from flask import Flask
from flask import render_template, Blueprint

# define the order_views template
event_views = Blueprint(
    "event_views",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/event",
)


@event_views.route("/all_events", strict_slashes=False)
def get_all_events():
    return "Here is a list of all events"
