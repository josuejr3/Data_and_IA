
<h2 align="center" style="color: #00ff00;">Filtragem de Dados</h2>

Quando estamos falando de filtragem no Pandas a primeira coisa que podemos fazer é alterar a indexação, ou seja, ao invés de usarmos os índices padrão do Pandas podemos escolher uma das colunas e usar ela como índice.

> *Exemplo - Alterando Indices*

Nesse exemplo usamos a coluna de nome como índice ao invés da coluna de índice padrão do Pandas.

```python
df = df.set_index(df.columns[0])
```

Com isso eu posso "conversar" diretamente com o índice. 

> *Exemplo - Obtendo Informações*

```python
df.loc[["Fabiana"], ["Salário"]]
```

Para retornar aos índices padrões, fazemos:

```python
df = df.reset_index()
```

> *Exemplo - Filtragem a partir de uma coluna*

```python
mais_de_30 = df[df["Idade"] > 30]
```

Podemos ler o código acima como "selecione do dataframe df somente as linhas em que a coluna df é maior do que 30".

Ok, mas e se for necessário fazer a seleção de condições de mais de uma coluna, como fazer?

> *Exemplo - Condições em mais de uma coluna*

```python
mais_de_30 = df[(df["Idade"] > 30) & (df["Salário"] > 10000)]
print(mais_de_30)
```

-  Deve se usar operadores | ou & para comparação de colunas
-  Os ( ) são necessários para evitar erro na precedência de operadores

> *Exemplo - Verificação de valores nulos*

```python
print(df.isnull())
```

A função "*isnull( )*" retorna True nas células do dataframe que possuem valores nulos e False nos locais em que é não nulo.

```python
# Verificando se existe qualquer valor nulo 
print(df.isnull().any())
```

O any verifica coluna por coluna e rearanja da seguinte forma.

```
Nome       False
Idade       True
Cidade     False
Salário     True
dtype: bool
```

---

<h2 align="center" style="color: #00ff00;">Inspeção de DataFrames</h2>

Os DataFrames podem ser inspecionados, ou seja, podem ser obtidos resumos de cada dataframe trabalhado.

-  O método shape mostra a dimensão do dataframe, ou seja, a quantidade de colunas e linhas.

> *Exemplo - uso do shape*

```python
print(df.shape)
```

-  O head e o tail servem para selecionar as primeiras linhas desejadas ou as últimas.

>*Exemplo - uso de head e tail para selecionar primeiros e últimos elementos*

```python
df.head(5)
```

```python
df.tail(5)
```

- Já o método info traz várias informações à respeito do dataframe, como por exemplo os tipos de dados.

> *Exemplo - informações do datafrme*

```python
print(df.info())
```

Obs: no Pandas existem os tipos de dados númericos e tudo que não é númerico é chamado de object. É importante saber disso, pois quando usa-se esse método o Dtype pode aparecer como **object**.

-  O método describe basicamente informa estatísticas descritivas como média, mediana, máximos e mínimos.

> *Exemplo - uso do describe*

```python
print(df.describe())
```

Nesse caso ele mostra estatísticas descritivas somente de colunas numéricas. Se desejar incluir as não numéricas fazemos assim:

```python
print(df.describe(include = "all"))
```

Se for necessário selecionar somente um tipo o "all" poe ser substituido por um \[object] ou \[np.number]

```python
print(df.describe(include = [object]))  # Variáveis categóricas
```

