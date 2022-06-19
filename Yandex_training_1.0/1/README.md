### E. Скорая помощь
|                     |                                  |
|:--------------------|:---------------------------------|
| Ограничение времени | 1 секунда                        |
| Ограничение памяти  | 64Mb                             |
| Ввод                | стандартный ввод или input.txt   |
| Вывод               | стандартный вывод или output.txt |



<p>Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению, когда диспетчер получил вызов, он успел записать только адрес дома и номер квартиры <span class="tex-math-text">K<sub>1</sub></span>, а затем связь прервалась. Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала в квартиру <span class="tex-math-text">K<sub>2</sub></span>, которая расположена в подъезда <span class="tex-math-text">P<sub>2</sub></span> на этаже <span class="tex-math-text">N<sub>2</sub></span>. Известно, что в доме <span class="tex-math-text">M</span> этажей и количество квартир на каждой лестничной площадке одинаково. Напишите программу, которая вычилсяет номер подъезда   <span class="tex-math-text">P<sub>1</sub></span> и номер этажа <span class="tex-math-text">N<sub>1</sub></span> квартиры <span class="tex-math-text">K<sub>1</sub></span>.</p>

## Формат ввода

<p>Во входном файле записаны пять положительных целых чисел <span class="tex-math-text">K<sub>1</sub></span>, <span class="tex-math-text">M</span>, <span class="tex-math-text">K<sub>2</sub></span>, <span class="tex-math-text">P<sub>2</sub></span>, <span class="tex-math-text">N<sub>2</sub></span>. Все числа не превосходят <span class="tex-math-text">10<sup>6</sup></span>.</p>

## Формат вывода

<p>Выведите два числа <span class="tex-math-text">P<sub>1</sub></span> и <span class="tex-math-text">N<sub>1</sub></span>. Если входные данные не позволяют однозначно определить <span class="tex-math-text">P<sub>1</sub></span> или <span class="tex-math-text">N<sub>1</sub></span>, вместо соответствующего числа напечатайте <span class="tex-math-text">0</span>. Если входные данные противоречивы, напечатайте два числа <span class="tex-math-text">–1</span> (минус один).
         </p>

### Пример 1

| Ввод          | Вывод |
|:--------------|:------|
| 89 20 41 1 11 | 2 3   |

### Пример 2

| Ввод       | Вывод |
|:-----------|:------|
| 11 1 1 1 1 | 0 1   |

### Пример 3
| Ввод      | Вывод |
|:----------|:------|
| 3 2 2 2 1 | -1 -1 |
