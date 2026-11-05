// 1. Write a JavaScript program to calculate the sum of all even numbers between 1 and 50.

/* let num,i,s;
num = 50;
i=1;
s = 0;
while (i<=num){
    if (i%2==0){
        s+=i;
    }
    i++
}
console.log(s); */

// 2. Write a JavaScript program to count how many numbers between 1 and 100 are divisible by 5.

/* let num,i,count;
num =100;
i = 1;
count = 0
while (i<=num){
    if (i%5==0){
        count++
    }
    i++
}
console.log(count); */

// 3. Write a JavaScript program to find the factorial of a given number using a loop.

/* let num, i,fact;
num = 5;
i = 1;
fact = 1;
while (i<=num){
    fact *= i;
    i++
}
console.log(fact); */ 

// 4. Write a JavaScript program to check whether a given number is prime or not.

/* let num, i, isPrime;
num = 7;
isPrime = true;
for (i = 2; i < num; i++) {
    if (num % i === 0) {
        isPrime = false;
        break;
    }
}
console.log(isPrime); */

// 5. Write a JavaScript program to count the number of digits in a given number. Input: 123456 Output: 6

/* let num, count;
num = 123456;
count = 0;
while (num > 0) {
    num = parseInt(num / 10);
    count++;
}
console.log(count); */