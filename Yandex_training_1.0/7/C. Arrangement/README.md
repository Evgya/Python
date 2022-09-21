<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Рассадка в аудитории</h1>
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
         <p>Экзамен по берляндскому языку проходит в узкой и длинной аудитории. На экзамен пришло N студентов. Все они посажены в ряд.
            Таким образом, позиция каждого человека задается координатой на оси Ox (эта ось ведет вдоль длинной аудитории). Два человека
            могут разговаривать, если расстояние между ними меньше или равно D. Какое наименьшее количество типов билетов должен подготовить
            преподаватель, чтобы никакие два студента с одинаковыми билетами не могли разговаривать? Выведите способ раздачи преподавателем
            билетов.
         </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла содержится два целых числа N, D (1 ≤ N ≤ 10000; 0 ≤ D ≤ <span class="tex-math-text">10<sup>6</sup></span>). Вторая строка содержит последовательность различных целых чисел <span class="tex-math-text">X<sub>1</sub></span>, <span class="tex-math-text">X<sub>2</sub></span>, ..., <span class="tex-math-text">X<sub>N</sub></span>, где <span class="tex-math-text">X<sub>i</sub></span> (0 ≤ <span class="tex-math-text">X<sub>i</sub></span> ≤ <span class="tex-math-text">10<sup>6</sup></span>) обозначает координату вдоль оси Ox i-го студента
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В первую строчку выходного файла выведите количество вариантов, а во вторую, разделяя пробелами, номера вариантов студентов
            в том порядке, в каком они перечислены во входном файле.
         </p></span><p></p>
   </div>
