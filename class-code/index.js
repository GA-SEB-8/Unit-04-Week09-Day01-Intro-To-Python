function addTwoNumbers(){
    console.log(10+2)
}

const nums = [1,2,3,4,5,6]

function filterOddNumbers(num){
    return num %2 ==1
}

const oddNumbers = nums.filter(num=> num %2 ==1)
console.log(oddNumbers)



const doubledNumbers = nums.map((num)=>{return num*2})

console.log(doubledNumbers)