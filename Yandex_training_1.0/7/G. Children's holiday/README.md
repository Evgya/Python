<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Детский праздник</h1>
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
         <p>Организаторы детского праздника планируют надуть для него M воздушных шариков. С этой целью они пригласили N добровольных
            помощников, i-й среди которых надувает шарик за <span class="tex-math-text">T<sub>i</sub></span> минут, однако каждый раз после надувания <span class="tex-math-text">Z<sub>i</sub></span> шариков устает и отдыхает <span class="tex-math-text">Y<sub>i</sub></span> минут. Теперь организаторы праздника хотят узнать, через какое время будут надуты все шарики при наиболее оптимальной работе
            помощников, и сколько шариков надует каждый из них. (Если помощник надул шарик, и должен отдохнуть, но больше шариков ему
            надувать не придется, то считается, что он закончил работу сразу после окончания надувания последнего шарика, а не после отдыха).
         </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входных данных задаются числа M и N (0 ≤ M ≤ 15000, 1 ≤ N ≤ 1000). Следующие N строк содержат по три целых
            числа - <span class="tex-math-text">T<sub>i</sub></span>, <span class="tex-math-text">Z<sub>i</sub></span> и <span class="tex-math-text">Y<sub>i</sub></span> соответственно (1 ≤ <span class="tex-math-text">T<sub>i</sub></span>, <span class="tex-math-text">Y<sub>i</sub></span> ≤ 100, 1 ≤ <span class="tex-math-text">Z<sub>i</sub></span> ≤ 1000).
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите в первой строке число T - время, за которое будут надуты все шарики. Во второй строке выведите N чисел - количество
            шариков, надутых каждым из приглашенных помощников. Разделяйте числа пробелами. Если распределений шариков несколько, выведите
            любое из них.
         </p></span><p></p>
   </div>
