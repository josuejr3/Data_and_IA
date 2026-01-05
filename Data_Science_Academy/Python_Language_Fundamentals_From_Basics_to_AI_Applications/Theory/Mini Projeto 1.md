
-  Criação do Repositório
	-  README.md
	-  Gitignore
-  Criação do ambiente virtual 
```cmd
conda create -n .venv python=3.13.2
```
-  Ativar o ambiente
```cmd
conda activate .venv
```
-  Instalar o jupyer
```cmd
conda install jupyter
```

---

-  Instalar o watermark

```ipynb
!pip install -q -U watermark
```

Basicamente esse watermark serve para mostrar as versões das ferramentas que estamos utilizando. O -q é de quit que é para mostrar menos mensagens e o -U é para atualizar se o pacote já estiver instalado.

