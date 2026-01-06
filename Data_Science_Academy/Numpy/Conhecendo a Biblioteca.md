
<h2 align="center" style="color: #00ff00;">O Objeto ndarray</h2>
Um array NumPy é uma estrutura e dados multidimensional usada em computação científica e análise de dados. O NumPy fornece um objeto de matriz **N-dimensional** (ou ~={cyan}ndarray=~), que é uma grade homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros.

Os arrays Numpy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidade de dados, pois são implementados em Linguagem C e fornecem várias otimizações de desempenho. Além disso, o Numpy permite fácil leitura de arquivos de dados, integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs e GPUs.

> Exemplo visual de arrays Numpy

<img align="center" src="Imagens/Array Numpy.png">

Na imagem acima coseguimos ver estruturas com várias dimensões

-  1D Array - Vetor
-  2D Array - Matriz
-  3D Array - Tensor

_O PyTorch foi criado "em cima" do Numpy_

<h2 align="center" style="color: #00ff00;">Instanciação de Atributos</h2>O array (no caso o de uma e duas dimensões), vetores e matrizes, podem ser instanciados a partir de uma estrutura python já existente, como uma lista python ou lista de listas e usando o ".array()".

> Exemplos

```python
vector = np.array([17, 21, 100, 34])
matriz = np.array([[1, 2, 3], [4, 5, 6]])
```

Entretanto, quando queremos uma estrutura com dimensão maior ou igual a três a forma de instanciar é um pouco diferente. 

```python
arr = np.arange(24).reshape(4, 3, 2)
```

O numpy chama a função "arange" que define a quantidade total de elementos na estrutura. Já o reshape vai ser responsável por definir as dimensões. Nesse caso, teremos:

-  Eixo 0 - tamanho 4
-  Eixo 1 - tamanho 3
-  Eixo 2 - tamanho 2

Igual conseguimos ver na imagem anterior.

> Exemplo - Tensor de dimensão quatro

```python
tensor4d = np.arange(120).reshape(2, 3, 4, 5)
```


