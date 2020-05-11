// console.log('hello from main.js')

// QuerSelector can choose based on Tag, class, or ID
// QuerySelector will return only the first element it finds
// const postList = document.querySelector('#postList')

// QuerySelector All will return a Node List
// const postList = document.querySelectorAll('.postList')

// const postList = document.querySelector('.postList')
// // console.log(postList)
// // postList.innerHTML = '<h1>Hello World</h1>'
// // console.dir(postList) // python - print(dir(postList))

// const url = 'http://127.0.0.1:8000/post_api/'

// fetch(url)
// 	.then(result => result.json())
// 	.then(data => {
// 		console.log(data)
// 		// QuerySet in Django
// 		// data = Post.objects.all() -> queryset List
// 		// for post in data:
// 			// print(post.title)
// 		// postList.append(data.title)
// 		data.forEach(post => {

// 			let div = document.createElement('div')

// 			div.innerHTML = `
// 			<div class="card">
// 				<div class="card-header">
// 					<p>${post.title}</p>
// 					<p>Written By${post.author}</p>	
// 				</div>

// 				<div class="card-body">
// 					<p>${post.message}</p>
// 				</div>
// 			</div>` //print(f'{post.title}, {post.author}')
// 			postList.append(div)

// 		})
// 	})

function cardMaker(title, author, message){
	let card = document.createElement('div')
	card.className = 'card'
	
	let cardHeader = document.createElement('div')
	cardHeader.className = 'card-header'
	
	let cardBody = document.createElement('div')
	cardBody.className = 'card-body'

	let pTitle = document.createElement('p')
	let pTitleText = document.createTextNode(`${title}`)
	pTitle.append(pTitleText)

	let pAuthor = document.createElement('p')
	let pAuthorText = document.createTextNode(`${author}`)
	pAuthor.append(pAuthorText)
	
	let pMessage = document.createElement('p')
	let pMessageText = document.createTextNode(`${message}`)
	pMessage.append(pMessageText)
	
	cardHeader.append(pTitle)
	cardHeader.append(pAuthor)
	cardBody.append(pMessage)

	card.append(cardHeader)
	card.append(cardBody)
	return card
}

const postList = document.querySelector('.postList')
const url = 'http://127.0.0.1:8000/post_api/'
document.addEventListener('DOMContentLoaded', (e) =>{
	fetch(url)
	.then(result => result.json())
	.then(data => {
		console.log(data)
		// QuerySet in Django
		// data = Post.objects.all() -> queryset List
		// for post in data:
			// print(post.title)
		// postList.append(data.title)
		data.forEach(post => {

			// let div = document.createElement('div')
			
			// div.innerHTML = `
			// <div class="card">
			// 	<div class="card-header">
			// 		<p>${post.title}</p>
			// 		<p>Written By${post.author}</p>	
			// 	</div>

			// 	<div class="card-body">
			// 		<p>${post.message}</p>
			// 	</div>
			// </div>` //print(f'{post.title}, {post.author}')
			postList.append(cardMaker(post.title, post.author, post.message))

		})
	})
})






