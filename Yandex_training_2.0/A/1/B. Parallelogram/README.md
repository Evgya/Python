<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Параллелограмм</h1>
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
         <p>На уроке геометрии семиклассники Вася и Петя узнали, что такое параллелограмм. На перемене после урока они стали играть в
            игру: Петя называл координаты четырех точек в произвольном порядке, а Вася должен был ответить, являются ли эти точки вершинами
            параллелограмма.
         </p></span><p>Вася, если честно, не очень понял тему про параллелограммы, и ему требуется программа, умеющая правильно отвечать на Петины
         вопросы.
      </p>
      <p>Напомним, что параллелограммом называется четырехугольник, противоположные стороны которого равны и параллельны.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла записано целое число N (<span class="tex-math-text">1 &le; N &le; 10</span>) - количество заданных Петей вопросов. Каждая из N последующих строк содержит описание четырех точек - четыре пары целых
            чисел X и Y (<span class="tex-math-text">−100 &le; X &le; 100</span>, <span class="tex-math-text">−100 &le; Y &le; 100</span>), обозначающих координаты точки. Гарантируется, что четыре точки, о которых идет речь в одном вопросе, не лежат на одной
            прямой.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого из вопросов выведите "YES", если четыре заданные точки могут образовать параллелограмм, и "NO" в противном случае.
            Ответ на каждый из запросов должен быть в отдельной строке без кавычек.
         </p></span></div>
