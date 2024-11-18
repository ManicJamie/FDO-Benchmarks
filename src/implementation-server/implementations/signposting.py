from typing import Callable
from flask import Blueprint, Response, make_response, render_template, request

from werkzeug.exceptions import NotFound

from generation import FDO, FDO_REGISTER

bp = Blueprint("signposting", __name__, template_folder="templates")

@bp.route("/<feature>/<id>")
def resolve(feature, id):
    return FEATURES[feature](id)

def get_object(id: str) -> FDO:
    try:
        int_id = int(id)
        return FDO_REGISTER[int_id]
    except IndexError as e:
        raise NotFound(f"Cannot find object at index '{e.args[0]}'")

def link_rel(attr: str, value: str):
    return f'<{value}>;rel="{attr}"'

# Implementations
def full(id: str) -> Response:
    fdo = get_object(id)
    links = {
        "cite-as": request.url,
    }
    attrs = {
        "name": fdo["name"]
    }
    impl = "HTML-full"
    response = make_response(render_template("signposting.html", signpost_links=links, attrs=attrs, impl=impl))
    for l, href in links.items():
        response.headers.add("link", link_rel(l, href))
    return response


FEATURES: dict[str, Callable[[str], Response]] = {
    "full": full,
}
