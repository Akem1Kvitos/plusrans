from flask import Blueprint, current_app as app, render_template

tehosmotri_temp = Blueprint("tehosmotri", __name__, url_prefix="/tehosmotri")


@tehosmotri_temp.route("/", methods=["GET"])
def get_tehosmotri_template():
    result = app.config.tehosmotri_service.select()
    return render_template('tehosmotri.html', tehosmotri=result['results'])