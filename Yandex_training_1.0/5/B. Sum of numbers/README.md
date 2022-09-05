<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Сумма номеров</h1>
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
   <div class="legend"> Вася очень любит везде искать своё счастливое число $\mathbf{K}$
      Каждый день он ходит в школу по улице, вдоль которой припарковано $\mathbf{N}$ машин. Он заинтересовался вопросом, сколько существует наборов машин, стоящих подряд на местах с $\mathbf{L}$ до $\mathbf{R}$, что сумма их номеров равна $\mathbf{K}$.
      Помогите Васе узнать ответ на его вопрос.
      Например, если число $\mathbf{N = 5, K = 17}$, а номера машин равны 17, 7, 10, 7, 10, то существует 4 набора машин:
      <p>$17 \mathbf{(L=1, R=1)}$</p>
      <p>$7, 10 \mathbf{(L=2, R=3)}$</p>
      <p>$10, 7 \mathbf{(L=3, R=4)}$</p>
      <p>$7, 10 \mathbf{(L=4, R=5)}$</p>

   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке входных данных задаются числа $\mathbf{N}$ и $\mathbf{K (1 \leq \mathbf{N} \leq 100 000, 1 \leq K \leq 10^9).$    
      Во второй строке содержится $\mathbf{N}$ чисел, задающих номера машин. Номера машин могут принимать значения от $\mathbf{1}$ до $\mathbf{999}$ включительно.

   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Необходимо вывести одно число &nbsp;— количество наборов. </div>
