Claro, aqui está um exemplo de um arquivo README.md para o seu projeto de API RESTful em Python:

```markdown
# API RESTful Simples em Python

Esta é uma API RESTful simples criada em Python que permite adicionar, listar e excluir notas em um arquivo JSON.

## Pré-requisitos

Antes de começar, você deve ter o Python instalado no seu sistema.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/api-python-simples.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd api-python-simples
   ```

3. Execute o servidor:

   ```bash
   python api.py
   ```

A API estará rodando em http://127.0.0.1:8000/ por padrão. Certifique-se de que o servidor esteja em execução antes de fazer solicitações.

## Uso

A API possui os seguintes endpoints:

- `POST /adicionar`: Adiciona uma nova nota. Envie um JSON no corpo da solicitação com os campos `time`, `tittle` e `body`.

- `GET /Mostrar`: Lista todas as notas existentes.

- `DELETE /delete?titulo=TituloDaNota`: Exclui uma nota com um título específico.

### Exemplo de Uso com cURL

Adicione uma nota:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"time":"26/08/2023 21:35", "tittle":"Titulo da nota", "body":"corpo da nota"}' http://127.0.0.1:8000/adicionar
```

Liste todas as notas:

```bash
curl http://127.0.0.1:8000/Mostrar
```

Exclua uma nota por título:

```bash
curl -X DELETE http://127.0.0.1:8000/delete?titulo=TituloDaNota
```

Lembre-se de substituir `TituloDaNota` pelo título da nota que deseja excluir.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação pull.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

```
