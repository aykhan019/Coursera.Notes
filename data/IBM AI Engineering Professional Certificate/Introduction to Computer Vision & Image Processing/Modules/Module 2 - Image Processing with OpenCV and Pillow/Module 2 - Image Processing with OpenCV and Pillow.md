

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7UFUSGU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDMjEqb3dYGzYN2T1Xhe%2B8vBdP4v6mA3aOG87HJuqZJtAIgCgAADMVmS3PF2oXhQG7DJRFgUv9j37udfZsbkRn%2FOxAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKkoPlGbQv%2F3UIsjnircA5JV2JFMp4em0Hb0TcxwjmXsKmdLybdqKFtTTI7wVZq7X2wKZ0s1lAQoV5qpXg3E%2Bb6URIQ7Fu5pmRaZCxypsgNO%2FeBIfg2H1%2BhhOoUvqfG70uCOmh35jy3d4VviM4sNsLbGZwKpYzyhewkkiPlVLJaXDieydJvybL3RNY%2FbPBdI3bnj7j4Q2hYP%2FnPrnkwOvgejjXS3rwXK6%2FCB%2BmntZA3p2zUMBK6%2F9YAUxNCbVyPH3lnce1hcLiwiwtAVjnM0W%2BZZXL7dTQyCvjLfCoxRbtKdeVU%2FVNym8zMgZiGIFni4Og3Di%2BrQSoa1DzcoqBPstzd9FU6PgqoXJGINwN1aDbFP%2B%2BQndc20EtYqWFUud8n0K5DJ0r3jwuNXATX%2FscCHTGWkq8PAXbBu1lphko31lDo1IZmx4FmKPQcC19oUrJG64GoE0PCKJ4pK8L9sSgVu0F9Q8u06Y9v1O4U22F4F7uiG3kgX%2B4v6uGB2%2FIYhnFN14xhhWwTBidfdAMgVNgJxvEOPgUqKR%2BKmqDgZop8YG4HsdjmqCUSaj32jwzSDuvAOm269pBq9cFEu%2BuNKa3aVej%2F%2F2zPy5vILHYWkcO9Phk0pL7UNBS3fBxEVgdgcSQCLmUv8DK7CoW3w%2BjkjMMP5lr0GOqUBs0Zv%2FAk%2FbsJNq7NprFLjvq54rYH3VdxPk3xRtUO5wSlfG%2BRAkJMflHDEUY8RRf52%2F3Is6hrOjcd6n6FLNkbGD2v7e3tIpvXmzFZ9%2BlOGp3OoZf0IBqxTEtB0upTrRiZxVmDROou7PlZ2Y%2F%2F2U5jp4NoPZjnDeJH8EXStFuoscOwULqwvFRKEdngTBJ%2FPmVWfOjLIbJHWA6NehacVS33b9uAtAk8q&X-Amz-Signature=058bbaa2a2f094e385a0802ed832cc0fe97beeffe7532d47f64a0df0d70e6a71&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFWJ5XKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAs5EqKVWkkWFxUlFVIN%2FyB8Xlcx0kOz1gRToxmHNRgGAiArx%2BW5aBqTibsZ9wU8xBvD%2FI2cizymjJbaIkhbmbxZzyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM8aBSBdexJHD632XsKtwDDucz57kkDsjJkxN%2FFHxICn2iUDOVywbawBU093%2FYRNlfnsy%2BuJ9lzIBsy3MRDwyqV5QFkMhx2xFLLrI9j84uG3SO8MpQWjXQBaTkQyahIXY8PkdOgc6xfof%2Fe5a6ykqGRgB7cdNwKI4ejXD7aUjhAV3TyjPAGLcWpx5OE%2Fd7jwMqCrtYa99LXY5o7fE8VDOV6BEUTXq5Kz0bV0K7ET%2FDaPuV%2Bzqakjj2pSfk4FjccB0HT1ktsqZvhrPDqceyLJPOalHyUIR7SM70%2FqTvU%2FjZmLElq3uXzez8z4LzVXqTXQN34yoO6H9N2si95nPiDmIzfnsKM8SEfstI%2BqS%2BjiIhElnEKLn%2BGkCmY0wekLKCo06zeMsrASyLJBP9hdqJ3TDx8yt0nKahFcCVwfxwrF4jOgOL%2BNXixNtNY2hnuOXUJmociDDOHpEGhKUTd1mL5vOnvoCKlQqHZ2q7wPtDung4bheIbiwxgDaSOyIBwHB%2FTB0DTnLhWVIdxW9soSoGarYW3wcDrJr7P5xJbcvzJzqrCdbduPo9XJwniA%2BBz8Kw8vxKBXWrQ7eP4uGu9OK4qykULxwcD13AbvyfGUA9Gvf2i0Tg10borfXNeYoO1A1xxF7m6SrezzAgm9H75F8wz%2FmWvQY6pgHKpfV%2B92RqIfFaYP9CTQWdBsQcAHK8tAkinVTFqyh0Yl%2BnFRctH52QmTqSf4ExZo8R3od0lFXQi0SNcgrToN3BMlC15QbEV%2B8ew3WbK%2BR9XSBPAMaIqco6EJwOh2JKpNI0cU1IJjogjXoKmwHwSD6Uf%2FQqaSqX%2FPQ2gtFPxzMqzGZw9Vv0D7XAdYXB5adurSmHAV5wX3bUeYKKYNqzFy5%2FrqfW5kOq&X-Amz-Signature=983a82d68a4cc21ce877d89f64b3cd665ce1c0c97534a8bff810533e0da72121&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFWJ5XKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAs5EqKVWkkWFxUlFVIN%2FyB8Xlcx0kOz1gRToxmHNRgGAiArx%2BW5aBqTibsZ9wU8xBvD%2FI2cizymjJbaIkhbmbxZzyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM8aBSBdexJHD632XsKtwDDucz57kkDsjJkxN%2FFHxICn2iUDOVywbawBU093%2FYRNlfnsy%2BuJ9lzIBsy3MRDwyqV5QFkMhx2xFLLrI9j84uG3SO8MpQWjXQBaTkQyahIXY8PkdOgc6xfof%2Fe5a6ykqGRgB7cdNwKI4ejXD7aUjhAV3TyjPAGLcWpx5OE%2Fd7jwMqCrtYa99LXY5o7fE8VDOV6BEUTXq5Kz0bV0K7ET%2FDaPuV%2Bzqakjj2pSfk4FjccB0HT1ktsqZvhrPDqceyLJPOalHyUIR7SM70%2FqTvU%2FjZmLElq3uXzez8z4LzVXqTXQN34yoO6H9N2si95nPiDmIzfnsKM8SEfstI%2BqS%2BjiIhElnEKLn%2BGkCmY0wekLKCo06zeMsrASyLJBP9hdqJ3TDx8yt0nKahFcCVwfxwrF4jOgOL%2BNXixNtNY2hnuOXUJmociDDOHpEGhKUTd1mL5vOnvoCKlQqHZ2q7wPtDung4bheIbiwxgDaSOyIBwHB%2FTB0DTnLhWVIdxW9soSoGarYW3wcDrJr7P5xJbcvzJzqrCdbduPo9XJwniA%2BBz8Kw8vxKBXWrQ7eP4uGu9OK4qykULxwcD13AbvyfGUA9Gvf2i0Tg10borfXNeYoO1A1xxF7m6SrezzAgm9H75F8wz%2FmWvQY6pgHKpfV%2B92RqIfFaYP9CTQWdBsQcAHK8tAkinVTFqyh0Yl%2BnFRctH52QmTqSf4ExZo8R3od0lFXQi0SNcgrToN3BMlC15QbEV%2B8ew3WbK%2BR9XSBPAMaIqco6EJwOh2JKpNI0cU1IJjogjXoKmwHwSD6Uf%2FQqaSqX%2FPQ2gtFPxzMqzGZw9Vv0D7XAdYXB5adurSmHAV5wX3bUeYKKYNqzFy5%2FrqfW5kOq&X-Amz-Signature=5f338c6e8744184c57ddb4d026bd7c7b8f44fdbb9afe4ee3bad7e6376dc661ae&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFWJ5XKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAs5EqKVWkkWFxUlFVIN%2FyB8Xlcx0kOz1gRToxmHNRgGAiArx%2BW5aBqTibsZ9wU8xBvD%2FI2cizymjJbaIkhbmbxZzyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM8aBSBdexJHD632XsKtwDDucz57kkDsjJkxN%2FFHxICn2iUDOVywbawBU093%2FYRNlfnsy%2BuJ9lzIBsy3MRDwyqV5QFkMhx2xFLLrI9j84uG3SO8MpQWjXQBaTkQyahIXY8PkdOgc6xfof%2Fe5a6ykqGRgB7cdNwKI4ejXD7aUjhAV3TyjPAGLcWpx5OE%2Fd7jwMqCrtYa99LXY5o7fE8VDOV6BEUTXq5Kz0bV0K7ET%2FDaPuV%2Bzqakjj2pSfk4FjccB0HT1ktsqZvhrPDqceyLJPOalHyUIR7SM70%2FqTvU%2FjZmLElq3uXzez8z4LzVXqTXQN34yoO6H9N2si95nPiDmIzfnsKM8SEfstI%2BqS%2BjiIhElnEKLn%2BGkCmY0wekLKCo06zeMsrASyLJBP9hdqJ3TDx8yt0nKahFcCVwfxwrF4jOgOL%2BNXixNtNY2hnuOXUJmociDDOHpEGhKUTd1mL5vOnvoCKlQqHZ2q7wPtDung4bheIbiwxgDaSOyIBwHB%2FTB0DTnLhWVIdxW9soSoGarYW3wcDrJr7P5xJbcvzJzqrCdbduPo9XJwniA%2BBz8Kw8vxKBXWrQ7eP4uGu9OK4qykULxwcD13AbvyfGUA9Gvf2i0Tg10borfXNeYoO1A1xxF7m6SrezzAgm9H75F8wz%2FmWvQY6pgHKpfV%2B92RqIfFaYP9CTQWdBsQcAHK8tAkinVTFqyh0Yl%2BnFRctH52QmTqSf4ExZo8R3od0lFXQi0SNcgrToN3BMlC15QbEV%2B8ew3WbK%2BR9XSBPAMaIqco6EJwOh2JKpNI0cU1IJjogjXoKmwHwSD6Uf%2FQqaSqX%2FPQ2gtFPxzMqzGZw9Vv0D7XAdYXB5adurSmHAV5wX3bUeYKKYNqzFy5%2FrqfW5kOq&X-Amz-Signature=120f1da29e3b112ce40bc47d3c6e8e21cc6417dddea44c0eb4afd70aab03ed22&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFWJ5XKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAs5EqKVWkkWFxUlFVIN%2FyB8Xlcx0kOz1gRToxmHNRgGAiArx%2BW5aBqTibsZ9wU8xBvD%2FI2cizymjJbaIkhbmbxZzyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM8aBSBdexJHD632XsKtwDDucz57kkDsjJkxN%2FFHxICn2iUDOVywbawBU093%2FYRNlfnsy%2BuJ9lzIBsy3MRDwyqV5QFkMhx2xFLLrI9j84uG3SO8MpQWjXQBaTkQyahIXY8PkdOgc6xfof%2Fe5a6ykqGRgB7cdNwKI4ejXD7aUjhAV3TyjPAGLcWpx5OE%2Fd7jwMqCrtYa99LXY5o7fE8VDOV6BEUTXq5Kz0bV0K7ET%2FDaPuV%2Bzqakjj2pSfk4FjccB0HT1ktsqZvhrPDqceyLJPOalHyUIR7SM70%2FqTvU%2FjZmLElq3uXzez8z4LzVXqTXQN34yoO6H9N2si95nPiDmIzfnsKM8SEfstI%2BqS%2BjiIhElnEKLn%2BGkCmY0wekLKCo06zeMsrASyLJBP9hdqJ3TDx8yt0nKahFcCVwfxwrF4jOgOL%2BNXixNtNY2hnuOXUJmociDDOHpEGhKUTd1mL5vOnvoCKlQqHZ2q7wPtDung4bheIbiwxgDaSOyIBwHB%2FTB0DTnLhWVIdxW9soSoGarYW3wcDrJr7P5xJbcvzJzqrCdbduPo9XJwniA%2BBz8Kw8vxKBXWrQ7eP4uGu9OK4qykULxwcD13AbvyfGUA9Gvf2i0Tg10borfXNeYoO1A1xxF7m6SrezzAgm9H75F8wz%2FmWvQY6pgHKpfV%2B92RqIfFaYP9CTQWdBsQcAHK8tAkinVTFqyh0Yl%2BnFRctH52QmTqSf4ExZo8R3od0lFXQi0SNcgrToN3BMlC15QbEV%2B8ew3WbK%2BR9XSBPAMaIqco6EJwOh2JKpNI0cU1IJjogjXoKmwHwSD6Uf%2FQqaSqX%2FPQ2gtFPxzMqzGZw9Vv0D7XAdYXB5adurSmHAV5wX3bUeYKKYNqzFy5%2FrqfW5kOq&X-Amz-Signature=3a7f1d27c3093c29acd6ce9ad3b78e54343c628edf4c11216d55a94a9201aec7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFWJ5XKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIAs5EqKVWkkWFxUlFVIN%2FyB8Xlcx0kOz1gRToxmHNRgGAiArx%2BW5aBqTibsZ9wU8xBvD%2FI2cizymjJbaIkhbmbxZzyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM8aBSBdexJHD632XsKtwDDucz57kkDsjJkxN%2FFHxICn2iUDOVywbawBU093%2FYRNlfnsy%2BuJ9lzIBsy3MRDwyqV5QFkMhx2xFLLrI9j84uG3SO8MpQWjXQBaTkQyahIXY8PkdOgc6xfof%2Fe5a6ykqGRgB7cdNwKI4ejXD7aUjhAV3TyjPAGLcWpx5OE%2Fd7jwMqCrtYa99LXY5o7fE8VDOV6BEUTXq5Kz0bV0K7ET%2FDaPuV%2Bzqakjj2pSfk4FjccB0HT1ktsqZvhrPDqceyLJPOalHyUIR7SM70%2FqTvU%2FjZmLElq3uXzez8z4LzVXqTXQN34yoO6H9N2si95nPiDmIzfnsKM8SEfstI%2BqS%2BjiIhElnEKLn%2BGkCmY0wekLKCo06zeMsrASyLJBP9hdqJ3TDx8yt0nKahFcCVwfxwrF4jOgOL%2BNXixNtNY2hnuOXUJmociDDOHpEGhKUTd1mL5vOnvoCKlQqHZ2q7wPtDung4bheIbiwxgDaSOyIBwHB%2FTB0DTnLhWVIdxW9soSoGarYW3wcDrJr7P5xJbcvzJzqrCdbduPo9XJwniA%2BBz8Kw8vxKBXWrQ7eP4uGu9OK4qykULxwcD13AbvyfGUA9Gvf2i0Tg10borfXNeYoO1A1xxF7m6SrezzAgm9H75F8wz%2FmWvQY6pgHKpfV%2B92RqIfFaYP9CTQWdBsQcAHK8tAkinVTFqyh0Yl%2BnFRctH52QmTqSf4ExZo8R3od0lFXQi0SNcgrToN3BMlC15QbEV%2B8ew3WbK%2BR9XSBPAMaIqco6EJwOh2JKpNI0cU1IJjogjXoKmwHwSD6Uf%2FQqaSqX%2FPQ2gtFPxzMqzGZw9Vv0D7XAdYXB5adurSmHAV5wX3bUeYKKYNqzFy5%2FrqfW5kOq&X-Amz-Signature=658268fe4ced9921c5d8fb94c0da486fbe87b150643ba1217c7a78c453e80ce1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7UFUSGU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDMjEqb3dYGzYN2T1Xhe%2B8vBdP4v6mA3aOG87HJuqZJtAIgCgAADMVmS3PF2oXhQG7DJRFgUv9j37udfZsbkRn%2FOxAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKkoPlGbQv%2F3UIsjnircA5JV2JFMp4em0Hb0TcxwjmXsKmdLybdqKFtTTI7wVZq7X2wKZ0s1lAQoV5qpXg3E%2Bb6URIQ7Fu5pmRaZCxypsgNO%2FeBIfg2H1%2BhhOoUvqfG70uCOmh35jy3d4VviM4sNsLbGZwKpYzyhewkkiPlVLJaXDieydJvybL3RNY%2FbPBdI3bnj7j4Q2hYP%2FnPrnkwOvgejjXS3rwXK6%2FCB%2BmntZA3p2zUMBK6%2F9YAUxNCbVyPH3lnce1hcLiwiwtAVjnM0W%2BZZXL7dTQyCvjLfCoxRbtKdeVU%2FVNym8zMgZiGIFni4Og3Di%2BrQSoa1DzcoqBPstzd9FU6PgqoXJGINwN1aDbFP%2B%2BQndc20EtYqWFUud8n0K5DJ0r3jwuNXATX%2FscCHTGWkq8PAXbBu1lphko31lDo1IZmx4FmKPQcC19oUrJG64GoE0PCKJ4pK8L9sSgVu0F9Q8u06Y9v1O4U22F4F7uiG3kgX%2B4v6uGB2%2FIYhnFN14xhhWwTBidfdAMgVNgJxvEOPgUqKR%2BKmqDgZop8YG4HsdjmqCUSaj32jwzSDuvAOm269pBq9cFEu%2BuNKa3aVej%2F%2F2zPy5vILHYWkcO9Phk0pL7UNBS3fBxEVgdgcSQCLmUv8DK7CoW3w%2BjkjMMP5lr0GOqUBs0Zv%2FAk%2FbsJNq7NprFLjvq54rYH3VdxPk3xRtUO5wSlfG%2BRAkJMflHDEUY8RRf52%2F3Is6hrOjcd6n6FLNkbGD2v7e3tIpvXmzFZ9%2BlOGp3OoZf0IBqxTEtB0upTrRiZxVmDROou7PlZ2Y%2F%2F2U5jp4NoPZjnDeJH8EXStFuoscOwULqwvFRKEdngTBJ%2FPmVWfOjLIbJHWA6NehacVS33b9uAtAk8q&X-Amz-Signature=c83d97fdc1f924b5d5b140ea1f9d30e5cd2c75164d16e8eb29a012fbcc726347&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7UFUSGU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDMjEqb3dYGzYN2T1Xhe%2B8vBdP4v6mA3aOG87HJuqZJtAIgCgAADMVmS3PF2oXhQG7DJRFgUv9j37udfZsbkRn%2FOxAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKkoPlGbQv%2F3UIsjnircA5JV2JFMp4em0Hb0TcxwjmXsKmdLybdqKFtTTI7wVZq7X2wKZ0s1lAQoV5qpXg3E%2Bb6URIQ7Fu5pmRaZCxypsgNO%2FeBIfg2H1%2BhhOoUvqfG70uCOmh35jy3d4VviM4sNsLbGZwKpYzyhewkkiPlVLJaXDieydJvybL3RNY%2FbPBdI3bnj7j4Q2hYP%2FnPrnkwOvgejjXS3rwXK6%2FCB%2BmntZA3p2zUMBK6%2F9YAUxNCbVyPH3lnce1hcLiwiwtAVjnM0W%2BZZXL7dTQyCvjLfCoxRbtKdeVU%2FVNym8zMgZiGIFni4Og3Di%2BrQSoa1DzcoqBPstzd9FU6PgqoXJGINwN1aDbFP%2B%2BQndc20EtYqWFUud8n0K5DJ0r3jwuNXATX%2FscCHTGWkq8PAXbBu1lphko31lDo1IZmx4FmKPQcC19oUrJG64GoE0PCKJ4pK8L9sSgVu0F9Q8u06Y9v1O4U22F4F7uiG3kgX%2B4v6uGB2%2FIYhnFN14xhhWwTBidfdAMgVNgJxvEOPgUqKR%2BKmqDgZop8YG4HsdjmqCUSaj32jwzSDuvAOm269pBq9cFEu%2BuNKa3aVej%2F%2F2zPy5vILHYWkcO9Phk0pL7UNBS3fBxEVgdgcSQCLmUv8DK7CoW3w%2BjkjMMP5lr0GOqUBs0Zv%2FAk%2FbsJNq7NprFLjvq54rYH3VdxPk3xRtUO5wSlfG%2BRAkJMflHDEUY8RRf52%2F3Is6hrOjcd6n6FLNkbGD2v7e3tIpvXmzFZ9%2BlOGp3OoZf0IBqxTEtB0upTrRiZxVmDROou7PlZ2Y%2F%2F2U5jp4NoPZjnDeJH8EXStFuoscOwULqwvFRKEdngTBJ%2FPmVWfOjLIbJHWA6NehacVS33b9uAtAk8q&X-Amz-Signature=55e1bdf7179085fd69c3f5d5253a81f6f81b97349f0dec7bbb8cbed1dd288457&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7UFUSGU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDMjEqb3dYGzYN2T1Xhe%2B8vBdP4v6mA3aOG87HJuqZJtAIgCgAADMVmS3PF2oXhQG7DJRFgUv9j37udfZsbkRn%2FOxAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKkoPlGbQv%2F3UIsjnircA5JV2JFMp4em0Hb0TcxwjmXsKmdLybdqKFtTTI7wVZq7X2wKZ0s1lAQoV5qpXg3E%2Bb6URIQ7Fu5pmRaZCxypsgNO%2FeBIfg2H1%2BhhOoUvqfG70uCOmh35jy3d4VviM4sNsLbGZwKpYzyhewkkiPlVLJaXDieydJvybL3RNY%2FbPBdI3bnj7j4Q2hYP%2FnPrnkwOvgejjXS3rwXK6%2FCB%2BmntZA3p2zUMBK6%2F9YAUxNCbVyPH3lnce1hcLiwiwtAVjnM0W%2BZZXL7dTQyCvjLfCoxRbtKdeVU%2FVNym8zMgZiGIFni4Og3Di%2BrQSoa1DzcoqBPstzd9FU6PgqoXJGINwN1aDbFP%2B%2BQndc20EtYqWFUud8n0K5DJ0r3jwuNXATX%2FscCHTGWkq8PAXbBu1lphko31lDo1IZmx4FmKPQcC19oUrJG64GoE0PCKJ4pK8L9sSgVu0F9Q8u06Y9v1O4U22F4F7uiG3kgX%2B4v6uGB2%2FIYhnFN14xhhWwTBidfdAMgVNgJxvEOPgUqKR%2BKmqDgZop8YG4HsdjmqCUSaj32jwzSDuvAOm269pBq9cFEu%2BuNKa3aVej%2F%2F2zPy5vILHYWkcO9Phk0pL7UNBS3fBxEVgdgcSQCLmUv8DK7CoW3w%2BjkjMMP5lr0GOqUBs0Zv%2FAk%2FbsJNq7NprFLjvq54rYH3VdxPk3xRtUO5wSlfG%2BRAkJMflHDEUY8RRf52%2F3Is6hrOjcd6n6FLNkbGD2v7e3tIpvXmzFZ9%2BlOGp3OoZf0IBqxTEtB0upTrRiZxVmDROou7PlZ2Y%2F%2F2U5jp4NoPZjnDeJH8EXStFuoscOwULqwvFRKEdngTBJ%2FPmVWfOjLIbJHWA6NehacVS33b9uAtAk8q&X-Amz-Signature=33c4240dc8d58a14ad942eace421a341a12134d6ccd9850319401af37fb11b9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7UFUSGU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDMjEqb3dYGzYN2T1Xhe%2B8vBdP4v6mA3aOG87HJuqZJtAIgCgAADMVmS3PF2oXhQG7DJRFgUv9j37udfZsbkRn%2FOxAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKkoPlGbQv%2F3UIsjnircA5JV2JFMp4em0Hb0TcxwjmXsKmdLybdqKFtTTI7wVZq7X2wKZ0s1lAQoV5qpXg3E%2Bb6URIQ7Fu5pmRaZCxypsgNO%2FeBIfg2H1%2BhhOoUvqfG70uCOmh35jy3d4VviM4sNsLbGZwKpYzyhewkkiPlVLJaXDieydJvybL3RNY%2FbPBdI3bnj7j4Q2hYP%2FnPrnkwOvgejjXS3rwXK6%2FCB%2BmntZA3p2zUMBK6%2F9YAUxNCbVyPH3lnce1hcLiwiwtAVjnM0W%2BZZXL7dTQyCvjLfCoxRbtKdeVU%2FVNym8zMgZiGIFni4Og3Di%2BrQSoa1DzcoqBPstzd9FU6PgqoXJGINwN1aDbFP%2B%2BQndc20EtYqWFUud8n0K5DJ0r3jwuNXATX%2FscCHTGWkq8PAXbBu1lphko31lDo1IZmx4FmKPQcC19oUrJG64GoE0PCKJ4pK8L9sSgVu0F9Q8u06Y9v1O4U22F4F7uiG3kgX%2B4v6uGB2%2FIYhnFN14xhhWwTBidfdAMgVNgJxvEOPgUqKR%2BKmqDgZop8YG4HsdjmqCUSaj32jwzSDuvAOm269pBq9cFEu%2BuNKa3aVej%2F%2F2zPy5vILHYWkcO9Phk0pL7UNBS3fBxEVgdgcSQCLmUv8DK7CoW3w%2BjkjMMP5lr0GOqUBs0Zv%2FAk%2FbsJNq7NprFLjvq54rYH3VdxPk3xRtUO5wSlfG%2BRAkJMflHDEUY8RRf52%2F3Is6hrOjcd6n6FLNkbGD2v7e3tIpvXmzFZ9%2BlOGp3OoZf0IBqxTEtB0upTrRiZxVmDROou7PlZ2Y%2F%2F2U5jp4NoPZjnDeJH8EXStFuoscOwULqwvFRKEdngTBJ%2FPmVWfOjLIbJHWA6NehacVS33b9uAtAk8q&X-Amz-Signature=98efe83f64dde0005c9d34ef73007f0f7f24bac6ab96ee52537d5e1fdc41364c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7UFUSGU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDMjEqb3dYGzYN2T1Xhe%2B8vBdP4v6mA3aOG87HJuqZJtAIgCgAADMVmS3PF2oXhQG7DJRFgUv9j37udfZsbkRn%2FOxAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKkoPlGbQv%2F3UIsjnircA5JV2JFMp4em0Hb0TcxwjmXsKmdLybdqKFtTTI7wVZq7X2wKZ0s1lAQoV5qpXg3E%2Bb6URIQ7Fu5pmRaZCxypsgNO%2FeBIfg2H1%2BhhOoUvqfG70uCOmh35jy3d4VviM4sNsLbGZwKpYzyhewkkiPlVLJaXDieydJvybL3RNY%2FbPBdI3bnj7j4Q2hYP%2FnPrnkwOvgejjXS3rwXK6%2FCB%2BmntZA3p2zUMBK6%2F9YAUxNCbVyPH3lnce1hcLiwiwtAVjnM0W%2BZZXL7dTQyCvjLfCoxRbtKdeVU%2FVNym8zMgZiGIFni4Og3Di%2BrQSoa1DzcoqBPstzd9FU6PgqoXJGINwN1aDbFP%2B%2BQndc20EtYqWFUud8n0K5DJ0r3jwuNXATX%2FscCHTGWkq8PAXbBu1lphko31lDo1IZmx4FmKPQcC19oUrJG64GoE0PCKJ4pK8L9sSgVu0F9Q8u06Y9v1O4U22F4F7uiG3kgX%2B4v6uGB2%2FIYhnFN14xhhWwTBidfdAMgVNgJxvEOPgUqKR%2BKmqDgZop8YG4HsdjmqCUSaj32jwzSDuvAOm269pBq9cFEu%2BuNKa3aVej%2F%2F2zPy5vILHYWkcO9Phk0pL7UNBS3fBxEVgdgcSQCLmUv8DK7CoW3w%2BjkjMMP5lr0GOqUBs0Zv%2FAk%2FbsJNq7NprFLjvq54rYH3VdxPk3xRtUO5wSlfG%2BRAkJMflHDEUY8RRf52%2F3Is6hrOjcd6n6FLNkbGD2v7e3tIpvXmzFZ9%2BlOGp3OoZf0IBqxTEtB0upTrRiZxVmDROou7PlZ2Y%2F%2F2U5jp4NoPZjnDeJH8EXStFuoscOwULqwvFRKEdngTBJ%2FPmVWfOjLIbJHWA6NehacVS33b9uAtAk8q&X-Amz-Signature=ff93131f30a465a1f03baaf40fbfe304495c7ff7bbafb5f807031b5050860a6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


