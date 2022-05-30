import requests


def retorna_dados_cep(cep):
    response = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep))  # subistituimos o cep na url para declara-la na no main
    print(response.status_code)
    # vai retornar 200 significa que a pagina existe, se eu colocar aqui uma pagina que não exite
    # vai retornar erro 400
    print(response.text)
    print(type(response.text))  # tipo string
    print(response.json())
    print(type(response.json()))
    dados_cep = response.json()  # tipo dicionario
    print(dados_cep['logradouro'])
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


if __name__ == '__main__':
    # retorna_dados_cep('01001000')
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon)
