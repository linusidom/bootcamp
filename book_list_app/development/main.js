// console.log('hello from main.js')

const tableBody = document.querySelector('#tableBody')


// console.log(tableBody)


// Let's Refactor our code
// Refactoring is a way to clean the order of our code and make it more readable and efficient

function createTableRow(arr){
	let tableRow = document.createElement('tr')
	
	arr.forEach(entry => {
		// console.log(entry)
		let tableData = document.createElement('td')
		tableData.innerText = entry
		// console.log(tableData)
		tableRow.append(tableData)
		// console.log(tableRow)
	})
	
	let deleteButton = document.createElement('button')
	deleteButton.classList = 'delete btn btn-sm btn-danger m-2'
	deleteButton.innerText = 'Delete'
	tableRow.append(deleteButton)

	tableBody.append(tableRow)
}


function cleanUp(){

	document.querySelector('#bookTitle').value = ''
	document.querySelector('#bookAuthor').value = ''
	document.querySelector('#bookISBN').value = ''
}



// Objective
// Get data from the inputs
document.querySelector('form').addEventListener('submit', (e) =>{
	// console.log(e)
	// Forms default behavior is to refresh the page
	e.preventDefault()

	let title = document.querySelector('#bookTitle').value
	let author = document.querySelector('#bookAuthor').value
	let isbn = document.querySelector('#bookISBN').value
	// console.log(title, author, isbn)

	let formArr = [title, author, isbn]

	createTableRow(formArr)
	cleanUp()

})

// This will check it only when the page loads, not after
// const deleteButtons = document.querySelectorAll('.delete')

// console.log('Delete Button',deleteButtons)

// This will keep listening for anything on the AFTER it loads
tableBody.addEventListener('click', (e)=>{
	// console.log(e.target.classList.contains('delete'))
	if(e.target.classList.contains('delete')){
		// console.log(e.target.classList.contains('delete'))
		// console.dir(e.target.parentNode)
		e.target.parentNode.remove()
	}
})












