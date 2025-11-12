import java.util.*;

public class HashSort {
    public static void main(String[] args) {
        int[] arr = {4, 2, 7, 1, 3, 7, 2};

        // Usamos un HashSet para eliminar duplicados
        Set<Integer> hashSet = new HashSet<>();
        for (int num : arr)
            hashSet.add(num);

        // Convertimos en lista y la ordenamos
        List<Integer> sortedList = new ArrayList<>(hashSet);
        Collections.sort(sortedList);

        System.out.println("Arreglo ordenado sin duplicados:");
        for (int num : sortedList)
            System.out.print(num + " ");
    }
}
