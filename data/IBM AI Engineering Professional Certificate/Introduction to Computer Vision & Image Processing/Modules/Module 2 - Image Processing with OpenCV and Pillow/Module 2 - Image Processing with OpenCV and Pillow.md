

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAFIAJMO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQChHoAsViTkTGOY2eKxCfF1KHVvb6gwQ52%2Bb5GYg%2Fxw9QIhAKFQngjJjr0fpNjmfEYQ%2BKHfYt1rm0he%2BmVvHiBo1N%2BJKv8DCFYQABoMNjM3NDIzMTgzODA1IgxtTgWS9%2BDmc7X6dv0q3ANoyvzOzDHe2wtvbLgIfyLmxXlfvtBvRspq%2Fzv%2FbmfLdGgId3OV7zMRl4vieOXLNmzfRI6j6mJlIXlbXdMoju%2FHqpC%2BsghhWxD8iPrBLb%2FMFiUCxXsypJqaASxJmlhp%2B4TEp1j36EEjA3%2BMUcmIGmk8S8%2BL8PM0KMQ3GpihPk%2BdpppKQU58m1ZKygSpbUf8WJ4zCYyvKF8Rt6rQz3bZNG5tR23hXCUCxCeKo1bck0OMuzsAKfF02HY1zDAMHop6uvp45idkY7KDMPch9b8NFNfBEea6mVtfn0NptYJqgOfpwlI0d%2BnXsWvu%2BjVcUT9vpSz9IcPg0ySzuRyE8qf4DZgPWzEb2KYR0BbumpG%2FWgAyPtsUM%2Bq0Al40%2BHKxTu201zdldXbdQaWn30NZ%2BpqPbTzdZhKN7yspZ4Yz0iuvSA8Frs5I%2BlGQfBMJ5KNqxVSXr%2BSMYIiBJuhWLpRp8fLEiixlCgEhqWiKM%2FsuEXc5cZe1U5rJv%2FOoGCjKb93T570PCUrKcIJWnFa67OWPwHrJt8YBSGTGRsouAGjmJwkiNke7OgkSbu0QTFMObyzSvcvG5CS2vK76VjkG5OWF1MgGpSAfdWHB8Zv72Ap0Vi93fKahtNHCYIXdPEOgCyKoeDDk%2B5C9BjqkAe5bevGhvJHqjjjMXIPMSLZmZMIkwfHayhNlrCWsXdzcCD%2BOd9OW28mlJKZ3dWcLSMKrH87y2aZqyg5E5lo0hDp3Y9ghiflZpYnWG2XKRZsQ2gN6BqYBp2VQ8NOfGGD3L4RTV8V7txEeOXtLi5weISD4hXYIYRI%2Fo8Troc3y3tBSR1NoOtQKchGIHsSlWXutZX3dcEQLtn4HGVtGTp7f2zGvs3Pv&X-Amz-Signature=63894b9218f7967e2cbb0a0b8dea28409399d5f0bc9fe3c82f5a952c508e16dc&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4XVXC75%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICIRLfFOH%2Bj%2BmQl6zKtceDmjrJpBO2nnkYS3xQhTm4%2FKAiEAmz2xXoosS%2BMISNBEQojL8%2Fs4GmpTipe9lSBK99mCX7Uq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDP6S1x3TQkB24XExsSrcA6G7SQP4KSPt9FUSPUWADAO7HXjI%2FupbSueTkkkHkI5TmTpBYxHkJva7nn7Ge0muZBTmIetsEVZDuBSBgscNilOrTi%2Bm555yBDekfwyFQmK7XSQSLiPxmAQW8epZiqYeu8irT0oJFc5SfViKGCikGjT9w58hb%2BX41tBHGu5gzbroEKopA8USLSs0fgWDvu3TllFVnuCqe7H3oPes4r%2FB%2B33sGsdC4kANbgTjlH%2F1ulkHlsT6y8sg%2Bd3KDR9TILNWHyN8GENZA9Sk7ORJC5xkiabJc4YJrtudu3xfaHbRnRsXj0BUY%2FXJCvLrb65zuGTAQk2XAypLD3eFp9xWIwTG2jGukRurVxzwFmZ%2BejsNBPudEptA%2B0gdqjenV3W5qc337qCDsz68KnvGR4Q8dJGNc%2FX3Su1RZd8MsqoiyI0%2BBEwlWTX4Qavz%2FLEQvN37tR%2Fv7JyCcMrVZYtV3Dm56PZw%2BBUe7bMnFtn3%2BScuOYZb4UeN18vKX47Znbjtbdtzs4swSNArhyRgdQAjCBmC4lyH8rHlFECt1%2BhbuyCAH6tytWjQmsqjQeABkfQjJPY%2FDOOe45bOdC6K8Gju4DdKov4xk6GCpHNjSIlriKgOkTQoNp7a983G4i1XsELlHklgMIH8kL0GOqUBaYnssrigq6guKzC9UmcwRN9sYMefCSNrjUy2V6jV6MzFm4xdfqNBB23kO57j%2BszwNBvpaN4umTgPd7fGt%2B%2BdKfvzIBD2e2lxIe9PWjPVvgjwEwrev9J6FUc5qU%2BbPzcwvUit%2BEJkUImaBnqDaNWGoTIAWZm8oi2k7aiWma3fWZeFdtxrPn6gnFQFsBUV8QmHgVW9P9Q4bM7MqwLpLrAJ0YGlLmEP&X-Amz-Signature=62b71d23bc8b718ea81e5707676b534727148dc6a922c47ba74aa9fb5c805846&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4XVXC75%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICIRLfFOH%2Bj%2BmQl6zKtceDmjrJpBO2nnkYS3xQhTm4%2FKAiEAmz2xXoosS%2BMISNBEQojL8%2Fs4GmpTipe9lSBK99mCX7Uq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDP6S1x3TQkB24XExsSrcA6G7SQP4KSPt9FUSPUWADAO7HXjI%2FupbSueTkkkHkI5TmTpBYxHkJva7nn7Ge0muZBTmIetsEVZDuBSBgscNilOrTi%2Bm555yBDekfwyFQmK7XSQSLiPxmAQW8epZiqYeu8irT0oJFc5SfViKGCikGjT9w58hb%2BX41tBHGu5gzbroEKopA8USLSs0fgWDvu3TllFVnuCqe7H3oPes4r%2FB%2B33sGsdC4kANbgTjlH%2F1ulkHlsT6y8sg%2Bd3KDR9TILNWHyN8GENZA9Sk7ORJC5xkiabJc4YJrtudu3xfaHbRnRsXj0BUY%2FXJCvLrb65zuGTAQk2XAypLD3eFp9xWIwTG2jGukRurVxzwFmZ%2BejsNBPudEptA%2B0gdqjenV3W5qc337qCDsz68KnvGR4Q8dJGNc%2FX3Su1RZd8MsqoiyI0%2BBEwlWTX4Qavz%2FLEQvN37tR%2Fv7JyCcMrVZYtV3Dm56PZw%2BBUe7bMnFtn3%2BScuOYZb4UeN18vKX47Znbjtbdtzs4swSNArhyRgdQAjCBmC4lyH8rHlFECt1%2BhbuyCAH6tytWjQmsqjQeABkfQjJPY%2FDOOe45bOdC6K8Gju4DdKov4xk6GCpHNjSIlriKgOkTQoNp7a983G4i1XsELlHklgMIH8kL0GOqUBaYnssrigq6guKzC9UmcwRN9sYMefCSNrjUy2V6jV6MzFm4xdfqNBB23kO57j%2BszwNBvpaN4umTgPd7fGt%2B%2BdKfvzIBD2e2lxIe9PWjPVvgjwEwrev9J6FUc5qU%2BbPzcwvUit%2BEJkUImaBnqDaNWGoTIAWZm8oi2k7aiWma3fWZeFdtxrPn6gnFQFsBUV8QmHgVW9P9Q4bM7MqwLpLrAJ0YGlLmEP&X-Amz-Signature=83b09c4b56fb870258aaab9ca23716f74f7078430cf6aabcfb0cceccb2aca93e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4XVXC75%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICIRLfFOH%2Bj%2BmQl6zKtceDmjrJpBO2nnkYS3xQhTm4%2FKAiEAmz2xXoosS%2BMISNBEQojL8%2Fs4GmpTipe9lSBK99mCX7Uq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDP6S1x3TQkB24XExsSrcA6G7SQP4KSPt9FUSPUWADAO7HXjI%2FupbSueTkkkHkI5TmTpBYxHkJva7nn7Ge0muZBTmIetsEVZDuBSBgscNilOrTi%2Bm555yBDekfwyFQmK7XSQSLiPxmAQW8epZiqYeu8irT0oJFc5SfViKGCikGjT9w58hb%2BX41tBHGu5gzbroEKopA8USLSs0fgWDvu3TllFVnuCqe7H3oPes4r%2FB%2B33sGsdC4kANbgTjlH%2F1ulkHlsT6y8sg%2Bd3KDR9TILNWHyN8GENZA9Sk7ORJC5xkiabJc4YJrtudu3xfaHbRnRsXj0BUY%2FXJCvLrb65zuGTAQk2XAypLD3eFp9xWIwTG2jGukRurVxzwFmZ%2BejsNBPudEptA%2B0gdqjenV3W5qc337qCDsz68KnvGR4Q8dJGNc%2FX3Su1RZd8MsqoiyI0%2BBEwlWTX4Qavz%2FLEQvN37tR%2Fv7JyCcMrVZYtV3Dm56PZw%2BBUe7bMnFtn3%2BScuOYZb4UeN18vKX47Znbjtbdtzs4swSNArhyRgdQAjCBmC4lyH8rHlFECt1%2BhbuyCAH6tytWjQmsqjQeABkfQjJPY%2FDOOe45bOdC6K8Gju4DdKov4xk6GCpHNjSIlriKgOkTQoNp7a983G4i1XsELlHklgMIH8kL0GOqUBaYnssrigq6guKzC9UmcwRN9sYMefCSNrjUy2V6jV6MzFm4xdfqNBB23kO57j%2BszwNBvpaN4umTgPd7fGt%2B%2BdKfvzIBD2e2lxIe9PWjPVvgjwEwrev9J6FUc5qU%2BbPzcwvUit%2BEJkUImaBnqDaNWGoTIAWZm8oi2k7aiWma3fWZeFdtxrPn6gnFQFsBUV8QmHgVW9P9Q4bM7MqwLpLrAJ0YGlLmEP&X-Amz-Signature=fc9770fd3468fb4f3377e0edc03ab4a3e748392bbe9d719efbcb70780e0c8e8c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4XVXC75%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICIRLfFOH%2Bj%2BmQl6zKtceDmjrJpBO2nnkYS3xQhTm4%2FKAiEAmz2xXoosS%2BMISNBEQojL8%2Fs4GmpTipe9lSBK99mCX7Uq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDP6S1x3TQkB24XExsSrcA6G7SQP4KSPt9FUSPUWADAO7HXjI%2FupbSueTkkkHkI5TmTpBYxHkJva7nn7Ge0muZBTmIetsEVZDuBSBgscNilOrTi%2Bm555yBDekfwyFQmK7XSQSLiPxmAQW8epZiqYeu8irT0oJFc5SfViKGCikGjT9w58hb%2BX41tBHGu5gzbroEKopA8USLSs0fgWDvu3TllFVnuCqe7H3oPes4r%2FB%2B33sGsdC4kANbgTjlH%2F1ulkHlsT6y8sg%2Bd3KDR9TILNWHyN8GENZA9Sk7ORJC5xkiabJc4YJrtudu3xfaHbRnRsXj0BUY%2FXJCvLrb65zuGTAQk2XAypLD3eFp9xWIwTG2jGukRurVxzwFmZ%2BejsNBPudEptA%2B0gdqjenV3W5qc337qCDsz68KnvGR4Q8dJGNc%2FX3Su1RZd8MsqoiyI0%2BBEwlWTX4Qavz%2FLEQvN37tR%2Fv7JyCcMrVZYtV3Dm56PZw%2BBUe7bMnFtn3%2BScuOYZb4UeN18vKX47Znbjtbdtzs4swSNArhyRgdQAjCBmC4lyH8rHlFECt1%2BhbuyCAH6tytWjQmsqjQeABkfQjJPY%2FDOOe45bOdC6K8Gju4DdKov4xk6GCpHNjSIlriKgOkTQoNp7a983G4i1XsELlHklgMIH8kL0GOqUBaYnssrigq6guKzC9UmcwRN9sYMefCSNrjUy2V6jV6MzFm4xdfqNBB23kO57j%2BszwNBvpaN4umTgPd7fGt%2B%2BdKfvzIBD2e2lxIe9PWjPVvgjwEwrev9J6FUc5qU%2BbPzcwvUit%2BEJkUImaBnqDaNWGoTIAWZm8oi2k7aiWma3fWZeFdtxrPn6gnFQFsBUV8QmHgVW9P9Q4bM7MqwLpLrAJ0YGlLmEP&X-Amz-Signature=905139f18daaba0f5a48d0b72482ec88a6d565bdbcaee493948af5305ed4c320&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4XVXC75%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICIRLfFOH%2Bj%2BmQl6zKtceDmjrJpBO2nnkYS3xQhTm4%2FKAiEAmz2xXoosS%2BMISNBEQojL8%2Fs4GmpTipe9lSBK99mCX7Uq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDP6S1x3TQkB24XExsSrcA6G7SQP4KSPt9FUSPUWADAO7HXjI%2FupbSueTkkkHkI5TmTpBYxHkJva7nn7Ge0muZBTmIetsEVZDuBSBgscNilOrTi%2Bm555yBDekfwyFQmK7XSQSLiPxmAQW8epZiqYeu8irT0oJFc5SfViKGCikGjT9w58hb%2BX41tBHGu5gzbroEKopA8USLSs0fgWDvu3TllFVnuCqe7H3oPes4r%2FB%2B33sGsdC4kANbgTjlH%2F1ulkHlsT6y8sg%2Bd3KDR9TILNWHyN8GENZA9Sk7ORJC5xkiabJc4YJrtudu3xfaHbRnRsXj0BUY%2FXJCvLrb65zuGTAQk2XAypLD3eFp9xWIwTG2jGukRurVxzwFmZ%2BejsNBPudEptA%2B0gdqjenV3W5qc337qCDsz68KnvGR4Q8dJGNc%2FX3Su1RZd8MsqoiyI0%2BBEwlWTX4Qavz%2FLEQvN37tR%2Fv7JyCcMrVZYtV3Dm56PZw%2BBUe7bMnFtn3%2BScuOYZb4UeN18vKX47Znbjtbdtzs4swSNArhyRgdQAjCBmC4lyH8rHlFECt1%2BhbuyCAH6tytWjQmsqjQeABkfQjJPY%2FDOOe45bOdC6K8Gju4DdKov4xk6GCpHNjSIlriKgOkTQoNp7a983G4i1XsELlHklgMIH8kL0GOqUBaYnssrigq6guKzC9UmcwRN9sYMefCSNrjUy2V6jV6MzFm4xdfqNBB23kO57j%2BszwNBvpaN4umTgPd7fGt%2B%2BdKfvzIBD2e2lxIe9PWjPVvgjwEwrev9J6FUc5qU%2BbPzcwvUit%2BEJkUImaBnqDaNWGoTIAWZm8oi2k7aiWma3fWZeFdtxrPn6gnFQFsBUV8QmHgVW9P9Q4bM7MqwLpLrAJ0YGlLmEP&X-Amz-Signature=f6224bef5de0654014a4b217587ac85c5ab9d591234378a307d9ce57644ee466&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAFIAJMO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQChHoAsViTkTGOY2eKxCfF1KHVvb6gwQ52%2Bb5GYg%2Fxw9QIhAKFQngjJjr0fpNjmfEYQ%2BKHfYt1rm0he%2BmVvHiBo1N%2BJKv8DCFYQABoMNjM3NDIzMTgzODA1IgxtTgWS9%2BDmc7X6dv0q3ANoyvzOzDHe2wtvbLgIfyLmxXlfvtBvRspq%2Fzv%2FbmfLdGgId3OV7zMRl4vieOXLNmzfRI6j6mJlIXlbXdMoju%2FHqpC%2BsghhWxD8iPrBLb%2FMFiUCxXsypJqaASxJmlhp%2B4TEp1j36EEjA3%2BMUcmIGmk8S8%2BL8PM0KMQ3GpihPk%2BdpppKQU58m1ZKygSpbUf8WJ4zCYyvKF8Rt6rQz3bZNG5tR23hXCUCxCeKo1bck0OMuzsAKfF02HY1zDAMHop6uvp45idkY7KDMPch9b8NFNfBEea6mVtfn0NptYJqgOfpwlI0d%2BnXsWvu%2BjVcUT9vpSz9IcPg0ySzuRyE8qf4DZgPWzEb2KYR0BbumpG%2FWgAyPtsUM%2Bq0Al40%2BHKxTu201zdldXbdQaWn30NZ%2BpqPbTzdZhKN7yspZ4Yz0iuvSA8Frs5I%2BlGQfBMJ5KNqxVSXr%2BSMYIiBJuhWLpRp8fLEiixlCgEhqWiKM%2FsuEXc5cZe1U5rJv%2FOoGCjKb93T570PCUrKcIJWnFa67OWPwHrJt8YBSGTGRsouAGjmJwkiNke7OgkSbu0QTFMObyzSvcvG5CS2vK76VjkG5OWF1MgGpSAfdWHB8Zv72Ap0Vi93fKahtNHCYIXdPEOgCyKoeDDk%2B5C9BjqkAe5bevGhvJHqjjjMXIPMSLZmZMIkwfHayhNlrCWsXdzcCD%2BOd9OW28mlJKZ3dWcLSMKrH87y2aZqyg5E5lo0hDp3Y9ghiflZpYnWG2XKRZsQ2gN6BqYBp2VQ8NOfGGD3L4RTV8V7txEeOXtLi5weISD4hXYIYRI%2Fo8Troc3y3tBSR1NoOtQKchGIHsSlWXutZX3dcEQLtn4HGVtGTp7f2zGvs3Pv&X-Amz-Signature=34378d32f04d081c5d0b94a02a66d362615ab98583453324c270940979a88e02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAFIAJMO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQChHoAsViTkTGOY2eKxCfF1KHVvb6gwQ52%2Bb5GYg%2Fxw9QIhAKFQngjJjr0fpNjmfEYQ%2BKHfYt1rm0he%2BmVvHiBo1N%2BJKv8DCFYQABoMNjM3NDIzMTgzODA1IgxtTgWS9%2BDmc7X6dv0q3ANoyvzOzDHe2wtvbLgIfyLmxXlfvtBvRspq%2Fzv%2FbmfLdGgId3OV7zMRl4vieOXLNmzfRI6j6mJlIXlbXdMoju%2FHqpC%2BsghhWxD8iPrBLb%2FMFiUCxXsypJqaASxJmlhp%2B4TEp1j36EEjA3%2BMUcmIGmk8S8%2BL8PM0KMQ3GpihPk%2BdpppKQU58m1ZKygSpbUf8WJ4zCYyvKF8Rt6rQz3bZNG5tR23hXCUCxCeKo1bck0OMuzsAKfF02HY1zDAMHop6uvp45idkY7KDMPch9b8NFNfBEea6mVtfn0NptYJqgOfpwlI0d%2BnXsWvu%2BjVcUT9vpSz9IcPg0ySzuRyE8qf4DZgPWzEb2KYR0BbumpG%2FWgAyPtsUM%2Bq0Al40%2BHKxTu201zdldXbdQaWn30NZ%2BpqPbTzdZhKN7yspZ4Yz0iuvSA8Frs5I%2BlGQfBMJ5KNqxVSXr%2BSMYIiBJuhWLpRp8fLEiixlCgEhqWiKM%2FsuEXc5cZe1U5rJv%2FOoGCjKb93T570PCUrKcIJWnFa67OWPwHrJt8YBSGTGRsouAGjmJwkiNke7OgkSbu0QTFMObyzSvcvG5CS2vK76VjkG5OWF1MgGpSAfdWHB8Zv72Ap0Vi93fKahtNHCYIXdPEOgCyKoeDDk%2B5C9BjqkAe5bevGhvJHqjjjMXIPMSLZmZMIkwfHayhNlrCWsXdzcCD%2BOd9OW28mlJKZ3dWcLSMKrH87y2aZqyg5E5lo0hDp3Y9ghiflZpYnWG2XKRZsQ2gN6BqYBp2VQ8NOfGGD3L4RTV8V7txEeOXtLi5weISD4hXYIYRI%2Fo8Troc3y3tBSR1NoOtQKchGIHsSlWXutZX3dcEQLtn4HGVtGTp7f2zGvs3Pv&X-Amz-Signature=1c134031a0c9d6cab5948867306500a22c52d94a076cd82cb3dc4d56505ee107&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAFIAJMO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQChHoAsViTkTGOY2eKxCfF1KHVvb6gwQ52%2Bb5GYg%2Fxw9QIhAKFQngjJjr0fpNjmfEYQ%2BKHfYt1rm0he%2BmVvHiBo1N%2BJKv8DCFYQABoMNjM3NDIzMTgzODA1IgxtTgWS9%2BDmc7X6dv0q3ANoyvzOzDHe2wtvbLgIfyLmxXlfvtBvRspq%2Fzv%2FbmfLdGgId3OV7zMRl4vieOXLNmzfRI6j6mJlIXlbXdMoju%2FHqpC%2BsghhWxD8iPrBLb%2FMFiUCxXsypJqaASxJmlhp%2B4TEp1j36EEjA3%2BMUcmIGmk8S8%2BL8PM0KMQ3GpihPk%2BdpppKQU58m1ZKygSpbUf8WJ4zCYyvKF8Rt6rQz3bZNG5tR23hXCUCxCeKo1bck0OMuzsAKfF02HY1zDAMHop6uvp45idkY7KDMPch9b8NFNfBEea6mVtfn0NptYJqgOfpwlI0d%2BnXsWvu%2BjVcUT9vpSz9IcPg0ySzuRyE8qf4DZgPWzEb2KYR0BbumpG%2FWgAyPtsUM%2Bq0Al40%2BHKxTu201zdldXbdQaWn30NZ%2BpqPbTzdZhKN7yspZ4Yz0iuvSA8Frs5I%2BlGQfBMJ5KNqxVSXr%2BSMYIiBJuhWLpRp8fLEiixlCgEhqWiKM%2FsuEXc5cZe1U5rJv%2FOoGCjKb93T570PCUrKcIJWnFa67OWPwHrJt8YBSGTGRsouAGjmJwkiNke7OgkSbu0QTFMObyzSvcvG5CS2vK76VjkG5OWF1MgGpSAfdWHB8Zv72Ap0Vi93fKahtNHCYIXdPEOgCyKoeDDk%2B5C9BjqkAe5bevGhvJHqjjjMXIPMSLZmZMIkwfHayhNlrCWsXdzcCD%2BOd9OW28mlJKZ3dWcLSMKrH87y2aZqyg5E5lo0hDp3Y9ghiflZpYnWG2XKRZsQ2gN6BqYBp2VQ8NOfGGD3L4RTV8V7txEeOXtLi5weISD4hXYIYRI%2Fo8Troc3y3tBSR1NoOtQKchGIHsSlWXutZX3dcEQLtn4HGVtGTp7f2zGvs3Pv&X-Amz-Signature=8919b5243fdf554df181cdc436f10a052a98cf60e5239432d6b9f7f963d7eec3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAFIAJMO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQChHoAsViTkTGOY2eKxCfF1KHVvb6gwQ52%2Bb5GYg%2Fxw9QIhAKFQngjJjr0fpNjmfEYQ%2BKHfYt1rm0he%2BmVvHiBo1N%2BJKv8DCFYQABoMNjM3NDIzMTgzODA1IgxtTgWS9%2BDmc7X6dv0q3ANoyvzOzDHe2wtvbLgIfyLmxXlfvtBvRspq%2Fzv%2FbmfLdGgId3OV7zMRl4vieOXLNmzfRI6j6mJlIXlbXdMoju%2FHqpC%2BsghhWxD8iPrBLb%2FMFiUCxXsypJqaASxJmlhp%2B4TEp1j36EEjA3%2BMUcmIGmk8S8%2BL8PM0KMQ3GpihPk%2BdpppKQU58m1ZKygSpbUf8WJ4zCYyvKF8Rt6rQz3bZNG5tR23hXCUCxCeKo1bck0OMuzsAKfF02HY1zDAMHop6uvp45idkY7KDMPch9b8NFNfBEea6mVtfn0NptYJqgOfpwlI0d%2BnXsWvu%2BjVcUT9vpSz9IcPg0ySzuRyE8qf4DZgPWzEb2KYR0BbumpG%2FWgAyPtsUM%2Bq0Al40%2BHKxTu201zdldXbdQaWn30NZ%2BpqPbTzdZhKN7yspZ4Yz0iuvSA8Frs5I%2BlGQfBMJ5KNqxVSXr%2BSMYIiBJuhWLpRp8fLEiixlCgEhqWiKM%2FsuEXc5cZe1U5rJv%2FOoGCjKb93T570PCUrKcIJWnFa67OWPwHrJt8YBSGTGRsouAGjmJwkiNke7OgkSbu0QTFMObyzSvcvG5CS2vK76VjkG5OWF1MgGpSAfdWHB8Zv72Ap0Vi93fKahtNHCYIXdPEOgCyKoeDDk%2B5C9BjqkAe5bevGhvJHqjjjMXIPMSLZmZMIkwfHayhNlrCWsXdzcCD%2BOd9OW28mlJKZ3dWcLSMKrH87y2aZqyg5E5lo0hDp3Y9ghiflZpYnWG2XKRZsQ2gN6BqYBp2VQ8NOfGGD3L4RTV8V7txEeOXtLi5weISD4hXYIYRI%2Fo8Troc3y3tBSR1NoOtQKchGIHsSlWXutZX3dcEQLtn4HGVtGTp7f2zGvs3Pv&X-Amz-Signature=622e99fdd8d521a3e431fb7d18de9a902bab5248308c87cdc94465c618868831&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAFIAJMO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQChHoAsViTkTGOY2eKxCfF1KHVvb6gwQ52%2Bb5GYg%2Fxw9QIhAKFQngjJjr0fpNjmfEYQ%2BKHfYt1rm0he%2BmVvHiBo1N%2BJKv8DCFYQABoMNjM3NDIzMTgzODA1IgxtTgWS9%2BDmc7X6dv0q3ANoyvzOzDHe2wtvbLgIfyLmxXlfvtBvRspq%2Fzv%2FbmfLdGgId3OV7zMRl4vieOXLNmzfRI6j6mJlIXlbXdMoju%2FHqpC%2BsghhWxD8iPrBLb%2FMFiUCxXsypJqaASxJmlhp%2B4TEp1j36EEjA3%2BMUcmIGmk8S8%2BL8PM0KMQ3GpihPk%2BdpppKQU58m1ZKygSpbUf8WJ4zCYyvKF8Rt6rQz3bZNG5tR23hXCUCxCeKo1bck0OMuzsAKfF02HY1zDAMHop6uvp45idkY7KDMPch9b8NFNfBEea6mVtfn0NptYJqgOfpwlI0d%2BnXsWvu%2BjVcUT9vpSz9IcPg0ySzuRyE8qf4DZgPWzEb2KYR0BbumpG%2FWgAyPtsUM%2Bq0Al40%2BHKxTu201zdldXbdQaWn30NZ%2BpqPbTzdZhKN7yspZ4Yz0iuvSA8Frs5I%2BlGQfBMJ5KNqxVSXr%2BSMYIiBJuhWLpRp8fLEiixlCgEhqWiKM%2FsuEXc5cZe1U5rJv%2FOoGCjKb93T570PCUrKcIJWnFa67OWPwHrJt8YBSGTGRsouAGjmJwkiNke7OgkSbu0QTFMObyzSvcvG5CS2vK76VjkG5OWF1MgGpSAfdWHB8Zv72Ap0Vi93fKahtNHCYIXdPEOgCyKoeDDk%2B5C9BjqkAe5bevGhvJHqjjjMXIPMSLZmZMIkwfHayhNlrCWsXdzcCD%2BOd9OW28mlJKZ3dWcLSMKrH87y2aZqyg5E5lo0hDp3Y9ghiflZpYnWG2XKRZsQ2gN6BqYBp2VQ8NOfGGD3L4RTV8V7txEeOXtLi5weISD4hXYIYRI%2Fo8Troc3y3tBSR1NoOtQKchGIHsSlWXutZX3dcEQLtn4HGVtGTp7f2zGvs3Pv&X-Amz-Signature=48a47d0f939b858689c360cc331592a1d26add7efba542d7c06a3faf8126b622&X-Amz-SignedHeaders=host&x-id=GetObject)
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


