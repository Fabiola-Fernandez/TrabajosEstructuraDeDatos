function bucketSort(arr) {
  let n = arr.length;
  if (n <= 0) return arr;

  let buckets = Array.from({ length: n }, () => []);

  // Colocar elementos en cubetas
  for (let i = 0; i < n; i++) {
    let index = Math.floor(arr[i] * n);
    buckets[index].push(arr[i]);
  }

  // Ordenar cada cubeta
  for (let i = 0; i < n; i++) {
    buckets[i].sort((a, b) => a - b);
  }

  // Unir cubetas
  return buckets.flat();
}

let arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68];
console.log("Arreglo ordenado:", bucketSort(arr));
