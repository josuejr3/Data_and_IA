
<h2 align="center" style="color: #00ff00;">Tipos de Dados</h2>
O Numpy detecta automaticamente os tipos de dados usados.

> Exemplo

```python
arr_inteiros = np.array([1, 2, 3])
print("Tipo de dado (inteiros): ", arr_inteiros.dtype)
```

```python
arr_float = np.array([1.0, 2.0, 3.0])
print("Tipo de dado (inteiros): ", arr_inteiros.dtype)
```

Para os casos de ML e IA nós trabalhamos normalmente com os tipos float, pois usando tipos inteiros ocorre muitos arredondamentos o que pode impactar no resultado final.

Entretanto, se não quiser que o numpy faça inferência automatica do tipo de dado, é possível passar o tipo desejado durante a definição da estrutura.

```python
arr_float = np.array([1, 2, 3], dtype = np.float64)
```

Outra coisa que da para fazer é a conversão de tipos float para inteiro, por exemplo

```python
arr_int = arr_float.astype(np.int64)
```

<h2 align="center" style="color: #00ff00;">Indexação e Fatiamento de Estruturas de Dados Numpy</h2>A indexação no Numpy é semelhante a que nós temos no Python, passando o índice entre colchectes.

> Exemplo

```python
data = np.arange(16).reshape(4, 4)
```

Para acessar o elemento da terceira linha e terceira coluna fazemo o seguinte.

```python
print(data[2, 2])
```

**Mas por qual motivo passar o dois ao invés do três?** Lembre-se que Python é zero indexado, ou seja, ele sempre começa suas estruturas com a posição zero. Dessa forma, para acessar as terceiras posições devemos usar o número dois.

O fatiamento também é semelhante ao Python puro, se quisermos pegar a primeira linha de uma matriz podemos fazer o seguinte

```python
print(data[1])
```

Vai retornar toda a linha de indice um.
<p align="center" style="background: green;">É importante, para facilitar a legibilidade, usarmos a sintaxe de<br> 
[ LINHA, COLUNAS ]</p>
Do mesmo jeito que fizemos para as linhas, podemos fazer para as colunas

```python
data[:, 3]
```

Esse código vai retornar todas as linhas da coluna três. 

> Exemplo - sub matriz da matriz maior (inferior e esquerda)

```python
block_inf_right = data[2:, 2:]
print(block_inf_right)
```

Nesse caso, o índice é exclusivo, ou seja, ele não vai ser incluido na operação. Como aqui eu estou cobrindo do índice dois até o final ele pegará todos os elementos a partir da coluna e linha de índice dois.

Outra coisa que podemos fazer é a indexação/fatiamento através de booleanos

```python
greather_than_10 = data[data > 10]
```

A mesma sintaxe que usamos no for de *"start:stop:step"* pode ser usada no numpy.

```python
resultado = matriz[::2, 1::2]
```

