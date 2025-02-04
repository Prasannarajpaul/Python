import logging

## Configuring logging setting - kernel need to be restarted inorder update the config
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

