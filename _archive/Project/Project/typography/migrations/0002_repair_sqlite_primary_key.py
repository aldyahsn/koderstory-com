from django.db import migrations


def repair_sqlite_primary_key(apps, schema_editor):
    """Repair databases created while the typography migrations were hidden."""
    if schema_editor.connection.vendor != "sqlite":
        return

    table_name = "typography_typographysettings"
    with schema_editor.connection.cursor() as cursor:
        columns = schema_editor.connection.introspection.get_table_description(
            cursor, table_name
        )

    id_column = next(column for column in columns if column.name == "id")
    if id_column.type_code.upper() == "INTEGER":
        return

    TypographySettings = apps.get_model("typography", "TypographySettings")
    schema_editor._remake_table(TypographySettings)


class Migration(migrations.Migration):
    dependencies = [
        ("typography", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(repair_sqlite_primary_key, migrations.RunPython.noop),
    ]
