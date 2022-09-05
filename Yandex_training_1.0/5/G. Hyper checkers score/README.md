<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Счет в гипершашках</h1>
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
         <p>Андрей работает судьей на чемпионате по гипершашкам. В каждой игре в гипершашки участвует три игрока. По ходу игры каждый
            из игроков набирает некоторое положительное целое число баллов. Если после окончания игры первый игрок набрал a баллов, второй
            — b, а третий c, то говорят, что игра закончилась со счетом a:b:c.
         </p></span><p>Андрей знает, что правила игры гипершашек устроены таким образом, что в результате игры баллы любых двух игроков различаются
         не более чем в k раз.
      </p>
      <p>После матча Андрей показывает его результат, размещая три карточки с очками игроков на специальном табло. Для этого у него
         есть набор из n карточек, на которых написаны числа <span class="tex-math-text">x<sub>1</sub></span>, <span class="tex-math-text">x<sub>2</sub></span>, …, <span class="tex-math-text">x<sub>n</sub></span>. Чтобы выяснить, насколько он готов к чемпионату, Андрей хочет понять, сколько различных вариантов счета он сможет показать
         на табло, используя имеющиеся карточки.
      </p>
      <p>Требуется написать программу, которая по числу k и значениям чисел на карточках, которые имеются у Андрея, определяет количество
         различных вариантов счета, которые Андрей может показать на табло.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входного файла содержит два целых числа: n и k (<span class="tex-math-text">3 &le; n &le; 100000, 1 &le; k &le; 10<sup>9</sup></span>).
         </p></span><p>Вторая строка входного файла содержит n целых чисел <span class="tex-math-text">x<sub>1</sub></span>, <span class="tex-math-text">x<sub>2</sub></span>, …, <span class="tex-math-text">x<sub>n</sub></span> (<span class="tex-math-text">1 &le; x<sub>i</sub> &le; 10<sup>9</sup></span>).
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выходной файл должен содержать одно целое число — искомое количество различных вариантов счета.</p></span><p></p>
   </div>
