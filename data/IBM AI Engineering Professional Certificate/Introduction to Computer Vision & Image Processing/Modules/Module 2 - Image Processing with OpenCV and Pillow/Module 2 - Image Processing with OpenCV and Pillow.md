

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM627JKT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCCpRbkMY61XA6jH5msD7h2xC0AENjdjQWyhf74q4m3wQIhAPRWdnt0Jq0QB0MZFpESbF6GLXcHujsZNV8oRQs9t%2By0Kv8DCC4QABoMNjM3NDIzMTgzODA1IgyanT5QQywuilvDOVQq3AO%2FQ%2BzZi9TfSm%2FHxQlomsd7F4h7JQovGCX%2Bzwl6AlFUftiefsy7UxyM3jUu%2B1cQlX9WFIOCC33mTsoelGGOXoXlTLzc5JF755jDFugDKPXRZKGTgFsmyompzlm0IHXYgSfukDNxlLPioFTPOgDCuc2py9swZhPGSbYgQ5VhR%2F83SjkjbVXEurxxumJ70AMX7s9jkWI7G9Gg%2BAC7hNLSKo31KrH1HQRCjBNMMlyifNiqPquuXy86rz6DxE4Gvrcx3ac1fKFWlWkSougO4h13lCQe0TY7U1kjKA3PVo8JCgyDiNwYBFsqQPgiE9brgTsaXdCuXKR%2Bujr0Kjz0mB%2BAUcJegX4iAwG7aNnDWNqoPwweXAM5u4KCzJ5qjDPR8D2rKkTxRcGtfr5WPTjKtwYkjuFNamg93FEvJ7ty8%2F8G70U3J%2BD%2BCVkrjAL5ygNYh9KcHVx%2FoUaEZrA3TQLIQh99%2FgTlN3nGPu6nN0y9fiwD1dZfsgbrYhj%2B16L2TdO%2F1HhRI2sFNiV93tfAgVqG0Y42rKTeLvjNveG5qES0mvLdM8twczX1Gl%2BhkF%2B%2Bes5IUDoAAC%2FADTAhuWi45q4gJtnzgcoc88wjE3VVIHnDJzK0GqitROittZML%2Byx8ZAUVzTCWnoi9BjqkAc1WwLCtZXXGj2meWq7WEWg%2BxWZ4Wu32TGI5U4M%2BNydpAvuWT1fEyEuIqYatalLl%2FMYKwA3rQeTdVWAYpQxpJdIPU%2F8N8cWtOTTxCMXUIY8SjmcaKaapaA3XuH8FDEf0sje%2BY0UEXG8GsTDCyl%2F7ued3ZV26yFVWd5LQNock9Rmxb8eEsvKOQmf2ww9%2FNuk0E%2FIzJJ1EHS6b0W8ahKbMQr4dy5PE&X-Amz-Signature=bf65ef3a59c7b0295decac01fc2d2aa5af9b78550a2c68a14b73c5a66fa10bea&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJT5FFGV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIHcFt5F6tqoKx2sgFKQdwGF69j43xKz381fNLynVaSzuAiEA%2FaxOsvYZi0KPHgNGxU3jvRfO4BTyg5YxbGwDx%2BLAyRMq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDABKbSOUod0xqkNjtircA5hlVUV6teljtx2sgNvpU4FQ%2BNRdyq49hIfMcIbN3Um3yrOo5MsMyFkUPdrU%2FwyEdo6F8rJfqB36RY8w3oIlSeRaQQXM9n%2Ft7FS%2FXaPIqN%2B2WVnO%2FTh5PvCXCF6HHPzZ0MMJezfEJgs3cjm0NUtv8t3QMtieUvvrOeNHA7KMit%2BKbW92ZQ7UuvoVbLeaaCe3tSthgJCVS9KDGShReyG9Hiyv2gX0IWytcGGnH8nbMBenYeWEz53PiDe%2FLNkbB7E%2BmjexvRJLzA3bBi5%2B9hlPQNm3jUXDzRi3A6gSrDyVgeWg%2BODgwRA%2F%2BJY8AXHzxlYog8XAE19PdZOlzGwTQLo%2F7GSsCPF%2Fym0ftPywoDsGJhHbWQM%2FXdd7ivV0YvU9zA2x3%2BaJ7cQKZQqeVLIy2YQehE3p2vbgqRyuZO55snuKhffewf01tD24coRbUaqP1xuhTfXdw%2BiOEX%2FDg8O1JgBANsa%2FqBoErHKdKdBnj%2BgGILaiwcqRRWY%2BEeViYQz8hsxLNWMblD3aa%2F9i6gKdjFL2BgdKN21iccki4oYu55650H2VPKX6RK9rJBI49PE7dbsT6dZ12IqM6Tcge3ePmpRBQAgFf08KovILeidWWm%2FmdTcAMd8056JjeIv%2FjsN5MLCeiL0GOqUB12ymOvxusXlNZxg%2Bu0kbwRwDRpM0Y3VBSucOrhQQWCwZSAO%2FzDrjLXX6XEwCfTx1y5Pdw8fV8senq3QG5K5hh%2F%2B6MBmN%2FyUkZVlskaZAxVcMr6jQh500D9QelhcgTWGSr4FH3z2A32zliKMoFlOEFaf%2FEB%2B6ccPIH6A3doRe787p1jbdikJgbMaiU1yI%2BdvEIIVC7x93mnt8xlpAnWs1zgCdaI45&X-Amz-Signature=2be5ce26481901df0ad382387b77db2a72ef9da32dc83e8212f45d9746ca7e15&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJT5FFGV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIHcFt5F6tqoKx2sgFKQdwGF69j43xKz381fNLynVaSzuAiEA%2FaxOsvYZi0KPHgNGxU3jvRfO4BTyg5YxbGwDx%2BLAyRMq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDABKbSOUod0xqkNjtircA5hlVUV6teljtx2sgNvpU4FQ%2BNRdyq49hIfMcIbN3Um3yrOo5MsMyFkUPdrU%2FwyEdo6F8rJfqB36RY8w3oIlSeRaQQXM9n%2Ft7FS%2FXaPIqN%2B2WVnO%2FTh5PvCXCF6HHPzZ0MMJezfEJgs3cjm0NUtv8t3QMtieUvvrOeNHA7KMit%2BKbW92ZQ7UuvoVbLeaaCe3tSthgJCVS9KDGShReyG9Hiyv2gX0IWytcGGnH8nbMBenYeWEz53PiDe%2FLNkbB7E%2BmjexvRJLzA3bBi5%2B9hlPQNm3jUXDzRi3A6gSrDyVgeWg%2BODgwRA%2F%2BJY8AXHzxlYog8XAE19PdZOlzGwTQLo%2F7GSsCPF%2Fym0ftPywoDsGJhHbWQM%2FXdd7ivV0YvU9zA2x3%2BaJ7cQKZQqeVLIy2YQehE3p2vbgqRyuZO55snuKhffewf01tD24coRbUaqP1xuhTfXdw%2BiOEX%2FDg8O1JgBANsa%2FqBoErHKdKdBnj%2BgGILaiwcqRRWY%2BEeViYQz8hsxLNWMblD3aa%2F9i6gKdjFL2BgdKN21iccki4oYu55650H2VPKX6RK9rJBI49PE7dbsT6dZ12IqM6Tcge3ePmpRBQAgFf08KovILeidWWm%2FmdTcAMd8056JjeIv%2FjsN5MLCeiL0GOqUB12ymOvxusXlNZxg%2Bu0kbwRwDRpM0Y3VBSucOrhQQWCwZSAO%2FzDrjLXX6XEwCfTx1y5Pdw8fV8senq3QG5K5hh%2F%2B6MBmN%2FyUkZVlskaZAxVcMr6jQh500D9QelhcgTWGSr4FH3z2A32zliKMoFlOEFaf%2FEB%2B6ccPIH6A3doRe787p1jbdikJgbMaiU1yI%2BdvEIIVC7x93mnt8xlpAnWs1zgCdaI45&X-Amz-Signature=76e094009f8042318bff4bac661ea8c4c1f91b50c70d0f1cd2802691601c0bdd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJT5FFGV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIHcFt5F6tqoKx2sgFKQdwGF69j43xKz381fNLynVaSzuAiEA%2FaxOsvYZi0KPHgNGxU3jvRfO4BTyg5YxbGwDx%2BLAyRMq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDABKbSOUod0xqkNjtircA5hlVUV6teljtx2sgNvpU4FQ%2BNRdyq49hIfMcIbN3Um3yrOo5MsMyFkUPdrU%2FwyEdo6F8rJfqB36RY8w3oIlSeRaQQXM9n%2Ft7FS%2FXaPIqN%2B2WVnO%2FTh5PvCXCF6HHPzZ0MMJezfEJgs3cjm0NUtv8t3QMtieUvvrOeNHA7KMit%2BKbW92ZQ7UuvoVbLeaaCe3tSthgJCVS9KDGShReyG9Hiyv2gX0IWytcGGnH8nbMBenYeWEz53PiDe%2FLNkbB7E%2BmjexvRJLzA3bBi5%2B9hlPQNm3jUXDzRi3A6gSrDyVgeWg%2BODgwRA%2F%2BJY8AXHzxlYog8XAE19PdZOlzGwTQLo%2F7GSsCPF%2Fym0ftPywoDsGJhHbWQM%2FXdd7ivV0YvU9zA2x3%2BaJ7cQKZQqeVLIy2YQehE3p2vbgqRyuZO55snuKhffewf01tD24coRbUaqP1xuhTfXdw%2BiOEX%2FDg8O1JgBANsa%2FqBoErHKdKdBnj%2BgGILaiwcqRRWY%2BEeViYQz8hsxLNWMblD3aa%2F9i6gKdjFL2BgdKN21iccki4oYu55650H2VPKX6RK9rJBI49PE7dbsT6dZ12IqM6Tcge3ePmpRBQAgFf08KovILeidWWm%2FmdTcAMd8056JjeIv%2FjsN5MLCeiL0GOqUB12ymOvxusXlNZxg%2Bu0kbwRwDRpM0Y3VBSucOrhQQWCwZSAO%2FzDrjLXX6XEwCfTx1y5Pdw8fV8senq3QG5K5hh%2F%2B6MBmN%2FyUkZVlskaZAxVcMr6jQh500D9QelhcgTWGSr4FH3z2A32zliKMoFlOEFaf%2FEB%2B6ccPIH6A3doRe787p1jbdikJgbMaiU1yI%2BdvEIIVC7x93mnt8xlpAnWs1zgCdaI45&X-Amz-Signature=95d79dcfc46565873e824082153a985d7435638fe5601c920fd8aaf7f7f332da&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJT5FFGV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIHcFt5F6tqoKx2sgFKQdwGF69j43xKz381fNLynVaSzuAiEA%2FaxOsvYZi0KPHgNGxU3jvRfO4BTyg5YxbGwDx%2BLAyRMq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDABKbSOUod0xqkNjtircA5hlVUV6teljtx2sgNvpU4FQ%2BNRdyq49hIfMcIbN3Um3yrOo5MsMyFkUPdrU%2FwyEdo6F8rJfqB36RY8w3oIlSeRaQQXM9n%2Ft7FS%2FXaPIqN%2B2WVnO%2FTh5PvCXCF6HHPzZ0MMJezfEJgs3cjm0NUtv8t3QMtieUvvrOeNHA7KMit%2BKbW92ZQ7UuvoVbLeaaCe3tSthgJCVS9KDGShReyG9Hiyv2gX0IWytcGGnH8nbMBenYeWEz53PiDe%2FLNkbB7E%2BmjexvRJLzA3bBi5%2B9hlPQNm3jUXDzRi3A6gSrDyVgeWg%2BODgwRA%2F%2BJY8AXHzxlYog8XAE19PdZOlzGwTQLo%2F7GSsCPF%2Fym0ftPywoDsGJhHbWQM%2FXdd7ivV0YvU9zA2x3%2BaJ7cQKZQqeVLIy2YQehE3p2vbgqRyuZO55snuKhffewf01tD24coRbUaqP1xuhTfXdw%2BiOEX%2FDg8O1JgBANsa%2FqBoErHKdKdBnj%2BgGILaiwcqRRWY%2BEeViYQz8hsxLNWMblD3aa%2F9i6gKdjFL2BgdKN21iccki4oYu55650H2VPKX6RK9rJBI49PE7dbsT6dZ12IqM6Tcge3ePmpRBQAgFf08KovILeidWWm%2FmdTcAMd8056JjeIv%2FjsN5MLCeiL0GOqUB12ymOvxusXlNZxg%2Bu0kbwRwDRpM0Y3VBSucOrhQQWCwZSAO%2FzDrjLXX6XEwCfTx1y5Pdw8fV8senq3QG5K5hh%2F%2B6MBmN%2FyUkZVlskaZAxVcMr6jQh500D9QelhcgTWGSr4FH3z2A32zliKMoFlOEFaf%2FEB%2B6ccPIH6A3doRe787p1jbdikJgbMaiU1yI%2BdvEIIVC7x93mnt8xlpAnWs1zgCdaI45&X-Amz-Signature=4175fd4f20f995f73f53481ba83b8e2d4206de2c8ec4d020979585da77e337a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJT5FFGV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIHcFt5F6tqoKx2sgFKQdwGF69j43xKz381fNLynVaSzuAiEA%2FaxOsvYZi0KPHgNGxU3jvRfO4BTyg5YxbGwDx%2BLAyRMq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDABKbSOUod0xqkNjtircA5hlVUV6teljtx2sgNvpU4FQ%2BNRdyq49hIfMcIbN3Um3yrOo5MsMyFkUPdrU%2FwyEdo6F8rJfqB36RY8w3oIlSeRaQQXM9n%2Ft7FS%2FXaPIqN%2B2WVnO%2FTh5PvCXCF6HHPzZ0MMJezfEJgs3cjm0NUtv8t3QMtieUvvrOeNHA7KMit%2BKbW92ZQ7UuvoVbLeaaCe3tSthgJCVS9KDGShReyG9Hiyv2gX0IWytcGGnH8nbMBenYeWEz53PiDe%2FLNkbB7E%2BmjexvRJLzA3bBi5%2B9hlPQNm3jUXDzRi3A6gSrDyVgeWg%2BODgwRA%2F%2BJY8AXHzxlYog8XAE19PdZOlzGwTQLo%2F7GSsCPF%2Fym0ftPywoDsGJhHbWQM%2FXdd7ivV0YvU9zA2x3%2BaJ7cQKZQqeVLIy2YQehE3p2vbgqRyuZO55snuKhffewf01tD24coRbUaqP1xuhTfXdw%2BiOEX%2FDg8O1JgBANsa%2FqBoErHKdKdBnj%2BgGILaiwcqRRWY%2BEeViYQz8hsxLNWMblD3aa%2F9i6gKdjFL2BgdKN21iccki4oYu55650H2VPKX6RK9rJBI49PE7dbsT6dZ12IqM6Tcge3ePmpRBQAgFf08KovILeidWWm%2FmdTcAMd8056JjeIv%2FjsN5MLCeiL0GOqUB12ymOvxusXlNZxg%2Bu0kbwRwDRpM0Y3VBSucOrhQQWCwZSAO%2FzDrjLXX6XEwCfTx1y5Pdw8fV8senq3QG5K5hh%2F%2B6MBmN%2FyUkZVlskaZAxVcMr6jQh500D9QelhcgTWGSr4FH3z2A32zliKMoFlOEFaf%2FEB%2B6ccPIH6A3doRe787p1jbdikJgbMaiU1yI%2BdvEIIVC7x93mnt8xlpAnWs1zgCdaI45&X-Amz-Signature=a3a81fff5da74b02d1b9e9e06ae2da1cb3f16e29f94b7f255c8a79f124c45581&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM627JKT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCCpRbkMY61XA6jH5msD7h2xC0AENjdjQWyhf74q4m3wQIhAPRWdnt0Jq0QB0MZFpESbF6GLXcHujsZNV8oRQs9t%2By0Kv8DCC4QABoMNjM3NDIzMTgzODA1IgyanT5QQywuilvDOVQq3AO%2FQ%2BzZi9TfSm%2FHxQlomsd7F4h7JQovGCX%2Bzwl6AlFUftiefsy7UxyM3jUu%2B1cQlX9WFIOCC33mTsoelGGOXoXlTLzc5JF755jDFugDKPXRZKGTgFsmyompzlm0IHXYgSfukDNxlLPioFTPOgDCuc2py9swZhPGSbYgQ5VhR%2F83SjkjbVXEurxxumJ70AMX7s9jkWI7G9Gg%2BAC7hNLSKo31KrH1HQRCjBNMMlyifNiqPquuXy86rz6DxE4Gvrcx3ac1fKFWlWkSougO4h13lCQe0TY7U1kjKA3PVo8JCgyDiNwYBFsqQPgiE9brgTsaXdCuXKR%2Bujr0Kjz0mB%2BAUcJegX4iAwG7aNnDWNqoPwweXAM5u4KCzJ5qjDPR8D2rKkTxRcGtfr5WPTjKtwYkjuFNamg93FEvJ7ty8%2F8G70U3J%2BD%2BCVkrjAL5ygNYh9KcHVx%2FoUaEZrA3TQLIQh99%2FgTlN3nGPu6nN0y9fiwD1dZfsgbrYhj%2B16L2TdO%2F1HhRI2sFNiV93tfAgVqG0Y42rKTeLvjNveG5qES0mvLdM8twczX1Gl%2BhkF%2B%2Bes5IUDoAAC%2FADTAhuWi45q4gJtnzgcoc88wjE3VVIHnDJzK0GqitROittZML%2Byx8ZAUVzTCWnoi9BjqkAc1WwLCtZXXGj2meWq7WEWg%2BxWZ4Wu32TGI5U4M%2BNydpAvuWT1fEyEuIqYatalLl%2FMYKwA3rQeTdVWAYpQxpJdIPU%2F8N8cWtOTTxCMXUIY8SjmcaKaapaA3XuH8FDEf0sje%2BY0UEXG8GsTDCyl%2F7ued3ZV26yFVWd5LQNock9Rmxb8eEsvKOQmf2ww9%2FNuk0E%2FIzJJ1EHS6b0W8ahKbMQr4dy5PE&X-Amz-Signature=923b0b979b73ed6791bfacba49194ea57a70fc0a212a3575cc1e082d608368c7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM627JKT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCCpRbkMY61XA6jH5msD7h2xC0AENjdjQWyhf74q4m3wQIhAPRWdnt0Jq0QB0MZFpESbF6GLXcHujsZNV8oRQs9t%2By0Kv8DCC4QABoMNjM3NDIzMTgzODA1IgyanT5QQywuilvDOVQq3AO%2FQ%2BzZi9TfSm%2FHxQlomsd7F4h7JQovGCX%2Bzwl6AlFUftiefsy7UxyM3jUu%2B1cQlX9WFIOCC33mTsoelGGOXoXlTLzc5JF755jDFugDKPXRZKGTgFsmyompzlm0IHXYgSfukDNxlLPioFTPOgDCuc2py9swZhPGSbYgQ5VhR%2F83SjkjbVXEurxxumJ70AMX7s9jkWI7G9Gg%2BAC7hNLSKo31KrH1HQRCjBNMMlyifNiqPquuXy86rz6DxE4Gvrcx3ac1fKFWlWkSougO4h13lCQe0TY7U1kjKA3PVo8JCgyDiNwYBFsqQPgiE9brgTsaXdCuXKR%2Bujr0Kjz0mB%2BAUcJegX4iAwG7aNnDWNqoPwweXAM5u4KCzJ5qjDPR8D2rKkTxRcGtfr5WPTjKtwYkjuFNamg93FEvJ7ty8%2F8G70U3J%2BD%2BCVkrjAL5ygNYh9KcHVx%2FoUaEZrA3TQLIQh99%2FgTlN3nGPu6nN0y9fiwD1dZfsgbrYhj%2B16L2TdO%2F1HhRI2sFNiV93tfAgVqG0Y42rKTeLvjNveG5qES0mvLdM8twczX1Gl%2BhkF%2B%2Bes5IUDoAAC%2FADTAhuWi45q4gJtnzgcoc88wjE3VVIHnDJzK0GqitROittZML%2Byx8ZAUVzTCWnoi9BjqkAc1WwLCtZXXGj2meWq7WEWg%2BxWZ4Wu32TGI5U4M%2BNydpAvuWT1fEyEuIqYatalLl%2FMYKwA3rQeTdVWAYpQxpJdIPU%2F8N8cWtOTTxCMXUIY8SjmcaKaapaA3XuH8FDEf0sje%2BY0UEXG8GsTDCyl%2F7ued3ZV26yFVWd5LQNock9Rmxb8eEsvKOQmf2ww9%2FNuk0E%2FIzJJ1EHS6b0W8ahKbMQr4dy5PE&X-Amz-Signature=b9e53c9e93a7a7f75f0e03324115dcb48d413098d424aeadd10d23537d47b96a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM627JKT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCCpRbkMY61XA6jH5msD7h2xC0AENjdjQWyhf74q4m3wQIhAPRWdnt0Jq0QB0MZFpESbF6GLXcHujsZNV8oRQs9t%2By0Kv8DCC4QABoMNjM3NDIzMTgzODA1IgyanT5QQywuilvDOVQq3AO%2FQ%2BzZi9TfSm%2FHxQlomsd7F4h7JQovGCX%2Bzwl6AlFUftiefsy7UxyM3jUu%2B1cQlX9WFIOCC33mTsoelGGOXoXlTLzc5JF755jDFugDKPXRZKGTgFsmyompzlm0IHXYgSfukDNxlLPioFTPOgDCuc2py9swZhPGSbYgQ5VhR%2F83SjkjbVXEurxxumJ70AMX7s9jkWI7G9Gg%2BAC7hNLSKo31KrH1HQRCjBNMMlyifNiqPquuXy86rz6DxE4Gvrcx3ac1fKFWlWkSougO4h13lCQe0TY7U1kjKA3PVo8JCgyDiNwYBFsqQPgiE9brgTsaXdCuXKR%2Bujr0Kjz0mB%2BAUcJegX4iAwG7aNnDWNqoPwweXAM5u4KCzJ5qjDPR8D2rKkTxRcGtfr5WPTjKtwYkjuFNamg93FEvJ7ty8%2F8G70U3J%2BD%2BCVkrjAL5ygNYh9KcHVx%2FoUaEZrA3TQLIQh99%2FgTlN3nGPu6nN0y9fiwD1dZfsgbrYhj%2B16L2TdO%2F1HhRI2sFNiV93tfAgVqG0Y42rKTeLvjNveG5qES0mvLdM8twczX1Gl%2BhkF%2B%2Bes5IUDoAAC%2FADTAhuWi45q4gJtnzgcoc88wjE3VVIHnDJzK0GqitROittZML%2Byx8ZAUVzTCWnoi9BjqkAc1WwLCtZXXGj2meWq7WEWg%2BxWZ4Wu32TGI5U4M%2BNydpAvuWT1fEyEuIqYatalLl%2FMYKwA3rQeTdVWAYpQxpJdIPU%2F8N8cWtOTTxCMXUIY8SjmcaKaapaA3XuH8FDEf0sje%2BY0UEXG8GsTDCyl%2F7ued3ZV26yFVWd5LQNock9Rmxb8eEsvKOQmf2ww9%2FNuk0E%2FIzJJ1EHS6b0W8ahKbMQr4dy5PE&X-Amz-Signature=eba3b17c8ff9eb126df357dc5ef89d4bf0b238ad6dd0e9ea94aa5a82db5de2df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM627JKT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCCpRbkMY61XA6jH5msD7h2xC0AENjdjQWyhf74q4m3wQIhAPRWdnt0Jq0QB0MZFpESbF6GLXcHujsZNV8oRQs9t%2By0Kv8DCC4QABoMNjM3NDIzMTgzODA1IgyanT5QQywuilvDOVQq3AO%2FQ%2BzZi9TfSm%2FHxQlomsd7F4h7JQovGCX%2Bzwl6AlFUftiefsy7UxyM3jUu%2B1cQlX9WFIOCC33mTsoelGGOXoXlTLzc5JF755jDFugDKPXRZKGTgFsmyompzlm0IHXYgSfukDNxlLPioFTPOgDCuc2py9swZhPGSbYgQ5VhR%2F83SjkjbVXEurxxumJ70AMX7s9jkWI7G9Gg%2BAC7hNLSKo31KrH1HQRCjBNMMlyifNiqPquuXy86rz6DxE4Gvrcx3ac1fKFWlWkSougO4h13lCQe0TY7U1kjKA3PVo8JCgyDiNwYBFsqQPgiE9brgTsaXdCuXKR%2Bujr0Kjz0mB%2BAUcJegX4iAwG7aNnDWNqoPwweXAM5u4KCzJ5qjDPR8D2rKkTxRcGtfr5WPTjKtwYkjuFNamg93FEvJ7ty8%2F8G70U3J%2BD%2BCVkrjAL5ygNYh9KcHVx%2FoUaEZrA3TQLIQh99%2FgTlN3nGPu6nN0y9fiwD1dZfsgbrYhj%2B16L2TdO%2F1HhRI2sFNiV93tfAgVqG0Y42rKTeLvjNveG5qES0mvLdM8twczX1Gl%2BhkF%2B%2Bes5IUDoAAC%2FADTAhuWi45q4gJtnzgcoc88wjE3VVIHnDJzK0GqitROittZML%2Byx8ZAUVzTCWnoi9BjqkAc1WwLCtZXXGj2meWq7WEWg%2BxWZ4Wu32TGI5U4M%2BNydpAvuWT1fEyEuIqYatalLl%2FMYKwA3rQeTdVWAYpQxpJdIPU%2F8N8cWtOTTxCMXUIY8SjmcaKaapaA3XuH8FDEf0sje%2BY0UEXG8GsTDCyl%2F7ued3ZV26yFVWd5LQNock9Rmxb8eEsvKOQmf2ww9%2FNuk0E%2FIzJJ1EHS6b0W8ahKbMQr4dy5PE&X-Amz-Signature=a98459eb38de8002230d6dd06c9d9c45e9ab8e736e62bfcf15c3c1faaa08a162&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM627JKT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCCpRbkMY61XA6jH5msD7h2xC0AENjdjQWyhf74q4m3wQIhAPRWdnt0Jq0QB0MZFpESbF6GLXcHujsZNV8oRQs9t%2By0Kv8DCC4QABoMNjM3NDIzMTgzODA1IgyanT5QQywuilvDOVQq3AO%2FQ%2BzZi9TfSm%2FHxQlomsd7F4h7JQovGCX%2Bzwl6AlFUftiefsy7UxyM3jUu%2B1cQlX9WFIOCC33mTsoelGGOXoXlTLzc5JF755jDFugDKPXRZKGTgFsmyompzlm0IHXYgSfukDNxlLPioFTPOgDCuc2py9swZhPGSbYgQ5VhR%2F83SjkjbVXEurxxumJ70AMX7s9jkWI7G9Gg%2BAC7hNLSKo31KrH1HQRCjBNMMlyifNiqPquuXy86rz6DxE4Gvrcx3ac1fKFWlWkSougO4h13lCQe0TY7U1kjKA3PVo8JCgyDiNwYBFsqQPgiE9brgTsaXdCuXKR%2Bujr0Kjz0mB%2BAUcJegX4iAwG7aNnDWNqoPwweXAM5u4KCzJ5qjDPR8D2rKkTxRcGtfr5WPTjKtwYkjuFNamg93FEvJ7ty8%2F8G70U3J%2BD%2BCVkrjAL5ygNYh9KcHVx%2FoUaEZrA3TQLIQh99%2FgTlN3nGPu6nN0y9fiwD1dZfsgbrYhj%2B16L2TdO%2F1HhRI2sFNiV93tfAgVqG0Y42rKTeLvjNveG5qES0mvLdM8twczX1Gl%2BhkF%2B%2Bes5IUDoAAC%2FADTAhuWi45q4gJtnzgcoc88wjE3VVIHnDJzK0GqitROittZML%2Byx8ZAUVzTCWnoi9BjqkAc1WwLCtZXXGj2meWq7WEWg%2BxWZ4Wu32TGI5U4M%2BNydpAvuWT1fEyEuIqYatalLl%2FMYKwA3rQeTdVWAYpQxpJdIPU%2F8N8cWtOTTxCMXUIY8SjmcaKaapaA3XuH8FDEf0sje%2BY0UEXG8GsTDCyl%2F7ued3ZV26yFVWd5LQNock9Rmxb8eEsvKOQmf2ww9%2FNuk0E%2FIzJJ1EHS6b0W8ahKbMQr4dy5PE&X-Amz-Signature=3cd2f1b2a6bef194c8e7bbf29f94239f01fd4726beb17c6978b4908cea524c19&X-Amz-SignedHeaders=host&x-id=GetObject)
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


