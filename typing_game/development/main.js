const keyboardSelection = {
	thaiLeftTop:['ภ','ถ','ุ'],
	thaiLeftUpper:['ๆ','ไ','ำ',"พ",'ะ'],
	thaiLeftHome:['ฟ','ห','ก','ด','เ'],
	thaiLeftLower:['ผ','ป','แ','อ',"ิ"],

	thaiLeftShiftUpper:['ฎ','ฑ','ธ',"ู"],
	thaiLeftShiftHome:['ฤ','ฆ','ฏ','โ','ฌ'],
	thaiLeftShiftLower:['ฉ','ฮ'],


	thaiRightTop:["ึ",'ค','ต','จ','ข','ช'],
	thaiRightUpper:["ั","ี",'ร','น','ย','บ','ล','ฃ'],
	thaiRightHome:['้','่','า','ส','ว','ง'],
	thaiRightLower:["ื",'ท','ม','ใ','ฝ'],

	thaiRightShiftUpper:["๊",'ณ','ฯ','ญ','ฐ','ฅ'],
	thaiRightShiftHome:["็","๋",'ษ','ศ','ซ'],
	thaiRightShiftLower:["ื",'ฒ','ฬ','ฦ'],
	testLetters: ['a','s','d','f']
}

const textDisplay = document.querySelector('#textDisplay')
const textInput = document.querySelector('#textInput')
const errorCounter = document.querySelector('#errorCounter')


// 30 Words each consisting of 3-5 letters each
function createWords(letters, min, max, numWords){

	// Number of letters per word, 3-5
	// Math.random returns a value between 0 and 1
	// console.log(letters[Math.floor(Math.random() * letters.length)])
	
	let sentenceWords = []
	for(let i=0; i< numWords;i++){
		let wordArr = []
		numLetters = Math.floor(Math.random() * (max - min + 1) + min)
		
		for(let i=0; i< numLetters;i++){
			wordArr.push(letters[Math.floor(Math.random() * letters.length)])
		}
		// console.log(wordArr.join(''))
		sentenceWords.push(wordArr.join(''))
	}
	// make sure you use the right Delimiter, we want spaces between each value
	// console.log('Array',sentenceWords)
	// console.log('Array No Spaces', sentenceWords.join(''))
	// console.log('Array Spaces', sentenceWords.join(' '))
	return sentenceWords.join(' ')
}

function addSpan(words){

	words.split('').forEach(letter => {
		// <span></span>
		let span = document.createElement('span')
		span.classList = 'letter'
		span.innerText = letter
		// textDisplay.innerText = span
		textDisplay.append(span)
		// console.log(span)
	})

}

function resetAll(){
	let spans = document.querySelectorAll('.letter')
	textInput.value = ''
	spans.forEach(span => {
		span.remove()
	})
	checkError()
}

function selector(element){
	resetAll()
	// console.log(keyboardSelection[element])
	textDisplay.setAttribute('data', element)
	// textDisplay.innerText = keyboardSelection[element]
	let words = createWords(keyboardSelection[element], 3, 5, 30)
	// console.log(words)
	// textDisplay.innerText = words
	addSpan(words)

}


function checkError(){
	let errors = document.querySelectorAll('.error')
	errorCounter.innerText = errors.length
}

document.querySelector('#textInput').addEventListener('input', (e) =>{
	// console.log(e.target.value)
	// console.log(e.data)
	let characters = e.target.value
	let spans = document.querySelectorAll('.letter')
	let correct = true
	spans.forEach((span, index) => {
		// console.log(span)
		if(characters[index] == null){
			span.classList.remove('correct')
			span.classList.remove('incorrect')
			correct = false
		}
		else if(characters[index] === span.innerText){
			span.classList.add('correct')
			// console.log('Matched', characters[index], span.innerText)
			correct = true
		}
		else{

			span.classList.add('incorrect')
			span.classList.add('error')
			correct = false
			checkError()
			// console.log('Not Matched', span)
		}
	})
	if(correct === true){
		console.log('Everything is Correct!')
		dataAttribute = textDisplay.getAttribute('data')
		console.log(dataAttribute)
		selector(dataAttribute)
	}
})


document.querySelector('#resetButton').addEventListener('click', (e)=>{
	let spans = document.querySelectorAll('.letter')
	spans.forEach(span => {
		span.classList.remove('correct')
		span.classList.remove('incorrect')
		span.classList.remove('error')

	})
	checkError()
})















