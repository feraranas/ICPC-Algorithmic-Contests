# ICPC Algorithmic Problems -> Exercises for Competitive Programming

<details>
  <summary> GENERAL STEPS IN SOLVING A PROBLEM</summary>
  <hr style="border:2px solid gray">
  <ol>
    <details>
    <summary>First. UNDERSTANDING THE PROBLEM</summary>
          <ol>
               <li>What is the required result? What are the data? What is the starting point, or the initial conditions? What are the rules? (What are the allowed operations?)</li>
               <li> Is it possible to get the result from the data (with or without following the rules)? Do the problem by hand. What steps did you take? Can you write them down? </li>
               <li> Is the problem divided into major parts? What are they? How do they fit together (what memory cells do they share)? </li>
               <li> Have you assumed conditions about the problem that are not specified? What are they? Do they restrict the generality of the problem? Does this make a difference? </li>
          </ol>
     </details>
     <details>
     <summary>Second. DEVISING A PLAN</summary>
          <ol>
               <li>Have you seen it before, or the same problem in a slightly different form?</li>
               <li>Do you know a related or previously solved problem that could be useful?</li>
               <li>Look at the result. Try to think of a familiar problem that has a similar result. </li>
               <li>Here is a problem related to yours and solved before. Could you use it? Could you use part of it? Could you use its method? Can you modify it so you can use it?</li>
               <li>Look at the data. Repetitions in data hint at loops in the solution. What are the patterns?</li>
               <li>If you cannot solve the proposed problem, try to solve first some related problem. Can you imagine a more accessible related problem? A more general problem? A more special problem? An analogous problem? Can you solve part of the problem? Keep only part of the result and drop the rest: How much can you solve of the modified problem? Can you think of a new rule that would help to solve the problem? Can you restate the operation of the new rule in terms of rules you already have?</li>
          </ol>
     </details>
     <details>
     <summary>Third. CARRYING OUT THE PLAN</summary>
          <ol>
               <li>Check each step. Can you see clearly that each step is correct? Have you considered special cases?</li>
               <li>Can you check the result? Is the "answer" correct? Can you arrive at the right result, given a reasonable set of data? Given an unreasonable set of data?</li>
               <li>Make certain you solution works for "boundary" conditions. Does it work if the data list is empty? Too long? Can you acquire data that results in division by zero (or other nonsense)?</li>
          </ol>
     </details>
     <details>
     <summary>Fourth. LOOKING BACK</summary>
          <ol>
               <li>Do you compute an intermediate result that ins't used later? Can you eliminate it to simplify the solution?</li>
               <li>Can you derive the result differently? Can you make your solution simpler or more general?</li>
               <li>Can you use the solution, or method, for another problem?</li>
          </ol>
     </details>
  </ol>
</details>

<hr style="border:2px solid gray">
<details>
<summary>DYNAMIC PROGRAMMING PROBLEMS</summary>
<hr style="border:2px solid gray">

- Best Sum Memoized [bestSum-memoization.js](./DynamicProgramming/NumericProblems/bestSum/bestSum-memoization.js)
- Can Sum Memoized [canSum-memoization.js](./DynamicProgramming/NumericProblems/canSum/canSum-memoization.js)
- Fibonacci Memoized [fib-memoization.js](./DynamicProgramming/NumericProblems/Fibonacci/fib-memoization.js)
- Grid Traveler Memoized [grid-traveler-memoization.js](./DynamicProgramming/NumericProblems/gridTraveler/grid-traveler-memoization.js)
- How Sum Memoized [howSum-memoization.js](./DynamicProgramming/NumericProblems/howSum/howSum-memoization.js)
</details>

<hr style="border:2px solid gray">
<details>
<summary>STRING MANIPULATION PROBLEMS</summary>

<hr style="border:2px solid gray">

- All Construct [.js](./DynamicProgramming/StringProblems/allConstruct/allConstruct.js)
- Can Construct Memoized [canConstructMemoized.js](./DynamicProgramming/StringProblems/canConstruct/canConstructMemoized.js)
- Count Construct Memoized [countConstruct-memoized.js](./DynamicProgramming/StringProblems/countConstruct/countConstruct-memoized.js)
</details>

<hr style="border:2px solid gray">
<details>
<summary>NUMERICAL PROBLEMS</summary>

<hr style="border:2px solid gray">

- GCD Arrays [gcdArrays.py](./ICPCExercises/GCDArrays/gcdArrays.py)
- Madoka and Math Dad [MadokaMathDad.py](./ICPCExercises/MadokaMathDad/MadokaMathDad.py)
- Gifts Fixing [GiftsFixing.py](./ICPCExercises/GiftsFixing/GiftsFixing.py)
- Gregory And Cryptography [GregoryAndCryptography.py](./ICPCExercises/GregorAndCryptography/GregoryAndCryptography.py)
- Jewels And Stones (1) [JewelsAndStones.cpp](./ICPCExercises/JewelsAndStones/JewelsAndStones.cpp)
- Jewels And Stones (2) [JewelsAndStones.py](./ICPCExercises/JewelsAndStones/JewelsAndStones.py)
- Magical Sticks [MagicalSticks.py](./ICPCExercises/MagicalSticks/MagicalSticks.py)
- Majority Element [MajorityElement.py](./ICPCExercises/MajorityElement/MajorityElement.py)
- Max Sell Stock [MaxSellStock.py](./ICPCExercises/MaxSellStock/MaxSellStock.py)
- Minimal Square [MinimalSquare.py](./ICPCExercises/MinimalSquare/MinimalSquare.py)
</details>

<hr style="border:2px solid gray">
<details>
<summary>NUMBER'S THEORY</summary>

<hr style="border:2px solid gray">

- Divide and Conquer [DivideAndConquer.py](./ICPCExercises/DivideAndConquer/DivideAndConquer.py)
- Marin and Anti-coprime Permutation [MarinAnti-coprimePermutation.py](./ICPCExercises/MarinAnti-coprimePermutation/MarinAnti-coprimePermutation.py)
</details>
<hr style="border:2px solid gray">

<details>
<summary>BACKTRACKING</summary>
<hr style="border:2px solid gray">

- README info [README.md](./Backtracking/README.md)
- [Permutation of a String](./Backtracking/permutationsString/README.md)
- [Permutations of a String To a String.py](./Backtracking/permutationsStringToString/README.md)
- [Subsets of a Given Array](./Backtracking/subsetsOfGivenArray/README.md)
</details>
<hr style="border:2px solid gray">
