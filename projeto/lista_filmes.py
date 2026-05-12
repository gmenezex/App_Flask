import urllib.request
import json
import ssl

#Ignora a verificação do certiicado SSL.
ssl._create_default_https_context = ssl._create_unverified_context
def resultado_filmes(tipo):
  if tipo == 'Populares':
    url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3c0468ed1d2ef4824c0aa68c4e9d72c'
  elif tipo == 'Animação':
    url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=3c0468ed1d2ef4824c0aa68c4e9d727c'
  elif tipo == '2010':
    url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=3c0468ed1d2ef4824c0aa68c4e9d727c'

  resposta = urllib.request.urlopen(url)

  dados = resposta.read()

  dados_json = json.loads(dados)
  return dados_json['results']
