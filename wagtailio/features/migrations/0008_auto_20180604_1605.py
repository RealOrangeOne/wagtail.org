# Generated by Django 2.0.6 on 2018-06-04 16:05

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('features', '0007_remove_introduction_and_secondary_menu_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureIndexPageMenuOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_menu_options', to='features.FeatureIndexPage')),
            ],
        ),
        migrations.RemoveField(
            model_name='featuredescriptionfeatureaspect',
            name='feature_aspect',
        ),
        migrations.RemoveField(
            model_name='featuredescriptionfeatureaspect',
            name='page',
        ),
        migrations.RemoveField(
            model_name='featurepage',
            name='listing_image',
        ),
        migrations.RemoveField(
            model_name='featurepage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='featurepage',
            name='social_image',
        ),
        migrations.AlterField(
            model_name='featurepagefeatureaspect',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_aspects', to='features.FeatureDescription'),
        ),
        migrations.DeleteModel(
            name='FeatureDescriptionFeatureAspect',
        ),
        migrations.DeleteModel(
            name='FeaturePage',
        ),
    ]