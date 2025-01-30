

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTVEJS4W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsmdzwAKuUI7YmTE52HLUtugRg3hdeiS4AO8DaSu8hGgIgXb7aR40%2BRC1Bzj7UIaWAn9dQ8%2B16jUuz7KGzvGJAaYkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZ%2BarWHYMDw7SHkwSrcA%2FlifbR%2B8m4IF5AEEFq4J8p%2F7fH2tJQF54V0756gcHcWELZKWFeXfuKbiEglVJ7Nk1DfXz4Is0a%2BpkaF3ZDmZrqbbLDhfnAYqdsDh08PEpAjt%2Fn2zPIgxhVVM1HhO1Y7b91FkzPKjqK6PGAF%2BrFRfQs2XvG9BOdMnE30tyNZN0%2FS3grAj%2BmZD2jrf8glj88LM6KpZNkH6Wrh3nMzA164URAUPQsGKQ783UzFwOVWZR0E55z3RjiVr6EQtfR%2B%2FtnqLl%2FpH97eE3rD6wpe5v%2BfhhThl1njmjBQfdl4HJwjldCrPi19tWe%2BJeTBGg9aeqJ4jH5b8%2FDjhlsX7%2BlCoUEyNCmmtPBtLb11ZAkZiMJxK9FSWuTp49OmXHdARVYYfU9%2FuYRV5hpFQ1yPbeYrdtrixB5Sfq%2FD3K9MIKSZPBZ7%2FBWtxxIEmOktR222jUJiePo7JSc8GvXr9U1tJDQsSsatu1gyWG2%2FuF3%2FDKWxDKW4UrnbsYlw8Mkx2b6tHM2pCUMN%2FNdgB65vdu4RPU%2FnCyUr%2BjgZzJrOe1PU1%2FwnCZGnBxWPwfMWVCn%2Fw4hZMVOQ9brG7X930AlqvZ7W2BZ1JwWvPrlYaJgJfrwhXAopF68aOfT62HjVIbIei3j7fYhoMLr977wGOqUBpxRAlvGYevrE3HYaL570qPypkIWwxIv2QaJPBSb9oP4ODJqu4NmenUD3bQ9t7h2bItVSSpy748e1lqbVDMMbTTtlZxWMtXefwgSFpHeBoTnsYvho6PsVTmasn51qtk0DQgnJ7vwL3Jskj1wwbC9QAV4PhLA2EJ%2BFsP%2BYIHsRsTnFievyi1HdDdlYcdzR6b0zpwPkRWh2m6bHRQt3RZXRg4eUrUg2&X-Amz-Signature=a07ff388472f967b218f085e967eb2ea81cebdf1ac25c9f178a8429527c45478&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB2PY5JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6VZdu6hfZR5pGQbblG0PNNWBEW62letwh4LO%2BaTZQBQIgUbkiIaBres93G4KxtL4OFF7QW2ejzjuIHKWoIfqTz1gqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNepAMj0krtnOE%2BZ3ircA6sAyccdPgDZc2anY0FtcKDWqRNjjqXnZ522h9r%2FIow7UrB7BEBA4n3Nq2JovTWKm6Q0QJ2QapwXNXFKZ0hJuaDNcSP7fpg8bf1BlheGB6Z%2Fauqm5dil0qZqLOw59YBVMHFSQ2SLXFKCYBqyRlRgureeSk9lOxIrlENd%2BTt1qmshrzFCI9Zc9qOpQJSZKV%2FZ8vuDBLLFoH%2F%2B%2BGBGtiDwSO%2FuxmdIJA%2BF3Ensa%2FaZP7RXE%2FYSuqUHbTwaLzopEDPzD5u0Uux%2FMUbeJWjChdQ2ISnhNXrFjw3avf%2FjnQveHwIjF3uZQXLr%2BZfdstwQl1f1sD5ZglI%2FoAK0b8iXpxrkalws6Yw33QvQlZGzcQ7zOBHBhsqR8AMEtWwphGPGH7CJn2WEqZ7J7qv3mjpc4he1Oe0rY2K2zWBehDyHC5TYJc9W0mB2ji1WCP56t5nrizDMCjx9OQiS2QUOqILlQEhzZznTPfyzbxNmliYLpMftrrakrbEJDMY7ldkSgn4eiwZVT5x%2BCp0AP1Krfv8cB0wjwHkcuGLTNKosF18%2FH6LmYIJ1kDGB0r4A0eKLEk0xUvn0nF8R18NmZpyC25nT%2Fx5VccOUoN4lMgkCRG%2BYG4c5HAtHW1sNOjtmLW%2BYCuSvMKv977wGOqUBnUCdYZhhaFohzrGVZBwwjqdAerdPCgDpeVmD5eE416MQzyWHJkpRrOIlj1R0lZxfonTSqEw92Ut6Z8ek4SzeI4YVDiVY4NZzbG8%2BwgWJRODhNqD7J1uYnuCeKRtIbxVaBLAUSnbH4h4dNo1y26qN3R0ln6DnLl1RaDCB2y5ZxmXN%2BzBlpGvq3HJyO0LTVDIVPlLcXOOhBlZ8lq22C0Ua5RHTFk2G&X-Amz-Signature=136cd573e0fffaf18cfd33deff1eca82f8c2c21d90151d0407100a2975f3daf2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB2PY5JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6VZdu6hfZR5pGQbblG0PNNWBEW62letwh4LO%2BaTZQBQIgUbkiIaBres93G4KxtL4OFF7QW2ejzjuIHKWoIfqTz1gqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNepAMj0krtnOE%2BZ3ircA6sAyccdPgDZc2anY0FtcKDWqRNjjqXnZ522h9r%2FIow7UrB7BEBA4n3Nq2JovTWKm6Q0QJ2QapwXNXFKZ0hJuaDNcSP7fpg8bf1BlheGB6Z%2Fauqm5dil0qZqLOw59YBVMHFSQ2SLXFKCYBqyRlRgureeSk9lOxIrlENd%2BTt1qmshrzFCI9Zc9qOpQJSZKV%2FZ8vuDBLLFoH%2F%2B%2BGBGtiDwSO%2FuxmdIJA%2BF3Ensa%2FaZP7RXE%2FYSuqUHbTwaLzopEDPzD5u0Uux%2FMUbeJWjChdQ2ISnhNXrFjw3avf%2FjnQveHwIjF3uZQXLr%2BZfdstwQl1f1sD5ZglI%2FoAK0b8iXpxrkalws6Yw33QvQlZGzcQ7zOBHBhsqR8AMEtWwphGPGH7CJn2WEqZ7J7qv3mjpc4he1Oe0rY2K2zWBehDyHC5TYJc9W0mB2ji1WCP56t5nrizDMCjx9OQiS2QUOqILlQEhzZznTPfyzbxNmliYLpMftrrakrbEJDMY7ldkSgn4eiwZVT5x%2BCp0AP1Krfv8cB0wjwHkcuGLTNKosF18%2FH6LmYIJ1kDGB0r4A0eKLEk0xUvn0nF8R18NmZpyC25nT%2Fx5VccOUoN4lMgkCRG%2BYG4c5HAtHW1sNOjtmLW%2BYCuSvMKv977wGOqUBnUCdYZhhaFohzrGVZBwwjqdAerdPCgDpeVmD5eE416MQzyWHJkpRrOIlj1R0lZxfonTSqEw92Ut6Z8ek4SzeI4YVDiVY4NZzbG8%2BwgWJRODhNqD7J1uYnuCeKRtIbxVaBLAUSnbH4h4dNo1y26qN3R0ln6DnLl1RaDCB2y5ZxmXN%2BzBlpGvq3HJyO0LTVDIVPlLcXOOhBlZ8lq22C0Ua5RHTFk2G&X-Amz-Signature=c92cf2eb1abcf0704c5a1086c630d879744517795dbd0b35e0ab8b70b8188da8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB2PY5JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6VZdu6hfZR5pGQbblG0PNNWBEW62letwh4LO%2BaTZQBQIgUbkiIaBres93G4KxtL4OFF7QW2ejzjuIHKWoIfqTz1gqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNepAMj0krtnOE%2BZ3ircA6sAyccdPgDZc2anY0FtcKDWqRNjjqXnZ522h9r%2FIow7UrB7BEBA4n3Nq2JovTWKm6Q0QJ2QapwXNXFKZ0hJuaDNcSP7fpg8bf1BlheGB6Z%2Fauqm5dil0qZqLOw59YBVMHFSQ2SLXFKCYBqyRlRgureeSk9lOxIrlENd%2BTt1qmshrzFCI9Zc9qOpQJSZKV%2FZ8vuDBLLFoH%2F%2B%2BGBGtiDwSO%2FuxmdIJA%2BF3Ensa%2FaZP7RXE%2FYSuqUHbTwaLzopEDPzD5u0Uux%2FMUbeJWjChdQ2ISnhNXrFjw3avf%2FjnQveHwIjF3uZQXLr%2BZfdstwQl1f1sD5ZglI%2FoAK0b8iXpxrkalws6Yw33QvQlZGzcQ7zOBHBhsqR8AMEtWwphGPGH7CJn2WEqZ7J7qv3mjpc4he1Oe0rY2K2zWBehDyHC5TYJc9W0mB2ji1WCP56t5nrizDMCjx9OQiS2QUOqILlQEhzZznTPfyzbxNmliYLpMftrrakrbEJDMY7ldkSgn4eiwZVT5x%2BCp0AP1Krfv8cB0wjwHkcuGLTNKosF18%2FH6LmYIJ1kDGB0r4A0eKLEk0xUvn0nF8R18NmZpyC25nT%2Fx5VccOUoN4lMgkCRG%2BYG4c5HAtHW1sNOjtmLW%2BYCuSvMKv977wGOqUBnUCdYZhhaFohzrGVZBwwjqdAerdPCgDpeVmD5eE416MQzyWHJkpRrOIlj1R0lZxfonTSqEw92Ut6Z8ek4SzeI4YVDiVY4NZzbG8%2BwgWJRODhNqD7J1uYnuCeKRtIbxVaBLAUSnbH4h4dNo1y26qN3R0ln6DnLl1RaDCB2y5ZxmXN%2BzBlpGvq3HJyO0LTVDIVPlLcXOOhBlZ8lq22C0Ua5RHTFk2G&X-Amz-Signature=1b2c0a160d01143aaf5a5f7859690b3c17d9d613df598cf2e84023bda2876814&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB2PY5JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6VZdu6hfZR5pGQbblG0PNNWBEW62letwh4LO%2BaTZQBQIgUbkiIaBres93G4KxtL4OFF7QW2ejzjuIHKWoIfqTz1gqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNepAMj0krtnOE%2BZ3ircA6sAyccdPgDZc2anY0FtcKDWqRNjjqXnZ522h9r%2FIow7UrB7BEBA4n3Nq2JovTWKm6Q0QJ2QapwXNXFKZ0hJuaDNcSP7fpg8bf1BlheGB6Z%2Fauqm5dil0qZqLOw59YBVMHFSQ2SLXFKCYBqyRlRgureeSk9lOxIrlENd%2BTt1qmshrzFCI9Zc9qOpQJSZKV%2FZ8vuDBLLFoH%2F%2B%2BGBGtiDwSO%2FuxmdIJA%2BF3Ensa%2FaZP7RXE%2FYSuqUHbTwaLzopEDPzD5u0Uux%2FMUbeJWjChdQ2ISnhNXrFjw3avf%2FjnQveHwIjF3uZQXLr%2BZfdstwQl1f1sD5ZglI%2FoAK0b8iXpxrkalws6Yw33QvQlZGzcQ7zOBHBhsqR8AMEtWwphGPGH7CJn2WEqZ7J7qv3mjpc4he1Oe0rY2K2zWBehDyHC5TYJc9W0mB2ji1WCP56t5nrizDMCjx9OQiS2QUOqILlQEhzZznTPfyzbxNmliYLpMftrrakrbEJDMY7ldkSgn4eiwZVT5x%2BCp0AP1Krfv8cB0wjwHkcuGLTNKosF18%2FH6LmYIJ1kDGB0r4A0eKLEk0xUvn0nF8R18NmZpyC25nT%2Fx5VccOUoN4lMgkCRG%2BYG4c5HAtHW1sNOjtmLW%2BYCuSvMKv977wGOqUBnUCdYZhhaFohzrGVZBwwjqdAerdPCgDpeVmD5eE416MQzyWHJkpRrOIlj1R0lZxfonTSqEw92Ut6Z8ek4SzeI4YVDiVY4NZzbG8%2BwgWJRODhNqD7J1uYnuCeKRtIbxVaBLAUSnbH4h4dNo1y26qN3R0ln6DnLl1RaDCB2y5ZxmXN%2BzBlpGvq3HJyO0LTVDIVPlLcXOOhBlZ8lq22C0Ua5RHTFk2G&X-Amz-Signature=b9cc2ac34618895e190de3a4713afc1c86636eb16f3966d329382dbbf19c62f7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB2PY5JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6VZdu6hfZR5pGQbblG0PNNWBEW62letwh4LO%2BaTZQBQIgUbkiIaBres93G4KxtL4OFF7QW2ejzjuIHKWoIfqTz1gqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNepAMj0krtnOE%2BZ3ircA6sAyccdPgDZc2anY0FtcKDWqRNjjqXnZ522h9r%2FIow7UrB7BEBA4n3Nq2JovTWKm6Q0QJ2QapwXNXFKZ0hJuaDNcSP7fpg8bf1BlheGB6Z%2Fauqm5dil0qZqLOw59YBVMHFSQ2SLXFKCYBqyRlRgureeSk9lOxIrlENd%2BTt1qmshrzFCI9Zc9qOpQJSZKV%2FZ8vuDBLLFoH%2F%2B%2BGBGtiDwSO%2FuxmdIJA%2BF3Ensa%2FaZP7RXE%2FYSuqUHbTwaLzopEDPzD5u0Uux%2FMUbeJWjChdQ2ISnhNXrFjw3avf%2FjnQveHwIjF3uZQXLr%2BZfdstwQl1f1sD5ZglI%2FoAK0b8iXpxrkalws6Yw33QvQlZGzcQ7zOBHBhsqR8AMEtWwphGPGH7CJn2WEqZ7J7qv3mjpc4he1Oe0rY2K2zWBehDyHC5TYJc9W0mB2ji1WCP56t5nrizDMCjx9OQiS2QUOqILlQEhzZznTPfyzbxNmliYLpMftrrakrbEJDMY7ldkSgn4eiwZVT5x%2BCp0AP1Krfv8cB0wjwHkcuGLTNKosF18%2FH6LmYIJ1kDGB0r4A0eKLEk0xUvn0nF8R18NmZpyC25nT%2Fx5VccOUoN4lMgkCRG%2BYG4c5HAtHW1sNOjtmLW%2BYCuSvMKv977wGOqUBnUCdYZhhaFohzrGVZBwwjqdAerdPCgDpeVmD5eE416MQzyWHJkpRrOIlj1R0lZxfonTSqEw92Ut6Z8ek4SzeI4YVDiVY4NZzbG8%2BwgWJRODhNqD7J1uYnuCeKRtIbxVaBLAUSnbH4h4dNo1y26qN3R0ln6DnLl1RaDCB2y5ZxmXN%2BzBlpGvq3HJyO0LTVDIVPlLcXOOhBlZ8lq22C0Ua5RHTFk2G&X-Amz-Signature=7d18d35f0da9b9716f650133f1b43a1f169cd8955d44285b418f42d1a4396d3e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTVEJS4W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsmdzwAKuUI7YmTE52HLUtugRg3hdeiS4AO8DaSu8hGgIgXb7aR40%2BRC1Bzj7UIaWAn9dQ8%2B16jUuz7KGzvGJAaYkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZ%2BarWHYMDw7SHkwSrcA%2FlifbR%2B8m4IF5AEEFq4J8p%2F7fH2tJQF54V0756gcHcWELZKWFeXfuKbiEglVJ7Nk1DfXz4Is0a%2BpkaF3ZDmZrqbbLDhfnAYqdsDh08PEpAjt%2Fn2zPIgxhVVM1HhO1Y7b91FkzPKjqK6PGAF%2BrFRfQs2XvG9BOdMnE30tyNZN0%2FS3grAj%2BmZD2jrf8glj88LM6KpZNkH6Wrh3nMzA164URAUPQsGKQ783UzFwOVWZR0E55z3RjiVr6EQtfR%2B%2FtnqLl%2FpH97eE3rD6wpe5v%2BfhhThl1njmjBQfdl4HJwjldCrPi19tWe%2BJeTBGg9aeqJ4jH5b8%2FDjhlsX7%2BlCoUEyNCmmtPBtLb11ZAkZiMJxK9FSWuTp49OmXHdARVYYfU9%2FuYRV5hpFQ1yPbeYrdtrixB5Sfq%2FD3K9MIKSZPBZ7%2FBWtxxIEmOktR222jUJiePo7JSc8GvXr9U1tJDQsSsatu1gyWG2%2FuF3%2FDKWxDKW4UrnbsYlw8Mkx2b6tHM2pCUMN%2FNdgB65vdu4RPU%2FnCyUr%2BjgZzJrOe1PU1%2FwnCZGnBxWPwfMWVCn%2Fw4hZMVOQ9brG7X930AlqvZ7W2BZ1JwWvPrlYaJgJfrwhXAopF68aOfT62HjVIbIei3j7fYhoMLr977wGOqUBpxRAlvGYevrE3HYaL570qPypkIWwxIv2QaJPBSb9oP4ODJqu4NmenUD3bQ9t7h2bItVSSpy748e1lqbVDMMbTTtlZxWMtXefwgSFpHeBoTnsYvho6PsVTmasn51qtk0DQgnJ7vwL3Jskj1wwbC9QAV4PhLA2EJ%2BFsP%2BYIHsRsTnFievyi1HdDdlYcdzR6b0zpwPkRWh2m6bHRQt3RZXRg4eUrUg2&X-Amz-Signature=70fd512159317fd9cb48c24fcf0e7feb8eabfcf62fe8d32f555c7b4744ed2adf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTVEJS4W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsmdzwAKuUI7YmTE52HLUtugRg3hdeiS4AO8DaSu8hGgIgXb7aR40%2BRC1Bzj7UIaWAn9dQ8%2B16jUuz7KGzvGJAaYkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZ%2BarWHYMDw7SHkwSrcA%2FlifbR%2B8m4IF5AEEFq4J8p%2F7fH2tJQF54V0756gcHcWELZKWFeXfuKbiEglVJ7Nk1DfXz4Is0a%2BpkaF3ZDmZrqbbLDhfnAYqdsDh08PEpAjt%2Fn2zPIgxhVVM1HhO1Y7b91FkzPKjqK6PGAF%2BrFRfQs2XvG9BOdMnE30tyNZN0%2FS3grAj%2BmZD2jrf8glj88LM6KpZNkH6Wrh3nMzA164URAUPQsGKQ783UzFwOVWZR0E55z3RjiVr6EQtfR%2B%2FtnqLl%2FpH97eE3rD6wpe5v%2BfhhThl1njmjBQfdl4HJwjldCrPi19tWe%2BJeTBGg9aeqJ4jH5b8%2FDjhlsX7%2BlCoUEyNCmmtPBtLb11ZAkZiMJxK9FSWuTp49OmXHdARVYYfU9%2FuYRV5hpFQ1yPbeYrdtrixB5Sfq%2FD3K9MIKSZPBZ7%2FBWtxxIEmOktR222jUJiePo7JSc8GvXr9U1tJDQsSsatu1gyWG2%2FuF3%2FDKWxDKW4UrnbsYlw8Mkx2b6tHM2pCUMN%2FNdgB65vdu4RPU%2FnCyUr%2BjgZzJrOe1PU1%2FwnCZGnBxWPwfMWVCn%2Fw4hZMVOQ9brG7X930AlqvZ7W2BZ1JwWvPrlYaJgJfrwhXAopF68aOfT62HjVIbIei3j7fYhoMLr977wGOqUBpxRAlvGYevrE3HYaL570qPypkIWwxIv2QaJPBSb9oP4ODJqu4NmenUD3bQ9t7h2bItVSSpy748e1lqbVDMMbTTtlZxWMtXefwgSFpHeBoTnsYvho6PsVTmasn51qtk0DQgnJ7vwL3Jskj1wwbC9QAV4PhLA2EJ%2BFsP%2BYIHsRsTnFievyi1HdDdlYcdzR6b0zpwPkRWh2m6bHRQt3RZXRg4eUrUg2&X-Amz-Signature=36e8057fd9fdb7635925a03a06ce787cf273392e706a4ef5fdeb94f96d84f864&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTVEJS4W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsmdzwAKuUI7YmTE52HLUtugRg3hdeiS4AO8DaSu8hGgIgXb7aR40%2BRC1Bzj7UIaWAn9dQ8%2B16jUuz7KGzvGJAaYkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZ%2BarWHYMDw7SHkwSrcA%2FlifbR%2B8m4IF5AEEFq4J8p%2F7fH2tJQF54V0756gcHcWELZKWFeXfuKbiEglVJ7Nk1DfXz4Is0a%2BpkaF3ZDmZrqbbLDhfnAYqdsDh08PEpAjt%2Fn2zPIgxhVVM1HhO1Y7b91FkzPKjqK6PGAF%2BrFRfQs2XvG9BOdMnE30tyNZN0%2FS3grAj%2BmZD2jrf8glj88LM6KpZNkH6Wrh3nMzA164URAUPQsGKQ783UzFwOVWZR0E55z3RjiVr6EQtfR%2B%2FtnqLl%2FpH97eE3rD6wpe5v%2BfhhThl1njmjBQfdl4HJwjldCrPi19tWe%2BJeTBGg9aeqJ4jH5b8%2FDjhlsX7%2BlCoUEyNCmmtPBtLb11ZAkZiMJxK9FSWuTp49OmXHdARVYYfU9%2FuYRV5hpFQ1yPbeYrdtrixB5Sfq%2FD3K9MIKSZPBZ7%2FBWtxxIEmOktR222jUJiePo7JSc8GvXr9U1tJDQsSsatu1gyWG2%2FuF3%2FDKWxDKW4UrnbsYlw8Mkx2b6tHM2pCUMN%2FNdgB65vdu4RPU%2FnCyUr%2BjgZzJrOe1PU1%2FwnCZGnBxWPwfMWVCn%2Fw4hZMVOQ9brG7X930AlqvZ7W2BZ1JwWvPrlYaJgJfrwhXAopF68aOfT62HjVIbIei3j7fYhoMLr977wGOqUBpxRAlvGYevrE3HYaL570qPypkIWwxIv2QaJPBSb9oP4ODJqu4NmenUD3bQ9t7h2bItVSSpy748e1lqbVDMMbTTtlZxWMtXefwgSFpHeBoTnsYvho6PsVTmasn51qtk0DQgnJ7vwL3Jskj1wwbC9QAV4PhLA2EJ%2BFsP%2BYIHsRsTnFievyi1HdDdlYcdzR6b0zpwPkRWh2m6bHRQt3RZXRg4eUrUg2&X-Amz-Signature=916f6a8a59a3794cebd7c57053c1be9d883953092531b2dba1006cd0a8eda686&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTVEJS4W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsmdzwAKuUI7YmTE52HLUtugRg3hdeiS4AO8DaSu8hGgIgXb7aR40%2BRC1Bzj7UIaWAn9dQ8%2B16jUuz7KGzvGJAaYkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZ%2BarWHYMDw7SHkwSrcA%2FlifbR%2B8m4IF5AEEFq4J8p%2F7fH2tJQF54V0756gcHcWELZKWFeXfuKbiEglVJ7Nk1DfXz4Is0a%2BpkaF3ZDmZrqbbLDhfnAYqdsDh08PEpAjt%2Fn2zPIgxhVVM1HhO1Y7b91FkzPKjqK6PGAF%2BrFRfQs2XvG9BOdMnE30tyNZN0%2FS3grAj%2BmZD2jrf8glj88LM6KpZNkH6Wrh3nMzA164URAUPQsGKQ783UzFwOVWZR0E55z3RjiVr6EQtfR%2B%2FtnqLl%2FpH97eE3rD6wpe5v%2BfhhThl1njmjBQfdl4HJwjldCrPi19tWe%2BJeTBGg9aeqJ4jH5b8%2FDjhlsX7%2BlCoUEyNCmmtPBtLb11ZAkZiMJxK9FSWuTp49OmXHdARVYYfU9%2FuYRV5hpFQ1yPbeYrdtrixB5Sfq%2FD3K9MIKSZPBZ7%2FBWtxxIEmOktR222jUJiePo7JSc8GvXr9U1tJDQsSsatu1gyWG2%2FuF3%2FDKWxDKW4UrnbsYlw8Mkx2b6tHM2pCUMN%2FNdgB65vdu4RPU%2FnCyUr%2BjgZzJrOe1PU1%2FwnCZGnBxWPwfMWVCn%2Fw4hZMVOQ9brG7X930AlqvZ7W2BZ1JwWvPrlYaJgJfrwhXAopF68aOfT62HjVIbIei3j7fYhoMLr977wGOqUBpxRAlvGYevrE3HYaL570qPypkIWwxIv2QaJPBSb9oP4ODJqu4NmenUD3bQ9t7h2bItVSSpy748e1lqbVDMMbTTtlZxWMtXefwgSFpHeBoTnsYvho6PsVTmasn51qtk0DQgnJ7vwL3Jskj1wwbC9QAV4PhLA2EJ%2BFsP%2BYIHsRsTnFievyi1HdDdlYcdzR6b0zpwPkRWh2m6bHRQt3RZXRg4eUrUg2&X-Amz-Signature=dad84e38fd54187d48fcd94809eb69d1a87ffc9be60f1d14c3e6bbac51e5d2d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTVEJS4W%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsmdzwAKuUI7YmTE52HLUtugRg3hdeiS4AO8DaSu8hGgIgXb7aR40%2BRC1Bzj7UIaWAn9dQ8%2B16jUuz7KGzvGJAaYkqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZ%2BarWHYMDw7SHkwSrcA%2FlifbR%2B8m4IF5AEEFq4J8p%2F7fH2tJQF54V0756gcHcWELZKWFeXfuKbiEglVJ7Nk1DfXz4Is0a%2BpkaF3ZDmZrqbbLDhfnAYqdsDh08PEpAjt%2Fn2zPIgxhVVM1HhO1Y7b91FkzPKjqK6PGAF%2BrFRfQs2XvG9BOdMnE30tyNZN0%2FS3grAj%2BmZD2jrf8glj88LM6KpZNkH6Wrh3nMzA164URAUPQsGKQ783UzFwOVWZR0E55z3RjiVr6EQtfR%2B%2FtnqLl%2FpH97eE3rD6wpe5v%2BfhhThl1njmjBQfdl4HJwjldCrPi19tWe%2BJeTBGg9aeqJ4jH5b8%2FDjhlsX7%2BlCoUEyNCmmtPBtLb11ZAkZiMJxK9FSWuTp49OmXHdARVYYfU9%2FuYRV5hpFQ1yPbeYrdtrixB5Sfq%2FD3K9MIKSZPBZ7%2FBWtxxIEmOktR222jUJiePo7JSc8GvXr9U1tJDQsSsatu1gyWG2%2FuF3%2FDKWxDKW4UrnbsYlw8Mkx2b6tHM2pCUMN%2FNdgB65vdu4RPU%2FnCyUr%2BjgZzJrOe1PU1%2FwnCZGnBxWPwfMWVCn%2Fw4hZMVOQ9brG7X930AlqvZ7W2BZ1JwWvPrlYaJgJfrwhXAopF68aOfT62HjVIbIei3j7fYhoMLr977wGOqUBpxRAlvGYevrE3HYaL570qPypkIWwxIv2QaJPBSb9oP4ODJqu4NmenUD3bQ9t7h2bItVSSpy748e1lqbVDMMbTTtlZxWMtXefwgSFpHeBoTnsYvho6PsVTmasn51qtk0DQgnJ7vwL3Jskj1wwbC9QAV4PhLA2EJ%2BFsP%2BYIHsRsTnFievyi1HdDdlYcdzR6b0zpwPkRWh2m6bHRQt3RZXRg4eUrUg2&X-Amz-Signature=299a3ad4a9211284aded609e4158b3c5ee62fa0a50a47cc48e7ba010a4a94720&X-Amz-SignedHeaders=host&x-id=GetObject)
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


