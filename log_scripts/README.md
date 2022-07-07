# Описание работы скриптов
## Bash скрипты
### Запуск скриптов
Перед запуском скрипта необходимо ввести в терминал следующую команду:
```
chmod +rx *scriptname*
```
Для запуска скрипта необходимо использовать команду
```
./*scriptname* *logfile*
```
`scriptname`-имя скрипта.
`logfile`-файл с логами.
### Формат вывода
`all_req.sh` выводит данные в файл `all_req_out.txt` в формате:
```
Total number of requests
total_number_of_requests
```
___
`all_req_by_type.sh` выводит данные в файл `all_req_by_type_out.txt` в формате:
```
Total number of requests by type
request_type - request_type_number
...
```
___
`frequent_req.sh` выводит данные в файл `frequent_req_out.txt` в формате:
```
Top 10 most frequent searches
requests_number_for_url url
...
```
___
`largest_req.sh` выводит данные в файл `largest_req_out.txt` в формате:
```
Top 5 largest requests that failed with client error
ip_address url status_code request_size
...
```
___
`users_num_req.sh` выводит данные в файл `users_num_req_out.txt` в формате:
```
Top 5 users by the number of requests that ended with a server error
number_of_requests ip_address
...
```
## Python скрипты
### Запуск скриптов
Для запуска скрипта необходимо использовать команду
```
python3 scriptname logfile [--json]
```
`logfile`-файл с логами, если есть флаг `--json` вывод будет в JSON формате.
###Формат вывода
`all_req.py` выводит данные в файл `all_req_out.txt` в формате:
```
Total number of requests
total_number_of_requests
```
___
`all_req_by_type.py` выводит данные в файл `all_req_by_type_out.txt` в формате:
```
Total number of requests by type
request_type - request_type_number
...
```
___
`frequent_req.py` выводит данные в файл `frequent_req_out.txt` в формате:
```
Top 10 most frequent searches
requests_number_for_url url
...
```
___
`largest_req.py` выводит данные в файл `largest_req_out.txt` в формате:
```
Top 5 largest requests that failed with client error
ip_address url status_code request_size
...
```
___
`users_num_req.py` выводит данные в файл `users_num_req_out.txt` в формате:
```
Top 5 users by the number of requests that ended with a server error
number_of_requests ip_address
...
```
# Минусы и плюсы решения на Bash и на Python
* Плюсы написания скриптов на Bash.
    * Небольшой объём кода.
    * Работает без установки дополнительного ПО.
* Минусы написания на Bash.
    * Сложно читаемый код.
* Плюсы написания на Python.
    * Легко читаемый код.
    * Больше контроля над программой.
* Минусы написания на Python.
    * Больше по объёму кода.