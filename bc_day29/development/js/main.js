// function myFunction(){
// 	var div = document.getElementById('div')
// 	if (div.style.display === 'none'){
// 		div.style.display = 'block';
// 	}
// 	else{
// 		div.style.display = 'none';	
// 		}
// 	}
// 	var variable;
// 	console.log('Print This', variable)

// console.log('This is from Main.js');

// This is a Comment in JavaScript # This is a Comment in Python

// Python: print('Hello World')
// console.log = print
// console.log('Hello World');

/*
This is a Multiline Comment
and
It uses these symbols


'''
But in Python these are Multiline Comments
'''
*/

/*
Variables
var, let const
*/

// x = 5
// var are normal variables that can be used globally
// var x = 5
// console.log(x)
// var x = 'String'
// console.log(x)


// // Let is a special variable that should be used inside conditionals/loops/functions, not global
// let y = 5
// console.log(y)
// // let y = 'String' Illegal Statement
// y = 'String';
// console.log(y)

// // Used for variables that won't change
// // If we declare a const, we cannot reassign it, but we can change it if we use arrays
// const z = 5
// console.log(z)
// // z = 'String' //Identifier 'z' has already been declared and  Assignment to constant variable.

//PEMDAS
// Parentheses
// Exponents
// Multiplication
// Division
// Addition
// Subtraction

// var x = 10
// var y = 20
// console.log(x + y)
// console.log(x - y)
// console.log(x * y)
// console.log(x / y)
// console.log(x % y)

// var totalBill = 100
// var serviceCharge = .10
// var totalCost = totalBill * (1 + serviceCharge)
// console.log(totalCost)


var x = 'The Quick Brown Fox Jumped Over the Fence';
// console.log(x[0], x[1])
// console.log(x.substring(0,20)) //Python x[0:20]
// x[0] = 'Q'; //Won't work because Strings are Immutable = Cannot Change
// console.log(x)

// Turn string to array - same as Python
// console.log(x.split(' '))

// Arrays (JavaScript) and Lists (python) are the same thing
y = x.split(' ')
// console.log(y)

// y[3] = ['Dog', 'Cat', 'Horse'];
// console.log(y)

//Pop Remove the last element / Same as Python
// y.pop()
// console.log(y)

// Add an element to the end - Python uses append
// y.push('Fence')
// console.log(y)

// Add to the beginning - Python y.insert(0, 'Added')
// y.unshift('Added')
// console.log(y)

// IndexOf to find where the element exists - Python y.index('Jumped')
// console.log(y.indexOf('Jumped'))



// console.log(y.slice(0,4))

// Splice changes the array in Place, don't have to save to a variable
// y.splice(2,0, 'Inserted')
// console.log(y)
// var fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.splice(2, 0, "Lemon", "Kiwi");
// console.log(fruits)


// Dictionaries - same as Python
// y = {
// 	"name":'John',
// 	"age":30,
// 	"height": 175,
// }
// console.log(y['name'])
// console.log(y.name)


// y['address'] = {
// 	"street":"101 Place",
// 	"city":"Bangkok",
// 	"country":"Thailand"}
// console.log(y.address.city) //Bangkok

// In Python the program will stop running
// In Javascript the program keep going with undefined
// console.log(y.address.state) //undefined - not error


// Null value Javascript will error - Program Stops
// Undeclared Variable will error - Program Stops
// Undefined will not error - Program keeps going



// Conditionals

// x = 5;
// y = '5';
// // Use Triple Equals (===) Always, never use == (double equal)
// if (x === y){
// 	console.log('X and Y are equal', x, y)
// 	console.log(typeof x)
// 	console.log(typeof y)
// }
// else{
// 	console.log('X does NOT equal Y', x, y)
// }
 

// Python
// if x == y:
// elif x != y:
// else:

// Basic Construction of conditional statements
// if (x===y){}
// else if(x != y){}
// else{}


// Break clause defined outside of while loop
// let x = 0
// while (x < 5){
// 	console.log(x);
// 	x++;
// }

// Python while loop
// x = 5
// while x < 5:
// 	print('x')
// 	x += 1




// python automatically does forEach

console.log(y)
// y.forEach(word => {
// 	console.log('This is the word, ', word)
// })

// y.forEach(function (word) {
// 	console.log('This is the word, ', word)
// })

// Indexing
y.forEach((word, index) => {
	console.log(index, word)
});

for(let i = 0; i<y.length; i = i + 3){
	console.log(i, y[i])
}

// Python len(y) = y.length (javascript)

// Python
// for word in y:
// 	print('This is the word', word)

// For Loop indexing
// for index, word in enumerate(y):
// 	print(index, word)

















































