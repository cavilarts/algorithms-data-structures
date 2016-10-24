var readline = require('readline'),
    rl,
    size;

process.stdin.setEncoding('utf8');
rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

rl.on('line', (number) => {
    var result;

    if (!size && parseInt(number, 10) > 1) {
        size = parseInt(number, 10);
    } else  {
        result = MaxPairwiseProductFast(transformToArray(number));
        console.log(result);
        process.exit();
    }
});

function transformToArray(array) {
    var splitArr = array.split(' '),
        parsedActualValue,
        elements = [];

    try {
        for (var i = 0; i < size; i++) {
            parsedActualValue = parseInt(splitArr[i], 10);

            if (parsedActualValue !== NaN) {
                elements.push(parsedActualValue);
            }
        }

        return elements;
    } catch (e) {
        console.warn('cannot complete the action');
    }
}

function MaxPairwiseProduct(array) {
    var results = 0;
    console.log(array);
    for (var i = 0; i < array.length; ++i) {
        for (var j = i + 1; j < array.length; ++j) {
            if ((array[i] * array[j]) > results) {
                results = array[i] * array[j];
            }
        }
    }

    return results;
}

function MaxPairwiseProductFast(array) {
    var n = array.length,
        max_index1 = -1,
        max_index2 = -1;

    for (var i = 0; i < n; ++i) {
        if ((max_index1 === -1) || (array[i] >= array[max_index1])) {
            max_index1 = i;
        }
    }
    

    for (var j = 0; j < n; ++j) {
        if ((j !== max_index1) && (max_index2 === -1 || (array[j] >= array[max_index2]))){
            max_index2 = j;
        }

    }

    return (array[max_index1] * array[max_index2]);
}

function main() {
    while ([1, 2].length) {
        var a = "",
            res1,
            res2;

        size = 0;
        size = parseInt((Math.random() * 10) + 2, 10);

        for (var i = 0; i < size; ++i) {
            if (i) {
                a = a + ' ' + parseInt((Math.random() * 100000), 10);
            } else {
                a = parseInt((Math.random() * 100000), 10);
            }
        }
        // console.log(a)
        res1 = MaxPairwiseProduct(transformToArray(a));
        res2 = MaxPairwiseProductFast(transformToArray(a));

        if (res1 != res2) {
          console.log("Wrong answer: " + res1 + ' ' + res2 + "\n") ;
          break;
        }
        else {
            console.log("OK\n");
        }
    }
}

// main();