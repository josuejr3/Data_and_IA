<h2 align="center" style="color: #00ff00;">Operações Matemáticas Vetorizadas</h2><p style="text-indent: 2em;">A "vetorização" permite aplicar operações em arrays inteiros de uma vez, sem a necessidade de loops for, o que é extremamente rápido. O Numpy usa implementações em linguagem C otimizada e faz operações em bloco sobre arrays inteiros, evitando o loop python elemento a elemento. Isso brilha quando temos muitos dados (milhares ou milhões de elementos).</p>

-  Para fazer uma operação sobre uma grande massa de dados basta usar o vetor em que os dados estão e a operação será realizada sobre todos os elementos.

> Exemplo

```python
precos = np.array([19.99, 25.50, 8.90, 43.00])
# Aplicando multiplicação dos valores por 0.90
precos_com_desconto = precos * 0.90
```

<h2 align="center" style="color: #00ff00;">Agregações Estatísticas com NumPy</h2><p style="text-indent: 2em;">Como vimos, operações matemáticas vetorizadas é basicamente aplicar a operação matemática a cada elemento do array numpy. Agregação é basicamente aplicar a operação a todos os elementos do array</p>

> Exemplo

```python
print(f"Média geral da turma: {notas.mean():.2f}")
```

Nesse caso, ainda é uma operação vetorizada, porém é estatística, uma vez que considera todos os elementos.

-  A agregação (considerar todos os dados e fazer operação estatística) pode ser feita em um único eixo, (o axis é o eixo das colunas). 

```python
# Faz a média por eixo e arredonda para duas casas decimais.
media_por_aluno = notas.mean(axis=1).round(2)
print(media_por_aluno)
```

-  Se quisessemos considerar apenas as linhas o valor de axis deveria ser zero.

<h2 align="center" style="color: #00ff00;">Broadcasting</h2>
<p style="text-indent: 2em;">Broadcasting nada mais é do que realizar operações aritméticas entre arrays de formas (shapes) diferentes, sem precisar copiar ou replicar manualmente os dados. Ela funciona expandindo automaticamente as dimensões de arrays menores para que fiquem compatíveis com os maiores, seguindo um conjunto de regras.</p><p style="text-indent: 2em;">Isso evita laços (loops) explicítos e melhora muito a eficiência. Por exemplo, se você soma uma matriz 3x3 com um vetor de 3 elementos, o Numpy "estica" o vetor para que cada linha da matriz receba a soma correspondente elemento a elemento, sem criar cópias extras na memória.</p>

```python
resultado = matriz + vetor
```

Quando dois arrays de dimensões diferentes ele "expande" o array menor para ele ter as dimensões do maior.

<p align="center" style="background: green;">Observação Importante: dependeno do shape dos arrays que são os operandos as operações matemáticas vetorizadas podem não funcionar, sendo necessário fazer o reshape de uma delas</p>

A manipulação estrutural de arrays envolve normalmente três métodos

-  Transposta - inverte linhas e colunas

```python
print(matriz_3x4.T)
```

-  Reshape - transforma as dimensões do array

```python
matriz_3x4 = dados_sequenciais.reshape(3, 4)
print(f"Matriz\n{matriz_3x4}")
```

-  Flatten - coloca um array multidimensional em uma dimensão

```python
vetor_novamente = matriz_3x4.flatten()
print(vetor_novamente)
```