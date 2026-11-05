|             MODULE |                     CASE                   |        EXPECTATION        |         TEST DATA         | LATEST TEST | RESULT |
|-------------------:|:-------------------------------------------|:-------------------------:|:--------------------------|:-----------:|:-------|
|      matrix_object | created from bytes and then converted back | bytes matching            | "empty" bitmap image data |             | ok     |
|      matrix_object | set dimensions in constructor              | correct matrix dimensions | w = 1, h = 1              |             | ok     |
|               rect | shadows correctly                          |                           | pokéball generation       |             | ok     |
|             circle | pokéball generation                        | correct shape             |             | ok     |
|      bitmap_object | correct conversion                         |                           |                           |             | ok     |
| pokéball_generator | single pokéball                            |                           |                           |             | ok     |
| pokéball_generator | pokerush                                   |                           |                           |             | ok     |
|               meta | parses data                                |                           |                           |             | ok     |
|            options | correct defaults                           |                           |                           |             | ok     |
|            options | negative arguments                         |                           |                           |             | ok     |
|          backupper | backs up data                              |                           |                           |             | ok     |
|          backupper | overwrites old backup                      |                           |                           |             | ok     |
|               main | no arguments                               |                           |                           |             | ok     |
|               main | image cropping                             |                           |                           |             | ok     |
|               main | pokéball top-left                          |                           |                           |             | ok     |
|               main | pokéball bot-right                         |                           |                           |             | ok     |
