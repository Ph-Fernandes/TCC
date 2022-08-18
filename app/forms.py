from django import forms 
from app.models import *
from localflavor.br.forms import BRCPFField 
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your forms here.

class ClienteForm(forms.ModelForm):
    statuspag = BLANK_CHOICE_DASH + [("10","Pagamento Integral"),("11","Pagamento Parcial"),("1","1 mês de atraso"),("2","2 meses de atraso"),("3","3 meses de atraso"),("4","4 meses de atraso"),("5","5 meses de atraso"),("6","6 meses de atraso"),("7","7 meses de atraso"),("8","8 meses de atraso"),("9","9 ou mais meses de atraso")]

    nomec = forms.CharField(label = "Nome Completo")
    cpf = BRCPFField(label = 'CPF')
    mit_bal = forms.IntegerField(label="Limite de crédito") 
    sex = forms.IntegerField(label = "Gênero",choices=BLANK_CHOICE_DASH + [("1","Masculino"),("2","Feminino")])
    education = forms.IntegerField(label = "Grau de Instrução",choices=BLANK_CHOICE_DASH + [("3","Ensino Médio Completo"),("2","Superior Completo"),("1","Pós Graduado"),("4","Outros")])
    marriage = forms.IntegerField(label = "Estado Civil",choices=BLANK_CHOICE_DASH + [("2","Solteiro(a)"),("1","Casado(a)"),("3","Outros")])
    age = forms.IntegerField(label = "Idade")
    pay_6 = forms.IntegerField(label = "Status de Pagamento 1",choices = statuspag)
    pay_5 = forms.IntegerField(label = "Status de Pagamento 2",choices = statuspag)
    pay_4 = forms.IntegerField(label = "Status de Pagamento 3",choices = statuspag)
    pay_3 = forms.IntegerField(label = "Status de Pagamento 4",choices = statuspag)
    pay_2 = forms.IntegerField(label = "Status de Pagamento 5",choices = statuspag)
    pay_1 = forms.IntegerField(label = "Status de Pagamento 6",choices = statuspag)
    bill_amt_6 = forms.IntegerField(label= "Conta 1")
    bill_amt_5 = forms.IntegerField(label= "Conta 2") 
    bill_amt_4 = forms.IntegerField(label= "Conta 3") 
    bill_amt_3 = forms.IntegerField(label= "Conta 4")
    bill_amt_2 = forms.IntegerField(label= "Conta 5") 
    bill_amt_1 = forms.IntegerField(label= "Conta 6")
    pay_amt_6 = forms.IntegerField(label= "Pagamento 1")
    pay_amt_5 = forms.IntegerField(label= "Pagamento 2")
    pay_amt_4 = forms.IntegerField(label= "Pagamento 3")
    pay_amt_3 = forms.IntegerField(label= "Pagamento 4")
    pay_amt_2 = forms.IntegerField(label= "Pagamento 5")
    pay_amt_1 = forms.IntegerField(label= "Pagamento 6")
    payment = forms.BooleanField(label= "Próximo Pagamento",choices= BLANK_CHOICE_DASH + ["1","Adimplente","0","Inadimplente"] )
    class Meta:
        model = Cliente
