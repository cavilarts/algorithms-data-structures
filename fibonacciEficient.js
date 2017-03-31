var readline = require('readline'),
    rl,
    size;

process.stdin.setEncoding('utf8');
rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

rl.on('line', function(n) {
	console.log(fibList(n));
	process.exit();
});



function fibList(num) {
	var list = [],
		n = parseInt(num, 10) + 1;

	for (var i = 0; i < n; i++) {
		if (i <= 1) {
			list.push(1);
		} else {
			list.push(list[i-1] + list[i-2]); 
		}
	}

	return list[list.length - 1];
}
