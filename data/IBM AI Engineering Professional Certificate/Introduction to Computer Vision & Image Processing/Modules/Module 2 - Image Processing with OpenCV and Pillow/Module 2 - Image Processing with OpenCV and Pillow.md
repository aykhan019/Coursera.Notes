

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AL23UNW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHCbTeJMJZPxjNBQQXe%2BXI1G%2FfGZx4KVLhCDywx40EWqAiBC4hnnk4v4avvo8e4HhTvl5vVSohBQQ6ltE40cu5TmZir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUO3roC%2BUFDZ8IOdkKtwDYyLWde5n9AJn9xiv0TnO%2BZo80m3l7UC7KIq%2FAExFEdEw72MO0JUfypwer2i2o2VPb5gf4nFVuTk4qnCAZzh7XM8AGwwhs%2FrGPekBubk6Q%2FL9YZfKjitWRpAh7Y4hji20Z0C%2BObtlF9d9xrBU0mD%2FU4p%2Fgdit2ff7hXbL0uQXG55RhGNnWMLirXq1u0dG0e4wrWM0M9NsddoAQVepyIOoGSHta6ow0O4ghCjW4tGs4Alln8Guk4w8ZQfXkSXMCq4eECe5G7qj7TjQxz2BEFvfNJgOf0B1shjTQ5KLtqtqvumQ8f5Gc%2FK%2BALKrmQ%2BAHnQ99PbYzV7lMWWrrymCHKaXA%2FNVuFhw1vheQo%2BVQBzUJ4FLdE5aP%2FtqCmjbmwv8jM59TgSuzvnOe2IjsfJGj5ukxOItEQlIBY6vZV%2FF7hUUdmOz8e8SGZlVYLBHmzrKH1csxDm2%2FuSqthui1dT3jMJ3CS2rNULJSWDDUkQN9ME4FYExUkOoTVJ4%2Bx2IUo4hFG%2BYyMc3qI%2FCGRtXh6aghDw6yCcChutJPoZL3ctUU7Qk%2F1tL9ewBf3DuG8L%2FqYdKW3Ha3xfCSPIjMiug%2BxZFkpxqYP4e62qd5%2F3v%2BjajsBY6NdLzpZLMLlNolzGc%2BScwzr6GvQY6pgHPieCXOXngJTIZTTzZTQhdo4SqdFQNgTdZ8EWJG2yaCXBnmHmpMil6%2FltxuyKmmF4KsNSNHMN51oJ4N6GcO273Yob73hmJ9k50nZEAXu3MshSIg%2F5RUPA3B6nhkCoTqJ00Ad9lIKMCSqi9adCkSKAbfJhWr%2BaQ9EpCkBVbykxAJWItKLsLp9EeFhkTCFj9VSKuX3HoWCBMvcS%2BJ%2Bg%2BaOCzafCk6BL3&X-Amz-Signature=89f1aedb5317cbc113a726cd050048960cda61cf8a84082a8a5e45596997570e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTRPF2F7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICgLaBlO360fn79nYca8Z022KsgjYVCgqb8Db0p74RmNAiEA9plv1kLSiIAmpdBSlstmeBW6pmnezruWcw4XstI7HRkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGnDTiSSTYEnJ4Cx3CrcA0%2F5MZncVqs6l3zaAtMaC81hEOyfKpaK8EOixRMuiQaZW7vvwprRUqLj3CeRrwOLoDOvRSmNxMBMCE%2FhW4s8SNd84uVTWnLFh9sLXUikaM9xVcBWew5vGC3xj%2BDZnMcSGnn1De2kS0VweH4YL4EVGDI7kop3zcU3FlIObaYUII%2BDEQWE6dw6FmOniKV7tZp3g3oeqMVBT%2BIbY%2F8PUxDW0bWXRoam01bfxwPlbLoQoComlnXqm%2FIoyoGDGnmRiuvhpGcFieL5NlQ7Vi4b%2FIOEGz8ja0Oda%2BbR7hIQ5ZJ1aiVKDypwb0bFr%2BArzawA8kokqgnVUSn6zIB4gq9PJBuIGVqnR445rgkyfU2ko2V90keZDU8VBSUjNDHFckDdsYFdEiUJfiQa%2B0RfFa%2Fl26S%2FzKcCQHo20U7dVJDZFmfkwA%2BzWGVpDwk7SmtVe1hbyTkz3jmy32NGU%2BITKmeRU3eZ9n8RVEuBIkrEIBje4LaYXXghzg1cuPcWfa%2F4Ivw27qkoF21j3BgoUtrEid%2BkEMmBaXIdRVdxnJM6QzkUdnBoUEf8IWnuEA9SHDQ16GzYA5QR%2BNiaTlEJmwDxJ1zHBi0iGnZ0erlGQj5RP9uD2b1jxaagT%2B6r1kh9kZ2wFFxhMP2%2Bhr0GOqUBSt2yP84ZD5EFfD2cFTxCwrtm54KI1N9lWCBs5iJUDK%2BtsN2kVSBbwKkv8EPTDALW9GjSC6XpyOY%2FdqF9jl4McxpDspnn6lYWrObIP%2FAa2mAKbtlau12404s%2Bq5GZ0u13ei9fziJGUt8w5gRKhIbkZnRoRz4%2BCm%2BmJvsnLM4Rfd8bgv1s3Cg6lJRbgUP2Izj0CjN7o9T9%2FjkxtD6gR2BUmf6wr%2BiW&X-Amz-Signature=eaf066e9f6827fd27cd470fc3cda8b66ced14e8bb3561b173a4f99c0951ddea1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTRPF2F7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICgLaBlO360fn79nYca8Z022KsgjYVCgqb8Db0p74RmNAiEA9plv1kLSiIAmpdBSlstmeBW6pmnezruWcw4XstI7HRkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGnDTiSSTYEnJ4Cx3CrcA0%2F5MZncVqs6l3zaAtMaC81hEOyfKpaK8EOixRMuiQaZW7vvwprRUqLj3CeRrwOLoDOvRSmNxMBMCE%2FhW4s8SNd84uVTWnLFh9sLXUikaM9xVcBWew5vGC3xj%2BDZnMcSGnn1De2kS0VweH4YL4EVGDI7kop3zcU3FlIObaYUII%2BDEQWE6dw6FmOniKV7tZp3g3oeqMVBT%2BIbY%2F8PUxDW0bWXRoam01bfxwPlbLoQoComlnXqm%2FIoyoGDGnmRiuvhpGcFieL5NlQ7Vi4b%2FIOEGz8ja0Oda%2BbR7hIQ5ZJ1aiVKDypwb0bFr%2BArzawA8kokqgnVUSn6zIB4gq9PJBuIGVqnR445rgkyfU2ko2V90keZDU8VBSUjNDHFckDdsYFdEiUJfiQa%2B0RfFa%2Fl26S%2FzKcCQHo20U7dVJDZFmfkwA%2BzWGVpDwk7SmtVe1hbyTkz3jmy32NGU%2BITKmeRU3eZ9n8RVEuBIkrEIBje4LaYXXghzg1cuPcWfa%2F4Ivw27qkoF21j3BgoUtrEid%2BkEMmBaXIdRVdxnJM6QzkUdnBoUEf8IWnuEA9SHDQ16GzYA5QR%2BNiaTlEJmwDxJ1zHBi0iGnZ0erlGQj5RP9uD2b1jxaagT%2B6r1kh9kZ2wFFxhMP2%2Bhr0GOqUBSt2yP84ZD5EFfD2cFTxCwrtm54KI1N9lWCBs5iJUDK%2BtsN2kVSBbwKkv8EPTDALW9GjSC6XpyOY%2FdqF9jl4McxpDspnn6lYWrObIP%2FAa2mAKbtlau12404s%2Bq5GZ0u13ei9fziJGUt8w5gRKhIbkZnRoRz4%2BCm%2BmJvsnLM4Rfd8bgv1s3Cg6lJRbgUP2Izj0CjN7o9T9%2FjkxtD6gR2BUmf6wr%2BiW&X-Amz-Signature=decf333a348da75da4ac431d05eb59f512f1b9d81cb92b3969fec31b079d4af0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTRPF2F7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICgLaBlO360fn79nYca8Z022KsgjYVCgqb8Db0p74RmNAiEA9plv1kLSiIAmpdBSlstmeBW6pmnezruWcw4XstI7HRkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGnDTiSSTYEnJ4Cx3CrcA0%2F5MZncVqs6l3zaAtMaC81hEOyfKpaK8EOixRMuiQaZW7vvwprRUqLj3CeRrwOLoDOvRSmNxMBMCE%2FhW4s8SNd84uVTWnLFh9sLXUikaM9xVcBWew5vGC3xj%2BDZnMcSGnn1De2kS0VweH4YL4EVGDI7kop3zcU3FlIObaYUII%2BDEQWE6dw6FmOniKV7tZp3g3oeqMVBT%2BIbY%2F8PUxDW0bWXRoam01bfxwPlbLoQoComlnXqm%2FIoyoGDGnmRiuvhpGcFieL5NlQ7Vi4b%2FIOEGz8ja0Oda%2BbR7hIQ5ZJ1aiVKDypwb0bFr%2BArzawA8kokqgnVUSn6zIB4gq9PJBuIGVqnR445rgkyfU2ko2V90keZDU8VBSUjNDHFckDdsYFdEiUJfiQa%2B0RfFa%2Fl26S%2FzKcCQHo20U7dVJDZFmfkwA%2BzWGVpDwk7SmtVe1hbyTkz3jmy32NGU%2BITKmeRU3eZ9n8RVEuBIkrEIBje4LaYXXghzg1cuPcWfa%2F4Ivw27qkoF21j3BgoUtrEid%2BkEMmBaXIdRVdxnJM6QzkUdnBoUEf8IWnuEA9SHDQ16GzYA5QR%2BNiaTlEJmwDxJ1zHBi0iGnZ0erlGQj5RP9uD2b1jxaagT%2B6r1kh9kZ2wFFxhMP2%2Bhr0GOqUBSt2yP84ZD5EFfD2cFTxCwrtm54KI1N9lWCBs5iJUDK%2BtsN2kVSBbwKkv8EPTDALW9GjSC6XpyOY%2FdqF9jl4McxpDspnn6lYWrObIP%2FAa2mAKbtlau12404s%2Bq5GZ0u13ei9fziJGUt8w5gRKhIbkZnRoRz4%2BCm%2BmJvsnLM4Rfd8bgv1s3Cg6lJRbgUP2Izj0CjN7o9T9%2FjkxtD6gR2BUmf6wr%2BiW&X-Amz-Signature=b9937554a771e02c847abd834ca7bd597dd9a536c1920889223bbeb674b6ca30&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTRPF2F7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICgLaBlO360fn79nYca8Z022KsgjYVCgqb8Db0p74RmNAiEA9plv1kLSiIAmpdBSlstmeBW6pmnezruWcw4XstI7HRkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGnDTiSSTYEnJ4Cx3CrcA0%2F5MZncVqs6l3zaAtMaC81hEOyfKpaK8EOixRMuiQaZW7vvwprRUqLj3CeRrwOLoDOvRSmNxMBMCE%2FhW4s8SNd84uVTWnLFh9sLXUikaM9xVcBWew5vGC3xj%2BDZnMcSGnn1De2kS0VweH4YL4EVGDI7kop3zcU3FlIObaYUII%2BDEQWE6dw6FmOniKV7tZp3g3oeqMVBT%2BIbY%2F8PUxDW0bWXRoam01bfxwPlbLoQoComlnXqm%2FIoyoGDGnmRiuvhpGcFieL5NlQ7Vi4b%2FIOEGz8ja0Oda%2BbR7hIQ5ZJ1aiVKDypwb0bFr%2BArzawA8kokqgnVUSn6zIB4gq9PJBuIGVqnR445rgkyfU2ko2V90keZDU8VBSUjNDHFckDdsYFdEiUJfiQa%2B0RfFa%2Fl26S%2FzKcCQHo20U7dVJDZFmfkwA%2BzWGVpDwk7SmtVe1hbyTkz3jmy32NGU%2BITKmeRU3eZ9n8RVEuBIkrEIBje4LaYXXghzg1cuPcWfa%2F4Ivw27qkoF21j3BgoUtrEid%2BkEMmBaXIdRVdxnJM6QzkUdnBoUEf8IWnuEA9SHDQ16GzYA5QR%2BNiaTlEJmwDxJ1zHBi0iGnZ0erlGQj5RP9uD2b1jxaagT%2B6r1kh9kZ2wFFxhMP2%2Bhr0GOqUBSt2yP84ZD5EFfD2cFTxCwrtm54KI1N9lWCBs5iJUDK%2BtsN2kVSBbwKkv8EPTDALW9GjSC6XpyOY%2FdqF9jl4McxpDspnn6lYWrObIP%2FAa2mAKbtlau12404s%2Bq5GZ0u13ei9fziJGUt8w5gRKhIbkZnRoRz4%2BCm%2BmJvsnLM4Rfd8bgv1s3Cg6lJRbgUP2Izj0CjN7o9T9%2FjkxtD6gR2BUmf6wr%2BiW&X-Amz-Signature=b8ff2e4fbc059b43ff57fa264d641421c6bda3f843f4e0b772210c4dd7db7b8f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTRPF2F7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICgLaBlO360fn79nYca8Z022KsgjYVCgqb8Db0p74RmNAiEA9plv1kLSiIAmpdBSlstmeBW6pmnezruWcw4XstI7HRkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGnDTiSSTYEnJ4Cx3CrcA0%2F5MZncVqs6l3zaAtMaC81hEOyfKpaK8EOixRMuiQaZW7vvwprRUqLj3CeRrwOLoDOvRSmNxMBMCE%2FhW4s8SNd84uVTWnLFh9sLXUikaM9xVcBWew5vGC3xj%2BDZnMcSGnn1De2kS0VweH4YL4EVGDI7kop3zcU3FlIObaYUII%2BDEQWE6dw6FmOniKV7tZp3g3oeqMVBT%2BIbY%2F8PUxDW0bWXRoam01bfxwPlbLoQoComlnXqm%2FIoyoGDGnmRiuvhpGcFieL5NlQ7Vi4b%2FIOEGz8ja0Oda%2BbR7hIQ5ZJ1aiVKDypwb0bFr%2BArzawA8kokqgnVUSn6zIB4gq9PJBuIGVqnR445rgkyfU2ko2V90keZDU8VBSUjNDHFckDdsYFdEiUJfiQa%2B0RfFa%2Fl26S%2FzKcCQHo20U7dVJDZFmfkwA%2BzWGVpDwk7SmtVe1hbyTkz3jmy32NGU%2BITKmeRU3eZ9n8RVEuBIkrEIBje4LaYXXghzg1cuPcWfa%2F4Ivw27qkoF21j3BgoUtrEid%2BkEMmBaXIdRVdxnJM6QzkUdnBoUEf8IWnuEA9SHDQ16GzYA5QR%2BNiaTlEJmwDxJ1zHBi0iGnZ0erlGQj5RP9uD2b1jxaagT%2B6r1kh9kZ2wFFxhMP2%2Bhr0GOqUBSt2yP84ZD5EFfD2cFTxCwrtm54KI1N9lWCBs5iJUDK%2BtsN2kVSBbwKkv8EPTDALW9GjSC6XpyOY%2FdqF9jl4McxpDspnn6lYWrObIP%2FAa2mAKbtlau12404s%2Bq5GZ0u13ei9fziJGUt8w5gRKhIbkZnRoRz4%2BCm%2BmJvsnLM4Rfd8bgv1s3Cg6lJRbgUP2Izj0CjN7o9T9%2FjkxtD6gR2BUmf6wr%2BiW&X-Amz-Signature=b177418a0743e934e845cc04975f2bccdb45260904ce207f0fdefdd6baaa7879&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AL23UNW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHCbTeJMJZPxjNBQQXe%2BXI1G%2FfGZx4KVLhCDywx40EWqAiBC4hnnk4v4avvo8e4HhTvl5vVSohBQQ6ltE40cu5TmZir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUO3roC%2BUFDZ8IOdkKtwDYyLWde5n9AJn9xiv0TnO%2BZo80m3l7UC7KIq%2FAExFEdEw72MO0JUfypwer2i2o2VPb5gf4nFVuTk4qnCAZzh7XM8AGwwhs%2FrGPekBubk6Q%2FL9YZfKjitWRpAh7Y4hji20Z0C%2BObtlF9d9xrBU0mD%2FU4p%2Fgdit2ff7hXbL0uQXG55RhGNnWMLirXq1u0dG0e4wrWM0M9NsddoAQVepyIOoGSHta6ow0O4ghCjW4tGs4Alln8Guk4w8ZQfXkSXMCq4eECe5G7qj7TjQxz2BEFvfNJgOf0B1shjTQ5KLtqtqvumQ8f5Gc%2FK%2BALKrmQ%2BAHnQ99PbYzV7lMWWrrymCHKaXA%2FNVuFhw1vheQo%2BVQBzUJ4FLdE5aP%2FtqCmjbmwv8jM59TgSuzvnOe2IjsfJGj5ukxOItEQlIBY6vZV%2FF7hUUdmOz8e8SGZlVYLBHmzrKH1csxDm2%2FuSqthui1dT3jMJ3CS2rNULJSWDDUkQN9ME4FYExUkOoTVJ4%2Bx2IUo4hFG%2BYyMc3qI%2FCGRtXh6aghDw6yCcChutJPoZL3ctUU7Qk%2F1tL9ewBf3DuG8L%2FqYdKW3Ha3xfCSPIjMiug%2BxZFkpxqYP4e62qd5%2F3v%2BjajsBY6NdLzpZLMLlNolzGc%2BScwzr6GvQY6pgHPieCXOXngJTIZTTzZTQhdo4SqdFQNgTdZ8EWJG2yaCXBnmHmpMil6%2FltxuyKmmF4KsNSNHMN51oJ4N6GcO273Yob73hmJ9k50nZEAXu3MshSIg%2F5RUPA3B6nhkCoTqJ00Ad9lIKMCSqi9adCkSKAbfJhWr%2BaQ9EpCkBVbykxAJWItKLsLp9EeFhkTCFj9VSKuX3HoWCBMvcS%2BJ%2Bg%2BaOCzafCk6BL3&X-Amz-Signature=041a84870c3e776406f1c66a0640640cf87f7b66afaf469288d4baca02805c65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AL23UNW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHCbTeJMJZPxjNBQQXe%2BXI1G%2FfGZx4KVLhCDywx40EWqAiBC4hnnk4v4avvo8e4HhTvl5vVSohBQQ6ltE40cu5TmZir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUO3roC%2BUFDZ8IOdkKtwDYyLWde5n9AJn9xiv0TnO%2BZo80m3l7UC7KIq%2FAExFEdEw72MO0JUfypwer2i2o2VPb5gf4nFVuTk4qnCAZzh7XM8AGwwhs%2FrGPekBubk6Q%2FL9YZfKjitWRpAh7Y4hji20Z0C%2BObtlF9d9xrBU0mD%2FU4p%2Fgdit2ff7hXbL0uQXG55RhGNnWMLirXq1u0dG0e4wrWM0M9NsddoAQVepyIOoGSHta6ow0O4ghCjW4tGs4Alln8Guk4w8ZQfXkSXMCq4eECe5G7qj7TjQxz2BEFvfNJgOf0B1shjTQ5KLtqtqvumQ8f5Gc%2FK%2BALKrmQ%2BAHnQ99PbYzV7lMWWrrymCHKaXA%2FNVuFhw1vheQo%2BVQBzUJ4FLdE5aP%2FtqCmjbmwv8jM59TgSuzvnOe2IjsfJGj5ukxOItEQlIBY6vZV%2FF7hUUdmOz8e8SGZlVYLBHmzrKH1csxDm2%2FuSqthui1dT3jMJ3CS2rNULJSWDDUkQN9ME4FYExUkOoTVJ4%2Bx2IUo4hFG%2BYyMc3qI%2FCGRtXh6aghDw6yCcChutJPoZL3ctUU7Qk%2F1tL9ewBf3DuG8L%2FqYdKW3Ha3xfCSPIjMiug%2BxZFkpxqYP4e62qd5%2F3v%2BjajsBY6NdLzpZLMLlNolzGc%2BScwzr6GvQY6pgHPieCXOXngJTIZTTzZTQhdo4SqdFQNgTdZ8EWJG2yaCXBnmHmpMil6%2FltxuyKmmF4KsNSNHMN51oJ4N6GcO273Yob73hmJ9k50nZEAXu3MshSIg%2F5RUPA3B6nhkCoTqJ00Ad9lIKMCSqi9adCkSKAbfJhWr%2BaQ9EpCkBVbykxAJWItKLsLp9EeFhkTCFj9VSKuX3HoWCBMvcS%2BJ%2Bg%2BaOCzafCk6BL3&X-Amz-Signature=4fc77db208a51cce00b7f8876d35a6f62972dcfc46e884c4d3e74ccca37e5256&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AL23UNW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHCbTeJMJZPxjNBQQXe%2BXI1G%2FfGZx4KVLhCDywx40EWqAiBC4hnnk4v4avvo8e4HhTvl5vVSohBQQ6ltE40cu5TmZir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUO3roC%2BUFDZ8IOdkKtwDYyLWde5n9AJn9xiv0TnO%2BZo80m3l7UC7KIq%2FAExFEdEw72MO0JUfypwer2i2o2VPb5gf4nFVuTk4qnCAZzh7XM8AGwwhs%2FrGPekBubk6Q%2FL9YZfKjitWRpAh7Y4hji20Z0C%2BObtlF9d9xrBU0mD%2FU4p%2Fgdit2ff7hXbL0uQXG55RhGNnWMLirXq1u0dG0e4wrWM0M9NsddoAQVepyIOoGSHta6ow0O4ghCjW4tGs4Alln8Guk4w8ZQfXkSXMCq4eECe5G7qj7TjQxz2BEFvfNJgOf0B1shjTQ5KLtqtqvumQ8f5Gc%2FK%2BALKrmQ%2BAHnQ99PbYzV7lMWWrrymCHKaXA%2FNVuFhw1vheQo%2BVQBzUJ4FLdE5aP%2FtqCmjbmwv8jM59TgSuzvnOe2IjsfJGj5ukxOItEQlIBY6vZV%2FF7hUUdmOz8e8SGZlVYLBHmzrKH1csxDm2%2FuSqthui1dT3jMJ3CS2rNULJSWDDUkQN9ME4FYExUkOoTVJ4%2Bx2IUo4hFG%2BYyMc3qI%2FCGRtXh6aghDw6yCcChutJPoZL3ctUU7Qk%2F1tL9ewBf3DuG8L%2FqYdKW3Ha3xfCSPIjMiug%2BxZFkpxqYP4e62qd5%2F3v%2BjajsBY6NdLzpZLMLlNolzGc%2BScwzr6GvQY6pgHPieCXOXngJTIZTTzZTQhdo4SqdFQNgTdZ8EWJG2yaCXBnmHmpMil6%2FltxuyKmmF4KsNSNHMN51oJ4N6GcO273Yob73hmJ9k50nZEAXu3MshSIg%2F5RUPA3B6nhkCoTqJ00Ad9lIKMCSqi9adCkSKAbfJhWr%2BaQ9EpCkBVbykxAJWItKLsLp9EeFhkTCFj9VSKuX3HoWCBMvcS%2BJ%2Bg%2BaOCzafCk6BL3&X-Amz-Signature=ba0a6082cc4adfbed80ba5beda6536a9a05153dbf3e7208c28d82f0c20ac03f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AL23UNW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHCbTeJMJZPxjNBQQXe%2BXI1G%2FfGZx4KVLhCDywx40EWqAiBC4hnnk4v4avvo8e4HhTvl5vVSohBQQ6ltE40cu5TmZir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUO3roC%2BUFDZ8IOdkKtwDYyLWde5n9AJn9xiv0TnO%2BZo80m3l7UC7KIq%2FAExFEdEw72MO0JUfypwer2i2o2VPb5gf4nFVuTk4qnCAZzh7XM8AGwwhs%2FrGPekBubk6Q%2FL9YZfKjitWRpAh7Y4hji20Z0C%2BObtlF9d9xrBU0mD%2FU4p%2Fgdit2ff7hXbL0uQXG55RhGNnWMLirXq1u0dG0e4wrWM0M9NsddoAQVepyIOoGSHta6ow0O4ghCjW4tGs4Alln8Guk4w8ZQfXkSXMCq4eECe5G7qj7TjQxz2BEFvfNJgOf0B1shjTQ5KLtqtqvumQ8f5Gc%2FK%2BALKrmQ%2BAHnQ99PbYzV7lMWWrrymCHKaXA%2FNVuFhw1vheQo%2BVQBzUJ4FLdE5aP%2FtqCmjbmwv8jM59TgSuzvnOe2IjsfJGj5ukxOItEQlIBY6vZV%2FF7hUUdmOz8e8SGZlVYLBHmzrKH1csxDm2%2FuSqthui1dT3jMJ3CS2rNULJSWDDUkQN9ME4FYExUkOoTVJ4%2Bx2IUo4hFG%2BYyMc3qI%2FCGRtXh6aghDw6yCcChutJPoZL3ctUU7Qk%2F1tL9ewBf3DuG8L%2FqYdKW3Ha3xfCSPIjMiug%2BxZFkpxqYP4e62qd5%2F3v%2BjajsBY6NdLzpZLMLlNolzGc%2BScwzr6GvQY6pgHPieCXOXngJTIZTTzZTQhdo4SqdFQNgTdZ8EWJG2yaCXBnmHmpMil6%2FltxuyKmmF4KsNSNHMN51oJ4N6GcO273Yob73hmJ9k50nZEAXu3MshSIg%2F5RUPA3B6nhkCoTqJ00Ad9lIKMCSqi9adCkSKAbfJhWr%2BaQ9EpCkBVbykxAJWItKLsLp9EeFhkTCFj9VSKuX3HoWCBMvcS%2BJ%2Bg%2BaOCzafCk6BL3&X-Amz-Signature=fd24f79ad432f3c25793b4714a59a0c7c5db60bfda0f2591062e4338d55d47b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Video Sequences
A **video** can be viewed as a sequence of multiple **images** or **frames**.
### Image Formats
Common image file formats include:
- **JPEG** (Joint Photographic Expert Group)
- **PNG** (Portable Network Graphics)
These formats compress and reduce file sizes while maintaining image quality.
### Image Processing Libraries in Python
#### Pillow (PIL)
Pillow is a widely used Python library for image manipulation.
- To load an image:
```python
from PIL import Image
img = Image.open('image.png')
```
- **Attributes** of a Pillow image:
	- `format`: The file format (e.g., PNG, JPEG).
	- `size`: The dimensions of the image (width x height).
	- `mode`: The color space (e.g., RGB, L for grayscale).
#### Example: Converting to Gray-Scale
- Convert an image to **gray-scale**:
```python
gray_img = img.convert('L')
gray_img.show()
```
#### Example: Quantization
- **Quantize** an image to reduce the number of intensity levels:
```python
quantized_img = img.quantize(colors=16)
quantized_img.show()
```
#### OpenCV
**OpenCV** is a powerful library for **computer vision** with more functionality than PIL.
- Import OpenCV:
```python
import cv2
```
- Load an image:
```python
img = cv2.imread('image.png')
```
- **Attributes** of an OpenCV image:
	- OpenCV represents images as **NumPy arrays**.
	- The **color channels** are ordered as **BGR** (blue, green, red) instead of **RGB**.
#### Example: Color Space Conversion
- Convert from **BGR to RGB**:
```python
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
- Convert to **gray-scale**:
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
#### Example: Saving an Image
- Save an image using OpenCV:
```python
cv2.imwrite('output.png', img)
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AL23UNW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHCbTeJMJZPxjNBQQXe%2BXI1G%2FfGZx4KVLhCDywx40EWqAiBC4hnnk4v4avvo8e4HhTvl5vVSohBQQ6ltE40cu5TmZir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMUO3roC%2BUFDZ8IOdkKtwDYyLWde5n9AJn9xiv0TnO%2BZo80m3l7UC7KIq%2FAExFEdEw72MO0JUfypwer2i2o2VPb5gf4nFVuTk4qnCAZzh7XM8AGwwhs%2FrGPekBubk6Q%2FL9YZfKjitWRpAh7Y4hji20Z0C%2BObtlF9d9xrBU0mD%2FU4p%2Fgdit2ff7hXbL0uQXG55RhGNnWMLirXq1u0dG0e4wrWM0M9NsddoAQVepyIOoGSHta6ow0O4ghCjW4tGs4Alln8Guk4w8ZQfXkSXMCq4eECe5G7qj7TjQxz2BEFvfNJgOf0B1shjTQ5KLtqtqvumQ8f5Gc%2FK%2BALKrmQ%2BAHnQ99PbYzV7lMWWrrymCHKaXA%2FNVuFhw1vheQo%2BVQBzUJ4FLdE5aP%2FtqCmjbmwv8jM59TgSuzvnOe2IjsfJGj5ukxOItEQlIBY6vZV%2FF7hUUdmOz8e8SGZlVYLBHmzrKH1csxDm2%2FuSqthui1dT3jMJ3CS2rNULJSWDDUkQN9ME4FYExUkOoTVJ4%2Bx2IUo4hFG%2BYyMc3qI%2FCGRtXh6aghDw6yCcChutJPoZL3ctUU7Qk%2F1tL9ewBf3DuG8L%2FqYdKW3Ha3xfCSPIjMiug%2BxZFkpxqYP4e62qd5%2F3v%2BjajsBY6NdLzpZLMLlNolzGc%2BScwzr6GvQY6pgHPieCXOXngJTIZTTzZTQhdo4SqdFQNgTdZ8EWJG2yaCXBnmHmpMil6%2FltxuyKmmF4KsNSNHMN51oJ4N6GcO273Yob73hmJ9k50nZEAXu3MshSIg%2F5RUPA3B6nhkCoTqJ00Ad9lIKMCSqi9adCkSKAbfJhWr%2BaQ9EpCkBVbykxAJWItKLsLp9EeFhkTCFj9VSKuX3HoWCBMvcS%2BJ%2Bg%2BaOCzafCk6BL3&X-Amz-Signature=34169b157bd6fa2b48490bd852f2421020379e542d957b7dcfd086b7c5409226&X-Amz-SignedHeaders=host&x-id=GetObject)
### Working with Color Channels
Using **slices**, individual color channels (e.g., **blue**, **green**, **red**) can be extracted:
```python
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]
```
Each channel can then be processed or analyzed separately.
#### Conversion between PIL and NumPy Arrays
PIL images can be easily converted to **NumPy arrays** for further processing:
```python
import numpy as np
np_img = np.array(img)
```
This conversion is particularly useful when integrating with **OpenCV** and performing advanced operations.
### Conclusion
Both **PIL** and **OpenCV** are essential tools for handling and processing digital images in Python. Each has its strengths:
- **PIL** is simple and great for basic tasks.
- **OpenCV** offers more advanced capabilities for **computer vision** applications.
___


