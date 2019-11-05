import json

content = '''{
  "informacao1": "valor_informação1",
  "informacao2": "{dado=informação_dado}"
}'''
data = json.loads(content)
print(data.get("informacao2"))