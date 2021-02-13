// Server setup
const http = require('http');
const express = require('express');
const app = express();
app.use(express.json());
app.use(express.static("public"));
const server = http.createServer(app);
const port = 80;
server.listen(port);
console.debug('Server listening on ' + port);
// DB Setup
const MongoClient = require('mongodb').MongoClient
const connectionString = 'mongodb://localhost:27017/'
// Initialized variables
name_results = []
village_results = []
surname_results = []
function roll(arr) {
	var random = Math.floor(Math.random() * arr.length);
	return random
}
// Connect to DB
MongoClient.connect(connectionString, {
	useUnifiedTopology: true
}, (err, client) => {
	if (err) return console.error(err)
	console.log('Connected to Database')
	// Access collections
	db = client.db('kng')
	villages = db.collection('villages')
	names = db.collection('names')
	surnames = db.collection('surnames')
	// Pull data
	villages.find().toArray((err, result) => {
		if (err) return console.log(err);
		village_results = result
	});
	names.find().toArray((err, result) => {
		if (err) return console.log(err);
		name_results = result
	});
	surnames.find().toArray((err, result) => {
		if (err) return console.log(err);
		surname_results = result
	});
})
// Set routes
app.get('/new', (req, res) => {
	res.send({"village": village_results[roll(village_results)]["name"]["en"], "first": name_results[roll(name_results)]["name"], "middle": name_results[roll(name_results)]["name"], "last": surname_results[roll(surname_results)]["name"]})
});