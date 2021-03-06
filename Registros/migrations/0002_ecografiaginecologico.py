# Generated by Django 2.0.6 on 2018-07-17 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ecografiaginecologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivoExamen', models.CharField(max_length=500, verbose_name='MOTIVO DEL EXAMEN')),
                ('posicionUtero', models.CharField(choices=[('ANTEVERSO', 'Anteverso'), ('CENTRAL', 'Central'), ('RETROVRSO', 'Retroverso')], max_length=20)),
                ('contornoUtero', models.CharField(max_length=100, verbose_name='CONTORNO')),
                ('ecoestructura', models.CharField(max_length=100, verbose_name='ESTRUCTURA')),
                ('medidas', models.CharField(max_length=100, verbose_name='MEDIDAS')),
                ('endometrio', models.CharField(choices=[('MENSTRUAL', 'Menstrual'), ('PROLIF', 'Prolif.'), ('PERIOF', 'Periof.'), ('SECRET', 'Secret')], max_length=20)),
                ('descripcion', models.CharField(max_length=500, verbose_name='DESCRIPCION')),
                ('anexodermedidas', models.CharField(max_length=200, verbose_name='DESCRIPCION')),
                ('anexodermasas', models.CharField(choices=[('NO', 'No'), ('QUISTE', 'Quiste.'), ('SOLIDAS', 'Solidas.')], max_length=20)),
                ('anexoderdescripcion', models.CharField(max_length=300, verbose_name='DESCRIPCION')),
                ('anexoizqmedidas', models.CharField(max_length=200, verbose_name='DESCRIPCION')),
                ('anexoizqmasas', models.CharField(choices=[('NO', 'No'), ('QUISTE', 'Quiste.'), ('SOLIDAS', 'Solidas.')], max_length=20)),
                ('anexoizqdescripcion', models.CharField(max_length=300, verbose_name='DESCRIPCION')),
                ('liquidolibre', models.CharField(choices=[('NO', 'No'), ('ESCASO', 'Escaso.'), ('MODERADO', 'Moderado.'), ('ABUNDANTE', 'Abundante.')], max_length=20)),
                ('observacion', models.CharField(max_length=500, verbose_name='OBSERVACION')),
                ('presuncionDiagnostico', models.CharField(max_length=500, verbose_name='PRESUNCION_DIAGNOSTICA')),
                ('fech_informe', models.DateTimeField(auto_now_add=True, verbose_name='FECHA INFORME ECOGRAFICO GINECOLOGICO')),
                ('fech_actualizado', models.DateTimeField(auto_now=True, verbose_name='FECHA DE ACTUALIZACION')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registros.Paciente', verbose_name='PACIENTE')),
            ],
        ),
    ]
