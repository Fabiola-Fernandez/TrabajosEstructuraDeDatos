function hashSort(arr) {
  // Convertir a Set (elimina duplicados)
  let unique = [...new Set(arr)];
  // Ordenar
  unique.sort((a, b) => a - b);
  return unique;
}

let arr = [4, 2, 7, 1, 3, 7, 2];
console.log("Arreglo ordenado:", hashSort(arr));
