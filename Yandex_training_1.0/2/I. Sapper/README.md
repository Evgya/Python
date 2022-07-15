<div class="problem-statement">
   <div class="header">
      <h1 class="title">I. Сапер</h1>
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
         <p>Вам необходимо построить поле для игры "Сапер" по его конфигурации &ndash; размерам и координатам расставленных на нем мин.</p></span><p>Вкратце напомним правила построения поля для игры "Сапер":
         <ul>
            <li>Поле состоит из клеток с минами и пустых клеток </li>
            <li>Клетки с миной обозначаются символом <span style="font-weight:bold;">*</span>
            </li>
            <li>Пустые клетки содержат число <span class="tex-math-text">k<sub>i,j</sub>, 0&le; k<sub>i, j</sub> &le; 8</span> &ndash; количество мин на соседних клетках. <span style="font-style:italic;">Соседними клетками являются восемь клеток, имеющих смежный угол или сторону.</span>
            </li>
         </ul>
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке содержатся три числа: <span class="tex-math-text">N, 1 &le; N &le; 100</span> - количество строк на поле, <span class="tex-math-text">M, 1 &le; M &le; 100</span> - количество столбцов на поле, <span class="tex-math-text">K, 0 &le; K &le; N &#x22C5; M</span> - количество мин на поле.<br></p></span><p>В следующих <span class="tex-math-text">K</span> строках содержатся по два числа с координатами мин: <span class="tex-math-text">p, 1 &le; p &le; N</span> - номер строки мины, <span class="tex-math-text">q, 1 &le; 1 &le; M</span> - номер столбца мины.
      </p>
      <p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите построенное поле, разделяя строки поля переводом строки, а столбцы - пробелом.</p></span></div>
