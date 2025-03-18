import requests
from bs4 import BeautifulSoup
import re

def get_price_kabum(produto):
    url = f"https://www.kabum.com.br/search/?q={produto}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar todos os produtos na página
    produtos = soup.find_all("div", class_=re.compile("productCard"))  # Ajuste conforme necessário

    if produtos:
        primeiro_produto = produtos[0]  # Pegando apenas o primeiro produto encontrado
        
        # Agora buscamos a classe que contém o preço dentro deste produto específico
        price_elem = primeiro_produto.find("span", class_=re.compile("price"))

        if price_elem:
            price_text = price_elem.get_text(strip=True)
            price = float(price_text.replace("R$", "").replace(".", "").replace(",", "."))
            return price

    return None

# Testando a busca para um teclado específico
produto = "teclado logitech"
preco_kabum = get_price_kabum(produto)

if preco_kabum:
    print(f"Preço na Kabum: R$ {preco_kabum:.2f}")
else:
    print("Preço não encontrado na Kabum.")
