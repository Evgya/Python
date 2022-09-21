<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Наблюдение за студентами</h1>
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
         <p>На первом курсе одной Школы, учится <span class="tex-math-text">1 &le; N &le; 10<sup>9</sup></span> студентов. При проведении экзаменов студентов рассаживают в ряд, каждого за своей партой. Парты пронумерованы числами от
            <span class="tex-math-text">0</span> до <span class="tex-math-text">N - 1</span>.
         </p></span><p>Известно, что студент, оставшись без наблюдения, открывает телефон и начинает искать ответы на экзамен в поисковике Яндекса.</p>
      <p>Поэтому было решено позвать <span class="tex-math-text">M</span> преподавателей наблюдать за студентами. Когда за студентом наблюдает хотя бы один преподаватель, он стесняется и не идет
         искать ответы к экзамену. Преподаватель с номером <span class="tex-math-text">i</span> видит студентов сидящих за партами от <span class="tex-math-text">b<sub>i</sub></span> до <span class="tex-math-text">e<sub>i</sub></span> включительно.
      </p>
      <p>Необходимо посчитать количество студентов, которые все таки будут искать ответы к экзамену в Яндексе</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке находятся два целых числа <span class="tex-math-text">1 &le; N &le; 10<sup>9</sup></span>, <span class="tex-math-text">1 &le; M &le; 10<sup>4</sup></span>&nbsp;&mdash; число студентов и число преподавателей соответственно. В следующих <span class="tex-math-text">M</span> строках содержится по два целых числа <span class="tex-math-text">0 &le; b<sub>i</sub> &le; e<sub>i</sub> &le; N - 1</span>&nbsp;&mdash; парты, за которыми наблюдает <span class="tex-math-text">i</span>-й преподаватель.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно число&nbsp;&mdash; количество студентов оставшихся без наблюдения.</p></span></div>
