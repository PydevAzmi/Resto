# Generated by Django 4.2 on 2023-10-16 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menus", "0004_menuitem_is_fav_alter_menuitem_sale"),
        ("orders", "0005_alter_cart_code_alter_order_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="code",
            field=models.CharField(default="1D517B1F7", max_length=9),
        ),
        migrations.AlterField(
            model_name="customization",
            name="ingredient",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ingredient",
                to="menus.ingredient",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="code",
            field=models.CharField(default="668F269A4A8B875", max_length=15),
        ),
    ]