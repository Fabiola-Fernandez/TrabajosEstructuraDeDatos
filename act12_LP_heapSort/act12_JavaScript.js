function heapify(arr, n, i) {
    let mayor = i;
    let izquierda = 2*i + 1;
    let derecha = 2*i + 2;

    if (izquierda < n && arr[izquierda] > arr[mayor])
        mayor = izquierda;

    if (derecha < n && arr[derecha] > arr[mayor])
        mayor = derecha;

    if (mayor !== i) {
        [arr[i], arr[mayor]] = [arr[mayor], arr[i]];
        heapify(arr, n, mayor);
    }
}

function heapSort(arr) {
    let n = arr.length;

    for (let i = Math.floor(n/2) - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (let i = n-1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        heapify(arr, i, 0);
    }
    return arr;
}

let arr = [12, 11, 13, 5, 6, 7];
console.log("Arreglo ordenado:", heapSort(arr));