<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Приближенный двоичный поиск</h1>
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
         <p>Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.</p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входных данных содержатся числа N и K $(0 < N, K \leq 100 000)$. Во второй строке задаются <span class="tex-math-text">N</span> чисел первого массива, отсортированного по неубыванию, а в третьей строке – <span class="tex-math-text">K</span> чисел второго массива. Каждое число в обоих массивах по модулю не превосходит <span class="tex-math-text">2&#x22C5;10<sup>9</sup></span>.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого из <span class="tex-math-text">K</span> чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. Если таких несколько, выведите меньшее
            из них.
         </p>
         <p></p></span></div>
