#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let mx = -Infinity; let smx = -Infinity;
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > mx) {
      mx = parseInt(process.argv[i]);
    }
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > smx && parseInt(process.argv[i]) != mx) {
      smx = parseInt(process.argv[i]);
    }
  }
  console.log(smx);
}
