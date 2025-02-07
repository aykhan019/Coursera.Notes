

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ICS5JA7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCICzjxj74eR9MUBGmOda36Nx7AgvbdHB%2B1%2FvwJD8oDZX6AiEAhLn2xHyb7CkMYAnwFp7dsp%2BbhGNoTaOoV%2FKBpOTHc3Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBjCJEsozpCnKe9xmSrcAwAn7Y8czLLrHrF5qoactJBO2DRmabUldjFYWpDJmSmKW9%2Br7872cZzpv3VGUx3sSngN6XX7Nueiqn3fVdia%2Fa6GZg4j9DFMM7AwZzX8lCoMELhYNY6taAAHsExAhJBxxgEB6KKUYCYKs7wtvb9oaNqOjBDX411Y9vKTb0%2F63opzi20PkMnxEWkYi4EfqC0jYe3aXZcqLTWxvzuXHEXDU9so29ysuflyzZ6609fliftYnyETqkypfy1B2PaQUMzAAcpYLKP%2Bsg8ZExaKk3FxN95jNoYOk%2BAya1BxNKf%2BkLXcVI%2FQzeYwJwGKq0gJaTXIyr%2F84v9bxtdd5LFQMIUDEvipBBji1%2B6t5Iif5VedFFcg5zVcuAhmhaqy9F2QZk9qadhj767yFeO3CEiQeW5dx8IkuXYQCITMYF5W9wZdffzicMPA0r6ZHoLjca4%2FeMP%2FAFMSiazpjQrIl8c36T8HAgqXs8vTsFJoC77M%2FwF5cT0wpDSNldIRkq7qv%2Fx7Akt23QTmciZkO87fmwDHHieB6G6vtg9OgmsTWsuM7LzTsIklqCbR2S4QKFgrewX2mOFjWvDiw1IibAPMQG7gprqRw%2FYSIn3wDjtWKqQSOlA24Krr3KxhUQT%2FofuuyGx8MLualb0GOqUBOztAi1DsUvQeefUaGJb%2BSAzSTHIDMOrtIdhv95fewZv%2FvVRjG7EsmFTGFMNgCXs%2Bz6c0y%2BXqeCkYsIi3GGu%2FYolIe%2F6WnJAGaJB5yCv0mhB5Fc2Xo4XALC%2FxJVSeASZNAl8Qvjq5NPnWLWefrBQzLRFJlHDLPjvoIJduf4VgnAIhBjL06L6JBvuz7noLXnel4C0E3LsBNaFLJM8fLXZ9zJLfHdBE&X-Amz-Signature=9ed5e1f21907f6369a47cc6d3435bc2482fb92380833c0009760d4235ddc7b4e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=c5c523af6d62f0f12a8e09f81a45f3e9b01b5a7430e28dc09e17d71135594bf5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=a596b9d6dd4068646fadb441f500a442d43b15556d001487a74f09d40c596bdb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=af1d684647114683846198eeb12fc9fcfe1f286d2db9b6f804b69588a0e49076&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=e1ac49a58ed0e1271860a27aaf0b327a7b2a80087dd8a3a657e2d877ed9b9543&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=d248330afc52a933850d77fb49d59c5bb326e1e4e3c617355c0b7cfc4e908d8f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ICS5JA7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCICzjxj74eR9MUBGmOda36Nx7AgvbdHB%2B1%2FvwJD8oDZX6AiEAhLn2xHyb7CkMYAnwFp7dsp%2BbhGNoTaOoV%2FKBpOTHc3Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBjCJEsozpCnKe9xmSrcAwAn7Y8czLLrHrF5qoactJBO2DRmabUldjFYWpDJmSmKW9%2Br7872cZzpv3VGUx3sSngN6XX7Nueiqn3fVdia%2Fa6GZg4j9DFMM7AwZzX8lCoMELhYNY6taAAHsExAhJBxxgEB6KKUYCYKs7wtvb9oaNqOjBDX411Y9vKTb0%2F63opzi20PkMnxEWkYi4EfqC0jYe3aXZcqLTWxvzuXHEXDU9so29ysuflyzZ6609fliftYnyETqkypfy1B2PaQUMzAAcpYLKP%2Bsg8ZExaKk3FxN95jNoYOk%2BAya1BxNKf%2BkLXcVI%2FQzeYwJwGKq0gJaTXIyr%2F84v9bxtdd5LFQMIUDEvipBBji1%2B6t5Iif5VedFFcg5zVcuAhmhaqy9F2QZk9qadhj767yFeO3CEiQeW5dx8IkuXYQCITMYF5W9wZdffzicMPA0r6ZHoLjca4%2FeMP%2FAFMSiazpjQrIl8c36T8HAgqXs8vTsFJoC77M%2FwF5cT0wpDSNldIRkq7qv%2Fx7Akt23QTmciZkO87fmwDHHieB6G6vtg9OgmsTWsuM7LzTsIklqCbR2S4QKFgrewX2mOFjWvDiw1IibAPMQG7gprqRw%2FYSIn3wDjtWKqQSOlA24Krr3KxhUQT%2FofuuyGx8MLualb0GOqUBOztAi1DsUvQeefUaGJb%2BSAzSTHIDMOrtIdhv95fewZv%2FvVRjG7EsmFTGFMNgCXs%2Bz6c0y%2BXqeCkYsIi3GGu%2FYolIe%2F6WnJAGaJB5yCv0mhB5Fc2Xo4XALC%2FxJVSeASZNAl8Qvjq5NPnWLWefrBQzLRFJlHDLPjvoIJduf4VgnAIhBjL06L6JBvuz7noLXnel4C0E3LsBNaFLJM8fLXZ9zJLfHdBE&X-Amz-Signature=15351637cf26a1ca8349001eb218a7f01208957163e2c358ed11b0d01730fba0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ICS5JA7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCICzjxj74eR9MUBGmOda36Nx7AgvbdHB%2B1%2FvwJD8oDZX6AiEAhLn2xHyb7CkMYAnwFp7dsp%2BbhGNoTaOoV%2FKBpOTHc3Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBjCJEsozpCnKe9xmSrcAwAn7Y8czLLrHrF5qoactJBO2DRmabUldjFYWpDJmSmKW9%2Br7872cZzpv3VGUx3sSngN6XX7Nueiqn3fVdia%2Fa6GZg4j9DFMM7AwZzX8lCoMELhYNY6taAAHsExAhJBxxgEB6KKUYCYKs7wtvb9oaNqOjBDX411Y9vKTb0%2F63opzi20PkMnxEWkYi4EfqC0jYe3aXZcqLTWxvzuXHEXDU9so29ysuflyzZ6609fliftYnyETqkypfy1B2PaQUMzAAcpYLKP%2Bsg8ZExaKk3FxN95jNoYOk%2BAya1BxNKf%2BkLXcVI%2FQzeYwJwGKq0gJaTXIyr%2F84v9bxtdd5LFQMIUDEvipBBji1%2B6t5Iif5VedFFcg5zVcuAhmhaqy9F2QZk9qadhj767yFeO3CEiQeW5dx8IkuXYQCITMYF5W9wZdffzicMPA0r6ZHoLjca4%2FeMP%2FAFMSiazpjQrIl8c36T8HAgqXs8vTsFJoC77M%2FwF5cT0wpDSNldIRkq7qv%2Fx7Akt23QTmciZkO87fmwDHHieB6G6vtg9OgmsTWsuM7LzTsIklqCbR2S4QKFgrewX2mOFjWvDiw1IibAPMQG7gprqRw%2FYSIn3wDjtWKqQSOlA24Krr3KxhUQT%2FofuuyGx8MLualb0GOqUBOztAi1DsUvQeefUaGJb%2BSAzSTHIDMOrtIdhv95fewZv%2FvVRjG7EsmFTGFMNgCXs%2Bz6c0y%2BXqeCkYsIi3GGu%2FYolIe%2F6WnJAGaJB5yCv0mhB5Fc2Xo4XALC%2FxJVSeASZNAl8Qvjq5NPnWLWefrBQzLRFJlHDLPjvoIJduf4VgnAIhBjL06L6JBvuz7noLXnel4C0E3LsBNaFLJM8fLXZ9zJLfHdBE&X-Amz-Signature=cb13a5dcf371146baa39054b9d301e1713d13f9fea8168560193eea16402068d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ICS5JA7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCICzjxj74eR9MUBGmOda36Nx7AgvbdHB%2B1%2FvwJD8oDZX6AiEAhLn2xHyb7CkMYAnwFp7dsp%2BbhGNoTaOoV%2FKBpOTHc3Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBjCJEsozpCnKe9xmSrcAwAn7Y8czLLrHrF5qoactJBO2DRmabUldjFYWpDJmSmKW9%2Br7872cZzpv3VGUx3sSngN6XX7Nueiqn3fVdia%2Fa6GZg4j9DFMM7AwZzX8lCoMELhYNY6taAAHsExAhJBxxgEB6KKUYCYKs7wtvb9oaNqOjBDX411Y9vKTb0%2F63opzi20PkMnxEWkYi4EfqC0jYe3aXZcqLTWxvzuXHEXDU9so29ysuflyzZ6609fliftYnyETqkypfy1B2PaQUMzAAcpYLKP%2Bsg8ZExaKk3FxN95jNoYOk%2BAya1BxNKf%2BkLXcVI%2FQzeYwJwGKq0gJaTXIyr%2F84v9bxtdd5LFQMIUDEvipBBji1%2B6t5Iif5VedFFcg5zVcuAhmhaqy9F2QZk9qadhj767yFeO3CEiQeW5dx8IkuXYQCITMYF5W9wZdffzicMPA0r6ZHoLjca4%2FeMP%2FAFMSiazpjQrIl8c36T8HAgqXs8vTsFJoC77M%2FwF5cT0wpDSNldIRkq7qv%2Fx7Akt23QTmciZkO87fmwDHHieB6G6vtg9OgmsTWsuM7LzTsIklqCbR2S4QKFgrewX2mOFjWvDiw1IibAPMQG7gprqRw%2FYSIn3wDjtWKqQSOlA24Krr3KxhUQT%2FofuuyGx8MLualb0GOqUBOztAi1DsUvQeefUaGJb%2BSAzSTHIDMOrtIdhv95fewZv%2FvVRjG7EsmFTGFMNgCXs%2Bz6c0y%2BXqeCkYsIi3GGu%2FYolIe%2F6WnJAGaJB5yCv0mhB5Fc2Xo4XALC%2FxJVSeASZNAl8Qvjq5NPnWLWefrBQzLRFJlHDLPjvoIJduf4VgnAIhBjL06L6JBvuz7noLXnel4C0E3LsBNaFLJM8fLXZ9zJLfHdBE&X-Amz-Signature=72b67fe145ce96ee2e9945bd9a968b9b57850dec80399c051b6cbe59c0732239&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ICS5JA7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCICzjxj74eR9MUBGmOda36Nx7AgvbdHB%2B1%2FvwJD8oDZX6AiEAhLn2xHyb7CkMYAnwFp7dsp%2BbhGNoTaOoV%2FKBpOTHc3Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBjCJEsozpCnKe9xmSrcAwAn7Y8czLLrHrF5qoactJBO2DRmabUldjFYWpDJmSmKW9%2Br7872cZzpv3VGUx3sSngN6XX7Nueiqn3fVdia%2Fa6GZg4j9DFMM7AwZzX8lCoMELhYNY6taAAHsExAhJBxxgEB6KKUYCYKs7wtvb9oaNqOjBDX411Y9vKTb0%2F63opzi20PkMnxEWkYi4EfqC0jYe3aXZcqLTWxvzuXHEXDU9so29ysuflyzZ6609fliftYnyETqkypfy1B2PaQUMzAAcpYLKP%2Bsg8ZExaKk3FxN95jNoYOk%2BAya1BxNKf%2BkLXcVI%2FQzeYwJwGKq0gJaTXIyr%2F84v9bxtdd5LFQMIUDEvipBBji1%2B6t5Iif5VedFFcg5zVcuAhmhaqy9F2QZk9qadhj767yFeO3CEiQeW5dx8IkuXYQCITMYF5W9wZdffzicMPA0r6ZHoLjca4%2FeMP%2FAFMSiazpjQrIl8c36T8HAgqXs8vTsFJoC77M%2FwF5cT0wpDSNldIRkq7qv%2Fx7Akt23QTmciZkO87fmwDHHieB6G6vtg9OgmsTWsuM7LzTsIklqCbR2S4QKFgrewX2mOFjWvDiw1IibAPMQG7gprqRw%2FYSIn3wDjtWKqQSOlA24Krr3KxhUQT%2FofuuyGx8MLualb0GOqUBOztAi1DsUvQeefUaGJb%2BSAzSTHIDMOrtIdhv95fewZv%2FvVRjG7EsmFTGFMNgCXs%2Bz6c0y%2BXqeCkYsIi3GGu%2FYolIe%2F6WnJAGaJB5yCv0mhB5Fc2Xo4XALC%2FxJVSeASZNAl8Qvjq5NPnWLWefrBQzLRFJlHDLPjvoIJduf4VgnAIhBjL06L6JBvuz7noLXnel4C0E3LsBNaFLJM8fLXZ9zJLfHdBE&X-Amz-Signature=543ddda314713ef09d9558a3e9d11123cb283d1b2f2eda5759b4375ea9159b05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ICS5JA7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCICzjxj74eR9MUBGmOda36Nx7AgvbdHB%2B1%2FvwJD8oDZX6AiEAhLn2xHyb7CkMYAnwFp7dsp%2BbhGNoTaOoV%2FKBpOTHc3Qq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBjCJEsozpCnKe9xmSrcAwAn7Y8czLLrHrF5qoactJBO2DRmabUldjFYWpDJmSmKW9%2Br7872cZzpv3VGUx3sSngN6XX7Nueiqn3fVdia%2Fa6GZg4j9DFMM7AwZzX8lCoMELhYNY6taAAHsExAhJBxxgEB6KKUYCYKs7wtvb9oaNqOjBDX411Y9vKTb0%2F63opzi20PkMnxEWkYi4EfqC0jYe3aXZcqLTWxvzuXHEXDU9so29ysuflyzZ6609fliftYnyETqkypfy1B2PaQUMzAAcpYLKP%2Bsg8ZExaKk3FxN95jNoYOk%2BAya1BxNKf%2BkLXcVI%2FQzeYwJwGKq0gJaTXIyr%2F84v9bxtdd5LFQMIUDEvipBBji1%2B6t5Iif5VedFFcg5zVcuAhmhaqy9F2QZk9qadhj767yFeO3CEiQeW5dx8IkuXYQCITMYF5W9wZdffzicMPA0r6ZHoLjca4%2FeMP%2FAFMSiazpjQrIl8c36T8HAgqXs8vTsFJoC77M%2FwF5cT0wpDSNldIRkq7qv%2Fx7Akt23QTmciZkO87fmwDHHieB6G6vtg9OgmsTWsuM7LzTsIklqCbR2S4QKFgrewX2mOFjWvDiw1IibAPMQG7gprqRw%2FYSIn3wDjtWKqQSOlA24Krr3KxhUQT%2FofuuyGx8MLualb0GOqUBOztAi1DsUvQeefUaGJb%2BSAzSTHIDMOrtIdhv95fewZv%2FvVRjG7EsmFTGFMNgCXs%2Bz6c0y%2BXqeCkYsIi3GGu%2FYolIe%2F6WnJAGaJB5yCv0mhB5Fc2Xo4XALC%2FxJVSeASZNAl8Qvjq5NPnWLWefrBQzLRFJlHDLPjvoIJduf4VgnAIhBjL06L6JBvuz7noLXnel4C0E3LsBNaFLJM8fLXZ9zJLfHdBE&X-Amz-Signature=d3d9699699e3710915cd89cf4a571140ae72a47246dc4fab9d4e28aa8669a1ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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


