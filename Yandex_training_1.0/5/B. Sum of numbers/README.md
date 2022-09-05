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
   <div class="legend"> Вася очень любит везде искать своё счастливое число $\boldmath{K}$
      Каждый день он ходит в школу по улице, вдоль которой припарковано $\mathbold{N}$ машин. Он заинтересовался вопросом, сколько существует наборов машин, стоящих подряд на местах с $\mathbold{L}$ до $\mathbold{R}$, что сумма их номеров равна $\mathbold{K}$.
      Помогите Васе узнать ответ на его вопрос.
      Например, если число $\mathbold{ N = 5, K = 17}$, а номера машин равны 17, 7, 10, 7, 10, то существует 4 набора машин:
      <p>$17 (L=1, R=1)$</p>
      <p>$7, 10 (L=2, R=3)$</p>
      <p>$10, 7 (L=3, R=4)$</p>
      <p>$7, 10 (L=4, R=5)$</p>

   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке входных данных задаются числа $\mathbf{N}$ и $\mathbf{K}$ $1 \leq \mathbf{N} \leq \mathbf{100 000}$
      и <!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math>
      (<!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>N</mi> <mo>≤</mo> <mn>1</mn><mn>0</mn><mn>0</mn><mspace width="0.3em"><mn>0</mn><mn>0</mn><mn>0</mn></mspace></math>,
      <!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>K</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>). <!--l. 62-->
      <p style="text-indent: 0em;">Во второй строке содержится <!--l. 62--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
      чисел, задающих номера машин. Номера машин могут принимать значения от <!--l. 62--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> до <!--l. 62--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mn>9</mn><mn>9</mn></math> включительно. </p>

   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Необходимо вывести одно число&nbsp;— количество наборов. </div>
