from django.utils.translation import gettext

from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from wagtail.core import hooks

from .richtext import KaTeXEntityElementHandler, katex_entity_decorator


@hooks.register('register_rich_text_features')
def register_katex_features(features):
    features.default_features.append('katex')
    """
    Registering the `katex` feature, which uses the `KATEX` Draft.js entity type,
    and is stored as HTML with a `<div data-katex-embed="c = \\pm\\sqrt{a^2 + b^2}">` tag.
    """
    feature_name = 'katex-embed'
    type_ = 'KATEX-EMBED'

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            {
                'type': type_,
                'icon': 'square-root-alt',
                'description': gettext('Equation'),
            },
            js=[
                'wagtailkatex/katex/katex.min.js',
                'wagtailkatex/wagtailkatex.js',
            ],
            css={
                'all': [
                    'wagtailkatex/katex/katex.min.css',
                ]
            }
        )
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'div[data-katex-embed]': KaTeXEntityElementHandler()},
        'to_database_format': {'entity_decorators': {type_: katex_entity_decorator}},
    })
