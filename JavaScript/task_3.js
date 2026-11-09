// 1. Write a JavaScript program to move all zeros to the end of an array while maintaining the relative order of non-zero elements. 
// Input: let numbers = [0, 5, 0, 3, 8, 0, 2]; 
// Expected Output: [5, 3, 8, 2, 0, 0, 0]

/* let nums,n_li,num;
nums = [0, 5, 0, 3, 8, 0, 2];
n_li = [];
for (num of nums){
    if (num !== 0){
        n_li.push(num);
    } else{
        n_li.unshift(num);
    }

}
console.log(n_li) */

// 2. Write a JavaScript program to find the missing number from an array containing distinct numbers from 1 to N. 
// Input: let numbers = [1, 2, 4, 5, 6]; 
// Expected Output: Missing Number: 3

/* let nums,num,i,res,d;
nums = [1, 2, 4, 5, 6];
i=1;
d = 10;
while (i<=d){
    if (i!==nums[i-1]){
        console.log(i);
        break
    }
    i++;
} */

// 3. Write a JavaScript program to identify all duplicate elements in an array without using Set. 
// Input: let numbers = [4, 2, 7, 2, 8, 4, 9, 7]; 
// Expected Output: Duplicate Elements: [4, 2, 7]

/* let nums,num,n_li;
n_li=[];
nums = [4, 2, 7, 2, 8, 4, 9, 7];
for (num of nums){
    if(num in n_li){
        n_li.push(num);
    }
}
console.log(n_li); */

// 4. Write a JavaScript program to find the maximum difference between two elements where the larger element must appear after the smaller element.
// Input: let numbers = [7, 1, 5, 3, 6, 4]; 
// Expected Output: Maximum Difference: 5

/* let nums,num,max_diff,min_num;
nums = [7, 1, 5, 3, 6, 4];
min_num = nums[0];
max_diff = 0;
for (num of nums){
    if (num < min_num){
        min_num = num;
    } else if (num - min_num > max_diff){
        max_diff = num - min_num;
    }
}
console.log("Maximum Difference:", max_diff); */


//5. Write a JavaScript program to find an index where the sum of elements on the left is equal to the sum of elements on the right.
// Input: let numbers = [1, 3, 5, 2, 2]; 
// Expected Output: Equilibrium Index: 2


//6. Write a JavaScript program to create a new array where each element represents the product of all other elements except itself. Do not use division.Input: let numbers = [1, 2, 3, 4]; Expected Output: [24, 12, 8, 6]

/* let nums = [1, 2, 3, 4];
let result = [];
let leftProduct = 1;
let rightProduct = 1;
for (let i = 0; i < nums.length; i++) {
    result[i] = leftProduct;
    leftProduct *= nums[i];
}
for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= rightProduct;
    rightProduct *= nums[i];
}
console.log(result); */