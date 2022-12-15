#!/usr/bin/node
if ((process.argv.length) < 4) {
  console.log('0');
} else {
  let biggest = 0;
  let secondbiggest = 0;
  for (let i = 2; i <= process.argv.length; i++) {
    if (parseInt(process.argv[i]) > biggest) {
      secondbiggest = biggest;
      biggest = parseInt(process.argv[i]);
    } else if ((parseInt(process.argv[i]) > secondbiggest)) {
      secondbiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondbiggest);
}
