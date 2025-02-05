

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEBWNTS3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICtBsXNkihG%2BMXDwr6K1VT2%2B73ex4vETpGd2RfOwuelnAiAVynF0HOFsCGpLeBwABDVX%2Fn6vFoVwj%2FVnujlpCkz9YSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIML4XNd5OytNcka0L3KtwD2Dfx8nN8OJKvH3klHjOKml444wec59UfVoiZ25V420%2BXOjxSLbkMXJD6%2B7Vncpt4WKckg3mDn%2BgFZ8fBOTMLiLrcgNZtN2bTMFouQFW%2BMgiMSCfgbJWbanp3RegdzkNaRE%2FW2MPd3R5LIv9JLwothUWqbbZsqpUG2lpD%2Fuc1dK8eo%2BbR4bRD%2Btsc0lBOw%2Bj7BrKjYDBXvOlSrJRhjvI%2Fnis9cF8koI5KrdZKxLyUy3UmYMk0cQDe3VSpv4rtBiU%2BgZuuyctxcRqTIT1AOPYbTvcjopA06nL7%2BKBkRJsYohBtKpiCiCQuuhmb2C6dF9zTq1AhhnuWP4ytcD8sX38kdbj6LhOIhi%2BSThnGGeP4pz1XGXFfYM3EHIFbDglFO3awYoJIXDWHKOiVs%2BXyEsk%2FcfnUNxzepQxvFdrCrfFH%2B33rFLUeFjLBZ00cCmQfjU7NRE8LPok7ywC0eKiIMOiLzOhGlAD4apQxDRyu1L8GrbT0kgcPBmjvF5dmBka82LSKUIDqizR%2FEscE%2FxxmIKTxSPNUy5MMJgeIyj4sSdnIsjCWHvKNAsr5zsRATkHf7KidbjvVYJgChAnFwf%2FehRBZoA%2BUJ0FK0yoRlhA8%2F9vXkls%2B%2F%2Focc0f5G1kw3tUwks%2BMvQY6pgHF3x2KG%2FrQ7DFdje4dmRUMZo8q4iXIdaKwtMSPxpzbHAdvQhulm%2BqhvXvVayxTc6lOOcS%2F3ZHn4bdqKCetUso4A44hSC3ABu2ZTJaq7g%2Bd4LPCvStNXOa02Ya9iyysl%2BFcTfFny1YBXyQ50JA05kNqVX%2BLAgAwvODW3o1kFWCRZ14gmzXKIP1CeDLAN9Y0IrNBk4%2BRBv6QcfHlTMIFjLE3XDIelnhr&X-Amz-Signature=473c4f0d043eabda16760ccf19592c978e8442a313f10c36edcd4d56317a1759&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23XII72%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIGRsnQEf9gOUdPK3JFSv39NUwcXdajs7nFL6jKDnBpPHAiBXcMAPNmQMUmNKvuzQ1g7HPdGyDz0o5o%2FHMiUj5IASuyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMgjfHKomRVaFBYV3NKtwD6Kaj0PtfE6OkPBPdrKbQsvq33eJPSkKMIEG1QrEo3Kv2kL5RK2wvFgbVhSt8apCBrVHo4MpT%2BBZAoqI23oVgvmbErVt9FPJ84g7GeKbHS6OOf64stM8vQwn2MWk4evHh901ekcwhbnJXkjcWQvZGTgKXftcXkwtJf5Oc3UsMWqJxX7NdHLERiQk8y021YwBvuhilRlKnkmJChljlNl7mncEqK6RX7feHqMW1JN4jNTYh35U95oUT0GJ%2FdEQOhCdZndD3vad8NbiDJqhHEXoXZbRp2x7pKwwOz7Shpw%2BwAZs2ot3EpACMthS3q5qOuH6jt24qD%2B5dQg1369%2FGHX5HAbvIOOJ58k9By%2F%2B7Emv4ZvanEO1e70f7PJwQe6wPnGOJDnmRax7pDrtJZatZeed3bCqQPgdAwwKIjfpmY3QAR5iGjlxq6zy6Sh7OCNkKxTV7Ii2xYCfPMEFsPpcW3h6xNG6nqcHJ5bJxdjMqJ9f%2BmwlRLR8Ro0KfLtrOlWUD9BbzVoZeI7dj2OE1tmt%2BjHT1EXPdMSOWDWe92n%2F4VYt6TKhR9qwPhaXhfeu%2FuNeEf8wM6swW77%2B8aP4lroa1HPS1KFgr933XLLSP53TF2AaQCHKbePLiDCnxZ2BIpNUwx8%2BMvQY6pgEROb%2B0FKM9C9qlDmup%2BQoTw%2B8810B5%2FgJ%2FT0J668r%2BJ4A7twvhYRI7QSO8phpIZid3e8NEhT%2FQC8h80nDYS7m48T9niOxLO%2FxGxkQMCJoIGvPmKGEVXkza%2BcYRyMl2Y%2BLgSL6b1vOF565pHI6%2BorwsFivmRvLOuu1CDJVeVELzUliyLIbW6kaNv%2FBTV3CRXILFE7W9n3GRhfeQoIgXWWOxlCAlQ2p5&X-Amz-Signature=46fdd3c50bab87450b724857f54cb9e7751108786dddb6cc87bcf7d40e2239c2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23XII72%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIGRsnQEf9gOUdPK3JFSv39NUwcXdajs7nFL6jKDnBpPHAiBXcMAPNmQMUmNKvuzQ1g7HPdGyDz0o5o%2FHMiUj5IASuyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMgjfHKomRVaFBYV3NKtwD6Kaj0PtfE6OkPBPdrKbQsvq33eJPSkKMIEG1QrEo3Kv2kL5RK2wvFgbVhSt8apCBrVHo4MpT%2BBZAoqI23oVgvmbErVt9FPJ84g7GeKbHS6OOf64stM8vQwn2MWk4evHh901ekcwhbnJXkjcWQvZGTgKXftcXkwtJf5Oc3UsMWqJxX7NdHLERiQk8y021YwBvuhilRlKnkmJChljlNl7mncEqK6RX7feHqMW1JN4jNTYh35U95oUT0GJ%2FdEQOhCdZndD3vad8NbiDJqhHEXoXZbRp2x7pKwwOz7Shpw%2BwAZs2ot3EpACMthS3q5qOuH6jt24qD%2B5dQg1369%2FGHX5HAbvIOOJ58k9By%2F%2B7Emv4ZvanEO1e70f7PJwQe6wPnGOJDnmRax7pDrtJZatZeed3bCqQPgdAwwKIjfpmY3QAR5iGjlxq6zy6Sh7OCNkKxTV7Ii2xYCfPMEFsPpcW3h6xNG6nqcHJ5bJxdjMqJ9f%2BmwlRLR8Ro0KfLtrOlWUD9BbzVoZeI7dj2OE1tmt%2BjHT1EXPdMSOWDWe92n%2F4VYt6TKhR9qwPhaXhfeu%2FuNeEf8wM6swW77%2B8aP4lroa1HPS1KFgr933XLLSP53TF2AaQCHKbePLiDCnxZ2BIpNUwx8%2BMvQY6pgEROb%2B0FKM9C9qlDmup%2BQoTw%2B8810B5%2FgJ%2FT0J668r%2BJ4A7twvhYRI7QSO8phpIZid3e8NEhT%2FQC8h80nDYS7m48T9niOxLO%2FxGxkQMCJoIGvPmKGEVXkza%2BcYRyMl2Y%2BLgSL6b1vOF565pHI6%2BorwsFivmRvLOuu1CDJVeVELzUliyLIbW6kaNv%2FBTV3CRXILFE7W9n3GRhfeQoIgXWWOxlCAlQ2p5&X-Amz-Signature=045e0b19f8137a3060393eebfa3bf658d4779c1a306bd2cdff8e037f61f341f4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23XII72%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIGRsnQEf9gOUdPK3JFSv39NUwcXdajs7nFL6jKDnBpPHAiBXcMAPNmQMUmNKvuzQ1g7HPdGyDz0o5o%2FHMiUj5IASuyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMgjfHKomRVaFBYV3NKtwD6Kaj0PtfE6OkPBPdrKbQsvq33eJPSkKMIEG1QrEo3Kv2kL5RK2wvFgbVhSt8apCBrVHo4MpT%2BBZAoqI23oVgvmbErVt9FPJ84g7GeKbHS6OOf64stM8vQwn2MWk4evHh901ekcwhbnJXkjcWQvZGTgKXftcXkwtJf5Oc3UsMWqJxX7NdHLERiQk8y021YwBvuhilRlKnkmJChljlNl7mncEqK6RX7feHqMW1JN4jNTYh35U95oUT0GJ%2FdEQOhCdZndD3vad8NbiDJqhHEXoXZbRp2x7pKwwOz7Shpw%2BwAZs2ot3EpACMthS3q5qOuH6jt24qD%2B5dQg1369%2FGHX5HAbvIOOJ58k9By%2F%2B7Emv4ZvanEO1e70f7PJwQe6wPnGOJDnmRax7pDrtJZatZeed3bCqQPgdAwwKIjfpmY3QAR5iGjlxq6zy6Sh7OCNkKxTV7Ii2xYCfPMEFsPpcW3h6xNG6nqcHJ5bJxdjMqJ9f%2BmwlRLR8Ro0KfLtrOlWUD9BbzVoZeI7dj2OE1tmt%2BjHT1EXPdMSOWDWe92n%2F4VYt6TKhR9qwPhaXhfeu%2FuNeEf8wM6swW77%2B8aP4lroa1HPS1KFgr933XLLSP53TF2AaQCHKbePLiDCnxZ2BIpNUwx8%2BMvQY6pgEROb%2B0FKM9C9qlDmup%2BQoTw%2B8810B5%2FgJ%2FT0J668r%2BJ4A7twvhYRI7QSO8phpIZid3e8NEhT%2FQC8h80nDYS7m48T9niOxLO%2FxGxkQMCJoIGvPmKGEVXkza%2BcYRyMl2Y%2BLgSL6b1vOF565pHI6%2BorwsFivmRvLOuu1CDJVeVELzUliyLIbW6kaNv%2FBTV3CRXILFE7W9n3GRhfeQoIgXWWOxlCAlQ2p5&X-Amz-Signature=5bd4911094a580bb63e9493b9163ee8d9c85a20a18ffa0a7003ca658150d3aff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23XII72%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIGRsnQEf9gOUdPK3JFSv39NUwcXdajs7nFL6jKDnBpPHAiBXcMAPNmQMUmNKvuzQ1g7HPdGyDz0o5o%2FHMiUj5IASuyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMgjfHKomRVaFBYV3NKtwD6Kaj0PtfE6OkPBPdrKbQsvq33eJPSkKMIEG1QrEo3Kv2kL5RK2wvFgbVhSt8apCBrVHo4MpT%2BBZAoqI23oVgvmbErVt9FPJ84g7GeKbHS6OOf64stM8vQwn2MWk4evHh901ekcwhbnJXkjcWQvZGTgKXftcXkwtJf5Oc3UsMWqJxX7NdHLERiQk8y021YwBvuhilRlKnkmJChljlNl7mncEqK6RX7feHqMW1JN4jNTYh35U95oUT0GJ%2FdEQOhCdZndD3vad8NbiDJqhHEXoXZbRp2x7pKwwOz7Shpw%2BwAZs2ot3EpACMthS3q5qOuH6jt24qD%2B5dQg1369%2FGHX5HAbvIOOJ58k9By%2F%2B7Emv4ZvanEO1e70f7PJwQe6wPnGOJDnmRax7pDrtJZatZeed3bCqQPgdAwwKIjfpmY3QAR5iGjlxq6zy6Sh7OCNkKxTV7Ii2xYCfPMEFsPpcW3h6xNG6nqcHJ5bJxdjMqJ9f%2BmwlRLR8Ro0KfLtrOlWUD9BbzVoZeI7dj2OE1tmt%2BjHT1EXPdMSOWDWe92n%2F4VYt6TKhR9qwPhaXhfeu%2FuNeEf8wM6swW77%2B8aP4lroa1HPS1KFgr933XLLSP53TF2AaQCHKbePLiDCnxZ2BIpNUwx8%2BMvQY6pgEROb%2B0FKM9C9qlDmup%2BQoTw%2B8810B5%2FgJ%2FT0J668r%2BJ4A7twvhYRI7QSO8phpIZid3e8NEhT%2FQC8h80nDYS7m48T9niOxLO%2FxGxkQMCJoIGvPmKGEVXkza%2BcYRyMl2Y%2BLgSL6b1vOF565pHI6%2BorwsFivmRvLOuu1CDJVeVELzUliyLIbW6kaNv%2FBTV3CRXILFE7W9n3GRhfeQoIgXWWOxlCAlQ2p5&X-Amz-Signature=0778475a1db6eadc13634e98be508b9ca611b66475742bd362e4d54c709f9b56&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23XII72%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIGRsnQEf9gOUdPK3JFSv39NUwcXdajs7nFL6jKDnBpPHAiBXcMAPNmQMUmNKvuzQ1g7HPdGyDz0o5o%2FHMiUj5IASuyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMgjfHKomRVaFBYV3NKtwD6Kaj0PtfE6OkPBPdrKbQsvq33eJPSkKMIEG1QrEo3Kv2kL5RK2wvFgbVhSt8apCBrVHo4MpT%2BBZAoqI23oVgvmbErVt9FPJ84g7GeKbHS6OOf64stM8vQwn2MWk4evHh901ekcwhbnJXkjcWQvZGTgKXftcXkwtJf5Oc3UsMWqJxX7NdHLERiQk8y021YwBvuhilRlKnkmJChljlNl7mncEqK6RX7feHqMW1JN4jNTYh35U95oUT0GJ%2FdEQOhCdZndD3vad8NbiDJqhHEXoXZbRp2x7pKwwOz7Shpw%2BwAZs2ot3EpACMthS3q5qOuH6jt24qD%2B5dQg1369%2FGHX5HAbvIOOJ58k9By%2F%2B7Emv4ZvanEO1e70f7PJwQe6wPnGOJDnmRax7pDrtJZatZeed3bCqQPgdAwwKIjfpmY3QAR5iGjlxq6zy6Sh7OCNkKxTV7Ii2xYCfPMEFsPpcW3h6xNG6nqcHJ5bJxdjMqJ9f%2BmwlRLR8Ro0KfLtrOlWUD9BbzVoZeI7dj2OE1tmt%2BjHT1EXPdMSOWDWe92n%2F4VYt6TKhR9qwPhaXhfeu%2FuNeEf8wM6swW77%2B8aP4lroa1HPS1KFgr933XLLSP53TF2AaQCHKbePLiDCnxZ2BIpNUwx8%2BMvQY6pgEROb%2B0FKM9C9qlDmup%2BQoTw%2B8810B5%2FgJ%2FT0J668r%2BJ4A7twvhYRI7QSO8phpIZid3e8NEhT%2FQC8h80nDYS7m48T9niOxLO%2FxGxkQMCJoIGvPmKGEVXkza%2BcYRyMl2Y%2BLgSL6b1vOF565pHI6%2BorwsFivmRvLOuu1CDJVeVELzUliyLIbW6kaNv%2FBTV3CRXILFE7W9n3GRhfeQoIgXWWOxlCAlQ2p5&X-Amz-Signature=a2dea4fce675f242a757e0062836470f9ce1cb5daabdd4ce6fff2ec0b30f3baa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEBWNTS3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICtBsXNkihG%2BMXDwr6K1VT2%2B73ex4vETpGd2RfOwuelnAiAVynF0HOFsCGpLeBwABDVX%2Fn6vFoVwj%2FVnujlpCkz9YSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIML4XNd5OytNcka0L3KtwD2Dfx8nN8OJKvH3klHjOKml444wec59UfVoiZ25V420%2BXOjxSLbkMXJD6%2B7Vncpt4WKckg3mDn%2BgFZ8fBOTMLiLrcgNZtN2bTMFouQFW%2BMgiMSCfgbJWbanp3RegdzkNaRE%2FW2MPd3R5LIv9JLwothUWqbbZsqpUG2lpD%2Fuc1dK8eo%2BbR4bRD%2Btsc0lBOw%2Bj7BrKjYDBXvOlSrJRhjvI%2Fnis9cF8koI5KrdZKxLyUy3UmYMk0cQDe3VSpv4rtBiU%2BgZuuyctxcRqTIT1AOPYbTvcjopA06nL7%2BKBkRJsYohBtKpiCiCQuuhmb2C6dF9zTq1AhhnuWP4ytcD8sX38kdbj6LhOIhi%2BSThnGGeP4pz1XGXFfYM3EHIFbDglFO3awYoJIXDWHKOiVs%2BXyEsk%2FcfnUNxzepQxvFdrCrfFH%2B33rFLUeFjLBZ00cCmQfjU7NRE8LPok7ywC0eKiIMOiLzOhGlAD4apQxDRyu1L8GrbT0kgcPBmjvF5dmBka82LSKUIDqizR%2FEscE%2FxxmIKTxSPNUy5MMJgeIyj4sSdnIsjCWHvKNAsr5zsRATkHf7KidbjvVYJgChAnFwf%2FehRBZoA%2BUJ0FK0yoRlhA8%2F9vXkls%2B%2F%2Focc0f5G1kw3tUwks%2BMvQY6pgHF3x2KG%2FrQ7DFdje4dmRUMZo8q4iXIdaKwtMSPxpzbHAdvQhulm%2BqhvXvVayxTc6lOOcS%2F3ZHn4bdqKCetUso4A44hSC3ABu2ZTJaq7g%2Bd4LPCvStNXOa02Ya9iyysl%2BFcTfFny1YBXyQ50JA05kNqVX%2BLAgAwvODW3o1kFWCRZ14gmzXKIP1CeDLAN9Y0IrNBk4%2BRBv6QcfHlTMIFjLE3XDIelnhr&X-Amz-Signature=5da3d6c374396b6dc14236edb56c67a203a5be65a562f1af92bc190385b97d41&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEBWNTS3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICtBsXNkihG%2BMXDwr6K1VT2%2B73ex4vETpGd2RfOwuelnAiAVynF0HOFsCGpLeBwABDVX%2Fn6vFoVwj%2FVnujlpCkz9YSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIML4XNd5OytNcka0L3KtwD2Dfx8nN8OJKvH3klHjOKml444wec59UfVoiZ25V420%2BXOjxSLbkMXJD6%2B7Vncpt4WKckg3mDn%2BgFZ8fBOTMLiLrcgNZtN2bTMFouQFW%2BMgiMSCfgbJWbanp3RegdzkNaRE%2FW2MPd3R5LIv9JLwothUWqbbZsqpUG2lpD%2Fuc1dK8eo%2BbR4bRD%2Btsc0lBOw%2Bj7BrKjYDBXvOlSrJRhjvI%2Fnis9cF8koI5KrdZKxLyUy3UmYMk0cQDe3VSpv4rtBiU%2BgZuuyctxcRqTIT1AOPYbTvcjopA06nL7%2BKBkRJsYohBtKpiCiCQuuhmb2C6dF9zTq1AhhnuWP4ytcD8sX38kdbj6LhOIhi%2BSThnGGeP4pz1XGXFfYM3EHIFbDglFO3awYoJIXDWHKOiVs%2BXyEsk%2FcfnUNxzepQxvFdrCrfFH%2B33rFLUeFjLBZ00cCmQfjU7NRE8LPok7ywC0eKiIMOiLzOhGlAD4apQxDRyu1L8GrbT0kgcPBmjvF5dmBka82LSKUIDqizR%2FEscE%2FxxmIKTxSPNUy5MMJgeIyj4sSdnIsjCWHvKNAsr5zsRATkHf7KidbjvVYJgChAnFwf%2FehRBZoA%2BUJ0FK0yoRlhA8%2F9vXkls%2B%2F%2Focc0f5G1kw3tUwks%2BMvQY6pgHF3x2KG%2FrQ7DFdje4dmRUMZo8q4iXIdaKwtMSPxpzbHAdvQhulm%2BqhvXvVayxTc6lOOcS%2F3ZHn4bdqKCetUso4A44hSC3ABu2ZTJaq7g%2Bd4LPCvStNXOa02Ya9iyysl%2BFcTfFny1YBXyQ50JA05kNqVX%2BLAgAwvODW3o1kFWCRZ14gmzXKIP1CeDLAN9Y0IrNBk4%2BRBv6QcfHlTMIFjLE3XDIelnhr&X-Amz-Signature=836fe807431fa392bca657fa17f21ada27b102697d573c2dd000558a2c9a3dae&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEBWNTS3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICtBsXNkihG%2BMXDwr6K1VT2%2B73ex4vETpGd2RfOwuelnAiAVynF0HOFsCGpLeBwABDVX%2Fn6vFoVwj%2FVnujlpCkz9YSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIML4XNd5OytNcka0L3KtwD2Dfx8nN8OJKvH3klHjOKml444wec59UfVoiZ25V420%2BXOjxSLbkMXJD6%2B7Vncpt4WKckg3mDn%2BgFZ8fBOTMLiLrcgNZtN2bTMFouQFW%2BMgiMSCfgbJWbanp3RegdzkNaRE%2FW2MPd3R5LIv9JLwothUWqbbZsqpUG2lpD%2Fuc1dK8eo%2BbR4bRD%2Btsc0lBOw%2Bj7BrKjYDBXvOlSrJRhjvI%2Fnis9cF8koI5KrdZKxLyUy3UmYMk0cQDe3VSpv4rtBiU%2BgZuuyctxcRqTIT1AOPYbTvcjopA06nL7%2BKBkRJsYohBtKpiCiCQuuhmb2C6dF9zTq1AhhnuWP4ytcD8sX38kdbj6LhOIhi%2BSThnGGeP4pz1XGXFfYM3EHIFbDglFO3awYoJIXDWHKOiVs%2BXyEsk%2FcfnUNxzepQxvFdrCrfFH%2B33rFLUeFjLBZ00cCmQfjU7NRE8LPok7ywC0eKiIMOiLzOhGlAD4apQxDRyu1L8GrbT0kgcPBmjvF5dmBka82LSKUIDqizR%2FEscE%2FxxmIKTxSPNUy5MMJgeIyj4sSdnIsjCWHvKNAsr5zsRATkHf7KidbjvVYJgChAnFwf%2FehRBZoA%2BUJ0FK0yoRlhA8%2F9vXkls%2B%2F%2Focc0f5G1kw3tUwks%2BMvQY6pgHF3x2KG%2FrQ7DFdje4dmRUMZo8q4iXIdaKwtMSPxpzbHAdvQhulm%2BqhvXvVayxTc6lOOcS%2F3ZHn4bdqKCetUso4A44hSC3ABu2ZTJaq7g%2Bd4LPCvStNXOa02Ya9iyysl%2BFcTfFny1YBXyQ50JA05kNqVX%2BLAgAwvODW3o1kFWCRZ14gmzXKIP1CeDLAN9Y0IrNBk4%2BRBv6QcfHlTMIFjLE3XDIelnhr&X-Amz-Signature=f4de1c6bfecab72f7b1ef3e1a39b2ea9f459efa6f312391bb0242241229b018b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEBWNTS3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICtBsXNkihG%2BMXDwr6K1VT2%2B73ex4vETpGd2RfOwuelnAiAVynF0HOFsCGpLeBwABDVX%2Fn6vFoVwj%2FVnujlpCkz9YSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIML4XNd5OytNcka0L3KtwD2Dfx8nN8OJKvH3klHjOKml444wec59UfVoiZ25V420%2BXOjxSLbkMXJD6%2B7Vncpt4WKckg3mDn%2BgFZ8fBOTMLiLrcgNZtN2bTMFouQFW%2BMgiMSCfgbJWbanp3RegdzkNaRE%2FW2MPd3R5LIv9JLwothUWqbbZsqpUG2lpD%2Fuc1dK8eo%2BbR4bRD%2Btsc0lBOw%2Bj7BrKjYDBXvOlSrJRhjvI%2Fnis9cF8koI5KrdZKxLyUy3UmYMk0cQDe3VSpv4rtBiU%2BgZuuyctxcRqTIT1AOPYbTvcjopA06nL7%2BKBkRJsYohBtKpiCiCQuuhmb2C6dF9zTq1AhhnuWP4ytcD8sX38kdbj6LhOIhi%2BSThnGGeP4pz1XGXFfYM3EHIFbDglFO3awYoJIXDWHKOiVs%2BXyEsk%2FcfnUNxzepQxvFdrCrfFH%2B33rFLUeFjLBZ00cCmQfjU7NRE8LPok7ywC0eKiIMOiLzOhGlAD4apQxDRyu1L8GrbT0kgcPBmjvF5dmBka82LSKUIDqizR%2FEscE%2FxxmIKTxSPNUy5MMJgeIyj4sSdnIsjCWHvKNAsr5zsRATkHf7KidbjvVYJgChAnFwf%2FehRBZoA%2BUJ0FK0yoRlhA8%2F9vXkls%2B%2F%2Focc0f5G1kw3tUwks%2BMvQY6pgHF3x2KG%2FrQ7DFdje4dmRUMZo8q4iXIdaKwtMSPxpzbHAdvQhulm%2BqhvXvVayxTc6lOOcS%2F3ZHn4bdqKCetUso4A44hSC3ABu2ZTJaq7g%2Bd4LPCvStNXOa02Ya9iyysl%2BFcTfFny1YBXyQ50JA05kNqVX%2BLAgAwvODW3o1kFWCRZ14gmzXKIP1CeDLAN9Y0IrNBk4%2BRBv6QcfHlTMIFjLE3XDIelnhr&X-Amz-Signature=ffce07c6eebc466f10d1f5d9178300b6e3ad623e8ac6d32e50e8ce48eb00d67d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEBWNTS3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICtBsXNkihG%2BMXDwr6K1VT2%2B73ex4vETpGd2RfOwuelnAiAVynF0HOFsCGpLeBwABDVX%2Fn6vFoVwj%2FVnujlpCkz9YSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIML4XNd5OytNcka0L3KtwD2Dfx8nN8OJKvH3klHjOKml444wec59UfVoiZ25V420%2BXOjxSLbkMXJD6%2B7Vncpt4WKckg3mDn%2BgFZ8fBOTMLiLrcgNZtN2bTMFouQFW%2BMgiMSCfgbJWbanp3RegdzkNaRE%2FW2MPd3R5LIv9JLwothUWqbbZsqpUG2lpD%2Fuc1dK8eo%2BbR4bRD%2Btsc0lBOw%2Bj7BrKjYDBXvOlSrJRhjvI%2Fnis9cF8koI5KrdZKxLyUy3UmYMk0cQDe3VSpv4rtBiU%2BgZuuyctxcRqTIT1AOPYbTvcjopA06nL7%2BKBkRJsYohBtKpiCiCQuuhmb2C6dF9zTq1AhhnuWP4ytcD8sX38kdbj6LhOIhi%2BSThnGGeP4pz1XGXFfYM3EHIFbDglFO3awYoJIXDWHKOiVs%2BXyEsk%2FcfnUNxzepQxvFdrCrfFH%2B33rFLUeFjLBZ00cCmQfjU7NRE8LPok7ywC0eKiIMOiLzOhGlAD4apQxDRyu1L8GrbT0kgcPBmjvF5dmBka82LSKUIDqizR%2FEscE%2FxxmIKTxSPNUy5MMJgeIyj4sSdnIsjCWHvKNAsr5zsRATkHf7KidbjvVYJgChAnFwf%2FehRBZoA%2BUJ0FK0yoRlhA8%2F9vXkls%2B%2F%2Focc0f5G1kw3tUwks%2BMvQY6pgHF3x2KG%2FrQ7DFdje4dmRUMZo8q4iXIdaKwtMSPxpzbHAdvQhulm%2BqhvXvVayxTc6lOOcS%2F3ZHn4bdqKCetUso4A44hSC3ABu2ZTJaq7g%2Bd4LPCvStNXOa02Ya9iyysl%2BFcTfFny1YBXyQ50JA05kNqVX%2BLAgAwvODW3o1kFWCRZ14gmzXKIP1CeDLAN9Y0IrNBk4%2BRBv6QcfHlTMIFjLE3XDIelnhr&X-Amz-Signature=4175dc9047fd642f5d6b907f02e663e0f7aa13f14f019b9f7695d1e1676e8eda&X-Amz-SignedHeaders=host&x-id=GetObject)
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


