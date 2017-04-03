var readline = require('readline'),
    rl,
    size;

process.stdin.setEncoding('utf8');
rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

rl.on('line', function(n) {
	var elem = n.split(' '),
		a = parseInt(elem[0], 10),
		b = parseInt(elem[1], 10);

	console.log(euclidGDC(a, b));
	process.exit();
});

function euclidGDC(a, b) {
	if (b === 0) {
		return a;
	} else {
		return euclidGDC(b, a % b);
	}
}
