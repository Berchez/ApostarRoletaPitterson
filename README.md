# :moneybag: Apostar Roleta Pitterson **[DEPRECATED]**
 Esse é o repositório onde colocarei o bot que inicializa as apostas do site 'https://johnpittertv.com/roleta' automaticamente, de modo a ganhar o máximo de pitterson e correr um risco pequeno.

***

 ## :gear: Como configurar ?
1. Baixe ou clone o este repositório.

1. Para utilizar este repositório você deverá ter Python instalado na sua máquina, clique [aqui](https://python.org.br/instalacao-windows/) caso você não o tenha. Após obter o Python, baixe o [PIP](https://phoenixnap.com/kb/install-pip-windows).

 1. Depois isto, precisaremos instalar o selenium, execute este comando no terminal:
 >```pip install selenium```

 4. Ao terminar o download, baixe também a última versão do [ChromeDriver](https://chromedriver.chromium.org/downloads) e salve na pasta "C:\Program Files (x86)".

5. Feito isto, teremos que [criar um perfil](https://support.google.com/chrome/answer/2364824?co=GENIE.Platform%3DDesktop&hl=pt-BR) no Chrome (caso você já não tenha pelo menos um). Após, acesse o diretório "C:\Users\\**_NOME-DO-USUARIO-DO-SEU-PC_**\AppData\Local\Google\Chrome" e crie uma pasta chamada "AutoBot" (sem as aspas). Feito isto, copie todos os arquivos da pasta "UserData" e cole na pasta "AutoBot".

6. Troque o caminho que está na linha 63 do arquivo 'index.py', colocando o nome do seu PC:

![Screenshot_402](https://user-images.githubusercontent.com/50505615/109254418-bcd65c80-77d0-11eb-9337-9b89c09b6049.png)

7. Por fim, inicialize a variável com o valor desejado:

![Screenshot_401](https://user-images.githubusercontent.com/50505615/109253103-cca07180-77cd-11eb-8b71-237612f3ec21.png)


Eu recomendo um valor entre 11 e 15.

***

## :rocket: Como utilizar
[Abra o terminal na pasta baixada](https://www.softdownload.com.br/como-abrir-prompt-comando-windows-pasta-especifica.html#:~:text=Basta%20voc%C3%AA%20abrir%20a%20pasta,Abrir%20janela%20de%20comando%20aqui.) e digite:
>```python index.py```

## Licença
A licença do projeto é MIT License - olhar o arquivo LICENSE.md para mais detalhes.

