

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7BLRMGL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqVExUqD%2FHYc664Sev2H172KFdWi6PH3SIs8kSQwvkFQIgfoIVzdJu6V3zQRhQxvkjyAJMBvBTUeJQKF%2FqqUJGucgq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMVw5QqF0dJPaDXZTSrcA09ryxvNzyPx1TsIMDywKDvF8erJjL7dfL6IwP4l7%2B7y7PBT2%2BkFHZTp3QHKU5jimHeLxFu6w7oVtA002H6gPSwp%2F8xmKeuUEbINQ5QwBk23FkIUv6glok2YdT13mSS1RNsMdXvhpNo0K%2BO1skRpPSYjRF8CHeG9x8z6Wcsqc4EoaSVQH95PG76TYI2%2FNyNyAk9OMoPiGaDz9mKmDRP%2FsYWY1v%2BlPbTzjdRvKxwCajnaCV0VkFbFe34Gdn5z8gOFv8iOLw4DXoHgGQvT2E%2FiHfa%2BHNPHbiG7HOD59WJ7eLrucsMKeXWHj%2FKdk0ev6K9DZXIBXk0NZVROpWi23wob1hL57Qfh6euzFfZOR6RrHVRU3M7eJAWlGEY24BMRwn1RTOhtwJ2MvEci%2Fa5LDYP%2FOLSYF7FnU3kQV6NtWeFvZ1ubbKT8DLVS7CQdwCxAF1cVLiLemBpaYkFf83cUEhR5%2F48cPyl53DCr%2BeBxiL5xqfPylJdDuoozt1OHAqPACfBzoGFopJGzk790Ln8FXT7ajTGzamBrvP1J%2BniAy9VuSZn9cC1h0nxJ8zLabbG8B7bgAPqg3CWWD7h%2Bq6enHzmoUYkUazCxbxku3DZsTVwKhNI%2FnPcKCLHTxNuiDSTtMNzSgr0GOqUB2xc8AH8doU9I15ECloGYb4CWh85IjV67cwqvT%2BIRJD1vnYoPyA6jMpp6sB0DEy8gDqnSEHJINwycL8l5vEE8UNJSpsW%2BA2ns%2FG5EukWsjV3eMmbT5U5TLwiDyC7XBiQWnCm9bxQLwKP%2FyuQsHXArE8xU8z1s8siY7cigpVACHoOd%2BxRu9cyVC8A5noRK3B1eHiKeAheLyz4DDoxaEPDpztgE5w6G&X-Amz-Signature=feae13c2ac5427d385fa460ad738559b40e62adbfcd9c78ab2bb1970cc53f378&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YUHI3ED%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHuQD8tWDdyN6H094hxJkly%2FEXneszER%2FvXQceOb%2FVvNAiBy71J7K5kPS49%2BLxLUfcGvfHyGHMMSH%2F8cPdGvwQAlVCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMWVW8fqeMTK5wvWn4KtwDUtpcqpHKBA8meBFx2AYPVdUxNOZFEuZIObQVP8X4b0%2FMOr3mz%2Bpf9XUrGFyydJ3qvUwlzaRt2OwAKo4lqayDirIDoG2xzbpzVpJRNGC3jCJTgXzuV2w9L61leI6rii%2BGEbnu5OHHkiXl0lIltFhudpJoJoPe1m1e9ceRfpvtp9pnI91rEDQjtVSdBWh%2FxGELXosqf1L9uPoqf0EVmO7p%2BV8GR9D03tuMTNpRZI3yLLCCnUN%2FPK8eWuPN4DdM9WW9hXfpX03iBhdNkf0EqEuMRmZZvY8gTNCv3QNOUZSckDGgVnpBDYzCZnOi80Hb3EW1WVMNmzOfy%2FCUFjPF874ZH5tBPjdHFXMSZltaGak3DjW2ZYU3JWysEmCxywtb%2FaPGGUiDHG2OTlQXtqdaON9I7i7H2I335HKohlWiOtjssnT9UlMX5xgkHeON4zQZ%2Fqh2TN8Rl%2FvITPULgxwcItYD0LMdpFOHTZT3hSE4m1UJ8Hp0%2Ff%2FRieq%2BqCOnRoc%2BTtIFOi1KVnzEK7j7MRKKr9ws0zYYJHJcErh%2Blu5j%2BNTO9UbGwlB4AB0t8G7ArpMiunBMoH6K%2BkIYd5knKTsPPEIY6YvfNNJqFrS3G37FSzZE7Drel6R9p5q8NsUFq%2FQw%2F9KCvQY6pgFXEz1Tg2D9iu9M40NqDJv9EUfPd13LFkncv3NginXrj0jJUaaM1MTrxuzR%2F5YPQwHHpS5HFre%2BGGHiTjr%2Bh8wZleQTxenxb8KhKnPTwJKT5FXkUyUYQ8YHueC0aZkhCpS%2BiWmmJeS8f0HPyH4FUr0FAH%2B%2FhqHoM35C4gzEEiiZqsna0JqbcbGUsSSOFuwOfYRHgmAe7Bc24LeBdzp3%2BFIXiMuJjqT8&X-Amz-Signature=cd92c335037d3be886b25ef4077255808c7ad5c4c3dd4cf2f3e3b1551dab925c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YUHI3ED%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHuQD8tWDdyN6H094hxJkly%2FEXneszER%2FvXQceOb%2FVvNAiBy71J7K5kPS49%2BLxLUfcGvfHyGHMMSH%2F8cPdGvwQAlVCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMWVW8fqeMTK5wvWn4KtwDUtpcqpHKBA8meBFx2AYPVdUxNOZFEuZIObQVP8X4b0%2FMOr3mz%2Bpf9XUrGFyydJ3qvUwlzaRt2OwAKo4lqayDirIDoG2xzbpzVpJRNGC3jCJTgXzuV2w9L61leI6rii%2BGEbnu5OHHkiXl0lIltFhudpJoJoPe1m1e9ceRfpvtp9pnI91rEDQjtVSdBWh%2FxGELXosqf1L9uPoqf0EVmO7p%2BV8GR9D03tuMTNpRZI3yLLCCnUN%2FPK8eWuPN4DdM9WW9hXfpX03iBhdNkf0EqEuMRmZZvY8gTNCv3QNOUZSckDGgVnpBDYzCZnOi80Hb3EW1WVMNmzOfy%2FCUFjPF874ZH5tBPjdHFXMSZltaGak3DjW2ZYU3JWysEmCxywtb%2FaPGGUiDHG2OTlQXtqdaON9I7i7H2I335HKohlWiOtjssnT9UlMX5xgkHeON4zQZ%2Fqh2TN8Rl%2FvITPULgxwcItYD0LMdpFOHTZT3hSE4m1UJ8Hp0%2Ff%2FRieq%2BqCOnRoc%2BTtIFOi1KVnzEK7j7MRKKr9ws0zYYJHJcErh%2Blu5j%2BNTO9UbGwlB4AB0t8G7ArpMiunBMoH6K%2BkIYd5knKTsPPEIY6YvfNNJqFrS3G37FSzZE7Drel6R9p5q8NsUFq%2FQw%2F9KCvQY6pgFXEz1Tg2D9iu9M40NqDJv9EUfPd13LFkncv3NginXrj0jJUaaM1MTrxuzR%2F5YPQwHHpS5HFre%2BGGHiTjr%2Bh8wZleQTxenxb8KhKnPTwJKT5FXkUyUYQ8YHueC0aZkhCpS%2BiWmmJeS8f0HPyH4FUr0FAH%2B%2FhqHoM35C4gzEEiiZqsna0JqbcbGUsSSOFuwOfYRHgmAe7Bc24LeBdzp3%2BFIXiMuJjqT8&X-Amz-Signature=00fe891fc0ff338e613d2afee3d904f68a35b22fa52a6985bebacfb343908c48&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YUHI3ED%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHuQD8tWDdyN6H094hxJkly%2FEXneszER%2FvXQceOb%2FVvNAiBy71J7K5kPS49%2BLxLUfcGvfHyGHMMSH%2F8cPdGvwQAlVCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMWVW8fqeMTK5wvWn4KtwDUtpcqpHKBA8meBFx2AYPVdUxNOZFEuZIObQVP8X4b0%2FMOr3mz%2Bpf9XUrGFyydJ3qvUwlzaRt2OwAKo4lqayDirIDoG2xzbpzVpJRNGC3jCJTgXzuV2w9L61leI6rii%2BGEbnu5OHHkiXl0lIltFhudpJoJoPe1m1e9ceRfpvtp9pnI91rEDQjtVSdBWh%2FxGELXosqf1L9uPoqf0EVmO7p%2BV8GR9D03tuMTNpRZI3yLLCCnUN%2FPK8eWuPN4DdM9WW9hXfpX03iBhdNkf0EqEuMRmZZvY8gTNCv3QNOUZSckDGgVnpBDYzCZnOi80Hb3EW1WVMNmzOfy%2FCUFjPF874ZH5tBPjdHFXMSZltaGak3DjW2ZYU3JWysEmCxywtb%2FaPGGUiDHG2OTlQXtqdaON9I7i7H2I335HKohlWiOtjssnT9UlMX5xgkHeON4zQZ%2Fqh2TN8Rl%2FvITPULgxwcItYD0LMdpFOHTZT3hSE4m1UJ8Hp0%2Ff%2FRieq%2BqCOnRoc%2BTtIFOi1KVnzEK7j7MRKKr9ws0zYYJHJcErh%2Blu5j%2BNTO9UbGwlB4AB0t8G7ArpMiunBMoH6K%2BkIYd5knKTsPPEIY6YvfNNJqFrS3G37FSzZE7Drel6R9p5q8NsUFq%2FQw%2F9KCvQY6pgFXEz1Tg2D9iu9M40NqDJv9EUfPd13LFkncv3NginXrj0jJUaaM1MTrxuzR%2F5YPQwHHpS5HFre%2BGGHiTjr%2Bh8wZleQTxenxb8KhKnPTwJKT5FXkUyUYQ8YHueC0aZkhCpS%2BiWmmJeS8f0HPyH4FUr0FAH%2B%2FhqHoM35C4gzEEiiZqsna0JqbcbGUsSSOFuwOfYRHgmAe7Bc24LeBdzp3%2BFIXiMuJjqT8&X-Amz-Signature=61023ce952455f24d4c51b2ab07aa9ec1cda3e5faa6b980e000c27e4c3048237&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YUHI3ED%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHuQD8tWDdyN6H094hxJkly%2FEXneszER%2FvXQceOb%2FVvNAiBy71J7K5kPS49%2BLxLUfcGvfHyGHMMSH%2F8cPdGvwQAlVCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMWVW8fqeMTK5wvWn4KtwDUtpcqpHKBA8meBFx2AYPVdUxNOZFEuZIObQVP8X4b0%2FMOr3mz%2Bpf9XUrGFyydJ3qvUwlzaRt2OwAKo4lqayDirIDoG2xzbpzVpJRNGC3jCJTgXzuV2w9L61leI6rii%2BGEbnu5OHHkiXl0lIltFhudpJoJoPe1m1e9ceRfpvtp9pnI91rEDQjtVSdBWh%2FxGELXosqf1L9uPoqf0EVmO7p%2BV8GR9D03tuMTNpRZI3yLLCCnUN%2FPK8eWuPN4DdM9WW9hXfpX03iBhdNkf0EqEuMRmZZvY8gTNCv3QNOUZSckDGgVnpBDYzCZnOi80Hb3EW1WVMNmzOfy%2FCUFjPF874ZH5tBPjdHFXMSZltaGak3DjW2ZYU3JWysEmCxywtb%2FaPGGUiDHG2OTlQXtqdaON9I7i7H2I335HKohlWiOtjssnT9UlMX5xgkHeON4zQZ%2Fqh2TN8Rl%2FvITPULgxwcItYD0LMdpFOHTZT3hSE4m1UJ8Hp0%2Ff%2FRieq%2BqCOnRoc%2BTtIFOi1KVnzEK7j7MRKKr9ws0zYYJHJcErh%2Blu5j%2BNTO9UbGwlB4AB0t8G7ArpMiunBMoH6K%2BkIYd5knKTsPPEIY6YvfNNJqFrS3G37FSzZE7Drel6R9p5q8NsUFq%2FQw%2F9KCvQY6pgFXEz1Tg2D9iu9M40NqDJv9EUfPd13LFkncv3NginXrj0jJUaaM1MTrxuzR%2F5YPQwHHpS5HFre%2BGGHiTjr%2Bh8wZleQTxenxb8KhKnPTwJKT5FXkUyUYQ8YHueC0aZkhCpS%2BiWmmJeS8f0HPyH4FUr0FAH%2B%2FhqHoM35C4gzEEiiZqsna0JqbcbGUsSSOFuwOfYRHgmAe7Bc24LeBdzp3%2BFIXiMuJjqT8&X-Amz-Signature=00ebc21dd1f5017ef28bd2a79fc725a4b1ac88a544a6c3225d03e1198f022956&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YUHI3ED%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHuQD8tWDdyN6H094hxJkly%2FEXneszER%2FvXQceOb%2FVvNAiBy71J7K5kPS49%2BLxLUfcGvfHyGHMMSH%2F8cPdGvwQAlVCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMWVW8fqeMTK5wvWn4KtwDUtpcqpHKBA8meBFx2AYPVdUxNOZFEuZIObQVP8X4b0%2FMOr3mz%2Bpf9XUrGFyydJ3qvUwlzaRt2OwAKo4lqayDirIDoG2xzbpzVpJRNGC3jCJTgXzuV2w9L61leI6rii%2BGEbnu5OHHkiXl0lIltFhudpJoJoPe1m1e9ceRfpvtp9pnI91rEDQjtVSdBWh%2FxGELXosqf1L9uPoqf0EVmO7p%2BV8GR9D03tuMTNpRZI3yLLCCnUN%2FPK8eWuPN4DdM9WW9hXfpX03iBhdNkf0EqEuMRmZZvY8gTNCv3QNOUZSckDGgVnpBDYzCZnOi80Hb3EW1WVMNmzOfy%2FCUFjPF874ZH5tBPjdHFXMSZltaGak3DjW2ZYU3JWysEmCxywtb%2FaPGGUiDHG2OTlQXtqdaON9I7i7H2I335HKohlWiOtjssnT9UlMX5xgkHeON4zQZ%2Fqh2TN8Rl%2FvITPULgxwcItYD0LMdpFOHTZT3hSE4m1UJ8Hp0%2Ff%2FRieq%2BqCOnRoc%2BTtIFOi1KVnzEK7j7MRKKr9ws0zYYJHJcErh%2Blu5j%2BNTO9UbGwlB4AB0t8G7ArpMiunBMoH6K%2BkIYd5knKTsPPEIY6YvfNNJqFrS3G37FSzZE7Drel6R9p5q8NsUFq%2FQw%2F9KCvQY6pgFXEz1Tg2D9iu9M40NqDJv9EUfPd13LFkncv3NginXrj0jJUaaM1MTrxuzR%2F5YPQwHHpS5HFre%2BGGHiTjr%2Bh8wZleQTxenxb8KhKnPTwJKT5FXkUyUYQ8YHueC0aZkhCpS%2BiWmmJeS8f0HPyH4FUr0FAH%2B%2FhqHoM35C4gzEEiiZqsna0JqbcbGUsSSOFuwOfYRHgmAe7Bc24LeBdzp3%2BFIXiMuJjqT8&X-Amz-Signature=7d4f328df426f54c08030a64a59327f2e232d36b0788d8c747ec22ddb2ae3abd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7BLRMGL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqVExUqD%2FHYc664Sev2H172KFdWi6PH3SIs8kSQwvkFQIgfoIVzdJu6V3zQRhQxvkjyAJMBvBTUeJQKF%2FqqUJGucgq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMVw5QqF0dJPaDXZTSrcA09ryxvNzyPx1TsIMDywKDvF8erJjL7dfL6IwP4l7%2B7y7PBT2%2BkFHZTp3QHKU5jimHeLxFu6w7oVtA002H6gPSwp%2F8xmKeuUEbINQ5QwBk23FkIUv6glok2YdT13mSS1RNsMdXvhpNo0K%2BO1skRpPSYjRF8CHeG9x8z6Wcsqc4EoaSVQH95PG76TYI2%2FNyNyAk9OMoPiGaDz9mKmDRP%2FsYWY1v%2BlPbTzjdRvKxwCajnaCV0VkFbFe34Gdn5z8gOFv8iOLw4DXoHgGQvT2E%2FiHfa%2BHNPHbiG7HOD59WJ7eLrucsMKeXWHj%2FKdk0ev6K9DZXIBXk0NZVROpWi23wob1hL57Qfh6euzFfZOR6RrHVRU3M7eJAWlGEY24BMRwn1RTOhtwJ2MvEci%2Fa5LDYP%2FOLSYF7FnU3kQV6NtWeFvZ1ubbKT8DLVS7CQdwCxAF1cVLiLemBpaYkFf83cUEhR5%2F48cPyl53DCr%2BeBxiL5xqfPylJdDuoozt1OHAqPACfBzoGFopJGzk790Ln8FXT7ajTGzamBrvP1J%2BniAy9VuSZn9cC1h0nxJ8zLabbG8B7bgAPqg3CWWD7h%2Bq6enHzmoUYkUazCxbxku3DZsTVwKhNI%2FnPcKCLHTxNuiDSTtMNzSgr0GOqUB2xc8AH8doU9I15ECloGYb4CWh85IjV67cwqvT%2BIRJD1vnYoPyA6jMpp6sB0DEy8gDqnSEHJINwycL8l5vEE8UNJSpsW%2BA2ns%2FG5EukWsjV3eMmbT5U5TLwiDyC7XBiQWnCm9bxQLwKP%2FyuQsHXArE8xU8z1s8siY7cigpVACHoOd%2BxRu9cyVC8A5noRK3B1eHiKeAheLyz4DDoxaEPDpztgE5w6G&X-Amz-Signature=ac14bd759d48d8d4b3580286f401044726702143b02e34efc74bd5c9290db81c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7BLRMGL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqVExUqD%2FHYc664Sev2H172KFdWi6PH3SIs8kSQwvkFQIgfoIVzdJu6V3zQRhQxvkjyAJMBvBTUeJQKF%2FqqUJGucgq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMVw5QqF0dJPaDXZTSrcA09ryxvNzyPx1TsIMDywKDvF8erJjL7dfL6IwP4l7%2B7y7PBT2%2BkFHZTp3QHKU5jimHeLxFu6w7oVtA002H6gPSwp%2F8xmKeuUEbINQ5QwBk23FkIUv6glok2YdT13mSS1RNsMdXvhpNo0K%2BO1skRpPSYjRF8CHeG9x8z6Wcsqc4EoaSVQH95PG76TYI2%2FNyNyAk9OMoPiGaDz9mKmDRP%2FsYWY1v%2BlPbTzjdRvKxwCajnaCV0VkFbFe34Gdn5z8gOFv8iOLw4DXoHgGQvT2E%2FiHfa%2BHNPHbiG7HOD59WJ7eLrucsMKeXWHj%2FKdk0ev6K9DZXIBXk0NZVROpWi23wob1hL57Qfh6euzFfZOR6RrHVRU3M7eJAWlGEY24BMRwn1RTOhtwJ2MvEci%2Fa5LDYP%2FOLSYF7FnU3kQV6NtWeFvZ1ubbKT8DLVS7CQdwCxAF1cVLiLemBpaYkFf83cUEhR5%2F48cPyl53DCr%2BeBxiL5xqfPylJdDuoozt1OHAqPACfBzoGFopJGzk790Ln8FXT7ajTGzamBrvP1J%2BniAy9VuSZn9cC1h0nxJ8zLabbG8B7bgAPqg3CWWD7h%2Bq6enHzmoUYkUazCxbxku3DZsTVwKhNI%2FnPcKCLHTxNuiDSTtMNzSgr0GOqUB2xc8AH8doU9I15ECloGYb4CWh85IjV67cwqvT%2BIRJD1vnYoPyA6jMpp6sB0DEy8gDqnSEHJINwycL8l5vEE8UNJSpsW%2BA2ns%2FG5EukWsjV3eMmbT5U5TLwiDyC7XBiQWnCm9bxQLwKP%2FyuQsHXArE8xU8z1s8siY7cigpVACHoOd%2BxRu9cyVC8A5noRK3B1eHiKeAheLyz4DDoxaEPDpztgE5w6G&X-Amz-Signature=b4e659185904cf18f393fe53926b1d998da99bcd9b991d7452e9e25ca1ae2569&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7BLRMGL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqVExUqD%2FHYc664Sev2H172KFdWi6PH3SIs8kSQwvkFQIgfoIVzdJu6V3zQRhQxvkjyAJMBvBTUeJQKF%2FqqUJGucgq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMVw5QqF0dJPaDXZTSrcA09ryxvNzyPx1TsIMDywKDvF8erJjL7dfL6IwP4l7%2B7y7PBT2%2BkFHZTp3QHKU5jimHeLxFu6w7oVtA002H6gPSwp%2F8xmKeuUEbINQ5QwBk23FkIUv6glok2YdT13mSS1RNsMdXvhpNo0K%2BO1skRpPSYjRF8CHeG9x8z6Wcsqc4EoaSVQH95PG76TYI2%2FNyNyAk9OMoPiGaDz9mKmDRP%2FsYWY1v%2BlPbTzjdRvKxwCajnaCV0VkFbFe34Gdn5z8gOFv8iOLw4DXoHgGQvT2E%2FiHfa%2BHNPHbiG7HOD59WJ7eLrucsMKeXWHj%2FKdk0ev6K9DZXIBXk0NZVROpWi23wob1hL57Qfh6euzFfZOR6RrHVRU3M7eJAWlGEY24BMRwn1RTOhtwJ2MvEci%2Fa5LDYP%2FOLSYF7FnU3kQV6NtWeFvZ1ubbKT8DLVS7CQdwCxAF1cVLiLemBpaYkFf83cUEhR5%2F48cPyl53DCr%2BeBxiL5xqfPylJdDuoozt1OHAqPACfBzoGFopJGzk790Ln8FXT7ajTGzamBrvP1J%2BniAy9VuSZn9cC1h0nxJ8zLabbG8B7bgAPqg3CWWD7h%2Bq6enHzmoUYkUazCxbxku3DZsTVwKhNI%2FnPcKCLHTxNuiDSTtMNzSgr0GOqUB2xc8AH8doU9I15ECloGYb4CWh85IjV67cwqvT%2BIRJD1vnYoPyA6jMpp6sB0DEy8gDqnSEHJINwycL8l5vEE8UNJSpsW%2BA2ns%2FG5EukWsjV3eMmbT5U5TLwiDyC7XBiQWnCm9bxQLwKP%2FyuQsHXArE8xU8z1s8siY7cigpVACHoOd%2BxRu9cyVC8A5noRK3B1eHiKeAheLyz4DDoxaEPDpztgE5w6G&X-Amz-Signature=a903fb40fd4fb11a12d99ed7bd048536ecd9d6d16e92914eae6a921633400f74&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7BLRMGL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqVExUqD%2FHYc664Sev2H172KFdWi6PH3SIs8kSQwvkFQIgfoIVzdJu6V3zQRhQxvkjyAJMBvBTUeJQKF%2FqqUJGucgq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMVw5QqF0dJPaDXZTSrcA09ryxvNzyPx1TsIMDywKDvF8erJjL7dfL6IwP4l7%2B7y7PBT2%2BkFHZTp3QHKU5jimHeLxFu6w7oVtA002H6gPSwp%2F8xmKeuUEbINQ5QwBk23FkIUv6glok2YdT13mSS1RNsMdXvhpNo0K%2BO1skRpPSYjRF8CHeG9x8z6Wcsqc4EoaSVQH95PG76TYI2%2FNyNyAk9OMoPiGaDz9mKmDRP%2FsYWY1v%2BlPbTzjdRvKxwCajnaCV0VkFbFe34Gdn5z8gOFv8iOLw4DXoHgGQvT2E%2FiHfa%2BHNPHbiG7HOD59WJ7eLrucsMKeXWHj%2FKdk0ev6K9DZXIBXk0NZVROpWi23wob1hL57Qfh6euzFfZOR6RrHVRU3M7eJAWlGEY24BMRwn1RTOhtwJ2MvEci%2Fa5LDYP%2FOLSYF7FnU3kQV6NtWeFvZ1ubbKT8DLVS7CQdwCxAF1cVLiLemBpaYkFf83cUEhR5%2F48cPyl53DCr%2BeBxiL5xqfPylJdDuoozt1OHAqPACfBzoGFopJGzk790Ln8FXT7ajTGzamBrvP1J%2BniAy9VuSZn9cC1h0nxJ8zLabbG8B7bgAPqg3CWWD7h%2Bq6enHzmoUYkUazCxbxku3DZsTVwKhNI%2FnPcKCLHTxNuiDSTtMNzSgr0GOqUB2xc8AH8doU9I15ECloGYb4CWh85IjV67cwqvT%2BIRJD1vnYoPyA6jMpp6sB0DEy8gDqnSEHJINwycL8l5vEE8UNJSpsW%2BA2ns%2FG5EukWsjV3eMmbT5U5TLwiDyC7XBiQWnCm9bxQLwKP%2FyuQsHXArE8xU8z1s8siY7cigpVACHoOd%2BxRu9cyVC8A5noRK3B1eHiKeAheLyz4DDoxaEPDpztgE5w6G&X-Amz-Signature=64412d20362c601fb22010c137e2509533ccf7ad0c3ce3ace99587885e01e7ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7BLRMGL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqVExUqD%2FHYc664Sev2H172KFdWi6PH3SIs8kSQwvkFQIgfoIVzdJu6V3zQRhQxvkjyAJMBvBTUeJQKF%2FqqUJGucgq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMVw5QqF0dJPaDXZTSrcA09ryxvNzyPx1TsIMDywKDvF8erJjL7dfL6IwP4l7%2B7y7PBT2%2BkFHZTp3QHKU5jimHeLxFu6w7oVtA002H6gPSwp%2F8xmKeuUEbINQ5QwBk23FkIUv6glok2YdT13mSS1RNsMdXvhpNo0K%2BO1skRpPSYjRF8CHeG9x8z6Wcsqc4EoaSVQH95PG76TYI2%2FNyNyAk9OMoPiGaDz9mKmDRP%2FsYWY1v%2BlPbTzjdRvKxwCajnaCV0VkFbFe34Gdn5z8gOFv8iOLw4DXoHgGQvT2E%2FiHfa%2BHNPHbiG7HOD59WJ7eLrucsMKeXWHj%2FKdk0ev6K9DZXIBXk0NZVROpWi23wob1hL57Qfh6euzFfZOR6RrHVRU3M7eJAWlGEY24BMRwn1RTOhtwJ2MvEci%2Fa5LDYP%2FOLSYF7FnU3kQV6NtWeFvZ1ubbKT8DLVS7CQdwCxAF1cVLiLemBpaYkFf83cUEhR5%2F48cPyl53DCr%2BeBxiL5xqfPylJdDuoozt1OHAqPACfBzoGFopJGzk790Ln8FXT7ajTGzamBrvP1J%2BniAy9VuSZn9cC1h0nxJ8zLabbG8B7bgAPqg3CWWD7h%2Bq6enHzmoUYkUazCxbxku3DZsTVwKhNI%2FnPcKCLHTxNuiDSTtMNzSgr0GOqUB2xc8AH8doU9I15ECloGYb4CWh85IjV67cwqvT%2BIRJD1vnYoPyA6jMpp6sB0DEy8gDqnSEHJINwycL8l5vEE8UNJSpsW%2BA2ns%2FG5EukWsjV3eMmbT5U5TLwiDyC7XBiQWnCm9bxQLwKP%2FyuQsHXArE8xU8z1s8siY7cigpVACHoOd%2BxRu9cyVC8A5noRK3B1eHiKeAheLyz4DDoxaEPDpztgE5w6G&X-Amz-Signature=e7f1af4a76c6b227f9242d454ca6b746f07fc305a474f58693bb5033c83e7c58&X-Amz-SignedHeaders=host&x-id=GetObject)
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


