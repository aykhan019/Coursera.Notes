

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4JDZWJ4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDOQn%2FBbHZ%2BoWlkJa0jPhzXrtqt721LpY7v2FN19PzmTwIgf0AlcY4t84LXG06J4UJ7qFYofQMbbCgai0FjSzAxL0cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEVE%2BobWNnv%2FlXDlBCrcAw4hu4gDo8Ygv4qvtYamHXUGm1vsF2wRBiv9qCypDiZoTjiROeUCxcs%2Fdb0LwtcdJIpwFE%2Bgy0vQcHU2D4dWxrSRz5eTkA0051x3WgI%2BTb04UN6%2FFGHFX42wuw95cFKXB4VY%2F1CJpQ%2FD%2BgmrIFA%2F9dSy50pMsKyys4nNfuR5eMvvXUHoQdGIv%2FzzuEUAekzMIjVlACWCbC7aA0tx7MPHj6jnWgUxL%2BYsqKIqu0CF75ZXX5QslxlBk2DvQGSj534wk8rry49XMSxv76%2Fi41EzY92%2FMkwmfox0UN%2F6zdOnNAai3XNH476G2DMiUokSkQReqorDvS4df2lNZ8qLSa2qPPxrTE9s2SnYdXJU8DkPaN8RzoijkiXp83LMRlfKm%2FFhuuGp6W5DItk9gprtB75RSfqt7GDqBFnFebUOkSND43ZD7s87WHGSb5%2FsrFNwijPRS%2F4R0w0J%2FV3SBHi3OK0kEWxKUwjkOGqgSnWL5p7vo0hem8mkx0efkfK7Or%2FGxX48TxqKYfio3ge5%2F%2Bjdu98VT0A7%2B9tM%2BheCfMaOS1g4Sdv1TMsS07709MgF0a00vUbdNj6ImnNJcwZ8g3BkEwdzwHaPx4j9AbWPZd3Ta%2FSZKh4AV7Mp3I603kDMDD6OMMnd5LwGOqUBy%2Fcv2PYhaDk3Reu%2FRjoDmAOGHSqk5HQJG0Oar9CmuiA0%2BGmr7%2BQjBWU5Mk9WMETH5Cs9W9sl3vZmAoEWTlpiu1Zxzyze76Jz1ShnXFAK4ag2xngta7vUT1Ik4OWMDnCBt3wuZ4zZlCFwRLUHbFMmlUkLtU2BOvxsFqszS1POfFaNjpjAJ50QUDP3F9doh7YLfHrAN47fImkZRibLWA7%2F7%2Bvpdr7o&X-Amz-Signature=53c55d251509377cedce7f9092510dad055a0046c13661d6216999242aa49ecb&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUZBKLLK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBVFEI8VleudnJDZNUbmWiKhWqLEqEPay%2BR6ul4IEkU%2FAiEAnNniOURYxeJqRL%2FFVY%2B2Nn2qhvJY67ctzw6QApytA68q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHJYaFyMZ0ZjdUHrtCrcA7sp%2FTo8lk62p9TIn3iz9ez8MyytzUirvWBX650FbAKlZ84z36RL4z60xre2ODf4fzihbkN3Zi8TIMhu51ESW4UathFGrPsOra0x9ml95AHlVJ80MTw1NF%2BOcGrnGANbE%2FJi%2BAIALdX0hO5OgLkpe1FJpxOwcp4GulIi1KVJd26TvvO4DiRKn0lfAh61rQLV1FCheZ5lF2Rk%2Fj1D5xWld9lIt03eyoReh%2FSH2Jkr9xYsH%2FPJSapnlFPILpArlZdu9YwcOtghdkY5AgTi5BmRQLN4cEQQAj%2FZuxGXJ6AlKF4fnxmoKxKITGkd191k2dz5Cw6opJ7FBeY27dDPo%2F7%2Fi0ba1fq2uTCZJj%2FBifbQkJeoAgKimK373RjE1Y0pSCgNnYcldCWT9paRCRvI7gbkqJVuOqTWgvCRCof9glQ5TIAxhu%2F5jO4f6FC5bn%2B6axqkfRbtoL8W3TSP5YkORXXlytLCGFBxIES6kgJoUOd5CIJRlGvzS1ewF1xL%2FM2TSD5RdOaLmo9tlBslVdeHLU3l%2FLf%2FYW1qs%2FlvSx9Ad4hnemZpJF2UltZ0BQ4QPrA%2BK0St%2BwBzy%2FU9xg%2BhkSUlQVHjao0ByK%2FbOmC%2B%2B97uf5MYc6d7KQZo0eLcB9F2Xt%2FNMJ3o5LwGOqUBahJ9PIc2CRoCOgPvDkCWPHePZ6FXCh%2FMmITy2A25JH0AlZln4oQXjFFVvBFnlQC3P29xVWGVTe%2BCMehmxITXxcsotepPLQW7zrtaNOxCtq7YHwWLmKMvFzPBVeP3%2FoxXrwTQhaS1T%2FfISi%2BpNYjnmA7dtggy5Dcm4cYcBRoR5hgeKwVw5ZgtjDyfrwMP6MucLp0yD9vR%2FN8jFbGkH5TQRChcAnHl&X-Amz-Signature=44f4d1078ef73f5b0e9e67cdfe38cad027b1a484c64484fd2bdcf759550d5a58&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUZBKLLK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBVFEI8VleudnJDZNUbmWiKhWqLEqEPay%2BR6ul4IEkU%2FAiEAnNniOURYxeJqRL%2FFVY%2B2Nn2qhvJY67ctzw6QApytA68q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHJYaFyMZ0ZjdUHrtCrcA7sp%2FTo8lk62p9TIn3iz9ez8MyytzUirvWBX650FbAKlZ84z36RL4z60xre2ODf4fzihbkN3Zi8TIMhu51ESW4UathFGrPsOra0x9ml95AHlVJ80MTw1NF%2BOcGrnGANbE%2FJi%2BAIALdX0hO5OgLkpe1FJpxOwcp4GulIi1KVJd26TvvO4DiRKn0lfAh61rQLV1FCheZ5lF2Rk%2Fj1D5xWld9lIt03eyoReh%2FSH2Jkr9xYsH%2FPJSapnlFPILpArlZdu9YwcOtghdkY5AgTi5BmRQLN4cEQQAj%2FZuxGXJ6AlKF4fnxmoKxKITGkd191k2dz5Cw6opJ7FBeY27dDPo%2F7%2Fi0ba1fq2uTCZJj%2FBifbQkJeoAgKimK373RjE1Y0pSCgNnYcldCWT9paRCRvI7gbkqJVuOqTWgvCRCof9glQ5TIAxhu%2F5jO4f6FC5bn%2B6axqkfRbtoL8W3TSP5YkORXXlytLCGFBxIES6kgJoUOd5CIJRlGvzS1ewF1xL%2FM2TSD5RdOaLmo9tlBslVdeHLU3l%2FLf%2FYW1qs%2FlvSx9Ad4hnemZpJF2UltZ0BQ4QPrA%2BK0St%2BwBzy%2FU9xg%2BhkSUlQVHjao0ByK%2FbOmC%2B%2B97uf5MYc6d7KQZo0eLcB9F2Xt%2FNMJ3o5LwGOqUBahJ9PIc2CRoCOgPvDkCWPHePZ6FXCh%2FMmITy2A25JH0AlZln4oQXjFFVvBFnlQC3P29xVWGVTe%2BCMehmxITXxcsotepPLQW7zrtaNOxCtq7YHwWLmKMvFzPBVeP3%2FoxXrwTQhaS1T%2FfISi%2BpNYjnmA7dtggy5Dcm4cYcBRoR5hgeKwVw5ZgtjDyfrwMP6MucLp0yD9vR%2FN8jFbGkH5TQRChcAnHl&X-Amz-Signature=28857525ebe32e4308c92ccb61c57787f8315aa1e455fc0088cc6550f5348f1d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUZBKLLK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBVFEI8VleudnJDZNUbmWiKhWqLEqEPay%2BR6ul4IEkU%2FAiEAnNniOURYxeJqRL%2FFVY%2B2Nn2qhvJY67ctzw6QApytA68q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHJYaFyMZ0ZjdUHrtCrcA7sp%2FTo8lk62p9TIn3iz9ez8MyytzUirvWBX650FbAKlZ84z36RL4z60xre2ODf4fzihbkN3Zi8TIMhu51ESW4UathFGrPsOra0x9ml95AHlVJ80MTw1NF%2BOcGrnGANbE%2FJi%2BAIALdX0hO5OgLkpe1FJpxOwcp4GulIi1KVJd26TvvO4DiRKn0lfAh61rQLV1FCheZ5lF2Rk%2Fj1D5xWld9lIt03eyoReh%2FSH2Jkr9xYsH%2FPJSapnlFPILpArlZdu9YwcOtghdkY5AgTi5BmRQLN4cEQQAj%2FZuxGXJ6AlKF4fnxmoKxKITGkd191k2dz5Cw6opJ7FBeY27dDPo%2F7%2Fi0ba1fq2uTCZJj%2FBifbQkJeoAgKimK373RjE1Y0pSCgNnYcldCWT9paRCRvI7gbkqJVuOqTWgvCRCof9glQ5TIAxhu%2F5jO4f6FC5bn%2B6axqkfRbtoL8W3TSP5YkORXXlytLCGFBxIES6kgJoUOd5CIJRlGvzS1ewF1xL%2FM2TSD5RdOaLmo9tlBslVdeHLU3l%2FLf%2FYW1qs%2FlvSx9Ad4hnemZpJF2UltZ0BQ4QPrA%2BK0St%2BwBzy%2FU9xg%2BhkSUlQVHjao0ByK%2FbOmC%2B%2B97uf5MYc6d7KQZo0eLcB9F2Xt%2FNMJ3o5LwGOqUBahJ9PIc2CRoCOgPvDkCWPHePZ6FXCh%2FMmITy2A25JH0AlZln4oQXjFFVvBFnlQC3P29xVWGVTe%2BCMehmxITXxcsotepPLQW7zrtaNOxCtq7YHwWLmKMvFzPBVeP3%2FoxXrwTQhaS1T%2FfISi%2BpNYjnmA7dtggy5Dcm4cYcBRoR5hgeKwVw5ZgtjDyfrwMP6MucLp0yD9vR%2FN8jFbGkH5TQRChcAnHl&X-Amz-Signature=eda0e93ee6fb6f1e5bbc9da5e15c3f1361a6feee22e1dce47937fea372a54547&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUZBKLLK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBVFEI8VleudnJDZNUbmWiKhWqLEqEPay%2BR6ul4IEkU%2FAiEAnNniOURYxeJqRL%2FFVY%2B2Nn2qhvJY67ctzw6QApytA68q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHJYaFyMZ0ZjdUHrtCrcA7sp%2FTo8lk62p9TIn3iz9ez8MyytzUirvWBX650FbAKlZ84z36RL4z60xre2ODf4fzihbkN3Zi8TIMhu51ESW4UathFGrPsOra0x9ml95AHlVJ80MTw1NF%2BOcGrnGANbE%2FJi%2BAIALdX0hO5OgLkpe1FJpxOwcp4GulIi1KVJd26TvvO4DiRKn0lfAh61rQLV1FCheZ5lF2Rk%2Fj1D5xWld9lIt03eyoReh%2FSH2Jkr9xYsH%2FPJSapnlFPILpArlZdu9YwcOtghdkY5AgTi5BmRQLN4cEQQAj%2FZuxGXJ6AlKF4fnxmoKxKITGkd191k2dz5Cw6opJ7FBeY27dDPo%2F7%2Fi0ba1fq2uTCZJj%2FBifbQkJeoAgKimK373RjE1Y0pSCgNnYcldCWT9paRCRvI7gbkqJVuOqTWgvCRCof9glQ5TIAxhu%2F5jO4f6FC5bn%2B6axqkfRbtoL8W3TSP5YkORXXlytLCGFBxIES6kgJoUOd5CIJRlGvzS1ewF1xL%2FM2TSD5RdOaLmo9tlBslVdeHLU3l%2FLf%2FYW1qs%2FlvSx9Ad4hnemZpJF2UltZ0BQ4QPrA%2BK0St%2BwBzy%2FU9xg%2BhkSUlQVHjao0ByK%2FbOmC%2B%2B97uf5MYc6d7KQZo0eLcB9F2Xt%2FNMJ3o5LwGOqUBahJ9PIc2CRoCOgPvDkCWPHePZ6FXCh%2FMmITy2A25JH0AlZln4oQXjFFVvBFnlQC3P29xVWGVTe%2BCMehmxITXxcsotepPLQW7zrtaNOxCtq7YHwWLmKMvFzPBVeP3%2FoxXrwTQhaS1T%2FfISi%2BpNYjnmA7dtggy5Dcm4cYcBRoR5hgeKwVw5ZgtjDyfrwMP6MucLp0yD9vR%2FN8jFbGkH5TQRChcAnHl&X-Amz-Signature=98fabd3adf4f2738c8c6ff8a3b2debde14bb2083956f3fb386103a4d0d375264&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUZBKLLK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBVFEI8VleudnJDZNUbmWiKhWqLEqEPay%2BR6ul4IEkU%2FAiEAnNniOURYxeJqRL%2FFVY%2B2Nn2qhvJY67ctzw6QApytA68q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHJYaFyMZ0ZjdUHrtCrcA7sp%2FTo8lk62p9TIn3iz9ez8MyytzUirvWBX650FbAKlZ84z36RL4z60xre2ODf4fzihbkN3Zi8TIMhu51ESW4UathFGrPsOra0x9ml95AHlVJ80MTw1NF%2BOcGrnGANbE%2FJi%2BAIALdX0hO5OgLkpe1FJpxOwcp4GulIi1KVJd26TvvO4DiRKn0lfAh61rQLV1FCheZ5lF2Rk%2Fj1D5xWld9lIt03eyoReh%2FSH2Jkr9xYsH%2FPJSapnlFPILpArlZdu9YwcOtghdkY5AgTi5BmRQLN4cEQQAj%2FZuxGXJ6AlKF4fnxmoKxKITGkd191k2dz5Cw6opJ7FBeY27dDPo%2F7%2Fi0ba1fq2uTCZJj%2FBifbQkJeoAgKimK373RjE1Y0pSCgNnYcldCWT9paRCRvI7gbkqJVuOqTWgvCRCof9glQ5TIAxhu%2F5jO4f6FC5bn%2B6axqkfRbtoL8W3TSP5YkORXXlytLCGFBxIES6kgJoUOd5CIJRlGvzS1ewF1xL%2FM2TSD5RdOaLmo9tlBslVdeHLU3l%2FLf%2FYW1qs%2FlvSx9Ad4hnemZpJF2UltZ0BQ4QPrA%2BK0St%2BwBzy%2FU9xg%2BhkSUlQVHjao0ByK%2FbOmC%2B%2B97uf5MYc6d7KQZo0eLcB9F2Xt%2FNMJ3o5LwGOqUBahJ9PIc2CRoCOgPvDkCWPHePZ6FXCh%2FMmITy2A25JH0AlZln4oQXjFFVvBFnlQC3P29xVWGVTe%2BCMehmxITXxcsotepPLQW7zrtaNOxCtq7YHwWLmKMvFzPBVeP3%2FoxXrwTQhaS1T%2FfISi%2BpNYjnmA7dtggy5Dcm4cYcBRoR5hgeKwVw5ZgtjDyfrwMP6MucLp0yD9vR%2FN8jFbGkH5TQRChcAnHl&X-Amz-Signature=329e4d2b59485ca3b714375fc3d31d45e9abb09970ccf5bade1fb385c91aabb4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4JDZWJ4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDOQn%2FBbHZ%2BoWlkJa0jPhzXrtqt721LpY7v2FN19PzmTwIgf0AlcY4t84LXG06J4UJ7qFYofQMbbCgai0FjSzAxL0cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEVE%2BobWNnv%2FlXDlBCrcAw4hu4gDo8Ygv4qvtYamHXUGm1vsF2wRBiv9qCypDiZoTjiROeUCxcs%2Fdb0LwtcdJIpwFE%2Bgy0vQcHU2D4dWxrSRz5eTkA0051x3WgI%2BTb04UN6%2FFGHFX42wuw95cFKXB4VY%2F1CJpQ%2FD%2BgmrIFA%2F9dSy50pMsKyys4nNfuR5eMvvXUHoQdGIv%2FzzuEUAekzMIjVlACWCbC7aA0tx7MPHj6jnWgUxL%2BYsqKIqu0CF75ZXX5QslxlBk2DvQGSj534wk8rry49XMSxv76%2Fi41EzY92%2FMkwmfox0UN%2F6zdOnNAai3XNH476G2DMiUokSkQReqorDvS4df2lNZ8qLSa2qPPxrTE9s2SnYdXJU8DkPaN8RzoijkiXp83LMRlfKm%2FFhuuGp6W5DItk9gprtB75RSfqt7GDqBFnFebUOkSND43ZD7s87WHGSb5%2FsrFNwijPRS%2F4R0w0J%2FV3SBHi3OK0kEWxKUwjkOGqgSnWL5p7vo0hem8mkx0efkfK7Or%2FGxX48TxqKYfio3ge5%2F%2Bjdu98VT0A7%2B9tM%2BheCfMaOS1g4Sdv1TMsS07709MgF0a00vUbdNj6ImnNJcwZ8g3BkEwdzwHaPx4j9AbWPZd3Ta%2FSZKh4AV7Mp3I603kDMDD6OMMnd5LwGOqUBy%2Fcv2PYhaDk3Reu%2FRjoDmAOGHSqk5HQJG0Oar9CmuiA0%2BGmr7%2BQjBWU5Mk9WMETH5Cs9W9sl3vZmAoEWTlpiu1Zxzyze76Jz1ShnXFAK4ag2xngta7vUT1Ik4OWMDnCBt3wuZ4zZlCFwRLUHbFMmlUkLtU2BOvxsFqszS1POfFaNjpjAJ50QUDP3F9doh7YLfHrAN47fImkZRibLWA7%2F7%2Bvpdr7o&X-Amz-Signature=1355e2e57b322b57676a1b37d8d4bff6c1901baa60c1ac8890c312fbc630c17a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4JDZWJ4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDOQn%2FBbHZ%2BoWlkJa0jPhzXrtqt721LpY7v2FN19PzmTwIgf0AlcY4t84LXG06J4UJ7qFYofQMbbCgai0FjSzAxL0cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEVE%2BobWNnv%2FlXDlBCrcAw4hu4gDo8Ygv4qvtYamHXUGm1vsF2wRBiv9qCypDiZoTjiROeUCxcs%2Fdb0LwtcdJIpwFE%2Bgy0vQcHU2D4dWxrSRz5eTkA0051x3WgI%2BTb04UN6%2FFGHFX42wuw95cFKXB4VY%2F1CJpQ%2FD%2BgmrIFA%2F9dSy50pMsKyys4nNfuR5eMvvXUHoQdGIv%2FzzuEUAekzMIjVlACWCbC7aA0tx7MPHj6jnWgUxL%2BYsqKIqu0CF75ZXX5QslxlBk2DvQGSj534wk8rry49XMSxv76%2Fi41EzY92%2FMkwmfox0UN%2F6zdOnNAai3XNH476G2DMiUokSkQReqorDvS4df2lNZ8qLSa2qPPxrTE9s2SnYdXJU8DkPaN8RzoijkiXp83LMRlfKm%2FFhuuGp6W5DItk9gprtB75RSfqt7GDqBFnFebUOkSND43ZD7s87WHGSb5%2FsrFNwijPRS%2F4R0w0J%2FV3SBHi3OK0kEWxKUwjkOGqgSnWL5p7vo0hem8mkx0efkfK7Or%2FGxX48TxqKYfio3ge5%2F%2Bjdu98VT0A7%2B9tM%2BheCfMaOS1g4Sdv1TMsS07709MgF0a00vUbdNj6ImnNJcwZ8g3BkEwdzwHaPx4j9AbWPZd3Ta%2FSZKh4AV7Mp3I603kDMDD6OMMnd5LwGOqUBy%2Fcv2PYhaDk3Reu%2FRjoDmAOGHSqk5HQJG0Oar9CmuiA0%2BGmr7%2BQjBWU5Mk9WMETH5Cs9W9sl3vZmAoEWTlpiu1Zxzyze76Jz1ShnXFAK4ag2xngta7vUT1Ik4OWMDnCBt3wuZ4zZlCFwRLUHbFMmlUkLtU2BOvxsFqszS1POfFaNjpjAJ50QUDP3F9doh7YLfHrAN47fImkZRibLWA7%2F7%2Bvpdr7o&X-Amz-Signature=d819f651eed29d9616b68f221a17915a7016d57d3c113d64388cf3e3ac7bce7a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4JDZWJ4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDOQn%2FBbHZ%2BoWlkJa0jPhzXrtqt721LpY7v2FN19PzmTwIgf0AlcY4t84LXG06J4UJ7qFYofQMbbCgai0FjSzAxL0cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEVE%2BobWNnv%2FlXDlBCrcAw4hu4gDo8Ygv4qvtYamHXUGm1vsF2wRBiv9qCypDiZoTjiROeUCxcs%2Fdb0LwtcdJIpwFE%2Bgy0vQcHU2D4dWxrSRz5eTkA0051x3WgI%2BTb04UN6%2FFGHFX42wuw95cFKXB4VY%2F1CJpQ%2FD%2BgmrIFA%2F9dSy50pMsKyys4nNfuR5eMvvXUHoQdGIv%2FzzuEUAekzMIjVlACWCbC7aA0tx7MPHj6jnWgUxL%2BYsqKIqu0CF75ZXX5QslxlBk2DvQGSj534wk8rry49XMSxv76%2Fi41EzY92%2FMkwmfox0UN%2F6zdOnNAai3XNH476G2DMiUokSkQReqorDvS4df2lNZ8qLSa2qPPxrTE9s2SnYdXJU8DkPaN8RzoijkiXp83LMRlfKm%2FFhuuGp6W5DItk9gprtB75RSfqt7GDqBFnFebUOkSND43ZD7s87WHGSb5%2FsrFNwijPRS%2F4R0w0J%2FV3SBHi3OK0kEWxKUwjkOGqgSnWL5p7vo0hem8mkx0efkfK7Or%2FGxX48TxqKYfio3ge5%2F%2Bjdu98VT0A7%2B9tM%2BheCfMaOS1g4Sdv1TMsS07709MgF0a00vUbdNj6ImnNJcwZ8g3BkEwdzwHaPx4j9AbWPZd3Ta%2FSZKh4AV7Mp3I603kDMDD6OMMnd5LwGOqUBy%2Fcv2PYhaDk3Reu%2FRjoDmAOGHSqk5HQJG0Oar9CmuiA0%2BGmr7%2BQjBWU5Mk9WMETH5Cs9W9sl3vZmAoEWTlpiu1Zxzyze76Jz1ShnXFAK4ag2xngta7vUT1Ik4OWMDnCBt3wuZ4zZlCFwRLUHbFMmlUkLtU2BOvxsFqszS1POfFaNjpjAJ50QUDP3F9doh7YLfHrAN47fImkZRibLWA7%2F7%2Bvpdr7o&X-Amz-Signature=644d2a5160d271e9913e430f9817b4f76005df6d0a9208c1f14cb255f155b6d8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4JDZWJ4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDOQn%2FBbHZ%2BoWlkJa0jPhzXrtqt721LpY7v2FN19PzmTwIgf0AlcY4t84LXG06J4UJ7qFYofQMbbCgai0FjSzAxL0cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEVE%2BobWNnv%2FlXDlBCrcAw4hu4gDo8Ygv4qvtYamHXUGm1vsF2wRBiv9qCypDiZoTjiROeUCxcs%2Fdb0LwtcdJIpwFE%2Bgy0vQcHU2D4dWxrSRz5eTkA0051x3WgI%2BTb04UN6%2FFGHFX42wuw95cFKXB4VY%2F1CJpQ%2FD%2BgmrIFA%2F9dSy50pMsKyys4nNfuR5eMvvXUHoQdGIv%2FzzuEUAekzMIjVlACWCbC7aA0tx7MPHj6jnWgUxL%2BYsqKIqu0CF75ZXX5QslxlBk2DvQGSj534wk8rry49XMSxv76%2Fi41EzY92%2FMkwmfox0UN%2F6zdOnNAai3XNH476G2DMiUokSkQReqorDvS4df2lNZ8qLSa2qPPxrTE9s2SnYdXJU8DkPaN8RzoijkiXp83LMRlfKm%2FFhuuGp6W5DItk9gprtB75RSfqt7GDqBFnFebUOkSND43ZD7s87WHGSb5%2FsrFNwijPRS%2F4R0w0J%2FV3SBHi3OK0kEWxKUwjkOGqgSnWL5p7vo0hem8mkx0efkfK7Or%2FGxX48TxqKYfio3ge5%2F%2Bjdu98VT0A7%2B9tM%2BheCfMaOS1g4Sdv1TMsS07709MgF0a00vUbdNj6ImnNJcwZ8g3BkEwdzwHaPx4j9AbWPZd3Ta%2FSZKh4AV7Mp3I603kDMDD6OMMnd5LwGOqUBy%2Fcv2PYhaDk3Reu%2FRjoDmAOGHSqk5HQJG0Oar9CmuiA0%2BGmr7%2BQjBWU5Mk9WMETH5Cs9W9sl3vZmAoEWTlpiu1Zxzyze76Jz1ShnXFAK4ag2xngta7vUT1Ik4OWMDnCBt3wuZ4zZlCFwRLUHbFMmlUkLtU2BOvxsFqszS1POfFaNjpjAJ50QUDP3F9doh7YLfHrAN47fImkZRibLWA7%2F7%2Bvpdr7o&X-Amz-Signature=f8009594b569d4f714a543092df1a90bcf74e04a49dc26ef9ddd760b484f4580&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4JDZWJ4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDOQn%2FBbHZ%2BoWlkJa0jPhzXrtqt721LpY7v2FN19PzmTwIgf0AlcY4t84LXG06J4UJ7qFYofQMbbCgai0FjSzAxL0cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEVE%2BobWNnv%2FlXDlBCrcAw4hu4gDo8Ygv4qvtYamHXUGm1vsF2wRBiv9qCypDiZoTjiROeUCxcs%2Fdb0LwtcdJIpwFE%2Bgy0vQcHU2D4dWxrSRz5eTkA0051x3WgI%2BTb04UN6%2FFGHFX42wuw95cFKXB4VY%2F1CJpQ%2FD%2BgmrIFA%2F9dSy50pMsKyys4nNfuR5eMvvXUHoQdGIv%2FzzuEUAekzMIjVlACWCbC7aA0tx7MPHj6jnWgUxL%2BYsqKIqu0CF75ZXX5QslxlBk2DvQGSj534wk8rry49XMSxv76%2Fi41EzY92%2FMkwmfox0UN%2F6zdOnNAai3XNH476G2DMiUokSkQReqorDvS4df2lNZ8qLSa2qPPxrTE9s2SnYdXJU8DkPaN8RzoijkiXp83LMRlfKm%2FFhuuGp6W5DItk9gprtB75RSfqt7GDqBFnFebUOkSND43ZD7s87WHGSb5%2FsrFNwijPRS%2F4R0w0J%2FV3SBHi3OK0kEWxKUwjkOGqgSnWL5p7vo0hem8mkx0efkfK7Or%2FGxX48TxqKYfio3ge5%2F%2Bjdu98VT0A7%2B9tM%2BheCfMaOS1g4Sdv1TMsS07709MgF0a00vUbdNj6ImnNJcwZ8g3BkEwdzwHaPx4j9AbWPZd3Ta%2FSZKh4AV7Mp3I603kDMDD6OMMnd5LwGOqUBy%2Fcv2PYhaDk3Reu%2FRjoDmAOGHSqk5HQJG0Oar9CmuiA0%2BGmr7%2BQjBWU5Mk9WMETH5Cs9W9sl3vZmAoEWTlpiu1Zxzyze76Jz1ShnXFAK4ag2xngta7vUT1Ik4OWMDnCBt3wuZ4zZlCFwRLUHbFMmlUkLtU2BOvxsFqszS1POfFaNjpjAJ50QUDP3F9doh7YLfHrAN47fImkZRibLWA7%2F7%2Bvpdr7o&X-Amz-Signature=0d1c99abea63780f9588ce7755a6a9de2772a72f2a05e88b9ab29ca6ea9d96f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


