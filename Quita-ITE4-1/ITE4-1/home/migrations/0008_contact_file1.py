

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='file1',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
