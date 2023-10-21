#!/usr/bin/python3

from flask import request, jsonify
from flask import Blueprint
from .schema import (
    UserNotFoundError,
    EmailNotFoundError,
    PictureNotFoundError,
    SaveUserSuccessfull,
    APIError,
)
from .services import save_user_to_db
from database import db

# define the order_views template
user_views = Blueprint(url_prefix="/user")


@user_views.route("/", methods=["POST"], strict_slashes=False)
async def get_all_users():
    try:
        data = request.get_json()
        username = data.get("fullname")
        email = data.get("email")
        photo = data.get("photo")

        if not username:
            return jsonify(UserNotFoundError().to_dict()), 400
        if not email:
            return jsonify(EmailNotFoundError().to_dict()), 400
        if not photo:
            return jsonify(PictureNotFoundError().to_dict()), 400
        user = {
            "username": username,
            "email":email,
            "photo":photo
        }
        await save_user_to_db(db,user)
        return jsonify(SaveUserSuccessfull().to_dict), 201
    except Exception as error:
        # TODO: A better way to handle these errors
        return jsonify(APIError().to_dict()), 500
