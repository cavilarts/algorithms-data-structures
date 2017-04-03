var readline = require('readline'),
    readLineInterface,
    size;

process.stdin.setEncoding('utf8');
readLineInterface = readline.createInterface({
    "input": process.stdin,
    "terminal": false
});

readLineInterface.on('line', (number) => {
    var result,
        parsedNumber = parseInt(number,10);

    if(!size && parsedNumber > 1) {
        size = parsedNumber;
    } else {
        result = maxPairwiseProductFast(transformToArray(number));
        console.log(result);
        process.exit();
    } 
});

function transformToArray(string) {
    var splitString = string.split(' ');

    return validateArrayElements(splitString);
}

function validateArrayElements(array) {
    return array.map(function(el) {
        var parsedValue = parseInt(el, 10);

        if (parsedValue) {
            return parsedValue;
        }
    });
}

function maxPairwiseProduct(array) {
    var results = 0;

    for (var i = 0; i < array.length; i++) {
        for (var j = i + 1; j < array.length; j++) {
            if (array[i] * array[j] > results) {
                results = array[i] * array[j];
            }
        }
    }

    return results;
}

function maxPairwiseProductFast(array) {
    var arrayLength = array.length,
        firstMaxIndex = -1,
        secondMaxIndex = -1;

    for (var i = 0; i < arrayLength; i++) {
        if ((firstMaxIndex === -1) || (array[i] >= array[firstMaxIndex])) {
            firstMaxIndex = i;
        }
    }

    for (var j = 0; j < arrayLength; j++) {
        if ((j !== firstMaxIndex) && (secondMaxIndex === -1 || (array[j] >= array[secondMaxIndex]))) {
            secondMaxIndex = j;
        }
    }

    return array[firstMaxIndex] * array[secondMaxIndex];
}

function stressTests() {
    while (true) {
        var a = "",
            slow,
            fast,
            size = 0;

        size = getSize();

        for (var i = 0; i < size; i++) {
           if (i) {
               a = a + ' ' + getRandomNum(); 
           } else {
               a = getRandomNum();
           }
       }

       console.log(a);
       slow = maxPairwiseProduct(transformToArray(a));
       fast = maxPairwiseProductFast(transformToArray(a));

       if (slow !== fast) {
           console.log("Wrong aswer" + slow + ' ' + fast + "\n");
           break;
       } else {
            console.log("OK\n");
       }
            
    }
}

function getSize() {
    return parseInt((Math.random() * 10) + 2, 10);
}

function getRandomNum() {
    return parseInt((Math.random() * 100000), 10) + 1;
}

stressTests();
