# Matrix-module

Create Matrix class with following methods:

1. __ init__ (self, 2d_array) must get 2d array in argument <br>
1.1. befor creating Matrix should be checked if matrix <br>
   . has anly numerical items <br>
   . rows have same length <br>
if not then raise Exception with corresponding message <br>

2. __ add__(self, other_matrix) method should add current instance to matrix instanse that pass as argument <br>
3. __ sub__(self, other_matrix) method should subtract from current instance a matrix instanse that pass as argument <br>
4. __ mul__(self, other_matrix) method should multiply current instance with matrix instanse that pass as argument <br>
5. __ str__(self, other_matrix) method shuld return string of matrix as follows: <br>
<br>
<pre>
⌈ 1.60  3.1 42.34 ⌉
|  4.0 5.00   6.9 |
⌊ 43.0  2.4  3.99 ⌋
</pre>
<br> 
 
6. determinant() calculates determinant of matrix <br>
7. inverse() calculate inverse of matrix <br>
8. same_dimention_with(other_matrix) makes sure other matrix has the same dimension as instance matrix <br>
9. is_square() check if matrix is square <br>
10. random_matrix() static method returns instance of Matrix by <br>


https://en.wikipedia.org/wiki/Matrix_(mathematics)
