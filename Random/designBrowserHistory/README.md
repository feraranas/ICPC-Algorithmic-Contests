# Design Browser History

You have a browser of one tab where you start on the ```homepage``` and you can ```visit``` another url, ```get back``` in the history number of ```steps``` or ```move forward``` in the history number of steps.

> Implement the BrowserHistory class:

- BrowserHistory(string homepage) Initializes the object with the homepage of the browser.

- void visit(string url) Visits url from the current page. It clears up all the forward history.

- string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.

- string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


<h2>Example:</h2>

<h4>Input:</h4>

> ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]

> [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

<h4>Output:</h4>

> [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

<h2>Explanation:</h2>

1. BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
2. browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
3. browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
4. browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
5. browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
6. browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
7. browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
8. browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
9. browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
10. browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
11. browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
 

Constraints:

- 1 <= homepage.length <= 20
- 1 <= url.length <= 20
- 1 <= steps <= 100
- homepage and url consist of  '.' or lower case English letters.
- At most 5000 calls will be made to visit, back, and forward.

References

[leetcode](https://leetcode.com/problems/design-browser-history/description/)