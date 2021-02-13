console.log('client OK');
// Get Elements
const village_name = document.getElementById('zero');
const first_name = document.getElementById('one');
const middle_name = document.getElementById('two');
const surname = document.getElementById('three');
// Randomize background colour
const colors = ["#ff3c26","#ffe226","#5cff26","#18e7a9","#26acff","#3f26ff","#9626ff","#e3275c"]
const random = Math.floor(Math.random() * colors.length);
document.body.style.backgroundColor = colors[random]
// Get and replace name element contents
fetch('/new', {method: 'GET'})
	.then(function(response) {
		if(response.ok) return response.json();
		throw new Error('Request failed.');
	})
	.then(function(data) {
		village_name.innerHTML = data["village"];
		first_name.innerHTML = data["first"];
		middle_name.innerHTML = data["middle"];
		surname.innerHTML = data["last"];
	})
	.catch(function(error) {
		console.log(error);
	});