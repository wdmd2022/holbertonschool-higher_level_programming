#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
    console.log('Not a number');
} else {
    ll_cool_num = parseInt(process.argv[2]);
    console.log('My number: ' + ll_cool_num);
}
