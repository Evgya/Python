<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Забавный конфуз</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Пусть <span class="tex-math-text">A</span> — массив, состоящий из <span class="tex-math-text">N</span> элементов <span class="tex-math-text">A<sub>1</sub>,&hellip;,A<sub>N</sub></span>. Обозначим его максимальное и минимальное значение через max(<span class="tex-math-text">A</span>) и min(<span class="tex-math-text">A</span>) соответственно. Вычислим сумму элементов <span class="tex-math-text">S</span>, <span class="tex-math-text">S=A<sub>1</sub>+A<sub>2</sub>+&hellip;+A<sub>N</sub></span>. Заменим каждый элемент массива на разницу <span class="tex-math-text">S</span> и этого элемента:
         $A_{i}:=S-A_{i}, 1 \leqslant i \leqslant N$
      <p>Такое преобразование массива <span class="tex-math-text">A</span> назовем операцией Confuse. Напишите программу, которая по массиву <span class="tex-math-text">B</span>, полученному в результате <span class="tex-math-text">K</span>-кратного применения операции Confuse к некоторому массиву <span class="tex-math-text">A</span>, вычислит разность max(<span class="tex-math-text">A</span>)-min(<span class="tex-math-text">A</span>).
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входного файла содержит целые числа <span class="tex-math-text">N</span> и <span class="tex-math-text">K</span>, где <span class="tex-math-text">N</span> — количество элементов массива <span class="tex-math-text">B</span> $(2 \leqslant N \leqslant 10000)$, а <span class="tex-math-text">K</span> — количество применений операции Confuse к начальному массиву <span class="tex-math-text">A</span>,$(1 \leqslant K \leqslant 100)$ . Вторая строка файла содержит <span class="tex-math-text">N</span> элементов массива <span class="tex-math-text">B</span>. Элементы массива <span class="tex-math-text">B</span> — целые числа, принадлежащие диапазону от <span class="tex-math-text">-2&nbsp;000&nbsp;000 000</span> до <span class="tex-math-text">2&nbsp;000&nbsp;000 000</span>.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Единственная строка выходного файла должна содержать целое число - разность max(A) и min(A).</p></span></div>
