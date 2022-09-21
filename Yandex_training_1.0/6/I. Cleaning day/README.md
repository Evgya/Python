<div class="problem-statement">
   <div class="header">
      <h1 class="title">I. Субботник</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
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
         <p>В классе учатся N человек. Классный руководитель получил указание направить на субботник R бригад по С человек в каждой.</p></span><p>Все бригады на субботнике будут заниматься переноской бревен. Каждое бревно одновременно несут все члены одной бригады. При
         этом бревно нести тем удобнее, чем менее различается рост членов этой бригады.
      </p>
      <p>Числом неудобства бригады будем называть разность между ростом самого высокого и ростом самого низкого членов этой бригады
         (если в бригаде только один человек, то эта разница равна 0). Классный руководитель решил сформировать бригады так, чтобы
         максимальное из чисел неудобства сформированных бригад было минимально. Помогите ему в этом!
      </p>
      <p>Рассмотрим следующий пример. Пусть в классе 8 человек, рост которых в сантиметрах равен 170, 205, 225, 190, 260, 130, 225,
         160, и необходимо сформировать две бригады по три человека в каждой. Тогда одним из вариантов является такой:
      </p>
      <p>1 бригада: люди с ростом 225, 205, 225</p>
      <p>2 бригада: люди с ростом 160, 190, 170</p>
      <p>При этом число неудобства первой бригады будет равно 20, а число неудобства второй — 30. Максимальное из чисел неудобств будет
         30, и это будет наилучший возможный результат.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводятся натуральные числа N, R и C — количество человек в классе, количество бригад и количество человек в каждой
            бригаде (1 ≤ R∙C ≤ N ≤ 100 000). Далее вводятся N целых чисел — рост каждого из N учеников. Рост ученика — натуральное число,
            не превышающее 1 000 000 000.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно число — наименьше возможное значение максимального числа неудобства сформированных бригад.</p></span><p></p>
   </div>