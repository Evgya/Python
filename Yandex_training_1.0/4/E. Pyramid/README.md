<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Пирамида</h1>
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
   <div class="legend"> Для строительство двухмерной пирамиды используются прямоугольные блоки, каждый из которых характеризуется шириной и высотой.
      Можно поставить один блок на другой, только если ширина верхнего блока строго меньше ширины нижнего. Самым нижним в пирамиде
      может быть блок любой ширины. По заданному набору блоков определите, пирамиду какой наибольшей высоты можно построить из них.

   </div>
   <h2>Формат ввода</h2>   
    В первой строке входных данных задается число $N --$ количество блоков $(1 \leq N \leq 100 000).$            
      В следующих $N$ строках задаются пары натуральных чисел $w_i$ и $h_i$ $(1 \leq w_i, h_i \leq 10^9)
      — ширина и высота блока соответственно.
      </p>

   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно целое число&nbsp;— максимальную высоту пирамиды. </div>