#!/usr/bin/python3

from flask import Flask
from flask import render_template, Blueprint

# define the order_views template
user_views = Blueprint(
    "user_views",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/user",
)


@user_views.route("/all_users", strict_slashes=False)
def get_all_users():
    return "Here is a list of all users"
