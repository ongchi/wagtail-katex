from draftjs_exporter.dom import DOM
from wagtail.admin.rich_text.converters.contentstate_models import Entity
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    AtomicBlockEntityElementHandler,
)


def katex_entity_decorator(props):
    """
    Takes Draft.js ContentState and converts it to HTML for saving in the database.
    """
    return DOM.create_element(
        "div",
        {"data-katex-embed": props["text"]},
    )


class KaTeXEntityElementHandler(AtomicBlockEntityElementHandler):
    """
    Takes Database HTML and converts it to Draft.js ContentState for display in the
    editor.
    """

    mutability = "MUTABLE"

    def create_entity(self, name, attrs, state, contentstate):
        return Entity(
            "KATEX-EMBED",
            "IMMUTABLE",
            {"text": attrs["data-katex-embed"]},
        )
