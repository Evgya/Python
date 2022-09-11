<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Площадь</h1>
      <table>
         <tr>
            <th>Язык</th>
            <th>Ограничение времени</th>
            <th>Ограничение памяти</th>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
         <tr>
            <td width="1%">Все языки</td>
            <td>0.5&nbsp;секунд</td>
            <td>64Mb</td>
            <td rowspan="8">стандартный ввод или input.txt</td>
            <td rowspan="8">стандартный вывод или output.txt</td>
         </tr>
         <tr>
            <td>
               <nobr>GNU C11 7.3</nobr>
            </td>
            <td>0.3&nbsp;секунды</td>
            <td>256Mb</td>
         </tr>
         <tr>
            <td>
               <nobr>GNU c++ 11 4.9</nobr>
            </td>
            <td>0.3&nbsp;секунды</td>
            <td>256Mb</td>
         </tr>
         <tr>
            <td>
               <nobr>GNU c++ 11 x32 4.9</nobr>
            </td>
            <td>0.3&nbsp;секунды</td>
            <td>256Mb</td>
         </tr>
         <tr>
            <td>
               <nobr>GCC 5.4.0 C++14</nobr>
            </td>
            <td>0.3&nbsp;секунды</td>
            <td>256Mb</td>
         </tr>
         <tr>
            <td>
               <nobr>GNU c++ 14 4.9</nobr>
            </td>
            <td>0.3&nbsp;секунды</td>
            <td>256Mb</td>
         </tr>
         <tr>
            <td>
               <nobr>GNU c++17 7.3</nobr>
            </td>
            <td>0.3&nbsp;секунды</td>
            <td>256Mb</td>
         </tr>
         <tr>
            <td>
               <nobr>GCC  C++17</nobr>
            </td>
            <td>0.3&nbsp;секунды</td>
            <td>256Mb</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Городская площадь имеет размер <span class="tex-math-text">n&times; m</span> и покрыта квадратной плиткой размером <span class="tex-math-text">1&times; 1</span>. При плановой замене плитки выяснилось, что новой плитки недостаточно для покрытия всей площади, поэтому было решено покрыть
            плиткой только дорожку по краю площади, а в центре площади разбить прямоугольную клумбу (см. рисунок к примеру). При этом
            дорожка должна иметь одинаковую ширину по всем сторонам площади. Определите максимальную ширину дорожки, которую можно выложить
            из имеющихся плиток.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая и вторая строки входных данных содержат по одному числу <span class="tex-math-text">n</span> и <span class="tex-math-text">m</span> (<span class="tex-math-text">3&le; n &le; 2&times; 10<sup>9</sup></span>, <span class="tex-math-text">3&le; m &le; 2&times; 10<sup>9</sup></span>)&nbsp;&mdash; размеры площади.
         </p></span><p>Третья строка содержит количество имеющихся плиток <span class="tex-math-text">t</span>, <span class="tex-math-text">1&le; t&lt; nm</span>.
      </p>
      <p><span style="font-weight:bold;">Обратите внимание, что значение <span class="tex-math-text">t</span> может быть больше, чем возможное значение 32-битной целочисленной переменной, поэтому необходимо использовать 64-битные числа
            (тип int64 в языке Pascal, тип long long в C и C++, тип long в Java и C#).</span>
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Программа должна вывести единственное число&nbsp;&mdash; максимальную ширину дорожки, которую можно выложить из имеющихся плиток.</p></span><p> </p>
   </div>
