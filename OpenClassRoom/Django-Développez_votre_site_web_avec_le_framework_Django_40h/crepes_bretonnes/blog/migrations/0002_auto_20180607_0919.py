# Generated by Django 2.0.6 on 2018-06-07 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('produits', models.ManyToManyField(related_name='_vendeur_produits_+', through='blog.Offre', to='blog.Produit')),
                ('produits_sans_prix', models.ManyToManyField(related_name='vendeurs', to='blog.Produit')),
            ],
        ),
        migrations.AddField(
            model_name='offre',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Produit'),
        ),
        migrations.AddField(
            model_name='offre',
            name='vendeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Vendeur'),
        ),
    ]
