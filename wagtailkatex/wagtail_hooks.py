from django.utils.translation import gettext
from wagtail import hooks
from wagtail.admin.rich_text.editors.draftail import \
    features as draftail_features

from .conf import get_conf
from .richtext import KaTeXEntityElementHandler, katex_entity_decorator


@hooks.register('register_rich_text_features')
def register_katex_feature(features):
    features.default_features.append('katex-embed')

    """
    Registering the `katex-embed` feature, which uses the `KATEX` Draft.js entity type,
    and is stored as HTML with a `div[data-katex-embed]` tag.
    """
    feature_name = 'katex-embed'
    type_ = 'KATEX-EMBED'

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            {
                'type': type_,
                'icon': 'square-root-variable',
                'description': gettext('Equation'),
            },
            js= get_conf('js') + get_conf('preview') + [
                'wagtailkatex/wagtailkatex.js',
            ],
            css={
                'all': get_conf('css') + [
                    'wagtailkatex/wagtailkatex.css',
                ],
            },
        ),
    )

    features.register_converter_rule(
        'contentstate',
        feature_name,
        {
            'from_database_format': {
                'div[data-katex-embed]': KaTeXEntityElementHandler()
            },
            'to_database_format': {
                'entity_decorators': {type_: katex_entity_decorator}
            },
        },
    )


@hooks.register('register_icons')
def register_icons(icons):
    return icons + [
        'wagtailkatex/square-root-variable.svg',
    ]
