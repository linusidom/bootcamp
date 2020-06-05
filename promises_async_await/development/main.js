// https://www.universal-tutorial.com/rest-apis/free-rest-api-for-country-state-city
// aol@aol.com


// https://www.universal-tutorial.com/api/getaccesstoken


// https://www.universal-tutorial.com/api/countries/

// Asynchronous function
// Promise first Step - get data
// Cannot get from promise,
// Have to process inside promise

// if the response processors try process before the response comes back 
// there is not data to process
// Therefore we have to setup a promise/wait/response
const token = 'u0USjzSnV3JiiQamRv2X9R3vejhclHOl_Jn-V4d6A8a36UypcqlEERhDGJp50fkF1Eg'
const output = document.querySelector('#output')


function createTableData(country){
	
	// console.log(country)
	// <tr>
	// <td>Country Name</td>
	// <td>Country Short Name</td>
	// <td>Country Phone Code</td>
	// </tr>
	
	let tableRow = document.createElement('tr')
	tableRow.classList = 'country'
	Object.entries(country).forEach(([item, value])=> {
		// console.log('Item ',item, value)
		// console.log('Item ',item[0], item[1])
		let tableData = document.createElement('td')
		tableData.innerText = value
		tableRow.append(tableData)
	})
	output.append(tableRow)

}	





// Traditional Promises
function getTokenFetch(){
	fetch('https://www.universal-tutorial.com/api/getaccesstoken', {
		method: 'GET',
		headers: {
			"Accept": "application/json",
			"api-token": token,
			"user-email": "aol@aol.com"
		}
	})
	.then(response => response.json())
	.then(data => {
		// console.log(data.auth_token)
		fetch('https://www.universal-tutorial.com/api/countries/', {
			method: 'GET',
			headers: {
				"Authorization": "Bearer " + data.auth_token,
				"Accept": "application/json"
			}
		})
		.then(response => response.json())
		.then(data => {
			console.log(data)
		})
	})
}

// getTokenFetch()




// Async Await

async function getTokenAsyncAwait(){
	let response = await fetch('https://www.universal-tutorial.com/api/getaccesstoken', {
		method: 'GET',
		headers: {
			"Accept": "application/json",
			"api-token": token,
			"user-email": "aol@aol.com"
		}
	})
	// if(fetch call has completed then move on)


	let data = await response.json()
	// if (response.json is complete then){
	// 	get data
	// }

	return data
}

async function getDataAsyncAwait(token) {
	let response = await fetch('https://www.universal-tutorial.com/api/countries/', {
			method: 'GET',
			headers: {
				"Authorization": "Bearer " + token,
				"Accept": "application/json"
			}
		})

	let data = await response.json()

	return data
}


getTokenAsyncAwait()
.then(data => {
	// console.log(data.auth_token)
	getDataAsyncAwait(data.auth_token)
	.then(data => {
		// console.log(data)
		data.forEach(country => {
			createTableData(country)
		})
	})
})


function  regexMatchFunction(input, country) {
	// Regex can only be used on strings
	// g = global, i = case insensitive
	let pattern = new RegExp(`${input}`, 'gi')
	// console.log(pattern)
	// console.log(typeof country)
	return country.match(pattern)
}


// Filter data with out Search form
document.querySelector('#search').addEventListener('input', (event) => {
	let input = event.target.value

	let countries = document.querySelectorAll('.country')

	// console.log(countries)
	countries.forEach(country => {
		// console.log(country)
		if (regexMatchFunction(input, country.innerText.toLowerCase())){
			country.style.display = '';
		}
		else{
			country.style.display = 'none';
		}
	})
})






