<div class="header">
     <h1 class="title">C. Телефонные номера</h1>
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
        <p>Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов: +7&lt;код&gt;&lt;номер&gt;, 8&lt;код&gt;&lt;номер&gt;, &lt;номер&gt;,
           где &lt;номер&gt;&nbsp;— это семь цифр, а &lt;код&gt;&nbsp;— это три цифры или три цифры в круглых скобках. Если код не указан, то считается, что
           он равен 495. Кроме того, в записи телефонного номера может стоять знак “-” между любыми двумя цифрами (см. пример). На данный
           момент в адресной книге телефона Васи записано всего три телефонных номера, и он хочет записать туда еще один. Но он не может
           понять, не записан ли уже такой номер в телефонной книге. Помогите ему! Два телефонных номера совпадают, если у них равны
           коды и равны номера. Например, +7(916)0123456 и 89160123456&nbsp;— это один и тот же номер.
        </p></span></div>
  <h2>Формат ввода</h2>
  <div class="input-specification"><span style="">
        <p>В первой строке входных данных записан номер телефона, который Вася хочет добавить в адресную книгу своего телефона. В следующих
           трех строках записаны три номера телефонов, которые уже находятся в адресной книге телефона Васи. Гарантируется, что каждая
           из записей соответствует одному из трех приведенных в условии форматов.
        </p></span></div>
  <h2>Формат вывода</h2>
  <div class="output-specification"><span style="">
        <p>Для каждого телефонного номера в адресной книге выведите YES (заглавными буквами), если он совпадает с тем телефонным номером,
           который Вася хочет добавить в адресную книгу или NO (заглавными буквами) в противном случае.
        </p></span></div>