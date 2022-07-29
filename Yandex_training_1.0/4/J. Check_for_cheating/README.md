<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. Дополнительная проверка на списывание</h1>
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
         <p>Преподаватель курса ОиМП заказал у одного известного психолога полное психологическое обследование всех студентов, поступивших
            на ФНК с целью выяснить их склонность к списыванию еще до начала занятий и отчислить их за списывание еще до того как они
            приступят к занятиям и смогут позорить ФНК своими преступлениями. Психолог, привлеченный для проведения обследования, известен
            своим инновационным методом, позволяющим понять склонность к списыванию студента по наиболее часто используемому им в программах
            идентификатору. Помогите известному психологу определить, какие из студентов потенциально являются преступниками. Напишите
            программу, которая по приведенной программе выяснит наиболее часто используемый в ней идентификатор.
         </p></span><p>Поскольку разные студенты на тестировании пишут программы на разных языках программирования, ваша программа должна уметь работать
         с произвольным языком. Поскольку в разных языках используются различные ключевые слова, то список ключевых слов в анализируемом
         языке предоставляется на вход программе. Все последовательности из латинских букв, цифр и знаков подчеркивания, которые не
         являются ключевыми словами и содержат хотя бы один символ, не являющийся цифрой, могут быть идентификаторами. При этом в некоторых
         языках идентификаторы могут начинаться с цифры, а в некоторых - нет. Если идентификатор не может начинаться с цифры, то последовательность,
         начинающаяся с цифры, идентификатором не является. Кроме этого, задано, является ли язык чувствительным к регистру символов,
         используемых в идентификаторах и ключевых словах.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке вводятся число n - количество ключевых слов в языке (0 &lt;= n &lt;= 50) и два слова C и D, каждое из которых равно
            либо "yes", либо "no". Слово C равно "yes", если идентификаторы и ключевые слова в языке чувствительны к регистру символов,
            и "no", если нет. Слово D равно "yes", если идентификаторы в языке могут начинаться с цифры, и "no", если нет.
         </p></span><p>Следующие n строк содержат по одному слову, состоящему из букв латинского алфавита и символов подчеркивания - ключевые слова.
         Все ключевые слова непусты, различны, при этом, если язык не чувствителен к регистру, то различны и без учета регистра. Длина
         каждого ключевого слова не превышает 50 символов.</p>
      <p>Далее до конца входных данных идет текст программы. Он содержит только символы с ASCII-кодами от 32 до 126 и переводы строки.
      </p>
      <p>Размер входных данных не превышает 10 килобайт. В программе есть хотя бы один идентификатор.</p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите идентификатор, встречающийся в программе максимальное число раз. Если таких идентификаторов несколько, следует вывести
            тот, который встречается в первый раз раньше. Если язык во входных данных не чувствителен к регистру, то можно выводить идентификатор
            в любом регистре.
         </p></span><p></p>
   </div>