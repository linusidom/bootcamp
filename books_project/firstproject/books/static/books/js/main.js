console.log('hello from main.js')

const output = document.querySelector('#output')
const url = 'http://127.0.0.1:8000/books_api'


function createForm(type){
	let div = document.createElement('div')
	let buttonClose = document.createElement('button')
	let buttonSubmit = document.createElement('button')
	
	buttonClose.classList = "btn btn-secondary"
	buttonClose.innerText = "Close"
	buttonClose.type = 'button'
	buttonClose.setAttribute('data-dismiss', 'modal')

	buttonSubmit.type = 'button'

	if(type === 'udpate'){
		let inputTitle = document.createElement('input')
		let inputAuthor = document.createElement('input')
		
		buttonSubmit.classList = "btn btn-primary"
		buttonSubmit.innerText = 'Save Changes'
		
		inputTitle.classList = 'form-control'
		inputAuthor.classList = 'form-control'
		inputTitle.placeholder = 'Enter Title'
		inputAuthor.placeholder = 'Enter Author'
		div.append(inputTitle, inputAuthor, buttonClose, buttonSubmit)
	}
	else{
		
		buttonSubmit.classList = "btn btn-danger"
		buttonSubmit.innerText = 'Delete'
		div.append(buttonClose, buttonSubmit)	

	}
	return div.innerHTML

}

function createModal(type, id){
	return `
	<div class="modal fade btn" id="${type}Modal-${id}" tabindex="-1" role="dialog" aria-labelledby="${type}ModalLabel" aria-hidden="true">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="${type}ModalLabel">${type.toUpperCase()} Book</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body">
						<form method='POST' class='form-group' action="${url}/${type}/${id}">
							${createForm(${type}, 'sample text')}
						</form>
					</div>
				</div>
			</div>
		</div>
	`
}

function createModalButton(type, id){
	return `
	<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#${type}Modal-${id}">${type.toUpperCase()} Book</button>	
	`
}

// console.log('Modal Button',createModalButton('update', 5))

function createCard(book){
	let div = document.createElement('div')
	div.classList = 'card'

	let p = document.createElement('p')
	p.innerHTML = `${book.title} Written By: ${book.author}`

	let divUpdate = document.createElement('div')
	let divDelete = document.createElement('div')
			

	let divButtonUpdate = document.createElement('div')
	let divButtonDelete = document.createElement('div')
	
	

	divButtonUpdate.innerHTML = createModalButton('update', book.id)
	divButtonDelete.innerHTML = createModalButton('delete', book.id)
	
	divUpdate.innerHTML = createModal('update', book.id)
	divDelete.innerHTML = createModal('delete', book.id)
	
	div.append(p, divButtonUpdate, divButtonDelete, divUpdate, divDelete)
	
	return div
}
// CRUD

// ListView

function listAPIView(){
	fetch(url)
	.then(res => res.json())
	.then(data => {
		data.forEach(book => {
			
			let card = createCard(book)
			
			output.append(card)
		})
	})
}



// CreateView

// UpdateView

// DeleteView




document.addEventListener('DOMContentLoaded', listAPIView())