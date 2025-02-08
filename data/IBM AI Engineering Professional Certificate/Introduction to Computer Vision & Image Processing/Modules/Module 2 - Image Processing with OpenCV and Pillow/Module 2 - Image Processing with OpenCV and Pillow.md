

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YKQUHUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICbNUXEC7iQGzQFJ%2BtHUf95HuDSzAx62J0xfj5UleEE9AiBzY54vBbIt1nLbDjHtFkiO8Ely3RE02gDE9%2BYd%2BJIjgyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHAOSSmUCQs5FsUoKtwDvZFj9lMH9KT5OmnVkNY2UL4u%2FIDoBUhAIb0c3zOz0Zy3RA8oSl2svcfRbmhX%2BXN6E0%2B9O%2FUxgooL0oKrp4uFpHFvLK9O%2BU5IlldqpAsmOIQTWiM2uEiVIsLZGevBC4dSlxFid6U3lzhjGSqUhg%2FfVMcrfEpM1H%2BU47lbq%2FPB0VtZDLSlIuQgrUFmdOoY2lTG2gbO8Fx1ErdxouzS9x8kGvFxwmUF6hWimklu0dztY6IZk5Br%2BLSKDx7EykYRGQFDmEyzRTsvtln53IwIi9iTIE%2FS09ewyedsSTYdQGPLJwIyLH3dOPnpZxO%2Bez9IuQgSy01QJf4%2BIAAXtuBPjiVMlk60%2F5%2FHTsCYsLuGCi2QKEQsmqxa016JPq8kmYFwQZH3bHjCqSTzdYQhsQdFDMbHCl8pd990NZmBdXccQbhodFrPHl9LJvJsFYjNDiPhV1zHXD%2Fw5K6axXwIFawbe75JKR7w5boI%2BpHE0IFNp93B7x14iYD17iRuQoldDbHKB3OtHaHqE3VpJ2dUAfTdc90F1Bo9Uv8rTkXA%2FpuUKio6UnDYRJmsB9HYLPSXF1bjOoyUvORDEkrutdZoxVAGlWP%2Bo6IYq9xI8XBAUZlT9yERgVEUygqvUNAaIGBsjXkw%2Be6bvQY6pgEOiOkCZZIvHSy9wvhBRgDjH3kVCwmLgWDr0bHVS47mxIH3dzSlLRSiWXg%2F%2FyoUO%2Fu4znY5c5XinCRDUz7YPmoQq2cgHjxbEE7%2FYRiAdi4XTPU7xpfzER0XaHytdxBVBtXG58TfLA5TgAARh9rQbqqPQIffyAoyQYacba0hIEIgKXfH1fH%2Bprc3jxyslL7hSsI72g9I4mp%2FF1vmIud1jfBLQ1wM5jxX&X-Amz-Signature=e4963c7ce0f3aacfe4177e2ee8455bfb397bcfe07d6015cfa881e933bfe436ea&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XJW5JN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDh74%2FarvVaPABwV7UvM7vg7wlnp2XsXbpZQY%2B1ExV9lAIhAPdWyvWbXa0CEJ2xA%2Fv%2F6SiYAUG922VyZNViwikkYouhKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjRJ70xSqWGDLlmboq3AOA0tGAQ%2BBLgpw5W3p7rn3ewyrraCPpAl8huHr9LcTZvp%2Bh8lv9KQQTDOvZwceeb8tXCrD3gQsu0%2BQBVcAwDR85rpYHRrr4E1hd2VhCyzHjvsvsKaJI2tqAG1rD53nTsyL83k%2BkaRk6kKhAcVK49elsIhUUnF2AWmrooTVDcWrjDhBDQzSwXUSsJngcc5NapoxvREsrPB7ddEkQwochqJ%2Bg5fc5jeyxe%2BQrQR4nw6ya9puZPPVDzbkdBjUk11p%2FhnmWhpWz7Erp1hIpRT0i8HVXPltNJ6jol9zyvD5NvbhEgoKP9nwKATEXwQ4lm9ksGUl8QFBMugahm1rYDImeHjKqHFZm1Z3qmxRbMYzOQedn%2BzsXD3mKHiwIzWjRYmF%2BfxIzz57%2Fra9HOaxVfq%2BqWlpoKzZyt%2FqHXYgKyKwjGJoihkMIJD9qJgWA4bMgCwJ4pgotgfX9WmwgoxcOcp8fPeutgZ2o9xuB4H%2Bw459SIVBCSadLVTsrDUN4nv4H2fsWmM5YY8H7oQsA8W1X9M%2Bfu%2BtPYoblutZd%2F%2BRj851tWusXFHTgp94vtFaM4FERVggF5EKwmuE2zmT9Hk%2B4xcZzR0xU1vXCzedEaPYHoGuSOgWpUMsDbxMYleMSck35ODCX75u9BjqkAdV%2B9HRySQ%2F0QosD3VGAn3LxMJban5KTPGvtHQPEFvy4doM8DrHVkzNZ61yMnKqQwDa1Y4%2FObVmpOEJCueGndrXK4u%2FPGsDF4Z2F7l8Zk4d2RCjAin5zMzGSetIT37I0jrZ4Y8zdCpxvjGIySmUeTFJdiaid8ScTMRycN%2FQUJhPh%2F8SweokClOlpns8%2Fi5NE1hQMM6dRAXHFdU2SocdRQv%2FfbXT6&X-Amz-Signature=1586c659b5337b9bfb9adf3a114567b2e1a8870aa2eee2e0192d8be7cfc98c3b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XJW5JN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDh74%2FarvVaPABwV7UvM7vg7wlnp2XsXbpZQY%2B1ExV9lAIhAPdWyvWbXa0CEJ2xA%2Fv%2F6SiYAUG922VyZNViwikkYouhKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjRJ70xSqWGDLlmboq3AOA0tGAQ%2BBLgpw5W3p7rn3ewyrraCPpAl8huHr9LcTZvp%2Bh8lv9KQQTDOvZwceeb8tXCrD3gQsu0%2BQBVcAwDR85rpYHRrr4E1hd2VhCyzHjvsvsKaJI2tqAG1rD53nTsyL83k%2BkaRk6kKhAcVK49elsIhUUnF2AWmrooTVDcWrjDhBDQzSwXUSsJngcc5NapoxvREsrPB7ddEkQwochqJ%2Bg5fc5jeyxe%2BQrQR4nw6ya9puZPPVDzbkdBjUk11p%2FhnmWhpWz7Erp1hIpRT0i8HVXPltNJ6jol9zyvD5NvbhEgoKP9nwKATEXwQ4lm9ksGUl8QFBMugahm1rYDImeHjKqHFZm1Z3qmxRbMYzOQedn%2BzsXD3mKHiwIzWjRYmF%2BfxIzz57%2Fra9HOaxVfq%2BqWlpoKzZyt%2FqHXYgKyKwjGJoihkMIJD9qJgWA4bMgCwJ4pgotgfX9WmwgoxcOcp8fPeutgZ2o9xuB4H%2Bw459SIVBCSadLVTsrDUN4nv4H2fsWmM5YY8H7oQsA8W1X9M%2Bfu%2BtPYoblutZd%2F%2BRj851tWusXFHTgp94vtFaM4FERVggF5EKwmuE2zmT9Hk%2B4xcZzR0xU1vXCzedEaPYHoGuSOgWpUMsDbxMYleMSck35ODCX75u9BjqkAdV%2B9HRySQ%2F0QosD3VGAn3LxMJban5KTPGvtHQPEFvy4doM8DrHVkzNZ61yMnKqQwDa1Y4%2FObVmpOEJCueGndrXK4u%2FPGsDF4Z2F7l8Zk4d2RCjAin5zMzGSetIT37I0jrZ4Y8zdCpxvjGIySmUeTFJdiaid8ScTMRycN%2FQUJhPh%2F8SweokClOlpns8%2Fi5NE1hQMM6dRAXHFdU2SocdRQv%2FfbXT6&X-Amz-Signature=076c7f49acb6a6ea026f61373dda56198f1db33f0f20426a6020e9271a9afd18&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XJW5JN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDh74%2FarvVaPABwV7UvM7vg7wlnp2XsXbpZQY%2B1ExV9lAIhAPdWyvWbXa0CEJ2xA%2Fv%2F6SiYAUG922VyZNViwikkYouhKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjRJ70xSqWGDLlmboq3AOA0tGAQ%2BBLgpw5W3p7rn3ewyrraCPpAl8huHr9LcTZvp%2Bh8lv9KQQTDOvZwceeb8tXCrD3gQsu0%2BQBVcAwDR85rpYHRrr4E1hd2VhCyzHjvsvsKaJI2tqAG1rD53nTsyL83k%2BkaRk6kKhAcVK49elsIhUUnF2AWmrooTVDcWrjDhBDQzSwXUSsJngcc5NapoxvREsrPB7ddEkQwochqJ%2Bg5fc5jeyxe%2BQrQR4nw6ya9puZPPVDzbkdBjUk11p%2FhnmWhpWz7Erp1hIpRT0i8HVXPltNJ6jol9zyvD5NvbhEgoKP9nwKATEXwQ4lm9ksGUl8QFBMugahm1rYDImeHjKqHFZm1Z3qmxRbMYzOQedn%2BzsXD3mKHiwIzWjRYmF%2BfxIzz57%2Fra9HOaxVfq%2BqWlpoKzZyt%2FqHXYgKyKwjGJoihkMIJD9qJgWA4bMgCwJ4pgotgfX9WmwgoxcOcp8fPeutgZ2o9xuB4H%2Bw459SIVBCSadLVTsrDUN4nv4H2fsWmM5YY8H7oQsA8W1X9M%2Bfu%2BtPYoblutZd%2F%2BRj851tWusXFHTgp94vtFaM4FERVggF5EKwmuE2zmT9Hk%2B4xcZzR0xU1vXCzedEaPYHoGuSOgWpUMsDbxMYleMSck35ODCX75u9BjqkAdV%2B9HRySQ%2F0QosD3VGAn3LxMJban5KTPGvtHQPEFvy4doM8DrHVkzNZ61yMnKqQwDa1Y4%2FObVmpOEJCueGndrXK4u%2FPGsDF4Z2F7l8Zk4d2RCjAin5zMzGSetIT37I0jrZ4Y8zdCpxvjGIySmUeTFJdiaid8ScTMRycN%2FQUJhPh%2F8SweokClOlpns8%2Fi5NE1hQMM6dRAXHFdU2SocdRQv%2FfbXT6&X-Amz-Signature=bea3db5c6b03d041245d2d7288485eee8dd4fea43047fc57afe981a1df7dcfde&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XJW5JN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDh74%2FarvVaPABwV7UvM7vg7wlnp2XsXbpZQY%2B1ExV9lAIhAPdWyvWbXa0CEJ2xA%2Fv%2F6SiYAUG922VyZNViwikkYouhKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjRJ70xSqWGDLlmboq3AOA0tGAQ%2BBLgpw5W3p7rn3ewyrraCPpAl8huHr9LcTZvp%2Bh8lv9KQQTDOvZwceeb8tXCrD3gQsu0%2BQBVcAwDR85rpYHRrr4E1hd2VhCyzHjvsvsKaJI2tqAG1rD53nTsyL83k%2BkaRk6kKhAcVK49elsIhUUnF2AWmrooTVDcWrjDhBDQzSwXUSsJngcc5NapoxvREsrPB7ddEkQwochqJ%2Bg5fc5jeyxe%2BQrQR4nw6ya9puZPPVDzbkdBjUk11p%2FhnmWhpWz7Erp1hIpRT0i8HVXPltNJ6jol9zyvD5NvbhEgoKP9nwKATEXwQ4lm9ksGUl8QFBMugahm1rYDImeHjKqHFZm1Z3qmxRbMYzOQedn%2BzsXD3mKHiwIzWjRYmF%2BfxIzz57%2Fra9HOaxVfq%2BqWlpoKzZyt%2FqHXYgKyKwjGJoihkMIJD9qJgWA4bMgCwJ4pgotgfX9WmwgoxcOcp8fPeutgZ2o9xuB4H%2Bw459SIVBCSadLVTsrDUN4nv4H2fsWmM5YY8H7oQsA8W1X9M%2Bfu%2BtPYoblutZd%2F%2BRj851tWusXFHTgp94vtFaM4FERVggF5EKwmuE2zmT9Hk%2B4xcZzR0xU1vXCzedEaPYHoGuSOgWpUMsDbxMYleMSck35ODCX75u9BjqkAdV%2B9HRySQ%2F0QosD3VGAn3LxMJban5KTPGvtHQPEFvy4doM8DrHVkzNZ61yMnKqQwDa1Y4%2FObVmpOEJCueGndrXK4u%2FPGsDF4Z2F7l8Zk4d2RCjAin5zMzGSetIT37I0jrZ4Y8zdCpxvjGIySmUeTFJdiaid8ScTMRycN%2FQUJhPh%2F8SweokClOlpns8%2Fi5NE1hQMM6dRAXHFdU2SocdRQv%2FfbXT6&X-Amz-Signature=dce6d013c0be4d964e8725235510685678ff171ebf2b72161b3925780972a3fa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XJW5JN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDh74%2FarvVaPABwV7UvM7vg7wlnp2XsXbpZQY%2B1ExV9lAIhAPdWyvWbXa0CEJ2xA%2Fv%2F6SiYAUG922VyZNViwikkYouhKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjRJ70xSqWGDLlmboq3AOA0tGAQ%2BBLgpw5W3p7rn3ewyrraCPpAl8huHr9LcTZvp%2Bh8lv9KQQTDOvZwceeb8tXCrD3gQsu0%2BQBVcAwDR85rpYHRrr4E1hd2VhCyzHjvsvsKaJI2tqAG1rD53nTsyL83k%2BkaRk6kKhAcVK49elsIhUUnF2AWmrooTVDcWrjDhBDQzSwXUSsJngcc5NapoxvREsrPB7ddEkQwochqJ%2Bg5fc5jeyxe%2BQrQR4nw6ya9puZPPVDzbkdBjUk11p%2FhnmWhpWz7Erp1hIpRT0i8HVXPltNJ6jol9zyvD5NvbhEgoKP9nwKATEXwQ4lm9ksGUl8QFBMugahm1rYDImeHjKqHFZm1Z3qmxRbMYzOQedn%2BzsXD3mKHiwIzWjRYmF%2BfxIzz57%2Fra9HOaxVfq%2BqWlpoKzZyt%2FqHXYgKyKwjGJoihkMIJD9qJgWA4bMgCwJ4pgotgfX9WmwgoxcOcp8fPeutgZ2o9xuB4H%2Bw459SIVBCSadLVTsrDUN4nv4H2fsWmM5YY8H7oQsA8W1X9M%2Bfu%2BtPYoblutZd%2F%2BRj851tWusXFHTgp94vtFaM4FERVggF5EKwmuE2zmT9Hk%2B4xcZzR0xU1vXCzedEaPYHoGuSOgWpUMsDbxMYleMSck35ODCX75u9BjqkAdV%2B9HRySQ%2F0QosD3VGAn3LxMJban5KTPGvtHQPEFvy4doM8DrHVkzNZ61yMnKqQwDa1Y4%2FObVmpOEJCueGndrXK4u%2FPGsDF4Z2F7l8Zk4d2RCjAin5zMzGSetIT37I0jrZ4Y8zdCpxvjGIySmUeTFJdiaid8ScTMRycN%2FQUJhPh%2F8SweokClOlpns8%2Fi5NE1hQMM6dRAXHFdU2SocdRQv%2FfbXT6&X-Amz-Signature=ea40a3fdcd2927a80b834f8df9da0003b59bcf60b72e53e0934eb4d7a623443e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YKQUHUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICbNUXEC7iQGzQFJ%2BtHUf95HuDSzAx62J0xfj5UleEE9AiBzY54vBbIt1nLbDjHtFkiO8Ely3RE02gDE9%2BYd%2BJIjgyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHAOSSmUCQs5FsUoKtwDvZFj9lMH9KT5OmnVkNY2UL4u%2FIDoBUhAIb0c3zOz0Zy3RA8oSl2svcfRbmhX%2BXN6E0%2B9O%2FUxgooL0oKrp4uFpHFvLK9O%2BU5IlldqpAsmOIQTWiM2uEiVIsLZGevBC4dSlxFid6U3lzhjGSqUhg%2FfVMcrfEpM1H%2BU47lbq%2FPB0VtZDLSlIuQgrUFmdOoY2lTG2gbO8Fx1ErdxouzS9x8kGvFxwmUF6hWimklu0dztY6IZk5Br%2BLSKDx7EykYRGQFDmEyzRTsvtln53IwIi9iTIE%2FS09ewyedsSTYdQGPLJwIyLH3dOPnpZxO%2Bez9IuQgSy01QJf4%2BIAAXtuBPjiVMlk60%2F5%2FHTsCYsLuGCi2QKEQsmqxa016JPq8kmYFwQZH3bHjCqSTzdYQhsQdFDMbHCl8pd990NZmBdXccQbhodFrPHl9LJvJsFYjNDiPhV1zHXD%2Fw5K6axXwIFawbe75JKR7w5boI%2BpHE0IFNp93B7x14iYD17iRuQoldDbHKB3OtHaHqE3VpJ2dUAfTdc90F1Bo9Uv8rTkXA%2FpuUKio6UnDYRJmsB9HYLPSXF1bjOoyUvORDEkrutdZoxVAGlWP%2Bo6IYq9xI8XBAUZlT9yERgVEUygqvUNAaIGBsjXkw%2Be6bvQY6pgEOiOkCZZIvHSy9wvhBRgDjH3kVCwmLgWDr0bHVS47mxIH3dzSlLRSiWXg%2F%2FyoUO%2Fu4znY5c5XinCRDUz7YPmoQq2cgHjxbEE7%2FYRiAdi4XTPU7xpfzER0XaHytdxBVBtXG58TfLA5TgAARh9rQbqqPQIffyAoyQYacba0hIEIgKXfH1fH%2Bprc3jxyslL7hSsI72g9I4mp%2FF1vmIud1jfBLQ1wM5jxX&X-Amz-Signature=2f218975cf37d8802d2d2a271e3063645ba97d9cea5608b082c3ebe79fec12a8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YKQUHUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICbNUXEC7iQGzQFJ%2BtHUf95HuDSzAx62J0xfj5UleEE9AiBzY54vBbIt1nLbDjHtFkiO8Ely3RE02gDE9%2BYd%2BJIjgyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHAOSSmUCQs5FsUoKtwDvZFj9lMH9KT5OmnVkNY2UL4u%2FIDoBUhAIb0c3zOz0Zy3RA8oSl2svcfRbmhX%2BXN6E0%2B9O%2FUxgooL0oKrp4uFpHFvLK9O%2BU5IlldqpAsmOIQTWiM2uEiVIsLZGevBC4dSlxFid6U3lzhjGSqUhg%2FfVMcrfEpM1H%2BU47lbq%2FPB0VtZDLSlIuQgrUFmdOoY2lTG2gbO8Fx1ErdxouzS9x8kGvFxwmUF6hWimklu0dztY6IZk5Br%2BLSKDx7EykYRGQFDmEyzRTsvtln53IwIi9iTIE%2FS09ewyedsSTYdQGPLJwIyLH3dOPnpZxO%2Bez9IuQgSy01QJf4%2BIAAXtuBPjiVMlk60%2F5%2FHTsCYsLuGCi2QKEQsmqxa016JPq8kmYFwQZH3bHjCqSTzdYQhsQdFDMbHCl8pd990NZmBdXccQbhodFrPHl9LJvJsFYjNDiPhV1zHXD%2Fw5K6axXwIFawbe75JKR7w5boI%2BpHE0IFNp93B7x14iYD17iRuQoldDbHKB3OtHaHqE3VpJ2dUAfTdc90F1Bo9Uv8rTkXA%2FpuUKio6UnDYRJmsB9HYLPSXF1bjOoyUvORDEkrutdZoxVAGlWP%2Bo6IYq9xI8XBAUZlT9yERgVEUygqvUNAaIGBsjXkw%2Be6bvQY6pgEOiOkCZZIvHSy9wvhBRgDjH3kVCwmLgWDr0bHVS47mxIH3dzSlLRSiWXg%2F%2FyoUO%2Fu4znY5c5XinCRDUz7YPmoQq2cgHjxbEE7%2FYRiAdi4XTPU7xpfzER0XaHytdxBVBtXG58TfLA5TgAARh9rQbqqPQIffyAoyQYacba0hIEIgKXfH1fH%2Bprc3jxyslL7hSsI72g9I4mp%2FF1vmIud1jfBLQ1wM5jxX&X-Amz-Signature=1779086d81bf0963150f4113df7f4fed799a4ed808a25ddde91709017fa851be&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YKQUHUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICbNUXEC7iQGzQFJ%2BtHUf95HuDSzAx62J0xfj5UleEE9AiBzY54vBbIt1nLbDjHtFkiO8Ely3RE02gDE9%2BYd%2BJIjgyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHAOSSmUCQs5FsUoKtwDvZFj9lMH9KT5OmnVkNY2UL4u%2FIDoBUhAIb0c3zOz0Zy3RA8oSl2svcfRbmhX%2BXN6E0%2B9O%2FUxgooL0oKrp4uFpHFvLK9O%2BU5IlldqpAsmOIQTWiM2uEiVIsLZGevBC4dSlxFid6U3lzhjGSqUhg%2FfVMcrfEpM1H%2BU47lbq%2FPB0VtZDLSlIuQgrUFmdOoY2lTG2gbO8Fx1ErdxouzS9x8kGvFxwmUF6hWimklu0dztY6IZk5Br%2BLSKDx7EykYRGQFDmEyzRTsvtln53IwIi9iTIE%2FS09ewyedsSTYdQGPLJwIyLH3dOPnpZxO%2Bez9IuQgSy01QJf4%2BIAAXtuBPjiVMlk60%2F5%2FHTsCYsLuGCi2QKEQsmqxa016JPq8kmYFwQZH3bHjCqSTzdYQhsQdFDMbHCl8pd990NZmBdXccQbhodFrPHl9LJvJsFYjNDiPhV1zHXD%2Fw5K6axXwIFawbe75JKR7w5boI%2BpHE0IFNp93B7x14iYD17iRuQoldDbHKB3OtHaHqE3VpJ2dUAfTdc90F1Bo9Uv8rTkXA%2FpuUKio6UnDYRJmsB9HYLPSXF1bjOoyUvORDEkrutdZoxVAGlWP%2Bo6IYq9xI8XBAUZlT9yERgVEUygqvUNAaIGBsjXkw%2Be6bvQY6pgEOiOkCZZIvHSy9wvhBRgDjH3kVCwmLgWDr0bHVS47mxIH3dzSlLRSiWXg%2F%2FyoUO%2Fu4znY5c5XinCRDUz7YPmoQq2cgHjxbEE7%2FYRiAdi4XTPU7xpfzER0XaHytdxBVBtXG58TfLA5TgAARh9rQbqqPQIffyAoyQYacba0hIEIgKXfH1fH%2Bprc3jxyslL7hSsI72g9I4mp%2FF1vmIud1jfBLQ1wM5jxX&X-Amz-Signature=f86d9bf2039d73076c21cc422090b58d08e3a28795321d91c826b9c1765203d7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YKQUHUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICbNUXEC7iQGzQFJ%2BtHUf95HuDSzAx62J0xfj5UleEE9AiBzY54vBbIt1nLbDjHtFkiO8Ely3RE02gDE9%2BYd%2BJIjgyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHAOSSmUCQs5FsUoKtwDvZFj9lMH9KT5OmnVkNY2UL4u%2FIDoBUhAIb0c3zOz0Zy3RA8oSl2svcfRbmhX%2BXN6E0%2B9O%2FUxgooL0oKrp4uFpHFvLK9O%2BU5IlldqpAsmOIQTWiM2uEiVIsLZGevBC4dSlxFid6U3lzhjGSqUhg%2FfVMcrfEpM1H%2BU47lbq%2FPB0VtZDLSlIuQgrUFmdOoY2lTG2gbO8Fx1ErdxouzS9x8kGvFxwmUF6hWimklu0dztY6IZk5Br%2BLSKDx7EykYRGQFDmEyzRTsvtln53IwIi9iTIE%2FS09ewyedsSTYdQGPLJwIyLH3dOPnpZxO%2Bez9IuQgSy01QJf4%2BIAAXtuBPjiVMlk60%2F5%2FHTsCYsLuGCi2QKEQsmqxa016JPq8kmYFwQZH3bHjCqSTzdYQhsQdFDMbHCl8pd990NZmBdXccQbhodFrPHl9LJvJsFYjNDiPhV1zHXD%2Fw5K6axXwIFawbe75JKR7w5boI%2BpHE0IFNp93B7x14iYD17iRuQoldDbHKB3OtHaHqE3VpJ2dUAfTdc90F1Bo9Uv8rTkXA%2FpuUKio6UnDYRJmsB9HYLPSXF1bjOoyUvORDEkrutdZoxVAGlWP%2Bo6IYq9xI8XBAUZlT9yERgVEUygqvUNAaIGBsjXkw%2Be6bvQY6pgEOiOkCZZIvHSy9wvhBRgDjH3kVCwmLgWDr0bHVS47mxIH3dzSlLRSiWXg%2F%2FyoUO%2Fu4znY5c5XinCRDUz7YPmoQq2cgHjxbEE7%2FYRiAdi4XTPU7xpfzER0XaHytdxBVBtXG58TfLA5TgAARh9rQbqqPQIffyAoyQYacba0hIEIgKXfH1fH%2Bprc3jxyslL7hSsI72g9I4mp%2FF1vmIud1jfBLQ1wM5jxX&X-Amz-Signature=648415d83ff878517fa39752c4d9fbcd0b2daae16d38cec5d77f7d8ccc28c2ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YKQUHUB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICbNUXEC7iQGzQFJ%2BtHUf95HuDSzAx62J0xfj5UleEE9AiBzY54vBbIt1nLbDjHtFkiO8Ely3RE02gDE9%2BYd%2BJIjgyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHAOSSmUCQs5FsUoKtwDvZFj9lMH9KT5OmnVkNY2UL4u%2FIDoBUhAIb0c3zOz0Zy3RA8oSl2svcfRbmhX%2BXN6E0%2B9O%2FUxgooL0oKrp4uFpHFvLK9O%2BU5IlldqpAsmOIQTWiM2uEiVIsLZGevBC4dSlxFid6U3lzhjGSqUhg%2FfVMcrfEpM1H%2BU47lbq%2FPB0VtZDLSlIuQgrUFmdOoY2lTG2gbO8Fx1ErdxouzS9x8kGvFxwmUF6hWimklu0dztY6IZk5Br%2BLSKDx7EykYRGQFDmEyzRTsvtln53IwIi9iTIE%2FS09ewyedsSTYdQGPLJwIyLH3dOPnpZxO%2Bez9IuQgSy01QJf4%2BIAAXtuBPjiVMlk60%2F5%2FHTsCYsLuGCi2QKEQsmqxa016JPq8kmYFwQZH3bHjCqSTzdYQhsQdFDMbHCl8pd990NZmBdXccQbhodFrPHl9LJvJsFYjNDiPhV1zHXD%2Fw5K6axXwIFawbe75JKR7w5boI%2BpHE0IFNp93B7x14iYD17iRuQoldDbHKB3OtHaHqE3VpJ2dUAfTdc90F1Bo9Uv8rTkXA%2FpuUKio6UnDYRJmsB9HYLPSXF1bjOoyUvORDEkrutdZoxVAGlWP%2Bo6IYq9xI8XBAUZlT9yERgVEUygqvUNAaIGBsjXkw%2Be6bvQY6pgEOiOkCZZIvHSy9wvhBRgDjH3kVCwmLgWDr0bHVS47mxIH3dzSlLRSiWXg%2F%2FyoUO%2Fu4znY5c5XinCRDUz7YPmoQq2cgHjxbEE7%2FYRiAdi4XTPU7xpfzER0XaHytdxBVBtXG58TfLA5TgAARh9rQbqqPQIffyAoyQYacba0hIEIgKXfH1fH%2Bprc3jxyslL7hSsI72g9I4mp%2FF1vmIud1jfBLQ1wM5jxX&X-Amz-Signature=2fab1d61229a951ff718b94f346a7e2662f90984801e05c128813f5ae40bbd0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


