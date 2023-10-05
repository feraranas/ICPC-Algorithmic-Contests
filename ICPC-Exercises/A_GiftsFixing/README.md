You have 𝑛 gifts and you want to give all of them to children. Of course, you don't want to offend anyone, so all gifts should be equal between each other. The 𝑖-th gift consists of $a_i$ candies and $b_i$ oranges.<br>

During one move, you can choose some gift $1≤𝑖≤𝑛$ and do one of the following operations:<br>

eat exactly one candy from this gift (decrease $𝑎_𝑖$ by one);<br>
eat exactly one orange from this gift (decrease $𝑏_𝑖$ by one);<br>

eat exactly one candy and exactly one orange from this gift (decrease both 𝑎𝑖 and 𝑏𝑖 by one).<br>

Of course, you can not eat a candy or orange if it's not present in the gift (so neither $a_i$ nor $𝑏_𝑖$ can become less than zero).<br>

As said above, all gifts should be equal. This means that after some sequence of moves the following two conditions should be satisfied: $𝑎_1=𝑎_2=⋯=𝑎_𝑛# and #𝑏_1=𝑏_2=⋯=𝑏_𝑛$ (and $𝑎_𝑖$ equals $𝑏_𝑖$ is not necessary).

Your task is to find the minimum number of moves required to equalize all the given gifts.<br>

You have to answer 𝑡 independent test cases.