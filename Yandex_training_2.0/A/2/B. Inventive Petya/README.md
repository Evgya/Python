<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Изобретательный Петя</h1>
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
         <p>Петя нашел на чердаке старый телеграфный аппарат и приделал к нему хитроумное устройство, которое может печатать на телеграфной
            ленте определенное слово (обозначим его X). Петино устройство может напечатать на ленте это слово сколько угодно раз. Петя
            может заставить аппарат напечатать на ленте и любое другое сообщение, но для этого ему нужно разобрать свое хитроумное устройство,
            и после этого он уже не сможет печатать сообщение X. А самое главное, что напечатать даже один символ другого сообщения потребует
            от Пети больше усилий, чем напечатать на ленте слово X с помощью хитроумного устройства.
         </p></span><p>Петя хочет сделать так, чтобы всем казалось, что ему по телеграфу пришло сообщение Z. Для этого он может (строго в этой последовательности):</p>
      <p>- сколько угодно раз напечатать сообщение X</p>
      <p>- разобрать хитроумное устройство и посимвольно напечатать еще что-нибудь (назовем это Y)</p>
      <p>- оторвать и выбросить начало ленты так, чтобы на оставшейся ленте было напечатано в точности сообщение Z</p>
      <p>Поскольку набирать отдельные символы сообщения Y довольно сложно, Петя хочет, чтобы в сообщении Y было как можно меньше символов.</p>      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке вводится слово X, которое Петя может печатать с помощью хитроумного устройства сколько угодно раз. Во второй
            строке вводится сообщение Z, которое хочет получить Петя. Каждое сообщение состоит только из маленьких латинских букв и имеет
            длину не более 100 символов.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите минимальное по длине сообщение Y, которое Пете придется допечатать вручную.</p></span><p></p>
   </div>