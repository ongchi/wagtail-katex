from django.db import migrations, models
import wagtail.fields


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    Page = apps.get_model("wagtailcore.Page")
    Site = apps.get_model("wagtailcore.Site")
    HomePage = apps.get_model("tests.HomePage")

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create content type for homepage model
    homepage_content_type, __ = ContentType.objects.get_or_create(
        model="homepage", app_label="tests"
    )

    # Create a new homepage
    homepage = HomePage.objects.create(
        title="Home",
        draft_title="Home",
        slug="home",
        content_type=homepage_content_type,
        path="00010001",
        depth=2,
        numchild=0,
        url_path="/home/",
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(hostname="localhost", root_page=homepage, is_default_site=True)


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0040_page_draft_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="homepage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        on_delete=models.CASCADE,
                        parent_link=True,
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AddField(
            model_name="homepage",
            name="text",
            field=wagtail.fields.RichTextField(
                default='<div data-katex-embed="c = \\sqrt{a^2 + b^2}"></div>'
            ),
            preserve_default=False,
        ),
        migrations.RunPython(create_homepage),
    ]
