// Kilos
// let pounds = (Math.round((weight * 2.2) * 100) / 100).toFixed(2);;
// let grams = (Math.round((weight * 1000) * 100) / 100).toFixed(2);;
// let ounces = (Math.round((weight * 35.274) * 100) / 100).toFixed(2);
		
// Pounds
// let kilos = (Math.round((weight / 2.2) * 100) / 100).toFixed(2);;
// let grams = (Math.round((weight / .0022046) * 100) / 100).toFixed(2);;
// let ounces = (Math.round((weight * 16) * 100) / 100).toFixed(2);;

console.log('hello from main.js')


const output = document.querySelector('#output')
const messages = document.querySelector('#messages')



function createCard(dictionary){
	// console.log(dictionary)
	console.log(Object.entries(dictionary))
	// We use variable unpacking to get the values we want
	Object.entries(dictionary).forEach(([key, value]) => {
		// console.log('array', array)
		// console.log('index', index)
		console.log(key, value)
		
		// <div></div>
		let div = document.createElement('div')

		div.innerHTML = `<div class="card m-4">
        		<div class="card-header">${key.toUpperCase()}</div>
        		<div class="card-body">${value}</div>
        	</div>`
        output.append(div)
	})
}



function messageDisplay(){
	messages.innerHTML = `<h6 class='alert alert-primary'>Data is Below</h6>`
	setTimeout(() => {
		messages.innerHTML = ''
	}, 3000)
}



function cleanUp(){
	setTimeout(() => {
		document.querySelector('#weightInput').value = ''
	}, 3000)
	output.innerHTML = ''
}




// Get data from input box
document.querySelector('#weightInput').addEventListener('input', (e) =>{
	let weight = e.target.value
	let weightType = document.querySelector('#weightType').value
	// console.dir(weightType)
	// console.log(weightType)
	
	cleanUp()



	if(weightType === 'pounds'){
		// console.log('pounds', weight)

		// console.log(Math.round(((weight * 2.2) * 100)/100).toFixed(2))
		let kilos = (Math.round((weight / 2.2) * 100) / 100).toFixed(2);;
		let grams = (Math.round((weight / .0022046) * 100) / 100).toFixed(2);;
		let ounces = (Math.round((weight * 16) * 100) / 100).toFixed(2);;

		// console.log(kilos, grams, ounces)
		
		weightDictionary = {
			kilos:kilos,
			grams:grams,
			ounces:ounces
		}
		// console.log(weightDictionary)

		createCard(weightDictionary)
		messageDisplay()
		// There is a better way to do this with functions

		// output.innerHTML = `<div class="card">
  //       		<div class="card-header">Kilo</div>
  //       		<div class="card-body">${kilos}</div>
  //       	</div>`
	}
	else if(weightType === 'kilos'){
		console.log('kilos', weight)

		// Kilos
		let pounds = (Math.round((weight * 2.2) * 100) / 100).toFixed(2);;
		let grams = (Math.round((weight * 1000) * 100) / 100).toFixed(2);;
		let ounces = (Math.round((weight * 35.274) * 100) / 100).toFixed(2);


		weightDictionary = {
			pounds:pounds,
			grams:grams,
			ounces:ounces
		}
		// console.log(weightDictionary)

		createCard(weightDictionary)
		messageDisplay()	
	}

})