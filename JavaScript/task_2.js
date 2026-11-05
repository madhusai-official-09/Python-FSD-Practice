// 1. Write a JavaScript program to find the largest among three given numbers using conditional statements. 
// Input: let a = 25; let b = 45; let c = 30; 
// Expected Output: Largest Number: 45

/* let a,b,c;
a = 25;
b = 45;
c = 30;
let large;
if (a>b && a>c){
    large = a;
} else if (b>a && b>c){
    large = b;
} else{
    large = c;
}
console.log("Largest Number:",large); */


// 2. Write a JavaScript program to print the multiplication table of a given number from 1 to 10 using a loop. 
// Input: let num = 5; 
// Expected Output: 5 x 1 = 5,5 x 2 = 10 ...,5 x 10 = 50

/* let num,i;
num = 5;
i = 1;
while (i<=10){
    console.log(num + "X" + i + "=" + num*i);
    i++;
} */


// 3. Write a JavaScript program to reverse a given number using a loop. 
// Input: let num = 12345; 
// Expected Output: Reversed Number: 54321

/* let num,rev,d;
num = 12345;
rev=0;
while (num>0){
    d = num%10;
    rev = rev*10 + d;
    num=parseInt(num/10);
}
console.log(rev); */

// 4. Write a JavaScript program to find the sum of all even elements in a given array using a loop. 
// Input: let numbers = [12, 7, 18, 5, 20, 9, 14]; 
// Expected Output: Sum of Even Elements: 64

/* let num,i,sum;
num = [12, 7, 18, 5, 20, 9, 14];
sum = 0;
for (i of num){
    if (i%2==0){
        sum += i;
    }
}
console.log("Sum of Even Elements:", sum); */

// 5. Write a JavaScript program to count the number of positive and negative elements in a given array using a loop. 
// Input: let numbers = [10, -5, 8, -12, 0, 15, -3, 7]; 
// Expected Output: Positive Numbers: 4 
// Negative Numbers: 3 
// Zero Count: 1

/* let num,positive,negative,zero;
num = [10, -5, 8, -12, 0, 15, -3, 7];
positive = 0;
negative = 0;
zero = 0;

for (let i of num){
    if (i > 0){
        positive++;
    } else if (i < 0){
        negative++;
    } else {
        zero++;
    }
}
console.log("Positive Numbers:", positive);
console.log("Negative Numbers:", negative);
console.log("Zero Count:", zero); */
