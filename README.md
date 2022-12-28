# FriDa
dai frisini per i frisini


# Windows

## Download e requisiti
### Python:
1. Controllare la versione del proprio sistema operativo
  Windows button -> digitare "System" -> 32 o 64 bit
2. Scarica l'installer adatto al tuo sistema:
  - [Python 3.9.13 (32 bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe)
  - [Python 3.9.13 (64 bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)
3. Apri l'installer:
  - Flaggare "Add python 3.x to PATH"
  - Customize installation
  - Nella sezione "Advanced Options" flaggare "Add python to environmental variables"
### Download
1. Clicca "Code" e "Download ZIP"
2. Seleziona la cartella di destinazione 
3. Click sinistro sulla cartella e seleziona "Estrai stutto"
### Librerie e moduli
1. Apri la cartella installata
2. Apri il terminale digitando `cmd` nel percorso del file
3. Digita il comando `pip install -r requirements.txt`


## Utilizzo
Per eseguire i seguenti comandi:
1. Apri la cartella installata
2. Apri il terminale digitando `cmd` nel percorso del file
3. Digitare `frida -help` per maggiori indicazioni
### Comandi
#### Website
- `frida website` apre una local webapp per poter gestire tutto ciò che riguarda FriDa
#### Dashboard
- `frida fridash` apre la dashboard con i grafici relativi ai tuoi voti
#### Help
- `frida -help` mostra l'elenco dei comandi disponibili
### Virtual environment
Puoi utilizzare automaticamente un virtual environment chiamato `env`, se presente nella cartella principale.
Per poterlo richiamare durante l'esecuzione aggiungere `-env` prima del comando desiderato.
Es.: `frida -env website`




