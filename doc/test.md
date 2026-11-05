# tested with Python 3.14

|            SUBJECT |                     CASE                   |           EXPECTATION          |           TEST DATA           | RESULT |
|-------------------:|:-------------------------------------------|:-------------------------------|:------------------------------|:-------|
|      matrix_object | created from bytes and then converted back | bytes matching                 | "empty" bitmap image data     | ok     |
|      matrix_object | set dimensions in constructor              | correct matrix dimensions      | w = 1, h = 1                  | ok     |
|               rect | pokéball generation                        | no new colored cells           | pokéball generation           | ok     |
|             circle | pokéball generation                        | correct shape                  | python main.py                | ok     |
|      bitmap_object | is generated with privided options         | correct conversion to bytes    | python main.py                | ok     |
| pokéball_generator | pokerush is not activated                  | single pokéball                | python main.py                | ok     |
| pokéball_generator | pokerush is activated                      | random pokéballs               | python main.py a pokerush     | ok     |
|               meta | program initialisation                     | parses correct data            | python main.py                | ok     |
|            options | program initialisation                     | defaults are set correctly     | python main.py                | ok     |
|            options | provided file exists and is not a bitmap   | exception raised               | python main.py                | ok     |
|            options | user provides -w or -h lesser than 20      | exception raised               | python main.py -w -1          | ok     |
|          backupper | the file exists                            | backs up data                  | python main.py (zweimal)      | ok     |
|          backupper | the backup exists                          | overwrites old backup          | python main.py (dreimal)      | ok     |
|               main | no arguments                               | uses default name for new file | python main.py                | ok     |
|               main | user defines -x and -y as 0, 0             | pokéball is at the top-left    | python main.py -x 0 -y 0      | ok     |
|               main | user defines -x and -y same as -w and -h   | pokéball is at the botom-right | python main.py -x 20 -y 20    | ok     |
|               main | pokéball generated over an existing bitmap | original image is preserved    | python main.py jolteon        | ok     |
|               main | user sets -w and -h when overwriting file  | the arguments are ignored      | python main.py jolteon -w 200 | ok     |
