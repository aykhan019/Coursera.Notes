

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNIODOQZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFL7DPQztTu%2FDxysLdU5RrRPVar8q9Iiak83GRAGiJ97AiEA7ANvVKeOrpPmgdy%2FeHJmNj66IjM8SyOg3%2BD32JW0JEEqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZbongiAzgh%2BjCuvCrcA5pR1LUxwaqKHYVeojhlEr0oSxOtAOzsxgWA9nZok1flg%2B9nmHaLwAQTukctaP5CbwjM4DwK1GoAKMNHoB%2BA2ivSc6hVu0z%2F%2F0FgIOCVymxEO0WFORDTYGOyjGkMTh7tYep86zSgNSneNqbKTQyGz2qpH2zsdImZ81OXHk37j5ZOps98HpQF64JIrxZq6RrhuYguzcfWfq1v3f6JxKd1%2FmfEdRvIX3KQCBW00ddmRcPcqQa9N9h3plnVI0KjeFPeToShgCgowEiOXL8PSJ%2BY13qPpVexxpmE0zCz0GYey1t%2BVjm%2FdzpkBq%2BLPuasMvmWFO3%2Be6vYpL2Q6R3vH%2B7RVAUhSjSY%2Bnuzyd%2FKWL61QGOt0TWtrGkOsE5zjLeX7mVQkGdAU51JEMsgJWAFLeyZAXYzrCdVC5DorBaIxqXd1ZbX0uTBDrmp03UFPAg0nmfhJo8UqzH9PEznZ6QpXcYckM09lEJ6Gza47%2B24d5m02n8OgDTiEEF8hL3njkyB0MGI0adD4JIttMaNjeNMcKct0mF7NxoUyrSAKyKVGX3nYIvrQNjOih9GN38Uvv%2FFIFKOLypdXHvg6pN3%2FCr%2BDNb63CDV9loHyulDa6GqOrifBbMj%2F4gBaTxOljKDFx9uMJ7s9bwGOqUBe%2BE%2Fqz4g%2FAk5ZUFjsK6eFMW4mKsPpvuFZ4mQb4mQgU6Q1%2BVsS1IpUPCaBazG0qOIvn2IQQJM0kPJ6jJTt5fHJYU09LiH7bBVVeOBhiPPk0KwepdD4OmAumFlUTWkfWjHwRdmNS5eCmqaXafkYk3VhR2BgbIbD002XXNE%2B1v9dclkGaqF61jgPcUHKFiLARi3eqZJMv3486PnPDVMKQDz6ywVtMKl&X-Amz-Signature=cc83ae3e5447127af53af910ec3138f77afa2a01dc550948a7f102f0bab11b43&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DIFJRT2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FbjXFAEE2x5E9M9Sm%2BVl10wxjtb2w7QDXOUEYR8PHaAiAfCepy3qvP7EEbSE%2BEAWOT0OKvOJ0jUbK4GNm1X3TvwSqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhbv%2F4qbQcJ%2BCX2hSKtwDvZqJyxktIbtP%2FOkHiyoZr9KZKr%2Fhbkag3b7TsD9HPHIYCsF2N%2BC7D1E7JYAKDHKI9tSPgWcT0InPF338mnwawWlIiG0lmVW2ItdIhdT6iCoPkrnpjD0IhHYTsdtqK%2Flm9T9ZfRzZuKHamSEWzPamxvn1N7B6aXftAhbL8q7CM%2F5yonVQnCKafAz6YY2%2F%2B2ZaXbpwqkikdyjsqB4G3RJ6%2FJRJD5tz9DHRlU6fWDeozjavXCyAMC3Oflm2JH4mcA3mYFYjw44HfCgg3zanCbN%2BAD8CUE1igTnNLf2MSpY5hc1EMwIFeUYEY9oGexoIZfPsvdZh5cqnjmOHt5mK%2FOjUDil7G3Zw2DkadCAhdeRuMhAYC2EF%2FuHUo7%2BPLq%2BxHmusg9CSCyDNXObtEe3qzG4ICkLBIqTi7z0n7OT1Z8nYDEt7PgIKfrrcIAXqHy2%2FXo4%2B4VPVP%2FvDflghx7PeH743spQR9NeDsoL1EHg8Og3%2BI1tXZkNcey9KIqpno1womc2bkou9xnEZCzOwwy%2BggUnLmisH9FOR%2FF1oA0jXkpzevlBbix%2FdoDfo77X7h45g5k12jxyzRob87sS0noYDVI9O40AqABpNR0jFH66%2BNoncuWWAul1rqxaqG%2BKtHrsw4%2Bz1vAY6pgFLI0bO4jlLA%2FlksSH83ntM4DvNqyLbhhEhsKmxuD3VjOzYSjaVc2iKKRn%2FYn%2F54bu3HeWfkDhqkvvJvjoTs%2FwM%2BJJQWsWsYMlBBKFeDQyzs90P3z49JN678FMAJXwVB2vjnk0NkMCC8A3gtAxcXwro7ePueNBiSntZdlk9JTarn7Odsi%2B9xZjpAnoh7sDpgHlQUttBjbBSuGdlPoGIjfYID75Nh%2BFK&X-Amz-Signature=178c44140727931935b7c457932069ccfc9fdbef869492906160d75ae9b52aec&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DIFJRT2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FbjXFAEE2x5E9M9Sm%2BVl10wxjtb2w7QDXOUEYR8PHaAiAfCepy3qvP7EEbSE%2BEAWOT0OKvOJ0jUbK4GNm1X3TvwSqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhbv%2F4qbQcJ%2BCX2hSKtwDvZqJyxktIbtP%2FOkHiyoZr9KZKr%2Fhbkag3b7TsD9HPHIYCsF2N%2BC7D1E7JYAKDHKI9tSPgWcT0InPF338mnwawWlIiG0lmVW2ItdIhdT6iCoPkrnpjD0IhHYTsdtqK%2Flm9T9ZfRzZuKHamSEWzPamxvn1N7B6aXftAhbL8q7CM%2F5yonVQnCKafAz6YY2%2F%2B2ZaXbpwqkikdyjsqB4G3RJ6%2FJRJD5tz9DHRlU6fWDeozjavXCyAMC3Oflm2JH4mcA3mYFYjw44HfCgg3zanCbN%2BAD8CUE1igTnNLf2MSpY5hc1EMwIFeUYEY9oGexoIZfPsvdZh5cqnjmOHt5mK%2FOjUDil7G3Zw2DkadCAhdeRuMhAYC2EF%2FuHUo7%2BPLq%2BxHmusg9CSCyDNXObtEe3qzG4ICkLBIqTi7z0n7OT1Z8nYDEt7PgIKfrrcIAXqHy2%2FXo4%2B4VPVP%2FvDflghx7PeH743spQR9NeDsoL1EHg8Og3%2BI1tXZkNcey9KIqpno1womc2bkou9xnEZCzOwwy%2BggUnLmisH9FOR%2FF1oA0jXkpzevlBbix%2FdoDfo77X7h45g5k12jxyzRob87sS0noYDVI9O40AqABpNR0jFH66%2BNoncuWWAul1rqxaqG%2BKtHrsw4%2Bz1vAY6pgFLI0bO4jlLA%2FlksSH83ntM4DvNqyLbhhEhsKmxuD3VjOzYSjaVc2iKKRn%2FYn%2F54bu3HeWfkDhqkvvJvjoTs%2FwM%2BJJQWsWsYMlBBKFeDQyzs90P3z49JN678FMAJXwVB2vjnk0NkMCC8A3gtAxcXwro7ePueNBiSntZdlk9JTarn7Odsi%2B9xZjpAnoh7sDpgHlQUttBjbBSuGdlPoGIjfYID75Nh%2BFK&X-Amz-Signature=f564288c63cbf4b43e853c4c7e3db345bc13175074f343cd756c966a83dea012&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DIFJRT2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FbjXFAEE2x5E9M9Sm%2BVl10wxjtb2w7QDXOUEYR8PHaAiAfCepy3qvP7EEbSE%2BEAWOT0OKvOJ0jUbK4GNm1X3TvwSqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhbv%2F4qbQcJ%2BCX2hSKtwDvZqJyxktIbtP%2FOkHiyoZr9KZKr%2Fhbkag3b7TsD9HPHIYCsF2N%2BC7D1E7JYAKDHKI9tSPgWcT0InPF338mnwawWlIiG0lmVW2ItdIhdT6iCoPkrnpjD0IhHYTsdtqK%2Flm9T9ZfRzZuKHamSEWzPamxvn1N7B6aXftAhbL8q7CM%2F5yonVQnCKafAz6YY2%2F%2B2ZaXbpwqkikdyjsqB4G3RJ6%2FJRJD5tz9DHRlU6fWDeozjavXCyAMC3Oflm2JH4mcA3mYFYjw44HfCgg3zanCbN%2BAD8CUE1igTnNLf2MSpY5hc1EMwIFeUYEY9oGexoIZfPsvdZh5cqnjmOHt5mK%2FOjUDil7G3Zw2DkadCAhdeRuMhAYC2EF%2FuHUo7%2BPLq%2BxHmusg9CSCyDNXObtEe3qzG4ICkLBIqTi7z0n7OT1Z8nYDEt7PgIKfrrcIAXqHy2%2FXo4%2B4VPVP%2FvDflghx7PeH743spQR9NeDsoL1EHg8Og3%2BI1tXZkNcey9KIqpno1womc2bkou9xnEZCzOwwy%2BggUnLmisH9FOR%2FF1oA0jXkpzevlBbix%2FdoDfo77X7h45g5k12jxyzRob87sS0noYDVI9O40AqABpNR0jFH66%2BNoncuWWAul1rqxaqG%2BKtHrsw4%2Bz1vAY6pgFLI0bO4jlLA%2FlksSH83ntM4DvNqyLbhhEhsKmxuD3VjOzYSjaVc2iKKRn%2FYn%2F54bu3HeWfkDhqkvvJvjoTs%2FwM%2BJJQWsWsYMlBBKFeDQyzs90P3z49JN678FMAJXwVB2vjnk0NkMCC8A3gtAxcXwro7ePueNBiSntZdlk9JTarn7Odsi%2B9xZjpAnoh7sDpgHlQUttBjbBSuGdlPoGIjfYID75Nh%2BFK&X-Amz-Signature=953a25ee6091f81766cab095da9c42a4adc787ebd533cb3736f52a68a9a8fb75&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DIFJRT2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FbjXFAEE2x5E9M9Sm%2BVl10wxjtb2w7QDXOUEYR8PHaAiAfCepy3qvP7EEbSE%2BEAWOT0OKvOJ0jUbK4GNm1X3TvwSqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhbv%2F4qbQcJ%2BCX2hSKtwDvZqJyxktIbtP%2FOkHiyoZr9KZKr%2Fhbkag3b7TsD9HPHIYCsF2N%2BC7D1E7JYAKDHKI9tSPgWcT0InPF338mnwawWlIiG0lmVW2ItdIhdT6iCoPkrnpjD0IhHYTsdtqK%2Flm9T9ZfRzZuKHamSEWzPamxvn1N7B6aXftAhbL8q7CM%2F5yonVQnCKafAz6YY2%2F%2B2ZaXbpwqkikdyjsqB4G3RJ6%2FJRJD5tz9DHRlU6fWDeozjavXCyAMC3Oflm2JH4mcA3mYFYjw44HfCgg3zanCbN%2BAD8CUE1igTnNLf2MSpY5hc1EMwIFeUYEY9oGexoIZfPsvdZh5cqnjmOHt5mK%2FOjUDil7G3Zw2DkadCAhdeRuMhAYC2EF%2FuHUo7%2BPLq%2BxHmusg9CSCyDNXObtEe3qzG4ICkLBIqTi7z0n7OT1Z8nYDEt7PgIKfrrcIAXqHy2%2FXo4%2B4VPVP%2FvDflghx7PeH743spQR9NeDsoL1EHg8Og3%2BI1tXZkNcey9KIqpno1womc2bkou9xnEZCzOwwy%2BggUnLmisH9FOR%2FF1oA0jXkpzevlBbix%2FdoDfo77X7h45g5k12jxyzRob87sS0noYDVI9O40AqABpNR0jFH66%2BNoncuWWAul1rqxaqG%2BKtHrsw4%2Bz1vAY6pgFLI0bO4jlLA%2FlksSH83ntM4DvNqyLbhhEhsKmxuD3VjOzYSjaVc2iKKRn%2FYn%2F54bu3HeWfkDhqkvvJvjoTs%2FwM%2BJJQWsWsYMlBBKFeDQyzs90P3z49JN678FMAJXwVB2vjnk0NkMCC8A3gtAxcXwro7ePueNBiSntZdlk9JTarn7Odsi%2B9xZjpAnoh7sDpgHlQUttBjbBSuGdlPoGIjfYID75Nh%2BFK&X-Amz-Signature=0adfcf69bc5fdf6c96dea60716780967797305f897d0eee81a7bf300a28c6534&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DIFJRT2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FbjXFAEE2x5E9M9Sm%2BVl10wxjtb2w7QDXOUEYR8PHaAiAfCepy3qvP7EEbSE%2BEAWOT0OKvOJ0jUbK4GNm1X3TvwSqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhbv%2F4qbQcJ%2BCX2hSKtwDvZqJyxktIbtP%2FOkHiyoZr9KZKr%2Fhbkag3b7TsD9HPHIYCsF2N%2BC7D1E7JYAKDHKI9tSPgWcT0InPF338mnwawWlIiG0lmVW2ItdIhdT6iCoPkrnpjD0IhHYTsdtqK%2Flm9T9ZfRzZuKHamSEWzPamxvn1N7B6aXftAhbL8q7CM%2F5yonVQnCKafAz6YY2%2F%2B2ZaXbpwqkikdyjsqB4G3RJ6%2FJRJD5tz9DHRlU6fWDeozjavXCyAMC3Oflm2JH4mcA3mYFYjw44HfCgg3zanCbN%2BAD8CUE1igTnNLf2MSpY5hc1EMwIFeUYEY9oGexoIZfPsvdZh5cqnjmOHt5mK%2FOjUDil7G3Zw2DkadCAhdeRuMhAYC2EF%2FuHUo7%2BPLq%2BxHmusg9CSCyDNXObtEe3qzG4ICkLBIqTi7z0n7OT1Z8nYDEt7PgIKfrrcIAXqHy2%2FXo4%2B4VPVP%2FvDflghx7PeH743spQR9NeDsoL1EHg8Og3%2BI1tXZkNcey9KIqpno1womc2bkou9xnEZCzOwwy%2BggUnLmisH9FOR%2FF1oA0jXkpzevlBbix%2FdoDfo77X7h45g5k12jxyzRob87sS0noYDVI9O40AqABpNR0jFH66%2BNoncuWWAul1rqxaqG%2BKtHrsw4%2Bz1vAY6pgFLI0bO4jlLA%2FlksSH83ntM4DvNqyLbhhEhsKmxuD3VjOzYSjaVc2iKKRn%2FYn%2F54bu3HeWfkDhqkvvJvjoTs%2FwM%2BJJQWsWsYMlBBKFeDQyzs90P3z49JN678FMAJXwVB2vjnk0NkMCC8A3gtAxcXwro7ePueNBiSntZdlk9JTarn7Odsi%2B9xZjpAnoh7sDpgHlQUttBjbBSuGdlPoGIjfYID75Nh%2BFK&X-Amz-Signature=e37fd3520ea665e21e6647268da13ad9edec848c3709a98decb2db5e33a0d72b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNIODOQZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFL7DPQztTu%2FDxysLdU5RrRPVar8q9Iiak83GRAGiJ97AiEA7ANvVKeOrpPmgdy%2FeHJmNj66IjM8SyOg3%2BD32JW0JEEqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZbongiAzgh%2BjCuvCrcA5pR1LUxwaqKHYVeojhlEr0oSxOtAOzsxgWA9nZok1flg%2B9nmHaLwAQTukctaP5CbwjM4DwK1GoAKMNHoB%2BA2ivSc6hVu0z%2F%2F0FgIOCVymxEO0WFORDTYGOyjGkMTh7tYep86zSgNSneNqbKTQyGz2qpH2zsdImZ81OXHk37j5ZOps98HpQF64JIrxZq6RrhuYguzcfWfq1v3f6JxKd1%2FmfEdRvIX3KQCBW00ddmRcPcqQa9N9h3plnVI0KjeFPeToShgCgowEiOXL8PSJ%2BY13qPpVexxpmE0zCz0GYey1t%2BVjm%2FdzpkBq%2BLPuasMvmWFO3%2Be6vYpL2Q6R3vH%2B7RVAUhSjSY%2Bnuzyd%2FKWL61QGOt0TWtrGkOsE5zjLeX7mVQkGdAU51JEMsgJWAFLeyZAXYzrCdVC5DorBaIxqXd1ZbX0uTBDrmp03UFPAg0nmfhJo8UqzH9PEznZ6QpXcYckM09lEJ6Gza47%2B24d5m02n8OgDTiEEF8hL3njkyB0MGI0adD4JIttMaNjeNMcKct0mF7NxoUyrSAKyKVGX3nYIvrQNjOih9GN38Uvv%2FFIFKOLypdXHvg6pN3%2FCr%2BDNb63CDV9loHyulDa6GqOrifBbMj%2F4gBaTxOljKDFx9uMJ7s9bwGOqUBe%2BE%2Fqz4g%2FAk5ZUFjsK6eFMW4mKsPpvuFZ4mQb4mQgU6Q1%2BVsS1IpUPCaBazG0qOIvn2IQQJM0kPJ6jJTt5fHJYU09LiH7bBVVeOBhiPPk0KwepdD4OmAumFlUTWkfWjHwRdmNS5eCmqaXafkYk3VhR2BgbIbD002XXNE%2B1v9dclkGaqF61jgPcUHKFiLARi3eqZJMv3486PnPDVMKQDz6ywVtMKl&X-Amz-Signature=ca72e87aa8304a2164222b31ec0e80fb9a2dbf608df4f8edef42cb3ba6fbab1e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNIODOQZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFL7DPQztTu%2FDxysLdU5RrRPVar8q9Iiak83GRAGiJ97AiEA7ANvVKeOrpPmgdy%2FeHJmNj66IjM8SyOg3%2BD32JW0JEEqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZbongiAzgh%2BjCuvCrcA5pR1LUxwaqKHYVeojhlEr0oSxOtAOzsxgWA9nZok1flg%2B9nmHaLwAQTukctaP5CbwjM4DwK1GoAKMNHoB%2BA2ivSc6hVu0z%2F%2F0FgIOCVymxEO0WFORDTYGOyjGkMTh7tYep86zSgNSneNqbKTQyGz2qpH2zsdImZ81OXHk37j5ZOps98HpQF64JIrxZq6RrhuYguzcfWfq1v3f6JxKd1%2FmfEdRvIX3KQCBW00ddmRcPcqQa9N9h3plnVI0KjeFPeToShgCgowEiOXL8PSJ%2BY13qPpVexxpmE0zCz0GYey1t%2BVjm%2FdzpkBq%2BLPuasMvmWFO3%2Be6vYpL2Q6R3vH%2B7RVAUhSjSY%2Bnuzyd%2FKWL61QGOt0TWtrGkOsE5zjLeX7mVQkGdAU51JEMsgJWAFLeyZAXYzrCdVC5DorBaIxqXd1ZbX0uTBDrmp03UFPAg0nmfhJo8UqzH9PEznZ6QpXcYckM09lEJ6Gza47%2B24d5m02n8OgDTiEEF8hL3njkyB0MGI0adD4JIttMaNjeNMcKct0mF7NxoUyrSAKyKVGX3nYIvrQNjOih9GN38Uvv%2FFIFKOLypdXHvg6pN3%2FCr%2BDNb63CDV9loHyulDa6GqOrifBbMj%2F4gBaTxOljKDFx9uMJ7s9bwGOqUBe%2BE%2Fqz4g%2FAk5ZUFjsK6eFMW4mKsPpvuFZ4mQb4mQgU6Q1%2BVsS1IpUPCaBazG0qOIvn2IQQJM0kPJ6jJTt5fHJYU09LiH7bBVVeOBhiPPk0KwepdD4OmAumFlUTWkfWjHwRdmNS5eCmqaXafkYk3VhR2BgbIbD002XXNE%2B1v9dclkGaqF61jgPcUHKFiLARi3eqZJMv3486PnPDVMKQDz6ywVtMKl&X-Amz-Signature=276a184d83aaae7b0621cb61d8e61b6a98e28da38429303f4f10b9fe35b9f196&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNIODOQZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFL7DPQztTu%2FDxysLdU5RrRPVar8q9Iiak83GRAGiJ97AiEA7ANvVKeOrpPmgdy%2FeHJmNj66IjM8SyOg3%2BD32JW0JEEqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZbongiAzgh%2BjCuvCrcA5pR1LUxwaqKHYVeojhlEr0oSxOtAOzsxgWA9nZok1flg%2B9nmHaLwAQTukctaP5CbwjM4DwK1GoAKMNHoB%2BA2ivSc6hVu0z%2F%2F0FgIOCVymxEO0WFORDTYGOyjGkMTh7tYep86zSgNSneNqbKTQyGz2qpH2zsdImZ81OXHk37j5ZOps98HpQF64JIrxZq6RrhuYguzcfWfq1v3f6JxKd1%2FmfEdRvIX3KQCBW00ddmRcPcqQa9N9h3plnVI0KjeFPeToShgCgowEiOXL8PSJ%2BY13qPpVexxpmE0zCz0GYey1t%2BVjm%2FdzpkBq%2BLPuasMvmWFO3%2Be6vYpL2Q6R3vH%2B7RVAUhSjSY%2Bnuzyd%2FKWL61QGOt0TWtrGkOsE5zjLeX7mVQkGdAU51JEMsgJWAFLeyZAXYzrCdVC5DorBaIxqXd1ZbX0uTBDrmp03UFPAg0nmfhJo8UqzH9PEznZ6QpXcYckM09lEJ6Gza47%2B24d5m02n8OgDTiEEF8hL3njkyB0MGI0adD4JIttMaNjeNMcKct0mF7NxoUyrSAKyKVGX3nYIvrQNjOih9GN38Uvv%2FFIFKOLypdXHvg6pN3%2FCr%2BDNb63CDV9loHyulDa6GqOrifBbMj%2F4gBaTxOljKDFx9uMJ7s9bwGOqUBe%2BE%2Fqz4g%2FAk5ZUFjsK6eFMW4mKsPpvuFZ4mQb4mQgU6Q1%2BVsS1IpUPCaBazG0qOIvn2IQQJM0kPJ6jJTt5fHJYU09LiH7bBVVeOBhiPPk0KwepdD4OmAumFlUTWkfWjHwRdmNS5eCmqaXafkYk3VhR2BgbIbD002XXNE%2B1v9dclkGaqF61jgPcUHKFiLARi3eqZJMv3486PnPDVMKQDz6ywVtMKl&X-Amz-Signature=3d98fc9da8a023defa3928b324f1fbf1e1e49655e7978101aba4272f538a6a93&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNIODOQZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFL7DPQztTu%2FDxysLdU5RrRPVar8q9Iiak83GRAGiJ97AiEA7ANvVKeOrpPmgdy%2FeHJmNj66IjM8SyOg3%2BD32JW0JEEqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZbongiAzgh%2BjCuvCrcA5pR1LUxwaqKHYVeojhlEr0oSxOtAOzsxgWA9nZok1flg%2B9nmHaLwAQTukctaP5CbwjM4DwK1GoAKMNHoB%2BA2ivSc6hVu0z%2F%2F0FgIOCVymxEO0WFORDTYGOyjGkMTh7tYep86zSgNSneNqbKTQyGz2qpH2zsdImZ81OXHk37j5ZOps98HpQF64JIrxZq6RrhuYguzcfWfq1v3f6JxKd1%2FmfEdRvIX3KQCBW00ddmRcPcqQa9N9h3plnVI0KjeFPeToShgCgowEiOXL8PSJ%2BY13qPpVexxpmE0zCz0GYey1t%2BVjm%2FdzpkBq%2BLPuasMvmWFO3%2Be6vYpL2Q6R3vH%2B7RVAUhSjSY%2Bnuzyd%2FKWL61QGOt0TWtrGkOsE5zjLeX7mVQkGdAU51JEMsgJWAFLeyZAXYzrCdVC5DorBaIxqXd1ZbX0uTBDrmp03UFPAg0nmfhJo8UqzH9PEznZ6QpXcYckM09lEJ6Gza47%2B24d5m02n8OgDTiEEF8hL3njkyB0MGI0adD4JIttMaNjeNMcKct0mF7NxoUyrSAKyKVGX3nYIvrQNjOih9GN38Uvv%2FFIFKOLypdXHvg6pN3%2FCr%2BDNb63CDV9loHyulDa6GqOrifBbMj%2F4gBaTxOljKDFx9uMJ7s9bwGOqUBe%2BE%2Fqz4g%2FAk5ZUFjsK6eFMW4mKsPpvuFZ4mQb4mQgU6Q1%2BVsS1IpUPCaBazG0qOIvn2IQQJM0kPJ6jJTt5fHJYU09LiH7bBVVeOBhiPPk0KwepdD4OmAumFlUTWkfWjHwRdmNS5eCmqaXafkYk3VhR2BgbIbD002XXNE%2B1v9dclkGaqF61jgPcUHKFiLARi3eqZJMv3486PnPDVMKQDz6ywVtMKl&X-Amz-Signature=68aff18fcaf67589574811c8cc6e35f761562ece3214df3bd3565ed4267bd730&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNIODOQZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFL7DPQztTu%2FDxysLdU5RrRPVar8q9Iiak83GRAGiJ97AiEA7ANvVKeOrpPmgdy%2FeHJmNj66IjM8SyOg3%2BD32JW0JEEqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZbongiAzgh%2BjCuvCrcA5pR1LUxwaqKHYVeojhlEr0oSxOtAOzsxgWA9nZok1flg%2B9nmHaLwAQTukctaP5CbwjM4DwK1GoAKMNHoB%2BA2ivSc6hVu0z%2F%2F0FgIOCVymxEO0WFORDTYGOyjGkMTh7tYep86zSgNSneNqbKTQyGz2qpH2zsdImZ81OXHk37j5ZOps98HpQF64JIrxZq6RrhuYguzcfWfq1v3f6JxKd1%2FmfEdRvIX3KQCBW00ddmRcPcqQa9N9h3plnVI0KjeFPeToShgCgowEiOXL8PSJ%2BY13qPpVexxpmE0zCz0GYey1t%2BVjm%2FdzpkBq%2BLPuasMvmWFO3%2Be6vYpL2Q6R3vH%2B7RVAUhSjSY%2Bnuzyd%2FKWL61QGOt0TWtrGkOsE5zjLeX7mVQkGdAU51JEMsgJWAFLeyZAXYzrCdVC5DorBaIxqXd1ZbX0uTBDrmp03UFPAg0nmfhJo8UqzH9PEznZ6QpXcYckM09lEJ6Gza47%2B24d5m02n8OgDTiEEF8hL3njkyB0MGI0adD4JIttMaNjeNMcKct0mF7NxoUyrSAKyKVGX3nYIvrQNjOih9GN38Uvv%2FFIFKOLypdXHvg6pN3%2FCr%2BDNb63CDV9loHyulDa6GqOrifBbMj%2F4gBaTxOljKDFx9uMJ7s9bwGOqUBe%2BE%2Fqz4g%2FAk5ZUFjsK6eFMW4mKsPpvuFZ4mQb4mQgU6Q1%2BVsS1IpUPCaBazG0qOIvn2IQQJM0kPJ6jJTt5fHJYU09LiH7bBVVeOBhiPPk0KwepdD4OmAumFlUTWkfWjHwRdmNS5eCmqaXafkYk3VhR2BgbIbD002XXNE%2B1v9dclkGaqF61jgPcUHKFiLARi3eqZJMv3486PnPDVMKQDz6ywVtMKl&X-Amz-Signature=b474e3b3aaffe2c3673de2c58b2da963968511fa196e0b4939c7d766c5013856&X-Amz-SignedHeaders=host&x-id=GetObject)
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


