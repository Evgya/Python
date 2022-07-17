<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Газон</h1>
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
         <p>Фермер Иван с юности следит за своим газоном. Газон можно считать плоскостью, на которой в каждой точке с целыми координатами
            растет один пучок травы.
         </p></span><p>В одно из воскресений Иван воспользовался газонокосилкой и постриг некоторый прямоугольный участок газона. Стороны этого участка
         параллельны осям координат, а две противоположные вершины расположены в точках (<span class="tex-math-text">x<sub>1</sub></span>, <span class="tex-math-text">y<sub>1</sub></span>) и (<span class="tex-math-text">x<sub>2</sub></span>, <span class="tex-math-text">y<sub>2</sub></span>). Следует отметить, что пучки травы, находящиеся на границе этого прямоугольника, также были пострижены.
      </p>
      <p>Довольный результатом Иван купил и установил на газоне дождевальную установку. Она была размещена в точке с координатами (<span class="tex-math-text">x<sub>3</sub></span>, <span class="tex-math-text">y<sub>3</sub></span>) и имела радиус действия струи r. Таким образом, установка начала поливать все пучки, расстояние от которых до точки (<span class="tex-math-text">x<sub>3</sub></span>, <span class="tex-math-text">y<sub>3</sub></span>) не превышало r.
      </p>
      <p>Все было хорошо, но Ивана заинтересовал следующий вопрос: сколько пучков травы оказалось и пострижено, и полито в это воскресенье?</p>
      <p>Требуется написать программу, которая позволит дать ответ на вопрос Ивана.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла содержатся четыре целых числа <span class="tex-math-text">x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub></span> (−100 000 ≤ <span class="tex-math-text">x<sub>1</sub> &lt; x<sub>2</sub></span> ≤ 100 000; −100 000 ≤ <span class="tex-math-text">y<sub>1</sub> &lt; y<sub>2</sub></span> ≤ 100 000).
         </p></span><p>Во второй строке входного файла содержатся три целых числа <span class="tex-math-text">x<sub>3</sub>, y<sub>3</sub></span>, r (−100 000 ≤ <span class="tex-math-text">x<sub>3</sub>, y<sub>3</sub></span> ≤ 100 000; 1 ≤ r ≤ 100 000)
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В выходной файл необходимо вывести одно целое число — число пучков травы, которые были и пострижены, и политы.</p></span><p></p>
   </div>
