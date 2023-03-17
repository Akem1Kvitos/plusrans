from flask import Blueprint, render_template

index_page = Blueprint("/", __name__, url_prefix="/")


@index_page.route("/", methods=["GET"])
def index():
    return render_template('base.html')
