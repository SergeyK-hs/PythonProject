var arr = poem.match(/[а-яА-ЯёЁйЙ]+/gi);		
var words = {};
arr.forEach(function(el, i) {
	var word = el.toLowerCase();
	if (words[word]) {
		words[word]++;
	} else {
		words[word] = 1;
	}
});
var wordsArr = Object.keys(words).sort(function(a,b){
	return words[b]-words[a];
});
var wordsSorted = {};
wordsArr.map(function(el) {
	wordsSorted[el] = words[el];
}); 
