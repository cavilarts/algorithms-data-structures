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
		n = parseInt(num, 10);

	for (var i = 0; i < n; i++) {
		if (i <= 1) {
			list.push(1);
		} else {
			list.push(list[i-1] + list[i-2]); 
		}
	}

	return toFixed(list[list.length - 1]);
}

function toFixed(x) {
  if (Math.abs(x) < 1.0) {
    var e = parseInt(x.toString().split('e-')[1]);
    if (e) {
        x *= Math.pow(10,e-1);
        x = '0.' + (new Array(e)).join('0') + x.toString().substring(2);
    }
  } else {
    var e = parseInt(x.toString().split('+')[1]);
    if (e > 20) {
        e -= 20;
        x /= Math.pow(10,e);
        x += (new Array(e+1)).join('0');
    }
  }
  return x;
}
