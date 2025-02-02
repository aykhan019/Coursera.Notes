

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFRBWTR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSCUzGNcEBhtGrb3aLfq8WC04hbJDgpWMIf7v3AWPc2QIgW7PrrV3r9%2BTqJ%2F9OFvt1WmST7rkkxIIvhLIf3J7t%2BRsqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLi8YVJyWOw7BnNMsyrcA3OJAiiFa12FEoW5oaa9ZyiK%2FpjIeTG%2BsdRuCR52rmhIrfhRp1%2Bq88Vy8Iq5xXe2UtnfPgWa3Y3O%2FiULhWCOxZCsOh%2BTq71qb72SML3ZX9UpCE42IiihqWfjRra5HZ3Uc4yk785Z6PqvIgCWuQiYEC9kEeg8o7QrgmbBDM4LIIk%2FQt5OijCcAgGtLLqZlGNJl4oogCNCA42VSaOC9MFXsFj0uSNFUwskgZrqiEAUX7cCB0rrvGV0iY437CCvaeAMeKUiAeX%2BVwyih0fdZmYnJV1gOetmQTSH7rl7iabbcb28i33%2FaZqAQXUu9RKP17CicDT8wx37OkM0%2BBdw%2BanytH35ihGi3cLGe8%2Fof1P6Dem1UewWQgk6XMAL0%2Fh%2BdXA5kn9Nb0ykL1wIJkZyHH%2F8pp44ZiL8SncdMCiKisldOwsG7ylNxewwY9CXO88KeikZbuUj3aQbeNHWfndfCbuisAZX2CKF%2FtKCksRvodtTTQl3MfC8R4FWkvHA%2F7UBgqNut0PtWmUP4hwD%2Bk3XlPvpZ3GLZDukjr3v9iLJrZdQrn08DnNZfyK6HC4Goatr247YLAAxNuU3MNlTIv7SK%2BVN5yAhfso9YVrBB10GqzsUNqn%2FeptJLAwQbuuOZlVzMM%2Bb%2FLwGOqUBDD3K1j4FZ8J8x6%2FM0y13Kj%2FHdV8i9u%2BEdlpHVPDfLy%2F2pzHr92H4MOTlHdUGkAZKtsadSbq%2Fd3RUX5H4OhqPxrKQfwWl1wxIoQmpdeJztmhqAJRFwa0PQX64SjUoFKqQZ1h0aUv%2BgVruLfoECRXgpk6%2Fy3ZrarOn2GZyaSKwWbvwZ0pjMZaIkgK%2FLOFdlDRXv%2FUEqPDVSTtf6Qgi4b188LDSEuC1&X-Amz-Signature=844fd7f6e87ba725a2832a1fd1627b53b564ba3b47d96fd8e375e0e5f92a4f90&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWD6NP4A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDb%2FNj0FV6Ocwvj%2FAnwrsBdvzCm6V9wPQBrK92WOmJO6wIhAOeEnF4Jd6Vsn0hbWIQbY5XRp6m0M1p8hHxmlghgUfiVKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0HpCHWvphX61i6Rwq3ANtBofxLIOb7dEbcL0tZ2PC%2BWN3oulkxuP5JtznPK%2BywmSGx8NJkVgLphQhWmkigVF%2Bm8Iur2GQSulNiJBGnKkR6KyoMD7AodjoBwPTDc8lhH%2FSlGKoav3qQPk20GGdGPGHouJ%2BfNmFa6TxNofLZuLg%2F21QqRDTowQGo%2B0Yjbnysfx98WCZDuzi4oxU%2FWxHbhn69ooPF%2FdPHRgTtNSqmHT4Qtoery172fo8RpRO6l%2B42Q2gHX4QkYjR7T5xdW4njjb1fLdy1gm3qRA4%2B23D8WvWSLQcJnWQjZxP7BurK5ercssLLO%2BFcyqp5s0GL%2FQhQV%2BrkMSxopz1lJjZ6Ujmoe3p%2FHEAcJb8V4QTFIr1YV77euivp6FjMp8mcbEiNiGiVOpnpzbRkLYmkf8nsrrva44Df6WoTYc9M405xFBp3D9pl0szRiCU7iCH3Nq9InkLHgDfnny%2FUNTF98968Q28kdwnXh852guCmy3sm%2FucfMlvrBZWP9baH4ze5vPqVGT4ZgULCIiXCCl2ahQndcyxN2AG5FauHapIAnQr48xQdc2hAXZ4ioJXkN%2FEMcmqwrEtBsRybaq%2BBYBeoSvP7SmYGlproMN5ghBlINpF%2Fv9%2FhOPrMUU40ZTtbGdKGfJifjDYm%2Fy8BjqkAfUztNwSjWScpCf28k4Bp5L7dPPNhvQYpWHbpJMONbjSasAOWfnpuU7essA2GHALJocw4MAlKb2irPEsEFnIAWCMamYZbjuQ7vofMDxCbguPE51GEBjQ0MvnkqUWDaWSMUNuSZ6AqrUjNy5oLwdBv7PujDzAynDYPHWmi3w6gHpu4bS8cTGWOxH%2BW4DJhfDrHzS8%2BolcsSAlAG%2BCt6dX1mRRFUJr&X-Amz-Signature=ce34a4571f123dfb584cb11990539fa1662e224ef2ed32a6bef72efbd33b6efc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWD6NP4A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDb%2FNj0FV6Ocwvj%2FAnwrsBdvzCm6V9wPQBrK92WOmJO6wIhAOeEnF4Jd6Vsn0hbWIQbY5XRp6m0M1p8hHxmlghgUfiVKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0HpCHWvphX61i6Rwq3ANtBofxLIOb7dEbcL0tZ2PC%2BWN3oulkxuP5JtznPK%2BywmSGx8NJkVgLphQhWmkigVF%2Bm8Iur2GQSulNiJBGnKkR6KyoMD7AodjoBwPTDc8lhH%2FSlGKoav3qQPk20GGdGPGHouJ%2BfNmFa6TxNofLZuLg%2F21QqRDTowQGo%2B0Yjbnysfx98WCZDuzi4oxU%2FWxHbhn69ooPF%2FdPHRgTtNSqmHT4Qtoery172fo8RpRO6l%2B42Q2gHX4QkYjR7T5xdW4njjb1fLdy1gm3qRA4%2B23D8WvWSLQcJnWQjZxP7BurK5ercssLLO%2BFcyqp5s0GL%2FQhQV%2BrkMSxopz1lJjZ6Ujmoe3p%2FHEAcJb8V4QTFIr1YV77euivp6FjMp8mcbEiNiGiVOpnpzbRkLYmkf8nsrrva44Df6WoTYc9M405xFBp3D9pl0szRiCU7iCH3Nq9InkLHgDfnny%2FUNTF98968Q28kdwnXh852guCmy3sm%2FucfMlvrBZWP9baH4ze5vPqVGT4ZgULCIiXCCl2ahQndcyxN2AG5FauHapIAnQr48xQdc2hAXZ4ioJXkN%2FEMcmqwrEtBsRybaq%2BBYBeoSvP7SmYGlproMN5ghBlINpF%2Fv9%2FhOPrMUU40ZTtbGdKGfJifjDYm%2Fy8BjqkAfUztNwSjWScpCf28k4Bp5L7dPPNhvQYpWHbpJMONbjSasAOWfnpuU7essA2GHALJocw4MAlKb2irPEsEFnIAWCMamYZbjuQ7vofMDxCbguPE51GEBjQ0MvnkqUWDaWSMUNuSZ6AqrUjNy5oLwdBv7PujDzAynDYPHWmi3w6gHpu4bS8cTGWOxH%2BW4DJhfDrHzS8%2BolcsSAlAG%2BCt6dX1mRRFUJr&X-Amz-Signature=c384870b42c22d727b7fb0165caeac2e6a309577b990ef1900e162615809f54f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWD6NP4A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDb%2FNj0FV6Ocwvj%2FAnwrsBdvzCm6V9wPQBrK92WOmJO6wIhAOeEnF4Jd6Vsn0hbWIQbY5XRp6m0M1p8hHxmlghgUfiVKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0HpCHWvphX61i6Rwq3ANtBofxLIOb7dEbcL0tZ2PC%2BWN3oulkxuP5JtznPK%2BywmSGx8NJkVgLphQhWmkigVF%2Bm8Iur2GQSulNiJBGnKkR6KyoMD7AodjoBwPTDc8lhH%2FSlGKoav3qQPk20GGdGPGHouJ%2BfNmFa6TxNofLZuLg%2F21QqRDTowQGo%2B0Yjbnysfx98WCZDuzi4oxU%2FWxHbhn69ooPF%2FdPHRgTtNSqmHT4Qtoery172fo8RpRO6l%2B42Q2gHX4QkYjR7T5xdW4njjb1fLdy1gm3qRA4%2B23D8WvWSLQcJnWQjZxP7BurK5ercssLLO%2BFcyqp5s0GL%2FQhQV%2BrkMSxopz1lJjZ6Ujmoe3p%2FHEAcJb8V4QTFIr1YV77euivp6FjMp8mcbEiNiGiVOpnpzbRkLYmkf8nsrrva44Df6WoTYc9M405xFBp3D9pl0szRiCU7iCH3Nq9InkLHgDfnny%2FUNTF98968Q28kdwnXh852guCmy3sm%2FucfMlvrBZWP9baH4ze5vPqVGT4ZgULCIiXCCl2ahQndcyxN2AG5FauHapIAnQr48xQdc2hAXZ4ioJXkN%2FEMcmqwrEtBsRybaq%2BBYBeoSvP7SmYGlproMN5ghBlINpF%2Fv9%2FhOPrMUU40ZTtbGdKGfJifjDYm%2Fy8BjqkAfUztNwSjWScpCf28k4Bp5L7dPPNhvQYpWHbpJMONbjSasAOWfnpuU7essA2GHALJocw4MAlKb2irPEsEFnIAWCMamYZbjuQ7vofMDxCbguPE51GEBjQ0MvnkqUWDaWSMUNuSZ6AqrUjNy5oLwdBv7PujDzAynDYPHWmi3w6gHpu4bS8cTGWOxH%2BW4DJhfDrHzS8%2BolcsSAlAG%2BCt6dX1mRRFUJr&X-Amz-Signature=11c232aa2a5c83b98a4b3a979171c91caf747a9719d5b134d24fd38de539a7ac&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWD6NP4A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDb%2FNj0FV6Ocwvj%2FAnwrsBdvzCm6V9wPQBrK92WOmJO6wIhAOeEnF4Jd6Vsn0hbWIQbY5XRp6m0M1p8hHxmlghgUfiVKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0HpCHWvphX61i6Rwq3ANtBofxLIOb7dEbcL0tZ2PC%2BWN3oulkxuP5JtznPK%2BywmSGx8NJkVgLphQhWmkigVF%2Bm8Iur2GQSulNiJBGnKkR6KyoMD7AodjoBwPTDc8lhH%2FSlGKoav3qQPk20GGdGPGHouJ%2BfNmFa6TxNofLZuLg%2F21QqRDTowQGo%2B0Yjbnysfx98WCZDuzi4oxU%2FWxHbhn69ooPF%2FdPHRgTtNSqmHT4Qtoery172fo8RpRO6l%2B42Q2gHX4QkYjR7T5xdW4njjb1fLdy1gm3qRA4%2B23D8WvWSLQcJnWQjZxP7BurK5ercssLLO%2BFcyqp5s0GL%2FQhQV%2BrkMSxopz1lJjZ6Ujmoe3p%2FHEAcJb8V4QTFIr1YV77euivp6FjMp8mcbEiNiGiVOpnpzbRkLYmkf8nsrrva44Df6WoTYc9M405xFBp3D9pl0szRiCU7iCH3Nq9InkLHgDfnny%2FUNTF98968Q28kdwnXh852guCmy3sm%2FucfMlvrBZWP9baH4ze5vPqVGT4ZgULCIiXCCl2ahQndcyxN2AG5FauHapIAnQr48xQdc2hAXZ4ioJXkN%2FEMcmqwrEtBsRybaq%2BBYBeoSvP7SmYGlproMN5ghBlINpF%2Fv9%2FhOPrMUU40ZTtbGdKGfJifjDYm%2Fy8BjqkAfUztNwSjWScpCf28k4Bp5L7dPPNhvQYpWHbpJMONbjSasAOWfnpuU7essA2GHALJocw4MAlKb2irPEsEFnIAWCMamYZbjuQ7vofMDxCbguPE51GEBjQ0MvnkqUWDaWSMUNuSZ6AqrUjNy5oLwdBv7PujDzAynDYPHWmi3w6gHpu4bS8cTGWOxH%2BW4DJhfDrHzS8%2BolcsSAlAG%2BCt6dX1mRRFUJr&X-Amz-Signature=5b05ab9d648c703ddae0c4837a5cbeeca7c4f6cb71079d11dbb78220e1983a3d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWD6NP4A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDb%2FNj0FV6Ocwvj%2FAnwrsBdvzCm6V9wPQBrK92WOmJO6wIhAOeEnF4Jd6Vsn0hbWIQbY5XRp6m0M1p8hHxmlghgUfiVKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0HpCHWvphX61i6Rwq3ANtBofxLIOb7dEbcL0tZ2PC%2BWN3oulkxuP5JtznPK%2BywmSGx8NJkVgLphQhWmkigVF%2Bm8Iur2GQSulNiJBGnKkR6KyoMD7AodjoBwPTDc8lhH%2FSlGKoav3qQPk20GGdGPGHouJ%2BfNmFa6TxNofLZuLg%2F21QqRDTowQGo%2B0Yjbnysfx98WCZDuzi4oxU%2FWxHbhn69ooPF%2FdPHRgTtNSqmHT4Qtoery172fo8RpRO6l%2B42Q2gHX4QkYjR7T5xdW4njjb1fLdy1gm3qRA4%2B23D8WvWSLQcJnWQjZxP7BurK5ercssLLO%2BFcyqp5s0GL%2FQhQV%2BrkMSxopz1lJjZ6Ujmoe3p%2FHEAcJb8V4QTFIr1YV77euivp6FjMp8mcbEiNiGiVOpnpzbRkLYmkf8nsrrva44Df6WoTYc9M405xFBp3D9pl0szRiCU7iCH3Nq9InkLHgDfnny%2FUNTF98968Q28kdwnXh852guCmy3sm%2FucfMlvrBZWP9baH4ze5vPqVGT4ZgULCIiXCCl2ahQndcyxN2AG5FauHapIAnQr48xQdc2hAXZ4ioJXkN%2FEMcmqwrEtBsRybaq%2BBYBeoSvP7SmYGlproMN5ghBlINpF%2Fv9%2FhOPrMUU40ZTtbGdKGfJifjDYm%2Fy8BjqkAfUztNwSjWScpCf28k4Bp5L7dPPNhvQYpWHbpJMONbjSasAOWfnpuU7essA2GHALJocw4MAlKb2irPEsEFnIAWCMamYZbjuQ7vofMDxCbguPE51GEBjQ0MvnkqUWDaWSMUNuSZ6AqrUjNy5oLwdBv7PujDzAynDYPHWmi3w6gHpu4bS8cTGWOxH%2BW4DJhfDrHzS8%2BolcsSAlAG%2BCt6dX1mRRFUJr&X-Amz-Signature=2a527ed7a5da030265d84976323ad1863cc8208b6aa9da4bb892ff637536fb84&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFRBWTR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSCUzGNcEBhtGrb3aLfq8WC04hbJDgpWMIf7v3AWPc2QIgW7PrrV3r9%2BTqJ%2F9OFvt1WmST7rkkxIIvhLIf3J7t%2BRsqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLi8YVJyWOw7BnNMsyrcA3OJAiiFa12FEoW5oaa9ZyiK%2FpjIeTG%2BsdRuCR52rmhIrfhRp1%2Bq88Vy8Iq5xXe2UtnfPgWa3Y3O%2FiULhWCOxZCsOh%2BTq71qb72SML3ZX9UpCE42IiihqWfjRra5HZ3Uc4yk785Z6PqvIgCWuQiYEC9kEeg8o7QrgmbBDM4LIIk%2FQt5OijCcAgGtLLqZlGNJl4oogCNCA42VSaOC9MFXsFj0uSNFUwskgZrqiEAUX7cCB0rrvGV0iY437CCvaeAMeKUiAeX%2BVwyih0fdZmYnJV1gOetmQTSH7rl7iabbcb28i33%2FaZqAQXUu9RKP17CicDT8wx37OkM0%2BBdw%2BanytH35ihGi3cLGe8%2Fof1P6Dem1UewWQgk6XMAL0%2Fh%2BdXA5kn9Nb0ykL1wIJkZyHH%2F8pp44ZiL8SncdMCiKisldOwsG7ylNxewwY9CXO88KeikZbuUj3aQbeNHWfndfCbuisAZX2CKF%2FtKCksRvodtTTQl3MfC8R4FWkvHA%2F7UBgqNut0PtWmUP4hwD%2Bk3XlPvpZ3GLZDukjr3v9iLJrZdQrn08DnNZfyK6HC4Goatr247YLAAxNuU3MNlTIv7SK%2BVN5yAhfso9YVrBB10GqzsUNqn%2FeptJLAwQbuuOZlVzMM%2Bb%2FLwGOqUBDD3K1j4FZ8J8x6%2FM0y13Kj%2FHdV8i9u%2BEdlpHVPDfLy%2F2pzHr92H4MOTlHdUGkAZKtsadSbq%2Fd3RUX5H4OhqPxrKQfwWl1wxIoQmpdeJztmhqAJRFwa0PQX64SjUoFKqQZ1h0aUv%2BgVruLfoECRXgpk6%2Fy3ZrarOn2GZyaSKwWbvwZ0pjMZaIkgK%2FLOFdlDRXv%2FUEqPDVSTtf6Qgi4b188LDSEuC1&X-Amz-Signature=474401b24ffa0718ee2e4b00bb5d050162df1b102cfc701a80b5b86d3b7d5e05&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFRBWTR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSCUzGNcEBhtGrb3aLfq8WC04hbJDgpWMIf7v3AWPc2QIgW7PrrV3r9%2BTqJ%2F9OFvt1WmST7rkkxIIvhLIf3J7t%2BRsqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLi8YVJyWOw7BnNMsyrcA3OJAiiFa12FEoW5oaa9ZyiK%2FpjIeTG%2BsdRuCR52rmhIrfhRp1%2Bq88Vy8Iq5xXe2UtnfPgWa3Y3O%2FiULhWCOxZCsOh%2BTq71qb72SML3ZX9UpCE42IiihqWfjRra5HZ3Uc4yk785Z6PqvIgCWuQiYEC9kEeg8o7QrgmbBDM4LIIk%2FQt5OijCcAgGtLLqZlGNJl4oogCNCA42VSaOC9MFXsFj0uSNFUwskgZrqiEAUX7cCB0rrvGV0iY437CCvaeAMeKUiAeX%2BVwyih0fdZmYnJV1gOetmQTSH7rl7iabbcb28i33%2FaZqAQXUu9RKP17CicDT8wx37OkM0%2BBdw%2BanytH35ihGi3cLGe8%2Fof1P6Dem1UewWQgk6XMAL0%2Fh%2BdXA5kn9Nb0ykL1wIJkZyHH%2F8pp44ZiL8SncdMCiKisldOwsG7ylNxewwY9CXO88KeikZbuUj3aQbeNHWfndfCbuisAZX2CKF%2FtKCksRvodtTTQl3MfC8R4FWkvHA%2F7UBgqNut0PtWmUP4hwD%2Bk3XlPvpZ3GLZDukjr3v9iLJrZdQrn08DnNZfyK6HC4Goatr247YLAAxNuU3MNlTIv7SK%2BVN5yAhfso9YVrBB10GqzsUNqn%2FeptJLAwQbuuOZlVzMM%2Bb%2FLwGOqUBDD3K1j4FZ8J8x6%2FM0y13Kj%2FHdV8i9u%2BEdlpHVPDfLy%2F2pzHr92H4MOTlHdUGkAZKtsadSbq%2Fd3RUX5H4OhqPxrKQfwWl1wxIoQmpdeJztmhqAJRFwa0PQX64SjUoFKqQZ1h0aUv%2BgVruLfoECRXgpk6%2Fy3ZrarOn2GZyaSKwWbvwZ0pjMZaIkgK%2FLOFdlDRXv%2FUEqPDVSTtf6Qgi4b188LDSEuC1&X-Amz-Signature=db6fa92da2b6c1031ea870744fe3b0ace3b68fa96152203243040803a373f709&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFRBWTR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSCUzGNcEBhtGrb3aLfq8WC04hbJDgpWMIf7v3AWPc2QIgW7PrrV3r9%2BTqJ%2F9OFvt1WmST7rkkxIIvhLIf3J7t%2BRsqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLi8YVJyWOw7BnNMsyrcA3OJAiiFa12FEoW5oaa9ZyiK%2FpjIeTG%2BsdRuCR52rmhIrfhRp1%2Bq88Vy8Iq5xXe2UtnfPgWa3Y3O%2FiULhWCOxZCsOh%2BTq71qb72SML3ZX9UpCE42IiihqWfjRra5HZ3Uc4yk785Z6PqvIgCWuQiYEC9kEeg8o7QrgmbBDM4LIIk%2FQt5OijCcAgGtLLqZlGNJl4oogCNCA42VSaOC9MFXsFj0uSNFUwskgZrqiEAUX7cCB0rrvGV0iY437CCvaeAMeKUiAeX%2BVwyih0fdZmYnJV1gOetmQTSH7rl7iabbcb28i33%2FaZqAQXUu9RKP17CicDT8wx37OkM0%2BBdw%2BanytH35ihGi3cLGe8%2Fof1P6Dem1UewWQgk6XMAL0%2Fh%2BdXA5kn9Nb0ykL1wIJkZyHH%2F8pp44ZiL8SncdMCiKisldOwsG7ylNxewwY9CXO88KeikZbuUj3aQbeNHWfndfCbuisAZX2CKF%2FtKCksRvodtTTQl3MfC8R4FWkvHA%2F7UBgqNut0PtWmUP4hwD%2Bk3XlPvpZ3GLZDukjr3v9iLJrZdQrn08DnNZfyK6HC4Goatr247YLAAxNuU3MNlTIv7SK%2BVN5yAhfso9YVrBB10GqzsUNqn%2FeptJLAwQbuuOZlVzMM%2Bb%2FLwGOqUBDD3K1j4FZ8J8x6%2FM0y13Kj%2FHdV8i9u%2BEdlpHVPDfLy%2F2pzHr92H4MOTlHdUGkAZKtsadSbq%2Fd3RUX5H4OhqPxrKQfwWl1wxIoQmpdeJztmhqAJRFwa0PQX64SjUoFKqQZ1h0aUv%2BgVruLfoECRXgpk6%2Fy3ZrarOn2GZyaSKwWbvwZ0pjMZaIkgK%2FLOFdlDRXv%2FUEqPDVSTtf6Qgi4b188LDSEuC1&X-Amz-Signature=549359909bdaea48c0760026d465cbf7e798f0ce0ddb5620e7602bb051359d4f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFRBWTR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSCUzGNcEBhtGrb3aLfq8WC04hbJDgpWMIf7v3AWPc2QIgW7PrrV3r9%2BTqJ%2F9OFvt1WmST7rkkxIIvhLIf3J7t%2BRsqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLi8YVJyWOw7BnNMsyrcA3OJAiiFa12FEoW5oaa9ZyiK%2FpjIeTG%2BsdRuCR52rmhIrfhRp1%2Bq88Vy8Iq5xXe2UtnfPgWa3Y3O%2FiULhWCOxZCsOh%2BTq71qb72SML3ZX9UpCE42IiihqWfjRra5HZ3Uc4yk785Z6PqvIgCWuQiYEC9kEeg8o7QrgmbBDM4LIIk%2FQt5OijCcAgGtLLqZlGNJl4oogCNCA42VSaOC9MFXsFj0uSNFUwskgZrqiEAUX7cCB0rrvGV0iY437CCvaeAMeKUiAeX%2BVwyih0fdZmYnJV1gOetmQTSH7rl7iabbcb28i33%2FaZqAQXUu9RKP17CicDT8wx37OkM0%2BBdw%2BanytH35ihGi3cLGe8%2Fof1P6Dem1UewWQgk6XMAL0%2Fh%2BdXA5kn9Nb0ykL1wIJkZyHH%2F8pp44ZiL8SncdMCiKisldOwsG7ylNxewwY9CXO88KeikZbuUj3aQbeNHWfndfCbuisAZX2CKF%2FtKCksRvodtTTQl3MfC8R4FWkvHA%2F7UBgqNut0PtWmUP4hwD%2Bk3XlPvpZ3GLZDukjr3v9iLJrZdQrn08DnNZfyK6HC4Goatr247YLAAxNuU3MNlTIv7SK%2BVN5yAhfso9YVrBB10GqzsUNqn%2FeptJLAwQbuuOZlVzMM%2Bb%2FLwGOqUBDD3K1j4FZ8J8x6%2FM0y13Kj%2FHdV8i9u%2BEdlpHVPDfLy%2F2pzHr92H4MOTlHdUGkAZKtsadSbq%2Fd3RUX5H4OhqPxrKQfwWl1wxIoQmpdeJztmhqAJRFwa0PQX64SjUoFKqQZ1h0aUv%2BgVruLfoECRXgpk6%2Fy3ZrarOn2GZyaSKwWbvwZ0pjMZaIkgK%2FLOFdlDRXv%2FUEqPDVSTtf6Qgi4b188LDSEuC1&X-Amz-Signature=267313b7108b06724eba321f2cdf3b69717097645be3e48d877e375993033e87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFRBWTR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSCUzGNcEBhtGrb3aLfq8WC04hbJDgpWMIf7v3AWPc2QIgW7PrrV3r9%2BTqJ%2F9OFvt1WmST7rkkxIIvhLIf3J7t%2BRsqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLi8YVJyWOw7BnNMsyrcA3OJAiiFa12FEoW5oaa9ZyiK%2FpjIeTG%2BsdRuCR52rmhIrfhRp1%2Bq88Vy8Iq5xXe2UtnfPgWa3Y3O%2FiULhWCOxZCsOh%2BTq71qb72SML3ZX9UpCE42IiihqWfjRra5HZ3Uc4yk785Z6PqvIgCWuQiYEC9kEeg8o7QrgmbBDM4LIIk%2FQt5OijCcAgGtLLqZlGNJl4oogCNCA42VSaOC9MFXsFj0uSNFUwskgZrqiEAUX7cCB0rrvGV0iY437CCvaeAMeKUiAeX%2BVwyih0fdZmYnJV1gOetmQTSH7rl7iabbcb28i33%2FaZqAQXUu9RKP17CicDT8wx37OkM0%2BBdw%2BanytH35ihGi3cLGe8%2Fof1P6Dem1UewWQgk6XMAL0%2Fh%2BdXA5kn9Nb0ykL1wIJkZyHH%2F8pp44ZiL8SncdMCiKisldOwsG7ylNxewwY9CXO88KeikZbuUj3aQbeNHWfndfCbuisAZX2CKF%2FtKCksRvodtTTQl3MfC8R4FWkvHA%2F7UBgqNut0PtWmUP4hwD%2Bk3XlPvpZ3GLZDukjr3v9iLJrZdQrn08DnNZfyK6HC4Goatr247YLAAxNuU3MNlTIv7SK%2BVN5yAhfso9YVrBB10GqzsUNqn%2FeptJLAwQbuuOZlVzMM%2Bb%2FLwGOqUBDD3K1j4FZ8J8x6%2FM0y13Kj%2FHdV8i9u%2BEdlpHVPDfLy%2F2pzHr92H4MOTlHdUGkAZKtsadSbq%2Fd3RUX5H4OhqPxrKQfwWl1wxIoQmpdeJztmhqAJRFwa0PQX64SjUoFKqQZ1h0aUv%2BgVruLfoECRXgpk6%2Fy3ZrarOn2GZyaSKwWbvwZ0pjMZaIkgK%2FLOFdlDRXv%2FUEqPDVSTtf6Qgi4b188LDSEuC1&X-Amz-Signature=26ddf356790ee4b5661063091b2c43ea67a826d9f4a7dead9a01a7e5cdc1d023&X-Amz-SignedHeaders=host&x-id=GetObject)
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


