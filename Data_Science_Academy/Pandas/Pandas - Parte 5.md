
<h2 align="center" style="color: #00ff00;">Operações e Transformações de Dados com Pandas</h2>

Primeiramente vamos abordar a criação de novas colunas no dataframe. 

> *Exemplo - Criação de Coluna* a partir de outra

```python
df["Salário Atual"] = df["Salário"] * 12
```

É similar a vetorizaão que temos com o Numpy. Nesse exemplo, usamos a coluna "Salário" para servir como base para a nova coluna "Salário Atual".

Ele executa automaticamente para cada uma das linhas.

> *Exemplo - Criando uma coluna e aplicando uma função sobre ela*

```python
df["Bônus"] = df["Salário"].apply(lambda x: x * 0.10 if x > 7000 else x * 0.05)
```

Nesse caso a coluna de "Bônus" é criada a partir da coluna salário e uma função é aplicada a cada um dos valores do salário se ele for maior que 7000 o valor na nova coluna será multiplicado por 0.10 se não, será multiplicado por 0.05.

> *Exemplo - Adicionando uma nova coluna e removendo*

```python
df["Teste"] = "x"
#df.head()
df.drop(columns=["Teste"], inplace=True)
df.head()
```

Nesse exemplo adicionamos a coluna "Teste" com o valor "x" para todas as linhas do dataframe e logo em seguida fazemos a remoção da coluna usando o método drop. Um fato curioso é que assim como muitos métodos do Pandas o drop retorna um novo dataframe de cópia e não o antigo modificado. Para alterar o dataframe real, usamos o "inplace" como True e passamos a coluna que queríamos remover.

> *Exemplo - Colunas criadas com base em regras*

```python
# Define os rótulos correspondentes
faixas = ["Menor de Idade", "Jovem", "Adulto", "Idoso"]
df["Faixa Etária"] = np.select(condicoes, faixas, default="Idade Não Informada")
df.head()
```

O método select do Numpy faz a "interligação" entre as máscaras que são as condições e as faixas que são os valores reais.

<h2 align="center" style="color: #00ff00;">Agrupamento de Dados</h2>

Por trabalhar com dados tabulares o Pandas também possui um método especial chamado GroupBy, assim como em linguagens SQL. 

> *Exemplo - Agrupando por cidade*

```python
media_salario_cidade = df.groupby("Cidade")["Salário"].mean()
```

Nesse caso, agrupamos por cidade, até ela é a coluna de agrupamento. A coluna do cálculo a ser feito/contabilizado é inserida depois, aqui usamos o salário e depois chamamos o método da média.

> *Exemplo - Agrupando e fazendo agregações*

```python
# Agrupando por cidade e calculando múltiplas agregações
agregacoes_cidade = df.groupby("Cidade").agg(Media_Salarial = ("Salário", "mean"),
                                             Idade_Maxima = ("Idade", "max"),
                                             Contagem = ("Nome", "count"))
```

Aqui, usamos o método "agg" que faz várias agregações ao mesmo tempo, como média, valores máximos, mínimos e contagem de valores. Para isso, passamos o nome da varíavel e em seguida atribuimos uma tupla com a coluna que será usada na agregação e a função que queremos usamos.

<h2 align="center" style="color: #00ff00;">Manipulação de Tipos de Dados</h2>

Antes de fazer manipulação nos tipos de dados que o dataframe possui, precisamos saber quais os tipos que estão sendo usados. Para isso, podemos usar o atributo dtypes.

> *Exemplo - Tipos de Dados*

```python
print(df.dtypes)
```

A conversão de valores, normlmente float para int e vice versa é feita através do método astype passando o novo tipo como parâmetro. 

> *Exemplo - Conversão Float - Int*

```python
df["Idade"] = df["Idade"].astype(int)
```

Entretanto, isso só vai funcionar se na coluna não tiver nenhum valor NaN (not a number). Para resolver, devemos remover todas as instâncias que tem NaN na coluna da idade.

> *Exemplo - Removendo valores ausentes*

```python
df = df.dropna(subset = ["Idade"])
df["Idade"] = df["Idade"].astype(int)
```

> *Exemplo - Conversão do tipo Object para String*

```python
df["Nome"] = df["Nome"].astype("string")
df["Cidade"] = df["Cidade"].astype("string")
df["Faixa Etária"] = df["Faixa Etária"].astype("string")
```

O ajuste dos dados para seus tipos corretos é importante pois flexibiliza a quantidade de ferramentas e operaçõs que podemos utilizar. 

> *Exemplo - Usando método de string Python*

```python
df["Faixa Etária"] = df["Faixa Etária"].apply(lambda x: x.upper())
df.head()
```














