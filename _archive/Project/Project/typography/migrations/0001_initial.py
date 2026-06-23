from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0091_remove_revision_submitted_for_moderation"),
    ]

    operations = [
        migrations.CreateModel(
            name='TypographySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1_font', models.CharField(blank=True, help_text='Font family for H1 headings (e.g., "Inter", "Playfair Display")', max_length=255)),
                ('h2_font', models.CharField(blank=True, help_text='Font family for H2 headings (e.g., "Inter", "Playfair Display")', max_length=255)),
                ('h3_font', models.CharField(blank=True, help_text='Font family for H3 headings (e.g., "Inter", "Playfair Display")', max_length=255)),
                ('h4_font', models.CharField(blank=True, help_text='Font family for H4 headings (e.g., "Inter", "Playfair Display")', max_length=255)),
                ('h5_font', models.CharField(blank=True, help_text='Font family for H5 headings (e.g., "Inter", "Playfair Display")', max_length=255)),
                ('h6_font', models.CharField(blank=True, help_text='Font family for H6 headings (e.g., "Inter", "Playfair Display")', max_length=255)),
                ('paragraph_font', models.CharField(blank=True, help_text='Font family for paragraph text (e.g., "Inter", "Open Sans")', max_length=255)),
                ('paragraph_font_weight', models.CharField(blank=True, help_text='Font weight for paragraph text (e.g., "normal", "300", "400", "500", "600")', max_length=50)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Typography settings',
            },
        ),
    ]
