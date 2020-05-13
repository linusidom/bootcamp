console.dir(document)

// List view
function listAPIView(){
	let url = `http://127.0.0.1:8000/post_api/`
	fetch(url)
	.then(res => res.json())
	.then(data => {
		data.forEach(post => {
		// Add the data to the Page
		// console.log(post)
		let div = document.querySelector('#newPost')
		let newPost = document.createElement('div')
		newPost.className = 'card post'
		newPost.innerHTML = `
			<div class="card-header">
				<a href="detail/${post.id}"><p>${post.title}</p></a>
				<p>Written By ${post.author}</p>
			</div>
			<div class="card-body">
				<p>${post.message}</p>
				<button class='btn btn-danger jsDelete ${post.id}'>Delete</button>
				<button type="button" class="btn btn-info jsUpdate ${post.id}" data-toggle="modal" data-target="#updatePost">
				Update</button>
			</div>`
		div.append(newPost)
		})
	})
}

// Create API Using Fetch

function createAPIView(data){
	// console.log(data)
	// URL for Create
	let url = `http://127.0.0.1:8000/post_api/create`
	
	// Use Fetch to POST Data
	fetch(url, {
		method: 'POST', // *GET, POST, PUT, DELETE, etc.
	    headers: {
	      'Content-Type': 'application/json'
	    },
	    body: data
		})
	.then(res => res.json())
	.then(post => {
		// Parse the Data
		// console.log(data)
		
		// Get the place for the data on the page
		let div = document.querySelector('#newPost')
		let newPost = document.createElement('div')
		newPost.className = 'card post'
		newPost.innerHTML = `
			<div class="card-header">
				<a href="detail/${post.id}"><p>${post.title}</p></a>
				<p>Written By ${post.author}</p>
			</div>
			<div class="card-body">
				<p>${post.message}</p>
				<button class='btn btn-danger jsDelete ${post.id}'>Delete</button>
				<button type="button" class="btn btn-info jsUpdate ${post.id}" data-toggle="modal" data-target="#updatePost">
				Update</button>
			</div>`
		div.append(newPost)
	})
}

// Update API View
function updateAPIView(data, postID){
	// console.log(data)
	// URL for Create
	let url = `http://127.0.0.1:8000/post_api/update/${postID}`
	
	// Use Fetch to POST Data
	fetch(url, {
		method: 'PUT', // *GET, POST, PUT, DELETE, etc.
	    headers: {
	      'Content-Type': 'application/json'
	    },
	    body: data
		})
	.then(res => res.json())
	.then(post => {return post})
	.catch(err => console.log(err))
	
	// Reset the page view and reload the content
	let div = document.querySelector('#newPost')
	div.innerHTML = ''
	listAPIView()
}

// Delete API
function deleteAPIView(postID){
	// console.log(data)
	// URL for Create
	let url = `http://127.0.0.1:8000/post_api/delete/${postID}`

	// Use Fetch to POST Data
	fetch(url, {
		method: 'DELETE', // *GET, POST, PUT, DELETE, etc.
	    headers: {
	      'Content-Type': 'application/json'
	    },
		})
		.catch(err => console.log(err))
}


Create - Grab data from the UI
const createPost = document.querySelector('.jsCreate')
createPost.addEventListener('click', (e) => {

	// console.log('Button clicked')

	// Get Data from the Django Form
	let title = document.querySelector('#id_title').value
	let author = document.querySelector('#id_author').value
	let message = document.querySelector('#id_message').value

	// console.log(title, author, message)

	// Put data into an object to Serialize in the API
	data = {
		title:title,
		author:author,
		message:message
	}
	// console.log(data)
	// console.log(JSON.stringify(data))

	// Turn the object into String and call the Create API function
	createAPIView(JSON.stringify(data))

	document.querySelector('#id_title').value = ''
	document.querySelector('#id_author').value = ''
	document.querySelector('#id_message').value = ''
})

const updatePost = document.querySelector('.jsUpdatePost')
updatePost.addEventListener('click', (e) => {

	// Get Data from the Django Form
	let postID = document.querySelector('#id_postID').value
	let title = document.querySelector('#id_update_title').value
	let author = document.querySelector('#id_update_author').value
	let message = document.querySelector('#id_update_message').value

	// console.log(title, author, message)

	// Put data into an object to Serialize in the API
	data = {
		title:title,
		author:author,
		message:message
	}
	// console.log(data)
	// console.log(JSON.stringify(data))

	// Turn the object into String and call the Create API function
	updateAPIView(JSON.stringify(data), postID)
})

document.addEventListener('DOMContentLoaded', listAPIView())

document.querySelector('#newPost').addEventListener('click', (e)=>{
	if (e.target.classList.contains('jsDelete')){
		deleteAPIView(e.target.classList[3])
		e.target.parentNode.parentNode.remove()
	}
	if (e.target.classList.contains('jsUpdate')){
		// console.dir(e.target)

		postID = e.target.classList[3]
		let message = e.target.previousElementSibling.previousElementSibling.textContent

		// Change NodeList to Array
		let children = Array.prototype.slice.call( e.target.parentNode.previousElementSibling.children )
		
		let authArr = children[1].innerText.split(' ')
		let author = authArr.slice(2).join(' ')
		
		let title = children[0].innerText
		document.querySelector('#id_postID').value = postID
		document.querySelector('#id_update_title').value = title
		document.querySelector('#id_update_author').value = author
		document.querySelector('#id_update_message').value = message
	}
})










