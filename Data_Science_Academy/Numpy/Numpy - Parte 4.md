
<h2 align="center" style="color: #00ff00;">Operações Matemáticas com Matrizes Numpy</h2>Até agora não tinhamos estudado a multiplicação entre matrizes. Diferente da multiplicação elemento à elemento, a multiplicação de matrizes tem um operador específico e segue a regra da álgebra linear. Sendo assim, a multiplicação é dada das linhas pelas colunas. 

Para fazer a multiplicação entre matrizes *(Produto Matricial)* podemos trabalhar de duas formas distintas. A primeira usando o operador especial "@" ou o *"np.dot"*

> Utilizando @

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

produto_matricial = A @ B
print(produto_matricial)
```

> Utilizando o np.dot( )

```python
produto_matricial = np.dot(A, B)
```

Para fazer a multiplicação de elemento por elemento, ou seja, **A MULTIPLICAÇÃO NÃO MATRICIAL**basta utilizar o operador de multiplicação comum ( * )

```python
produto_elemento_a_elemento = A * B
```

A multiplicação matricial é bastante usada no contexto de redes neurais.

Cada camada de uma rede neural realiza uma transformação linear dos dados de entrada. Essa transformação é feita multiplicano a matriz de pesos da camada (W) pelo vetor ou matriz de entrada (X).

	Saída = X @ W + bias

-   X - entradas (amostras + features)
-  W - pesos (features x neurônios)
-  bias - deslocamento adicionado depois
<p align="center">Todos modelos de IA usam operações matriciais.</p>
> Exemplo de operações elemento à elemento

```python
# Operacoes de Matrizes
soma = A + B
subtracao = A - B
divisao = A / B

print("Operações\n")
print(f"+: {soma}\n")
print(f"-: {subtracao}\n")
print(f"/: {divisao}\n")
```

<h2 align="center" style="color: #00ff00;">Exemplo de Operações com Matrizes no Processamento de Imagens</h2>

-  Imagens são matrizes com valores numéricos representando a tonalidade das cores.

