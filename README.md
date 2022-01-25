# montyhall
## Monty Hall problem strategy test

I was recently reintroduced to the Monty Hall problem from a book I was reading. The scenario is as follows:

  *You're on a game show with a host named Monty Hall. There's 3 doors. Hidden behind one of the doors is a car (which you want). You begin by choosing one of the doors. Monty, who knows what lies behind each door, opens one of the doors that you did not choose. By opening this door, he reveals that there is no car behind it (some versions of this problem have a goat behind it, but that might be a win to some... I prefer win = car, loss = nothing). Monty then allows you to switch your initial door choice to the other remaining door if you so choose. Should you switch?*

The correct answer is: you are more likely to win the car if you choose to switch doors every time. This problem is not intuitive to most, myself included. It seems that once Monty removes one of the two empty doors, you are left with a 50/50 choice, and therefore it does not matter whether or not you switch. 

While many common explanations make sense within the context of probability theory, they just don't "feel" correct. Eventually, the following explanation helped me the most: 

  *Imagine that instead of 3 doors, there are 100 doors. You start by picking one just the same. Then, monty removes 98 empty doors. He is forced to leave the door with the car behind it. Do you switch or stay?*
  
What are the odds that you chose correctly initially? What are the odds now that Monty is forced to leave only 2 doors? The key to this problem is the fact that it is not blind probability as to which doors are removed. Instead, Monty is forced to leave the door with the car behind it, and that makes all the difference. However, losing 98 doors versus losing 1 door feels much different. In the 100 door scenario, your chances would increase by almost 99%. For the original Monty Hall problem, they would only increase by 1/3. This smaller change in probabality is harder to perceive when making decisions. 

What better way to show the answer to this problem in an intuitive way than to actually try both strategies a million times and see which is better? In a real game show, this would be impossible. With code, we can easily run this simulation trying both the switching and staying strategies and then report the percentage of wins and loses. This code does just that and shows that switching will give you a win roughly 66% of the time, and staying will win only 33% of the time. 
 
