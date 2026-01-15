
<h2 align="center" style="color: #00ff00;">Seleção e Indexação com Pandas</h2>

O método "head()" basicamente funciona como se fosse um "select" de um Banco de Dados, no entanto, ele usa somente quantidade numéricas, ou seja, eu só posso obter os cinco primeiros elementos, os dez primeiros e assim por diante. 

> *Exemplo - Seleção com head*

```python
df.head()
```

Já para a seleção de uma coluna específica nós podemos usar a mesma lógica que usamos em um dicionário, através da chave.

Como estamos fazendo a seleção de uma única coluna basicamente temos o retorno de uma Series.

```python
name = df["Nome"]
name.head()
```

Da mesmo jeito que fizemos para uma única coluna poderíamos fazer para variás colunas usando uma lista das colunas

```python
info_pessoal = df[["Nome", "Cidade"]]
info_pessoal.head()
```

---

<h2 align="center" style="color: #00ff00;">Comandos loc e iloc</h2>

Os comandos loc e iloc são usados para obter elementos, ou seja, fazer a seleção de dados através de rótulo ou indice.

-  loc - usa uma combinação do indice da linha e o rótulo da coluna

> *Exemplo - Uso do loc*

Nesse exemplo está sendo feita a seleção da linha de índice 1 da coluna "Nome", que no nosso caso, corresponde ao Bruno.

```python
nome = df.loc[1, "Nome"]
```

Se fosse necessário outras colunas, bastava "envolver" o segundo parâmetro em uma lista.

```python
nome = df.loc[1, ["Nome", "Cidade"]]
```

-  iloc - usa o indice da linha e o da coluna

> *Exemplo - Uso do iloc*

Nesse exemplo vamos buscar o elemento que está na linha de índice 2 e coluna de índice 3, que nesse caso é "Salário". (A coluna de índice não é contabilizada)

```python
salario_fabi = df.iloc[2, 3]
```

Assim como eu posso acrescentar quantas colunas forem necessárias no loc eu posso fazer isso no iloc também.

```python
dados_fabi = df.iloc[2, [0, 1, 2, 3]]
```

