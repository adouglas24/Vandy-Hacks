# Vandy Hacks Summer Edition 7/10/20-7/12/20: ShopWhole
# Winners: Best Beginner Hackers
<img align="left" width="150" height="150" src="https://github.com/adouglas24/ShopWhole/blob/master/boga-project/static/shopwhole-transparent.png"> 


Welcome to ShopWhole!

Website: shopwhole.tech or 192.81.211.69:80

ShopWhole is a digital marketplace that gives individual students the ability to buy everyday goods at wholesale prices. ShopWhole is distinct from any other wholesale stores because customers are not dependent on other's purchases to receive a significantly discounted price, there is no requirement for consumers to purchase large quantities, and the prices of products on our website are fixed for a given sale. By using an optimization algorithm based on the purchase patterns of various college campuses, ShopWhole can determine the ideal listing price for various items. More specifically, our algorithm develops predictions for the expected number of products purchased at a given price, compares those values with the wholesale price offers, and then finds the optimal listing price. The algorithm updates with every delivery made, constantly learning more about the students’ purchasing patterns and maximizing the discounts we can offer. Our site acts similarly to insurance, as the consumers are not affected by the somewhat random behavior of other consumers. We assume the risk if not enough people place an order, to ensure that our customers have guaranteed low prices that they can count on. 

ShopWhole relies on a bulk order partnership with manufacturers, along with having a central delivery location at participating schools. 
A test of the algorithm is available in Backend and would be actually implemented once products are ready to be sold. We developed the ShopWhole website with Django, using a MySQL database and Bootstrap for styling. The website is currently hosted at www.shopwhole.tech. If this doesn't work, please try visiting 192.81.211.69:80.

<hr>

<h1>The Math</h1>
<p align="center">
<img align="center" src="https://github.com/adouglas24/ShopWhole/blob/master/boga-project/static/visualization.gif">
</p>

Our algorithm analyzes student consumption patterns and how the price level relates to the number of purchases made by ShopWhole users. With each order placed, our algorithm updates itself to more accurately represent student purchasing patterns. After multiple iterations, we observe that the predicted student behavior approaches the true relationship between purchase quantity and price point, when tested with mock school data. 

<p align="center">
<img src="https://github.com/adouglas24/ShopWhole/blob/master/boga-project/static/profitoptimization.png">
</p>

Once we are able to accurately predict consumer behavior, we calculate the optimal listing price for the product. As the listing price is repeatedly optimized with increased understanding of student purchasing habits, our profits show a clear, increasing trend, when tested with mock school data.
<hr>

<h1>The Business Model</h1>
ShopWhole is able to make profit through the increasing the accuracy of our predictions. We will sell items at prices just above our estimated wholesale cost. This price will continue to decrease as the number of students ordering goods increases. In short, the more users we have, the more accurate our predictions become, and the more we can profit the customer, the wholesaler, and ShopWhole.


Created by: Alex Douglas, Vinay Konuru, Angela Li, and Aidan Persaud
