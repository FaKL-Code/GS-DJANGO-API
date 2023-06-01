from django.db import models

VOLUME = ((
    ('PEQUENO', 'Pequeno'),
    ('MEDIO', 'Médio'),
    ('GRANDE', 'Grande'),
))

class Doador(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

def MinValueValidator(data):
    hoje = date.today()

    if data < hoje:
        raise ValidationError('Data de retirada não pode ser no passado')

class Doacao(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    volume = models.CharField(max_length=20, choices=VOLUME, null=False, blank=False)
    data_doacao = models.DateField(auto_now_add=True)
    data_retirada = models.DateField(validators=[MinValueValidator])

