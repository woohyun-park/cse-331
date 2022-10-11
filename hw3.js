function fs(arr) {
  const table = {
    0: 10,
    1: 4,
    2: 3,
    3: 11,
    4: 8,
    5: 14,
    6: 2,
    7: 12,
    8: 5,
    9: 7,
    10: 6,
    11: 15,
    12: 0,
    13: 1,
    14: 9,
    15: 13,
  };
  //   return arr.map((row, y) => row.map((elem, x) => table[elem]));
  return arr.map((elem) => table[elem]);
}

function fsi(arr) {
  const table = {
    0: 12,
    1: 13,
    2: 6,
    3: 2,
    4: 1,
    5: 8,
    6: 10,
    7: 9,
    8: 4,
    9: 14,
    10: 0,
    11: 3,
    12: 7,
    13: 15,
    14: 5,
    15: 11,
  };
  //   return arr.map((row, y) => row.map((elem, x) => table[elem]));
  return arr.map((elem) => table[elem]);
}

function fa(arr) {
  const result = [];
  result.push(arr[0]);
  result.push(arr[3]);
  result.push(arr[2]);
  result.push(arr[1]);
  return result;
}

console.log("fa: 8cd5 => 85dc", fa([8, 12, 13, 5]));

function strToHex(str) {
  const result = [];
  for (let i = 0; i < str.length; i++) {
    result.push(parseInt(str[i], 16));
  }
  return result;
}

console.log("6b5d =>", strToHex("6b5d"));

console.log(fs([4, 7, 15, 8]));

const babyr_enc = (block, key) => {
  console.log("enc");
};

const babyr_dec = (block, key) => {
  console.log("dec");
};
