#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let mx = -Infinity; let smx = -Infinity;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > mx) {
      smx = mx;
      mx = process.argv[i];
    }
  }
  console.log(smx);
}
