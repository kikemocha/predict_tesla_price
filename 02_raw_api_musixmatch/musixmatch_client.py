import json
import requests
import re


class MusixmatchClient:
    """
    Cliente para interactuar con la API de Musixmatch y descargar letras de canciones.
    """

    BASE_URL = "https://api.musixmatch.com/ws/1.1"

    def __init__(self, api_key):
        """
        Inicializa el cliente con una API Key válida.
        :param api_key: Clave de API de Musixmatch.
        """
        if not api_key:
            raise ValueError("Se requiere una clave API válida para inicializar el cliente.")
        self.api_key = api_key

    def _validate_response(self, response):
        """
        Valida si la respuesta del API.
        :param response: Respuesta del API.
        :return: True si es válida, False en caso contrario.
        """
        if response.get("message", {}).get("header", {}).get("status_code") == 200:
            lyrics_body = response.get("message", {}).get("body", {}).get("lyrics", {}).get("lyrics_body", "")
            return bool(lyrics_body)
        return False

    def get_lyrics(self, track, artist):
        """
        Obtiene las letras de una canción por título y artista.

        REFERENCIA: https://coda.io/@musixmatch/musixmatch-lyrics-api/matcher-lyrics-get-28
        
        :param track: Nombre de la canción.
        :param artist: Nombre del artista.
        :return: (dict) Diccionario como  {"lyrics":string}, o en caso de error un diccionario con {"error":str}.
        """
        url = f"{self.BASE_URL}/matcher.lyrics.get"
        params = {
            "q_track": track,
            "q_artist": artist,
            "apikey": self.api_key,
            "format": "json"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if self._validate_response(data):              
                return {"lyrics":data["message"]["body"]["lyrics"]["lyrics_body"]}
            else:
                return {"error": f"can not validate the response", "response": data}    
        else:
            return {"error": f"bad status code {response.status_code}"}
        
