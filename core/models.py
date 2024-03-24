from django.db import models

# Não esquecer de registrar o model em admin.py
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)

    # Retornar o nome cadastrado no painel admin ao invés do objeto
    def __str__(self):
        return self.nome