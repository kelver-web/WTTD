# Eventex

Sistemas de eventos encomendado pela morena

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com python 3.8
3. Ative o virtualenv
4. Instale as dependências
5. Configure a intância com o .env
6. Execute os textes


```Console
git clone git@github.com:henriquebastos/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp/contrib/env-sample .env
python manage.py test

```

## Como fazer o depoloy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina um DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```Console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib /secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```