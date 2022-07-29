<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Клавиатура</h1>
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
         <p>На региональном этапе Всероссийской олимпиады школьников по информатике в 2009 году предлагалась следующая задача. </p></span><p>Всем известно, что со временем клавиатура изнашивается,и клавиши на ней начинают залипать. Конечно, некоторое время такую
         клавиатуру еще можно использовать, но для нажатий клавиш приходиться использовать большую силу.
      </p>
      <p>При изготовлении клавиатуры изначально для каждой клавиши задается количество нажатий,которое она должна выдерживать. Если
         знать эти величины для используемой клавиатуры,то для определенной последовательности нажатых клавиш можно определить,какие
         клавиши в процессе их использования сломаются, а какие — нет.
      </p>      
      <p>Требуется написать программу, определяющую, какие клавиши сломаются в процессе заданного варианта эксплуатации клавиатуры.
      </p>
      <p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входных данных содержит целое число <span class="tex-math-text">n</span> (<span class="tex-math-text">1 &le; n &le; 1000</span>) —количество клавиш на клавиатуре. Вторая строка содержит <span class="tex-math-text">n</span> целых чисел —<span class="tex-math-text">с<sub>1</sub></span>, <span class="tex-math-text">с<sub>2</sub></span>, … , <span class="tex-math-text">с<sub>n</sub></span>, где <span class="tex-math-text">с<sub>i</sub></span> (<span class="tex-math-text">1 &le; c<sub>i</sub> &le; 100000</span>) — количество нажатий,выдерживаемых <span class="tex-math-text">i</span>-ой клавишей. Третья строка содержит целое число <span class="tex-math-text">k</span> (<span class="tex-math-text">1 &le; k &le; 100000</span>) — общее количество нажатий клавиш, и последняя строка содержит <span class="tex-math-text">k</span> целых чисел <span class="tex-math-text">p<sub>j</sub></span> (<span class="tex-math-text">1 &le; p<sub>j</sub> &le; n</span>) — последовательность нажатых клавиш.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Программа должна вывести n строк, содержащих информацию об исправности клавиш.Если <span class="tex-math-text">i</span>-я клавиша сломалась, то <span class="tex-math-text">i</span>-ая строка должна содержать слово YES,если же клавиша работоспособна — слово NO.
         </p></span><p></p>
   </div>
