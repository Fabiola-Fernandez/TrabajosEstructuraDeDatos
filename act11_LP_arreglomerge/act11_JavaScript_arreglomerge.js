function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    let mid = Math.floor(arr.length/2);
    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));

    let res = [];
    while (left.length && right.length) {
        res.push(left[0] < right[0] ? left.shift() : right.shift());
    }
    return res.concat(left, right);
}

let arr = [38, 27, 43, 3, 9, 82, 10];
console.log(mergeSort(arr));