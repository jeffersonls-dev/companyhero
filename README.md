# Desafio Company Hero

## Descrição:

Esta é uma pequena aplicação que tem como objetivo a criação de empresas e funcionários. Os funcionários são também usuários dentro dessa aplicação.

A aplicação também fornece endpoints para criação (POST) e consulta (GET) de empresas e consulta (GET) de funcionários

O código está devidamente comentado, mas caso surja alguma dúvida, fique a vontade para entrar em contato comigo :)

## Abordagem e Implementação:

A abordagem para realizar essa tarefa foi a criação de um modelo para empresa, no código chamado de Empresa, e um modelo para o funcionário, no código chamado de Funcionario.

Abaixo temos o código de Empresa:

```
class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    cnpj = models.CharField(max_length=14, help_text='CNPJ da empresa')

    def __str__(self):
        return self.nome
```

Abaixo temos o código de Funcionario:

```
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ManyToManyField(Empresa)

    def __str__(self):
        return self.nome
```

## Endpoints:

Para essa pequena API foram criados os seguintes endpoints:

| Endpoint               | Função                    | Método  | JSON/Parametros                                                               |
|------------------------|---------------------------|---------|--------------------------------------------------------------------|
|/api/criaremp/     | Criar uma empresa         | POST    | {"nome":"Nome da Empresa", "cnpj":"cnpj da empresa"}               |
|/api/empresas/         | Mostra todas as empresas  | GET     | ?id= , ?nome= , ?user=            |
|/api/empresas/pk/    | Dado o id de uma empresa, mostra os seus dados e seus funcionários         | GET    |    |
|/api/funcionarios/     | Retorna todos os Funcionários do sistema         | GET    | ?id= , ?nome= , ?user=               |
|/api/funcionarios/pk/     | Retorna informações de um Funcionário dado seu ID         | GET    |               |

## Como usar:

A aplicação foi publicada no Heroku, podendo ser acessada pelo link:

https://desafio-company-hero.herokuapp.com

Se ocorrer demora, é devido ao Heroku colocar em modo de espera uma aplicação que não está sendo usada no momento.

Como a aplicação é focada na sua API, nenhuma página retornará se o link acima for acessado, logo, 
é preciso ter em mente que essa aplicação só funcionará se algum dos endpoints acima for usado, por exemplo:

https://desafio-company-hero.herokuapp.com/api/empresas/

Esse link retornará todas as empresas cadastradas no sistema.

https://desafio-company-hero.herokuapp.com/api/funcionarios/

Esse link retornará todas os funcionarios cadastradas no sistema.

### Importante:
para buscar um usuario e suas empresas foi criado parametros para que se possa encontrar usuarios, então pode se passar na requisição desta forma:

https://desafio-company-hero.herokuapp.com/api/funcionarios/?user=jeffersonsilva

https://desafio-company-hero.herokuapp.com/api/empresas/?user=jeffersonsilva

### O que fazer:
1. Primeiramente, será necessario utilizar um dos links com seus Endpoints.
2. Depois, será necessario utilizar um token no cabeçalho do postgress sendo: Key = Authorization e Value = Token 6da128560f7125ae2812243b8c37d4d62ac42b03
3. Após isso conseguira acesso a todas as empresas e funcionarios na chamada, podendo passar parametros
4. Depois disso, já teremos dados a serem retornados nos endpoints de GET :D

#### p.s.: Caso necessário, O Django admin é acessado normalmente em /admin o superuser já existente se chama companyhero e a senha é hero
