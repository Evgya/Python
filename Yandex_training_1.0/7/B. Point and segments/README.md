<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Точки и отрезки</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>3&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
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
         <p>Дано n отрезков на числовой прямой и m точек на этой же прямой. Для каждой из данных точек определите, скольким отрезкам они
            принадлежат. Точка x считается принадлежащей отрезку с концами a и b, если выполняется двойное неравенство min(a, b) ≤ x ≤
            max(a, b).
         </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка содержит два целых числа n (1 ≤ n ≤ <span class="tex-math-text">10<sup>5</sup></span>) – число отрезков и m (1 ≤ m ≤ <span class="tex-math-text">10<sup>5</sup></span>) – число точек. В следующих n строках по два целых числи <span class="tex-math-text">a<sub>i</sub></span> и <span class="tex-math-text">b<sub>i</sub></span> – координаты концов соответствующего отрезка. В последней строке m целых чисел – координаты точек. Все числа по модулю не
            превосходят <span class="tex-math-text">10<sup>9</sup></span></p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В выходной файл выведите m чисел – для каждой точки количество отрезков, в которых она содержится.</p></span><p></p>
   </div>
