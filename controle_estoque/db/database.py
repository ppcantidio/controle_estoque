import boto3
from dynaconf import settings

def connection():
    """
    Realiza conexao com banco
    da aws dynamodb
    """
    return boto3.resource('dynamodb',
        region_name=settings['REGION_NAME'],
        aws_access_key_id=settings['AWS_ACESS_KEY_ID'],
        aws_secret_access_key=settings['AWS_ACESS_KEY_SETTINGS']
    )

def create_tables():
    """
    - Verifica existência de tabelas
    - Caso não existam, cria as tabelas
    """